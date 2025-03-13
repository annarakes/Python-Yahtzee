# 🎲 Yahtzee Game - Python Implementation
## Author: Anna Rakes
### 📜 Description
This project is a Python implementation of the classic dice game Yahtzee for Computer Science 1 at Elon University developed by Anna Rakes. It includes game logic, helper functions, and unit tests to ensure accurate gameplay. The game allows players to roll dice, select scoring categories, and try to achieve the highest possible score according to Yahtzee rules.

### 🚀 Features
**Rolling Dice:** Players can roll and reroll up to three times per turn.

**Scorecard Management:** Tracks scores for all 13 Yahtzee categories.

**Scoring Calculation:** Implements logic for full house, straights, of-a-kind, and other Yahtzee categories.

**Game Flow Management:** Handles the complete game cycle from start to finish.

**Unit Testing:** Ensures correct functionality of game logic and helper functions.
### 📂 Project Structure
```yahtzee.py```– Main game logic, handling turns, dice rolling, and scoring.

```yahtzeeHelper.py``` – Helper functions for dice rolling, scorecard initialization, and printing outputs.

```yahtzeeUnitTests.py``` – Unit tests to validate scoring calculations, dice rolls, and game mechanics.

```README.md``` – Project documentation.
### 🎮 How to Play
1. Run the script using Python:
```python yahtzee.py```
2. Roll five dice and decide which ones to keep.
3. You may reroll dice up to two more times.
4. Choose a category to score your final roll.
5. The game continues for 13 rounds until all categories are filled.
6. The final score is displayed at the end.
