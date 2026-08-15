# inbox/

Staging area for raw campaign material on its way into the codex. **Not canon.**

Drop anything here — Obsidian exports, Google Doc dumps, photographed session notes,
World Anvil JSON, a text file of names you like. Then run `/import` and the companion
will survey it, show you a manifest, and convert it into OKF concepts under `codex/`.

Contents are gitignored on purpose. Two reasons:

1. **Duplicate canon is worse than missing canon.** If the raw notes stay in the repo
   alongside the converted concepts, search returns both and neither is authoritative.
2. Exports are often large, binary-ish, or full of material you have already superseded.

This directory is indexed by QMD as the `inbox` collection, so you can search your raw
notes before converting them — `qmd search "harbourmaster" -c inbox`.

Once material is converted and you have checked the result, delete the source file.
