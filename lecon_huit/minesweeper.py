"""
    ** Обратный "Cапер".
    В игре "Сапер" у вас есть доска с несколькими минами,
    а на тех ячейках, которые не содержат мины, есть номер,
    который указывает общее количество мин в соседних ячейках.
    Дана расстановки мин, необходимо создать игровое поле с цифрами.
    Например, для расстановки мин
    matrix = [[true, false, false],
              [false, true, false],
              [false, false, false]]
    игровое поле будет выглядеть так:
    minefield = [[1, 2, 1],
                 [2, 1, 1],
                 [1, 1, 1]]
"""


def minesweeper(matrix):
    minefield = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'true':
                print(i, j)
                if i == 0 and j == 0:
                    minefield[i][j + 1] += 1
                    minefield[i + 1][j + 1] += 1
                    minefield[i + 1][j] += 1
                elif i == len(matrix) - 1 and j == len(matrix) - 1:
                    minefield[i - 1][j] += 1
                    minefield[i - 1][j - 1] += 1
                    minefield[i][j - 1] += 1
                elif i == 0 and j == len(matrix) - 1:
                    minefield[i][j - 1] += 1
                    minefield[i + 1][j - 1] += 1
                    minefield[i + 1][j] += 1
                elif i == len(matrix) - 1 and j == 0:
                    minefield[i - 1][j] += 1
                    minefield[i][j + 1] += 1
                    minefield[i - 1][j + 1] += 1
                elif i == 0 and j not in (0, len(matrix) - 1):
                    minefield[i][j - 1] += 1
                    minefield[i + 1][j - 1] += 1
                    minefield[i + 1][j] += 1
                    minefield[i + 1][j + 1] += 1
                    minefield[i][j + 1] += 1
                elif i == len(matrix) - 1 and j not in (0, len(matrix) - 1):
                    minefield[i][j - 1] += 1
                    minefield[i - 1][j - 1] += 1
                    minefield[i - 1][j] += 1
                    minefield[i - 1][j + 1] += 1
                    minefield[i][j + 1] += 1
                elif j == 0 and i not in (0, len(matrix) - 1):
                    minefield[i - 1][j] += 1
                    minefield[i - 1][j + 1] += 1
                    minefield[i][j + 1] += 1
                    minefield[i + 1][j + 1] += 1
                    minefield[i + 1][j] += 1
                elif j == len(matrix) - 1 and i not in (0, len(matrix) - 1):
                    minefield[i - 1][j] += 1
                    minefield[i - 1][j - 1] += 1
                    minefield[i][j - 1] += 1
                    minefield[i + 1][j - 1] += 1
                    minefield[i + 1][j] += 1
                else:
                    minefield[i - 1][j - 1] += 1
                    minefield[i - 1][j] += 1
                    minefield[i - 1][j + 1] += 1
                    minefield[i][j + 1] += 1
                    minefield[i + 1][j + 1] += 1
                    minefield[i + 1][j] += 1
                    minefield[i + 1][j - 1] += 1
                    minefield[i][j - 1] += 1

    return minefield


matrix = [['true', 'false', 'false'],
          ['false', 'true', 'false'],
          ['false', 'false', 'false']]

# matrix = [['false', 'true', 'false'],
#           ['false', 'true', 'false'],
#           ['false', 'false', 'true']]

# matrix = [['true', 'false', 'false'],
#           ['true', 'false', 'false'],
#           ['false', 'false', 'false']]

# matrix = [['false', 'false', 'true'],
#           ['false', 'false', 'true'],
#           ['true', 'true', 'true']]

for line in minesweeper(matrix):
    print(line)
