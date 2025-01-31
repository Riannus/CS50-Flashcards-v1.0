# Changelog

### [1.2.0] - 2025-01-23  
#### Added  
- **New Mode: Study Mode**   
  - Flashcards can be viewed at a relaxed pace with no penalties.  
  - Users can edit specific flashcards within Study Mode.  

#### Changed  
- Improved deck browsing experience with clearer instructions.  
- Minor UI adjustments for better readability.  

#### Fixed  
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

