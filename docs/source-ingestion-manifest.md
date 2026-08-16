---
manifest_version: 2
title: Full sources ingestion manifest
generated: { by: process:okf-import, at: 2026-08-15T23:12:07Z }
sources:
  - resource: "/sources/Backstories.pdf"
    availability: local-only
    sha256: e3200f29f572423baf07ade254950a7e1c75e784aa6b375385945d6ee8d35777
    disposition: partial
    proposed_disposition: full
    locator: "Enna pp.2-3; Bri pp.4-6; Bob pp.7-8; Liria pp.9-11; Yara pp.12-15"
    targets:
      - "/party/enna.md"
      - "/party/bri.md"
      - "/party/bob.md"
      - "/party/liria.md"
      - "/party/yara.md"
    rights: "unconfirmed-local-only"
    note: "Player-authored/private; keep binary local."
  - resource: "/sources/Capa.png"
    availability: local-only
    sha256: 348b74fca862e283a5d394243b9d017e80c683b561399b396bbf05be299faa22
    disposition: pending
    proposed_disposition: catalog-only
    locator: "arquivo completo"
    targets:
      - "/index.md"
    rights: "unconfirmed-local-only"
    note: "Campaign cover metadata; binary stays local."
  - resource: "/sources/Cenarios/Sessao 1/01. Quarto dos empregados.jpeg"
    availability: local-only
    sha256: 9aefba54f6c8f4da34d043feea0a6b2002879f729bbf8573fe1323f2fc8cd93c
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/quarto-dos-empregados.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 1/02. Quadro.webp"
    availability: local-only
    sha256: b5ce112a77175ddcd42abf39a5f7469d0fc89ff8767c72784f163cb97355033d
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/sala-de-pintura.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 1/03. Fora dos Quartos.webp"
    availability: local-only
    sha256: cbca7c2c8610b48e72f1597a84a9e8e4fb8990fcb6ef9b466f0f811bda4a7f6f
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/npcs/mordecai.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 1/04. Armazem.png"
    availability: local-only
    sha256: a7abcf0a9ea0855e6072cf274b5dc3bbe51321da96a7b27fbabeeea294f47fc3
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/armazem.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 1/04. Cozinha.png"
    availability: local-only
    sha256: bb45021345217ed8b3eb85ffdde663841c8f75cce59c1f960a763dd46006de1b
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/cozinha.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 1/04. Subsolo.png"
    availability: local-only
    sha256: 2fa0995e97b6ab9a4084c1a14cb4da532597ddec702c7e8016c42313aaead7f2
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/camara-nao-identificada-do-subsolo.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 1/05. Cozinheiro.webp"
    availability: local-only
    sha256: ddc48d8ceec6667eda17ad06a5785d806da362e541e305e6c5ee27ae3ed9f472
    disposition: catalog-only
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/npcs/chef-espectral.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 1/06. Mansion Outdoors.png"
    availability: local-only
    sha256: 519d777d8a66dcb63b2fa786a3e4d259d1b483fc6cde8a774e8de0a3ad6d38ac
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "Exact-byte alias group; retain every path but create one semantic description."
  - resource: "/sources/Cenarios/Sessao 1/07. Jardins da Mansao.png"
    availability: local-only
    sha256: f34cee95bf683c3084ee93a1b058141acef77474565e73d6a43d3fbb77682ce3
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/jardins-da-mansao.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 1/08. 1 Guardhouse.png"
    availability: local-only
    sha256: 9bb6875789cf810a80c9f653aa30db770e05112823aab82df4f54813f2232b59
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/casa-de-guarda.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 1/08. 2:3 Abandoned Storage and House.png"
    availability: local-only
    sha256: 22b1d1fc9ee5f61827b0b9a389ad99f4978d10b2d334495de03c28d218a3db01
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/anexo-abandonado.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 1/08. 4:5 Estabulos.png"
    availability: local-only
    sha256: 484ec7065e883094718245d728697ed15f5d2cae6ad1b51d91673dd8cb16275e
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/estabulos.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 1/08. 6 Casa do Jardineiro.png"
    availability: local-only
    sha256: 9644717040f4d90c6e289d3d782e0c85f4561b1df45af9c85accc4660bdf51f1
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/casa-do-jardineiro.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 1/08. Entrada Principal.png"
    availability: local-only
    sha256: 2d48a9a715ca6065f1e556708c7fc8501a61572df91d989714d4890f687e0b3e
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/entrada-principal.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 1/08. Fonte.png"
    availability: local-only
    sha256: 222ec3fdfecb4d4b9f2ac679da37cc2c21a6337d338a6037ae20f7f2003bd808
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/fonte-da-mansao.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 1/08. Portao.png"
    availability: local-only
    sha256: 1d3370c3b36cc7e0be86baf59d630647cbec48b2b19ccd058b4363e05794dde1
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/portao-da-mansao.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 2/00 Beetle Construct.png"
    availability: local-only
    sha256: e825399c27a888e7e74dbf7db153f7c4fb68db7cc3c1bae833f949eb8324e279
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable construct appearance only"
    targets:
      - "/homebrew/constructos-da-mansao.md"
    rights: "unconfirmed-local-only"
    note: "Do not infer mechanics or identity."
  - resource: "/sources/Cenarios/Sessao 2/00 Bird Construct.png"
    availability: local-only
    sha256: 423993d6f0efb4c60c8b9c2b129465e3530d603c0c54cda2bdf31feda33ee20a
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable construct appearance only"
    targets:
      - "/homebrew/constructos-da-mansao.md"
    rights: "unconfirmed-local-only"
    note: "Do not infer mechanics or identity."
  - resource: "/sources/Cenarios/Sessao 2/00 Salamander Construct.png"
    availability: local-only
    sha256: c9f5ebc7c9f51f579a129c39662f673c0cfb7feecfbd7b3c4f07c7c9446315ea
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable construct appearance only"
    targets:
      - "/homebrew/constructos-da-mansao.md"
    rights: "unconfirmed-local-only"
    note: "Do not infer mechanics or identity."
  - resource: "/sources/Cenarios/Sessao 2/00 Spider Construct.png"
    availability: local-only
    sha256: 80b59f34ea3c9bd0e609caa960a8fa140a3c5dcbc745d96840e365c3ae07d632
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable construct appearance only"
    targets:
      - "/homebrew/constructos-da-mansao.md"
    rights: "unconfirmed-local-only"
    note: "Do not infer mechanics or identity."
  - resource: "/sources/Cenarios/Sessao 2/B1 Corredor e Celas.png"
    availability: local-only
    sha256: 86ca34049f8d2044b297b27fe85656903a3041a687c2d6a0f91b768709bd3a9f
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/corredor-e-celas.md"
    rights: "unconfirmed-local-only"
    note: "Exact-byte alias group; retain every path but create one semantic description."
  - resource: "/sources/Cenarios/Sessao 2/B1 Laboratorio.png"
    availability: local-only
    sha256: 10c6c6962ae94ce683b59c0439e29668c0516f6450cf076b7b179b4d19453dca
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/laboratorio-de-contencao.md"
    rights: "unconfirmed-local-only"
    note: "Exact-byte alias group; retain every path but create one semantic description."
  - resource: "/sources/Cenarios/Sessao 2/B1 Passarela.png"
    availability: local-only
    sha256: 28086fde717b10114eee345a82cb66bb0147a5a0e121abb33ef030bf539412eb
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/passarela.md"
    rights: "unconfirmed-local-only"
    note: "Exact-byte alias group; retain every path but create one semantic description."
  - resource: "/sources/Cenarios/Sessao 2/F1 Biblioteca.png"
    availability: local-only
    sha256: 7a5d42d2722ef7e02d5742710c8bb924a1f4ef99419244385eb04761eddeedda
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/biblioteca.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 2/F1 Corredor principal.png"
    availability: local-only
    sha256: c94b7074c91edacb9023dd8f4a2c46536f25be87d4d75444679422022c568848
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/corredor-principal.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 2/F1 Sala de pintura.png"
    availability: local-only
    sha256: 81e680018fea04a89e91937098e0e1134115ecdb1cef029909807a09ce36db89
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/sala-de-pintura.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 2/F1 Salao Principal.png"
    availability: local-only
    sha256: ea2cc68b77de3bc6815602b143b157c3afa3d6b1de4dabbe304fccad9aeb724a
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/salao-principal.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 2/F1 Salão de Baile.png"
    availability: local-only
    sha256: b008ed0874c7b98931e675276ec41faeb2d8488dd9d5ada1e17ca251c24c5f16
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/salao-de-baile.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 3/B1 Corredor e Celas.png"
    availability: local-only
    sha256: 86ca34049f8d2044b297b27fe85656903a3041a687c2d6a0f91b768709bd3a9f
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/corredor-e-celas.md"
    rights: "unconfirmed-local-only"
    note: "Exact-byte alias group; retain every path but create one semantic description."
  - resource: "/sources/Cenarios/Sessao 3/B1 Laboratorio.png"
    availability: local-only
    sha256: 10c6c6962ae94ce683b59c0439e29668c0516f6450cf076b7b179b4d19453dca
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/laboratorio-de-contencao.md"
    rights: "unconfirmed-local-only"
    note: "Exact-byte alias group; retain every path but create one semantic description."
  - resource: "/sources/Cenarios/Sessao 3/B1 Onyx Negro.png"
    availability: local-only
    sha256: 33c7a9345c411e5356837572832c32092ca64bb7c2eb41a8e0c129ec76278c86
    disposition: pending
    proposed_disposition: catalog-only
    locator: "arquivo completo"
    targets:
      - "/items/onix-negro.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 3/B1 Passarela.png"
    availability: local-only
    sha256: 28086fde717b10114eee345a82cb66bb0147a5a0e121abb33ef030bf539412eb
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/passarela.md"
    rights: "unconfirmed-local-only"
    note: "Exact-byte alias group; retain every path but create one semantic description."
  - resource: "/sources/Cenarios/Sessao 3/B1 Portal.png"
    availability: local-only
    sha256: cdbcdbeba3262c37e8ee044fcfefe4a1498a9069f965021a35fcf8c9a692c015
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/sala-do-portal.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 3/B1 Treasure Room.png"
    availability: local-only
    sha256: 0db92dab8e2d2ece296cb9c741865b41c280c9ebcd21a82e9163eea5ad2426bf
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable scene and session/floor filename"
    targets:
      - "/locations/sala-do-tesouro.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 3/F1 - Fair - Crispim Catraca.png"
    availability: local-only
    sha256: ce1d72f738bcb21d1e6a1993ebabd479fc80491aa4572da53e7f75e0700a7e91
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable appearance only"
    targets:
      - "/npcs/crispim-catraca.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 3/F1 - Fair - Espirro Dourado.png"
    availability: local-only
    sha256: 2474401ab09d07180faed8cbdd168721e5429efb010f7d3508c176bea9aa8759
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable appearance only"
    targets:
      - "/npcs/espirro-dourado.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 3/F1 - Fair - Irmao Aurelio.png"
    availability: local-only
    sha256: ae63365e87f99e1b1d5ef2681c6b33d0d338794c8de2435e20c88daedf06eedd
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable appearance only"
    targets:
      - "/npcs/irmao-aurelio.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 3/F1 - Fair - Leoncio Mirtilo.png"
    availability: local-only
    sha256: e0ab021e437c42280c94597cd4b89cd0f4096cef425e49669b01489da89d7323
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable appearance only"
    targets:
      - "/npcs/leoncio-mirtilo.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 3/F1 - Fair - Silena Poucasombra.png"
    availability: local-only
    sha256: 9662e002641de0112f075d3487be6fd2af468f0ddd4692c3285ac02f6ffac982
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable appearance only"
    targets:
      - "/npcs/silena-pouca-sombra.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/Cenarios/Sessao 3/F1 - Fair - Valerio Veraneio.png"
    availability: local-only
    sha256: 6240509b5f81624656e04bf4c3597473ec05b057e251533dee60af26dc255739
    disposition: pending
    proposed_disposition: catalog-only
    locator: "observable appearance only"
    targets:
      - "/npcs/valerio-veraneio.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/DnD_2024_Character-Sheet - DLTHEDM - Fillable.pdf"
    availability: local-only
    sha256: 42d8d68abb38c38a4aed2187d88ff2b971516cc483422935b56abc88d8735f25
    disposition: pending
    proposed_disposition: catalog-only
    locator: "two-page blank AcroForm"
    targets:
      - "/rulebooks/ficha-de-personagem-dnd-2024.md"
    rights: "unconfirmed-local-only"
    note: "Reference metadata only."
  - resource: "/sources/Ficha Bob.pdf"
    availability: local-only
    sha256: ed2fe86e558c766a3269ba5b7eebbf9095c10bbe9909da28df6adae99369e875
    disposition: partial
    proposed_disposition: full
    locator: "populated AcroForm fields"
    targets:
      - "/party/bob.md"
    rights: "unconfirmed-local-only"
    note: "Player data; keep binary local."
  - resource: "/sources/Ficha Bri.pdf"
    availability: local-only
    sha256: 447c58f8c28ab4e20341430fbf962c616dfc719a06c0fe3fb9d0f8b203e5e73a
    disposition: partial
    proposed_disposition: full
    locator: "populated AcroForm fields"
    targets:
      - "/party/bri.md"
    rights: "unconfirmed-local-only"
    note: "Player data; keep binary local."
  - resource: "/sources/Ficha Enna.pdf"
    availability: local-only
    sha256: 0c25e212305951117dd9ee78152d1a96664320b116870cff2b588c8f2881fc73
    disposition: partial
    proposed_disposition: full
    locator: "populated AcroForm fields"
    targets:
      - "/party/enna.md"
    rights: "unconfirmed-local-only"
    note: "Player data; keep binary local."
  - resource: "/sources/Ficha Liria.pdf"
    availability: local-only
    sha256: 4389096ea154a95243137c61896f5a85ad479c47848e665d092009d339deb610
    disposition: partial
    proposed_disposition: full
    locator: "populated AcroForm fields"
    targets:
      - "/party/liria.md"
    rights: "unconfirmed-local-only"
    note: "Player data; keep binary local."
  - resource: "/sources/Ficha Yara.pdf"
    availability: local-only
    sha256: 49f5d29fd759dda2313dcfdffaea8b17f39fe705b789cd574cc43da28c58fbc9
    disposition: partial
    proposed_disposition: full
    locator: "populated AcroForm fields"
    targets:
      - "/party/yara.md"
    rights: "unconfirmed-local-only"
    note: "Player data; keep binary local."
  - resource: "/sources/Mansao_Valmorian_Sessao_1_Roteiro.pdf"
    availability: local-only
    sha256: 599bca3c37cb045b00e4e5a2acfb58b3bcf0ee481de79dfc04d2d21f52de0ba5
    disposition: partial
    proposed_disposition: full
    locator: "pages 1-5"
    targets:
      - "/sessions/sessao-01-plano.md"
      - "/locations/mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "Scripted plan, not evidence of played events."
  - resource: "/sources/Mapas/0. initial/B1.jpg"
    availability: local-only
    sha256: 2cc0031a812d7082d055942842c1a0a74627348b2fcf04b38e4fe6ada5b82890
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/0. initial/F1.jpg"
    availability: local-only
    sha256: 4f64b8234af2548d3115d2fa5ea36a36c28096fb0370fa805822231144587b0d
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/0. initial/F2.jpg"
    availability: local-only
    sha256: baed80b385ac3c969fe010872ed3dd17c5e37622ca7b67dc04ccd1a6007a2c93
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/0. initial/F3.jpg"
    availability: local-only
    sha256: 253474847dfd94e63d0f3b856080c9eb4c96e26632c028e60d1a13aff726e73b
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/0. initial/F4.jpg"
    availability: local-only
    sha256: 1187ff11829b6e3196a6d3e51443c38c84ef1c0e8be7b88cb5e67f54800f6e30
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/1. final/B1final.jpg"
    availability: local-only
    sha256: 60f5dc958f1b987d76eda53cc914422b6b7051636de3bb4539d904cd070c9659
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/1. final/F1final.jpg"
    availability: local-only
    sha256: 3634da1ba536a227d614d00ff899c0bba59981ffeae7249b0f6282824172ac83
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/1. final/F2final.jpg"
    availability: local-only
    sha256: 0b88c7063f3305d76305b83b46d6f8b7560c869fb4d570c0a54aea2eb5719b7c
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/1. final/F3final.jpg"
    availability: local-only
    sha256: 6f8836d8423c417b903df137d28e8c445e9269dae85bcf34bae65eb84cf9d701
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/1. final/F4final.jpg"
    availability: local-only
    sha256: 196a01c91a14a024aec6f3103082ec8f004fd327dd63b0a6c76af98b5758a9e9
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/2. day/F1_day.jpg"
    availability: local-only
    sha256: 920bf5f6191a3428ee9147bcfcece5185f91da8b8a406a38304bc2a88c76b5d2
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/2. day/F2day.jpg"
    availability: local-only
    sha256: d197d4543871aea9cc7ae4279ee974e01b7c7418f7c9c40cf9f2c5e147527a8c
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/2. day/F3day.jpg"
    availability: local-only
    sha256: 60515e688c04e96f2fb991eb5b995b90cfaafc1eb9060c515b08a5c7a9e1140b
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/2. day/F4day.jpg"
    availability: local-only
    sha256: e6d4c91ff9cb6fe751ed96f8d08582c05673d1d232a52f08f7866b54764387fd
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/3. revealed/F2_final_revealed.jpg"
    availability: local-only
    sha256: 963a4612914bfa39be47aab070a7688c6582e707079dc4f58cd25c619a942a50
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/3. revealed/F2_revealed.jpg"
    availability: local-only
    sha256: 801252b9bdf86d6e41b1dd2f73c59f1c404d73fa8bd0e5765f91b66516719eae
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/3. revealed/F2day_revealed.jpg"
    availability: local-only
    sha256: b753e01e20e85fe96a39f0c810316be691798efe773c0068cfc85297cf715ecd
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/4. custom/06. Mansion Outdoors.png"
    availability: local-only
    sha256: 519d777d8a66dcb63b2fa786a3e4d259d1b483fc6cde8a774e8de0a3ad6d38ac
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local. Exact-byte alias group; retain every path but create one semantic description."
  - resource: "/sources/Mapas/4. custom/Primeiro Andar.png"
    availability: local-only
    sha256: 3aa3715406c2aeb49fe7156b4b5d4690a5491691fd871f2219ee6f3fa9eaa476
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Mapas/4. custom/Subsolo.png"
    availability: local-only
    sha256: 52d1209c2d2330a836d68cfcc73a1ae6acf1835a0980c6e53c7b05933feacfee
    disposition: pending
    proposed_disposition: catalog-only
    locator: "map state and floor labels"
    targets:
      - "/locations/mapas-da-mansao-valmorian.md"
    rights: "unconfirmed-local-only"
    note: "GM spatial reference; licensing unconfirmed, binary stays local."
  - resource: "/sources/Yara/YARA.png"
    availability: local-only
    sha256: 44ba9bd21f816d650e32b62c40ed63680c51e3ef2e273481271bb088e19f494e
    disposition: pending
    proposed_disposition: catalog-only
    locator: "arquivo completo"
    targets:
      - "/party/yara.md"
    rights: "unconfirmed-local-only"
    note: "Player-character visual; binary stays local."
  - resource: "/sources/Yara/Yara2.png"
    availability: local-only
    sha256: 3e0a586d82c8cbde12ae4d765ceb13d118d6b9f2d92e68d705d1f4785d931e10
    disposition: pending
    proposed_disposition: catalog-only
    locator: "arquivo completo"
    targets:
      - "/party/yara.md"
    rights: "unconfirmed-local-only"
    note: "Player-character visual; binary stays local."
  - resource: "/sources/Yara/personagem_bruna1.png"
    availability: local-only
    sha256: 39c138c9e2bda9095817aa882a1ef311c2cd7251d57b1f69b475bf81545d22d6
    disposition: pending
    proposed_disposition: catalog-only
    locator: "arquivo completo"
    targets:
      - "/party/yara.md"
    rights: "unconfirmed-local-only"
    note: "Identity as Yara requires confirmation; catalog only."
  - resource: "/sources/Yara/personagem_bruna2.png"
    availability: local-only
    sha256: 20f79706e386837329f684481bc94bae3ad299509e43c69a9d603e9dc25fd1dc
    disposition: pending
    proposed_disposition: catalog-only
    locator: "arquivo completo"
    targets:
      - "/party/yara.md"
    rights: "unconfirmed-local-only"
    note: "Identity as Yara requires confirmation; catalog only."
  - resource: "/sources/Yara/yara3.png"
    availability: local-only
    sha256: 46b51b981086f8206e12d7c1da5b24057593d281ee7002662528209c5b46071c
    disposition: pending
    proposed_disposition: catalog-only
    locator: "arquivo completo"
    targets:
      - "/party/yara.md"
    rights: "unconfirmed-local-only"
    note: "Player-character visual; binary stays local."
  - resource: "/sources/dampd-5e---livro-do-jogador-2024.pdf"
    availability: local-only
    sha256: 55f530ae733992d95cf6c7a000b86b40a2166e98292347e76db4693941f7236c
    disposition: pending
    proposed_disposition: deferred
    locator: "397-page volume metadata only"
    targets:
      - "/rulebooks/livro-do-jogador-2024.md"
      - "qmd://rulebooks-local/"
    rights: "commercial-local-only"
    note: "Commercial text; full extraction remains gitignored and local."
  - resource: "/sources/handover-campanha-valmorian.md"
    availability: tracked
    sha256: 2cc558ef28032db4382ad7e0fefe1a417c224f7868d73e3f6480395720e2835f
    disposition: partial
    proposed_disposition: full
    locator: "sections 1-75"
    targets:
      - "multiple existing codex concepts"
      - "missing handover concepts in Batch A"
    rights: "campaign-authored"
  - resource: "/sources/npc_fichas.pdf"
    availability: local-only
    sha256: 635711cbaf9ae56f891d3d37203ea71e828be60f652ce51088e32964451eb8d7
    disposition: partial
    proposed_disposition: full
    locator: "NPCs pp.1-2; stat blocks pp.3-4"
    targets:
      - "/npcs/brinna-brasswhistle.md"
      - "/npcs/tivik-sprocketlash.md"
      - "/bestiary/gloem-protector.md"
      - "/bestiary/skitterjack.md"
    rights: "unconfirmed-local-only"
  - resource: "/sources/sessao_2_5_apoio_mesa_com_constructos_v2.docx.md"
    availability: tracked
    sha256: cb83d87b7cb6c8c062aabf347ae2f8caf8526aa18d9cecd7dfd3d21220599cb8
    disposition: partial
    proposed_disposition: full
    locator: "sections on rooms, underground conflict, fair, constructs"
    targets:
      - "/sessions/sessao-02-5-plano.md"
      - "Mansion room concepts"
      - "existing NPC concepts"
    rights: "campaign-authored"
  - resource: "/sources/sessao_3_estrutura_narrativa.md"
    availability: tracked
    sha256: 64ec6159703e2ed63b139fef35603fccfe208e2c6fac74aee8d279e049bb73e8
    disposition: partial
    proposed_disposition: full
    locator: "laboratory, cells, portal, fair, church and crypt sections"
    targets:
      - "/sessions/sessao-03-plano.md"
      - "existing fair/church/crypt concepts"
      - "Mansion room concepts"
    rights: "campaign-authored"
  - resource: "/sources/updated-my-amphitari-race-to-include-more-amphibians-v0-7y3rw2xa8f2d1.webp"
    availability: local-only
    sha256: f96094859feabb8cab39e0db904599c5ab3ea15b01fd8862ece2f1ddba86f001
    disposition: pending
    proposed_disposition: full
    locator: "visible two-column species rules"
    targets:
      - "/homebrew/amphitari.md"
    rights: "unconfirmed-local-only"
    note: "Third-party homebrew; rights unconfirmed, source image stays local."
