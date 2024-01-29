# Tic-Tac-Toe in Python

This project is a command-line implementation of Tic-Tac-Toe in Python, employing object-oriented programming (OOP) principles. It serves as a practical exercise for Python language concepts and testing.

## Features

- **Object-Oriented Design:**
  - Utilizes classes for players, the game board, and game management.
  
- **Input Validation:**
  - Ensures valid moves through player input validation.
  
- **Win and Draw Conditions:**
  - Detects win and draw conditions for a seamless gaming experience.
  
- **User-Friendly Interface:**
  - Presents a simple text-based interface for smooth user interaction.

- **Principles Followed:**
  - **Divide Concerns:**
    - Components are logically separated for better code organization and readability.

  - **Function Reusability:**
    - Functions are designed for reuse, promoting maintainability and efficiency.

  - **Good UX:**
    - Emphasizes clarity and intuitive prompts for a positive user experience.

  - **Compatibility:**
    - Compatible with both Windows and Linux operating systems.

  - **Simple UI:**
    - Features a clean and straightforward user interface.

  - **Performance:**
    - Optimized for efficient resource usage, ensuring a smooth gaming experience.

## Testing Structure

- **Unit Tests:**
  - The `tests` directory contains unit tests for individual components.
  - Run tests using a testing framework such as `unittest`.

- **Integration Tests:**
  - The `tests` directory may include integration tests for combined functionalities.
  - Ensure the entire system functions correctly in different scenarios.

- **Test Coverage:**
  - Strive for high test coverage to validate the robustness of the codebase.

## How to Run Tests

1. **Navigate to the project directory.**

    ```bash
    cd TicTacToe-py
    ```

2. **Run Unit Tests:**

    ```bash
    python -m unittest test_fun.py
    python -m unittest test_player.py
    ```

## Requirements

- Python 3.x

## How to Play

1. **Clone the repository to your local machine.**

    ```bash
    git clone https://github.com/Yousefeslam214/TicTacToe-py.git
    ```

2. **Navigate to the project directory.**

    ```bash
    cd TicTacToe-py
    ```

3. **Run the game.**

    ```bash
    python main.py
    ```

4. **Follow the on-screen instructions to make moves and enjoy the game.**

## Project Structure

- `main.py`: Main script to run the Tic-Tac-Toe game.
- `player.py`: Contains the `Player` class for handling player details.
- `menu.py`: Defines the `Menu` class for displaying menus.
- `help_fun.py`: Includes helper functions (e.g., screen clearing).
- ...

## Contributions

Contributions are welcome! If you find any issues or want to improve the project, feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
