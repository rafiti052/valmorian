import fs from "node:fs/promises";
import { createRequire } from "node:module";
import path from "node:path";
import process from "node:process";

const require = createRequire(import.meta.url);
const sharp = require("sharp");

const [inputPath, outputPath] = process.argv.slice(2);

if (!inputPath || !outputPath) {
  throw new Error("Usage: node scripts/create_exact_hex_battlemap.mjs <input> <output>");
}

const rows = 23;
const targetHeight = 1254;
const radius = targetHeight / (2 + (rows - 1) * 1.5);
const hexWidth = Math.sqrt(3) * radius;
const targetWidth = Math.round(23 * hexWidth);
const rowCounts = Array.from({ length: rows }, (_, row) => (row % 2 === 0 ? 22 : 23));

if (rowCounts.length !== 23 || rowCounts.at(-1) !== 22) {
  throw new Error("Invalid row sequence");
}

const hexPoints = (cx, cy) => [
  [cx, cy - radius],
  [cx + hexWidth / 2, cy - radius / 2],
  [cx + hexWidth / 2, cy + radius / 2],
  [cx, cy + radius],
  [cx - hexWidth / 2, cy + radius / 2],
  [cx - hexWidth / 2, cy - radius / 2],
]
  .map(([x, y]) => `${x.toFixed(3)},${y.toFixed(3)}`)
  .join(" ");

const polygons = rowCounts.flatMap((count, row) => {
  const firstCenterX = count === 23 ? hexWidth / 2 : hexWidth;
  const centerY = radius + row * 1.5 * radius;

  return Array.from({ length: count }, (_, column) => {
    const centerX = firstCenterX + column * hexWidth;
    return `<polygon points="${hexPoints(centerX, centerY)}" />`;
  });
});

const overlay = Buffer.from(`
  <svg xmlns="http://www.w3.org/2000/svg" width="${targetWidth}" height="${targetHeight}" viewBox="0 0 ${targetWidth} ${targetHeight}">
    <g fill="none" stroke="#131b17" stroke-opacity="0.5" stroke-width="0.9" stroke-linejoin="round">
      ${polygons.join("\n")}
    </g>
  </svg>
`);

await fs.mkdir(path.dirname(outputPath), { recursive: true });

await sharp(inputPath)
  .resize(targetWidth, targetHeight, { fit: "fill", kernel: sharp.kernel.lanczos3 })
  .composite([{ input: overlay, blend: "over" }])
  .png({ compressionLevel: 9 })
  .toFile(outputPath);

const metadata = await sharp(outputPath).metadata();
const totalHexes = rowCounts.reduce((sum, count) => sum + count, 0);

console.log(JSON.stringify({
  outputPath,
  width: metadata.width,
  height: metadata.height,
  rows: rowCounts.length,
  firstRows: rowCounts.slice(0, 4),
  lastRow: rowCounts.at(-1),
  totalHexes,
}, null, 2));
