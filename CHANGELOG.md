# Changelog

## [1.4.0] - 2025-03-12  
### Added  
- **New Game Modes**  
  - **Guess the Definition**: Multiple-choice mode (A, B, C, D).
  - **Survival Mode**: An endless quiz mode.
- **New deck**: Added Czech-Norwegian flashcards deck.
- **Correct Answer Display**: Now shows the correct answer when a wrong guess is made.

### Changed  
- Validation Improvement: Prevents entering an empty string for the deck ID.
- PyTest Updated


## [1.3.0] - 2025-03-07  
### Added  
- **Dynamic Text System**  
  - Introduced a JSON-based system for managing in-game text.  
  - All UI messages, prompts, and menu texts are now stored in `translations.json`.  
  - This allows for easier modifications and ensures consistency across the application.  

### Changed  
- **Refactor: Code restructuring**  
  - Updated all static text occurrences in the code to use the new dynamic text system.  
  - Improved maintainability by centralizing all UI-related text in a single file.  


## [1.2.1] - 2025-02-15  
### Added  
- **New Mode: Time Attack**  
  - Work in progress, not yet available for users.

### Changed  
- **Refactor: Code restructuring**  
  - The original code has been separated into multiple modules for better readability and maintainability.  
  - New structure includes separate folders for:  
    - `card_decks/`: Game decks saved as CSV files.  
    - `environments/`: Files for the menu, gameplay, deck browser, etc.  
    - `game_modes/`: Different game modes, including Study Mode and Time Attack.  
    - `models/`: Classes defining flashcards and decks.  
    - `utils/`: Helper functions for deck management, validation, etc.


## [1.2.0] - 2025-01-23  
### Added  
- **New Mode: Study Mode**   
  - Flashcards can be viewed at a relaxed pace with no penalties.  
  - Users can edit specific flashcards within Study Mode.  

### Changed  
- Improved deck browsing experience with clearer instructions.  
- Minor UI adjustments for better readability.  

### Fixed  
- Fixed minor text alignment issues in terminal outputs.  
- Ensured consistent file encoding when handling decks.

  
## [1.1.0] - 2025-01-19
### Added
- New feature: Ability to exit the game using the `exit_game` command.
- Added a new deck: Czech-English flashcards for language learning.

### Changed
- Improved text formatting for better orientation in the game.
- Added colors to terminal outputs for enhanced visibility.
- Unified commands to provide a more consistent user experience.
- Updated `README` for better clarity and information.
- Added a `CHANGELOG` to track updates and changes.

### Fixed
- Bug fix: Corrected terminal clearing issue for Windows users.
- Renamed the `requirements.tst` file to `requirements.txt` to fix dependency installation issues.
- Updated `scan_decks` to use cross-platform path handling with `pathlib`.
- Ensured UTF-8 encoding for all file operations to fix diacritics issues.

