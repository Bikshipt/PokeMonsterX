PokeMonsterX - Retro Monster RPG (pygame)

A Python/pygame RPG inspired by classic monster battlers and retro JRPGs. Explore a tiled overworld, talk to NPCs, encounter wild monsters, and battle using a real-time initiative system with elemental strengths and weaknesses.

Note on provenance: This repository contains a CC0 codebase and asset attributions. There are no embedded links to another GitHub repository; the included `README.md` previously referenced a YouTube tutorial and open asset sources but no original GitHub source. Keep attributions below intact if you redistribute builds.

## 🚀 Features

### Core Gameplay
- **Overworld Exploration**: Tiled world with animated water, coasts, and collision-aware movement
- **NPC Interactions**: Dialog trees, line-of-sight detection, and scripted trainer battles
- **Monster Encounters**: Random grass encounters with biome and level rules
- **Battle System**: Real-time initiative, abilities with costs, defend/catch/switch options
- **Elemental System**: Fire/Water/Plant interactions (double/half damage rules)
- **Evolution**: Level-based monster evolution with transition sequence
- **Monster Index**: In-game index overlay with icons, stats, and UI elements

### Technical Features
- **Pygame Rendering**: Layered sprite groups with y-sort and overlays
- **TMX Maps**: Tiled `.tmx` maps loaded via `pytmx` utilities
- **Sprite Systems**: Animated sprites, outlines, UI sprites, battle sprites
- **Audio**: Background music and SFX, with per-attack animations/sounds
- **Timers/Utilities**: Custom `Timer` class for delays and repeated actions

## 🛠️ Technology Stack

- **Language**: Python 3.10+
- **Game Library**: pygame
- **Tiled Loader**: pytmx.util_pygame
- **Data**: Hand-authored dictionaries for monsters, attacks, trainers

## 📦 Installation

1. Create and activate a virtual environment (recommended)
   ```bash
   python -m venv .venv
   .venv\\Scripts\\activate  # Windows PowerShell
   ```

2. Install dependencies
   ```bash
   pip install pygame pytmx
   ```

3. Run the game
   ```bash
   cd "code (finish)"
   python main.py
   ```

If you prefer to explore the starter scaffold, use the `code (start)` directory.

## 🎮 Controls

- **Arrow Keys**: Move player / Navigate menus
- **Space**: Interact, confirm, talk, select menu item
- **Enter**: Toggle Monster Index overlay
- **Esc**: Back/cancel in battle menus

## 🏗️ Project Structure

```
PokeMonsterX/
├── audio/                 # Music and sound effects
├── code (finish)/         # Complete game implementation
│   ├── main.py            # Entry point
│   ├── settings.py        # Constants, colors, battle positions
│   ├── game_data.py       # MONSTER_DATA, ATTACK_DATA, TRAINER_DATA
│   ├── entities.py        # Player/Character logic, movement, dialogs
│   ├── sprites.py         # Sprite classes (UI, monsters, outlines, etc.)
│   ├── battle.py          # Battle loop, UI, initiative, abilities
│   ├── monster.py         # Monster stats, abilities, XP/evolution
│   ├── dialog.py          # Dialog tree system
│   ├── evolution.py       # Evolution sequence
│   ├── groups.py          # Layered sprite groups
│   ├── support.py         # Importers, drawing helpers, utils
│   ├── timer.py           # Timer utility
│   └── monster_index.py   # In-game monster index overlay
├── code (start)/          # Starter version
├── data/
│   ├── maps/              # Tiled .tmx maps
│   └── tilesets/          # .tsx tileset definitions
├── graphics/              # Characters, monsters, UI, backgrounds
└── README.md
```

## 🎨 Design System (in-game)

- **Palette**: Defined in `settings.py` under `COLORS` (white/dark/gray + element colors)
- **UI Icons**: Located in `graphics/ui` (sword/shield/arrows/hand, highlighted variants)
- **Fonts**: Pixel fonts (`PixeloidSans.ttf`, `dogicapixelbold.otf`) configured in `main.py`
- **Battle Layout**: Positions (`BATTLE_POSITIONS`) and layers in `settings.py`

## 🔧 Configuration

Most gameplay constants are in `settings.py`:
- **Window/Tiles**: `WINDOW_WIDTH`, `WINDOW_HEIGHT`, `TILE_SIZE`
- **Battle**: `BATTLE_CHOICES`, outline width, layers
- **Colors**: `COLORS` mapping including element colors

Game content is in `game_data.py`:
- **Monsters**: `MONSTER_DATA` with stats, abilities, and `evolve` rules
- **Attacks**: `ATTACK_DATA` with target, amount, cost, element, and animation key
- **Trainers**: `TRAINER_DATA` for NPC dialog, party, biome, behavior

TMX assets are auto-loaded from `data/maps` via helpers in `support.py` and `main.py`.

## 📱 Features in Detail

1) **Overworld**
- Imports animated water/coast tiles, objects, transitions, collisions
- Player movement with collision resolution and y-sorted drawing

2) **Dialog & NPCs**
- `Character` uses timers, LOS raycast, and approach behavior to initiate dialogs or battles
- Nurse restores party to max HP/energy

3) **Encounters & Biomes**
- Grass patches define biome, monster pool, and encounter level ranges
- Random encounter timer with variability

4) **Battle System**
- Real-time initiative: monsters act when initiative reaches 100
- Options: fight, defend, switch, target
- Elemental multipliers and defense/guard adjustments
- Ability cost gating via energy; healing/support use negative amounts

5) **Progression**
- XP on defeating foes; level-ups recalc thresholds
- Evolution sequences with audio, blocking, and replacement in party

## 🚀 Running on Other Platforms

- Windows: Commands above (PowerShell). If SDL issues occur, update pygame.
- macOS/Linux: Use `python3 -m venv venv && source venv/bin/activate` then `pip install pygame pytmx` and run `python main.py` from `code (finish)`.

## 🔮 Future Enhancements

- Save/load system
- Controller support and key remapping
- Additional abilities/elements/status effects
- Expanded world with quests and bosses
- Balancing passes on stats and costs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/awesome-improvement`)
3. Commit your changes (`git commit -m "feat: add awesome improvement"`)
4. Push the branch (`git push origin feature/awesome-improvement`)
5. Open a Pull Request

## 📄 License

The code is released under **CC0 (Public Domain)** — use it freely, including commercially. Attributions are appreciated but not required.

## 🙏 Acknowledgments & Asset Credits

- Video tutorial reference: `https://www.youtube.com/watch?v=fo4e3njyGy0`
- Artwork by Scarloxy: `https://scarloxy.itch.io/mpwsp01`
- SFX/Music sources (OpenGameArt):
  - Fire attack: `https://opengameart.org/content/spell-4-fire`
  - Slash attack: `https://opengameart.org/content/knife-sharpening-slice-2`
  - Crack sounds: `https://opengameart.org/content/5-break-crunch-impacts`
  - Overworld music: `https://opengameart.org/content/nes-overworld-theme`
  - Notice sound: `https://opengameart.org/content/10-8bit-coin-sounds`
  - Battle music: `https://opengameart.org/content/boss-battle-1-8-bit-re-upload`
- Audio used in trailer:
  - `https://opengameart.org/content/porkymon-battle-theme`
  - `https://opengameart.org/content/face-the-facts`
  - `https://opengameart.org/content/jay-the-doggo-music`

PokeMonsterX — A retro-styled monster adventure powered by pygame."# PokeMonsterX" 
