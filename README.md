# 🎮 Rock Paper Scissors Tournament

A modern and interactive Rock Paper Scissors game built with Python and Tkinter, featuring tournament-style gameplay, betting system, and special skills.

![Game Screenshot](https://img.shields.io/badge/Python-Tkinter-blue) ![Version](https://img.shields.io/badge/Version-1.0-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

### 🎯 Core Gameplay
- **Tournament Style**: Best of 3 rounds per tournament
- **Betting System**: Place bets from 10 to ALL IN coins
- **Skill System**: Unlockable auto-win skills after 3 games
- **Coin Management**: Start with 100 coins, win double your bet

### ⚡ Special Features
- **Player Skill**: Guaranteed win for one round (15-second cooldown)
- **Computer AI**: Smart skill usage when behind in score
- **Skill Unlock**: Play 3 games to unlock both player and computer skills
- **Visual Feedback**: Color-coded buttons and real-time status updates

### 🎨 User Interface
- **Dark Theme**: Modern dark color scheme for comfortable gameplay
- **Responsive Design**: Fixed window size with organized layout
- **Visual Indicators**: 
  - Selected moves highlighted
  - Skill cooldown timers
  - Real-time score and coin updates
  - Game status messages

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually comes with Python)

### Running the Game
1. Clone or download the Python file
2. Run the script:
```bash
python rock_paper_scissors_tournament.py
```

## 🎮 How to Play

### Starting a Game
1. **Place Your Bet**: Choose from 10, 25, 50, 100 coins or go ALL IN
2. **Select Your Move**: Click ROCK ✊, PAPER ✋, or SCISSORS ✌️
3. **Play Round**: Click PLAY button to compete against computer
4. **Win Tournament**: First to win 2 rounds wins the tournament

### Using Skills
- **Unlock Requirement**: Complete 3 full tournaments
- **Player Skill**: Click "USE SKILL" before playing a round
- **Computer Skill**: Automatically used when computer is losing
- **Cooldown**: 15 seconds after use

### Game Rules
- **ROCK** beats SCISSORS
- **PAPER** beats ROCK  
- **SCISSORS** beats PAPER
- **Ties** result in no score change
- **Tournament** ends when a player wins 2 rounds

## 🎯 Game Controls

### Action Buttons
- **🎮 PLAY**: Play the current round with selected move
- **⚡ USE SKILL**: Activate auto-win skill (if available)
- **🔄 RESET**: Reset current game and return coins
- **🚪 EXIT**: Close the game

### Betting Options
- **10** 🟢 - Low risk bet
- **25** 🔵 - Medium risk bet  
- **50** 🟡 - High risk bet
- **100** 🔴 - Maximum fixed bet
- **ALL IN** 🟣 - Bet all remaining coins

## 📊 Game Statistics

The game displays real-time information:
- **💰 Coins**: Current coin balance
- **🎯 Current Bet**: Amount wagered in active tournament
- **🏆 Tournament**: Current round progress (1/3, 2/3, 3/3)
- **📊 Score**: Player vs Computer score
- **⚡ Skills**: Player and computer skill status

## 🎨 Color Scheme

- **Background**: Dark gray (#1a1a1a)
- **Cards**: Medium gray (#2d2d2d) 
- **Text**: Black (#000000) for maximum contrast
- **Accents**: Orange (#ff6b35) for highlights
- **Buttons**: Color-coded by function:
  - Green 🟢: Play and low bets
  - Blue 🔵: Reset and medium bets
  - Yellow 🟡: Skill and high bets
  - Red 🔴: Exit and maximum bets
  - Purple 🟣: All-in bets

## 🔧 Technical Details

### Global Variables
- `player_coins`: Track player's currency
- `current_bet`: Active tournament wager
- `games_played`: Count completed tournaments
- `skill_cooldown`: 15-second skill delay
- `games_required_for_skill`: 3 games to unlock

### Key Functions
- `play()`: Main game logic and round resolution
- `use_player_skill()`: Activate player's auto-win
- `check_tournament_winner()`: Determine tournament outcome
- `update_skill_unlock_status()`: Manage skill availability

## 🏆 Winning Strategies

1. **Start Small**: Begin with 10-coin bets to learn the game
2. **Manage Bankroll**: Don't go ALL IN until you're confident
3. **Save Skills**: Use skills strategically in crucial rounds
4. **Watch Patterns**: Computer may have subtle move patterns
5. **Reset Wisely**: Use RESET to recover coins from losing positions

## 🐛 Known Issues

- Game requires manual bet placement for each tournament
- Skills remain locked until exactly 3 games are completed
- No save/load functionality for game progress

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Feel free to fork this project and submit pull requests for:
- New features
- Bug fixes
- UI improvements
- Additional game modes

## 🎯 Future Enhancements

Planned features for future versions:
- [ ] Save/Load game progress
- [ ] Multiple difficulty levels
- [ ] Achievement system
- [ ] Sound effects and music
- [ ] Online multiplayer
- [ ] Tournament history

---

**Enjoy playing!** 🎮 If you have any questions or suggestions, feel free to open an issue or contribute to the project.
