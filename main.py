#

def greet():
    print("")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("")
    print("формат ввода: x, y через пробел")
    print("x - номер строки  ")
    print("y - номер столбца ")

def show():
    print()
    print("- 0 1 2")
    for i, row in enumerate(field):
        row_str = f"{i} {' '.join(row)}"
        print(row_str)
    print()

def ask():
    while True:
        cords = input("Ваш ход: ").split()

        if len(cords) != 2:
            print("Введите 2 координаты.")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа.")
            continue

        x, y = int(x), int(y)

        if not (0 <= x <= 2 and 0 <= y <= 2):
            print("Координаты вне диапазона!")
            continue

        if field[x][y] != '-':
            print("Клетка занята!")
            continue
        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            show()
            print("Выиграл X.")
            return True
        if symbols == ["0", "0", "0"]:
            show()
            print("Выиграл 0.")
            return True
    return False

greet()
field = [["-"] * 3 for i in range(3)]
num = 0

while True:

    num += 1
    show()

    if num % 2 != 0:
        print('Ходит крестик.')
    else:
        print('Ходит нолик.')

    x, y = ask()
    if num % 2 != 0:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if check_win():
        break

    if num == 9:
        break
        print('Ничья.')