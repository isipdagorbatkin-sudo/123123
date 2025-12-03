import random

def print_board(board):
    size = len(board)
    print("  ", end="")
    for i in range(1, size + 1):
        print(i, end=" ")
    print()

    for i in range(size):
        print(i + 1, end=" ")
        for j in range(size):
            print(board[i][j], end=" ")
        print()


def check_winner(board, player):
    size = len(board)

    # Проверка строк
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Проверка столбцов
    for col in range(size):
        if all(board[row][col] == player for row in range(size)):
            return True

    # Главная диагональ
    if all(board[i][i] == player for i in range(size)):
        return True

    # Побочная диагональ
    if all(board[i][size - 1 - i] == player for i in range(size)):
        return True

    return False


def board_full(board):
    for row in board:
        if "." in row:
            return False
    return True


# Главный
while True:

    # Ввод размера поля
    while True:
        try:
            size = int(input("Введите размер поля (3-9): "))
            if 3 <= size <= 9:
                break
            else:
                print("Неверный размер, введите число от 3 до 9")
        except:
            print("Ошибка ввода. Введите число")

    # Создаем поле
    board = [["." for _ in range(size)] for _ in range(size)]

    # Случайный выбор первого игрока
    current_player = random.choice(["X", "O"])
    print(f"\nПервым ходит {current_player}!\n")

    # Игровой процессы
    while True:
        print_board(board)

        # Ввод хода
        while True:
            try:
                move = input(f"Ход игрока {current_player}. Введите строку и столбец (например: 1 2): ")
                row, col = map(int, move.split())

                if row < 1 or row > size or col < 1 or col > size:
                    print("Координаты вне поля. Попробуйте снова.")
                    continue

                if board[row - 1][col - 1] != ".":
                    print("Эта клетка уже занята. Попробуйте другую.")
                    continue

                break
            except:
                print("Ошибка ввода. Введите два числа через пробел (например: 1 2)")

        board[row - 1][col - 1] = current_player

        # Проверка победы
        if check_winner(board, current_player):
            print_board(board)
            print(f"Игрок {current_player} ПОБЕДИЛ!")
            break

        # Проверка ничьи
        if board_full(board):
            print_board(board)
            print("НИЧЬЯ!")
            break

        # Смена игрока
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    # Повтор игры
    again = input("\nХотите сыграть ещё раз? (да/нет): ").lower()
    if again != "да":
        print("Спасибо за игру!")
        break