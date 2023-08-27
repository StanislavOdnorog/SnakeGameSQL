# SnakeGameSQL
A unique Snake game variation with 45-degree turns and PostgreSQL score tracking

# Snake Game Variation with PostgreSQL Connection

Welcome to the Snake game variation where you can turn the snake at 45-degree angles and save your results to a PostgreSQL database. This project provides an exciting twist on the classic Snake game, allowing for more strategic gameplay and enabling players to record their achievements in a database.

## Features

- Unique gameplay: Enjoy a Snake game that lets you turn the snake at 45-degree angles for enhanced maneuverability.
- PostgreSQL integration: Connect to a PostgreSQL database to store and track your game scores over time.
- Intuitive controls: Use arrow keys for basic movement and Q, W, E, R keys for diagonal turns.
- Leaderboard: Compete with yourself and others as you strive to achieve the highest score.
- Open-source and extensible: The project is open for contributions, so you can customize and improve it as you wish.

## Installation and Usage

1. Clone the repository and navigate to the project directory.
2. Set up a virtual environment and install the required dependencies.
3. Configure the PostgreSQL database connection in `build/src/lib/db_attributes.py`.
4. Run the game by executing `SnakeGame.exe` in the `build` folder.
5. Play the game, collect food, and see your scores saved to the database.

---
OR
---

1. Clone the repository and navigate to the project directory.
2. Set up a virtual environment and install the required dependencies.
3. Configure the PostgreSQL database connection in `src/lib/db_attributes.py`.
4. Run the game by executing `game.py` in the `src` folder.
5. Play the game, collect food, and see your scores saved to the database.

## Database Configuration

Before you can run the game, you need to configure the database connection details in the `db_attributes.py` file located in `build/src/lib`. Modify the file with your PostgreSQL database credentials:

```python
# db_attributes.py

ATTRIBUTES = {
    "database": "***",
    "host": "***",
    "user": "***",
    "password": "***"
}
```

## Contributing

Contributions are welcome! If you have ideas for improvements, bug fixes, or new features, please submit a pull request. Let's make this game even better together.