---

# Manifesto de ingestão completa de `sources/`

Este manifesto é o checkpoint anterior a qualquer novo lote canônico. Ele registra os 80
arquivos materiais encontrados, seus hashes, a situação atual, o destino proposto e o
tratamento de direitos. `proposed_disposition` não altera o estado atual até o lote ser
aprovado, escrito e validado.

## Resumo

- **11** fontes atualmente citadas, todas conservadoramente `partial` até a reconciliação.
- **69** fontes pendentes: 67 imagens, a ficha vazia e o Livro do Jogador.
- **4** pares de caminhos são duplicatas byte a byte; todos os caminhos serão preservados.
- **1** fonte fica `deferred`: o Livro do Jogador comercial, com texto integral somente local.
- Binários com direitos ou privacidade não confirmados permanecem fora do Git público.

`availability` distingue fontes `tracked`, que precisam existir em todo checkout, de fontes
`local-only`, que podem não existir em um clone limpo. Fontes locais têm o hash conferido
quando presentes; sua ausência, por si só, não é erro de integridade.

## Lotes propostos

1. **A — Handover e lacunas estruturais:** NPCs, Lagoa Nymrath, selo, regras e arco apoiados pelo handover.
2. **B — PDFs e fichas:** planos de sessão, personagens, NPCs e stat blocks com locadores de página/campo.
3. **C — Mansão e mapas:** locais semânticos, estados de mapa e aliases duplicados.
4. **D — Visuais e homebrew:** feira, Yara, constructos, Amphitari, capa e referências.
5. **E — Rulebooks:** ficha vazia catalogada; Livro do Jogador registrado como adiado/local.

## Conflitos que não serão resolvidos automaticamente

- Bri: `Soldado` na ficha versus `Heroína do Povo` em Backstories.
- Líria: CAR 18, mas os campos da ficha registram modificador +3, CD 13 e ataque +5.
- Bob: CD 15 é compatível com o tambor +1; ataque mágico +6 no codex não é, e a evidência aponta +5.
- Gloem/Skitterjack não são automaticamente Cão de Trava Planar/Ceifador de Vigília.
- Os roteiros de sessão são preparação, não prova do que efetivamente aconteceu.
- As imagens `personagem_bruna1/2` não serão identificadas como Yara sem confirmação.

## Duplicatas exatas

- Sessões 2/3: `B1 Corredor e Celas.png`.
- Sessões 2/3: `B1 Laboratorio.png`.
- Sessões 2/3: `B1 Passarela.png`.
- Sessão 1 `06. Mansion Outdoors.png` e `Mapas/4. custom/06. Mansion Outdoors.png`.

## Regra de promoção

Cada lote atualiza `disposition` somente depois de: escrita serial pelo coordenador,
proveniência completa, índices reconciliados, validação estrita e buscas QMD de aceitação.
