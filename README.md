# Tic Tac Toe with Minimax and Greedy Algorithms

This project is a simple implementation of the classic Tic Tac Toe game using Python and Tkinter for GUI.

The AI supports **two strategies**:
- **Minimax Algorithm** (default)
- **Greedy Algorithm** (can be enabled via a toggle button)

The player always plays as **"O"**, and the computer plays as **"X"**.

---

## Features

- Graphical interface using **Tkinter**
- Sound effects for **win**, **lose**, and **draw**
- Timer to track game duration
- Highlight winning cells
- **Switch button** to toggle between **Minimax** and **Greedy**
- Restart and Exit buttons

---

## How to Run

To run the game, simply execute:

```bash
python main.py
```

Make sure you have the required audio files (`win.mp3`, `lose.mp3`, `draw.mp3`) in the same directory.

---

## How to Play

- Click on any empty cell to place your move ("O").
- The computer will respond automatically with its move ("X").
- You can **toggle between Minimax and Greedy** strategies before playing by clicking the "Switch to Greedy / Minimax" button.
- Press **Restart** to start a new game, or **Exit** to close the app.

---

## AI Strategies

### 1. Minimax Algorithm

Minimax is a decision rule used for minimizing the possible loss in a worst-case scenario.  
In this game:
- The AI explores all possible moves recursively.
- It assumes the player is playing optimally.
- It guarantees the best possible outcome (win or draw).

**Time Complexity:**  
`O(b^d)`  
Where:
- `b` = branching factor (possible moves)
- `m` = max depth of the game tree (up to 9 for Tic Tac Toe)

---

### 2. Greedy Algorithm

The greedy strategy simply picks the **first available empty cell**.  
- It does **not** look ahead or try to block the player.
- It's very fast, but it can be easily defeated by a smart human.

**Time Complexity:**  
`O(n)`  
Where:
- `n` = number of empty cells (max 9)

---

## Why Minimax is Better

| Feature            | Minimax           | Greedy             |
|--------------------|-------------------|--------------------|
| Predicts Future    | Yes               | No                 |
| Guarantees Win/Draw| Yes               | No (can lose)      |
| AI Difficulty      | High (unbeatable) | Easy               |
| Time Complexity    | Higher            | Very Low           |

---

## Note
If you want to view the design PDF I pushed (`Tic-Tac-Toe.pdf`), download it first to your device.  
Alternatively, you can [view it directly on Canva](https://www.canva.com/design/DAGlox5a5T0/ZiXOye7cXr4q4bKcSlZJ6A/edit?utm_content=DAGlox5a5T0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).

---
## Team Members
- [Hagar Elbakry](https://github.com/Hagar-Elbakry)
- [Menna Hamada](https://github.com/MennaHamadaElsba3i)