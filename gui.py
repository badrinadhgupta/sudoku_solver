import pygame
pygame.font.init()

FPS = 20
SCREEN_WIDTH, SCREEN_HEIGHT = 450, 490
SCORE_WIDTH = 40

NUMBERS_FONT = pygame.font.SysFont('comicsans', 40)
TEMPORARY_NUMBERS_FONT = pygame.font.SysFont('comicsans', 20)
ERROR_FONT = pygame.font.SysFont('comicsans', 150)

CURRENT_GRID = [None, None]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PLAY SUDOKU!")

grid = [[0 for x in range(0, 10)] for y in range(0, 10)]

main_sudoku = [[5, 0, 0, 0, 1, 0, 0, 0, 4],
          [2, 7, 4, 0, 0, 0, 6, 0, 0],
          [0, 8, 0, 9, 0, 4, 0, 0, 0],
          [8, 1, 0, 4, 6, 0, 3, 0, 2],
          [0, 0, 2, 0, 3, 0, 1, 0, 0],
          [7, 0, 6, 0, 9, 1, 0, 5, 8],
          [0, 0, 0, 5, 0, 3, 0, 1, 0],
          [0, 0, 5, 0, 0, 0, 9, 2, 7],
          [1, 0, 0, 0, 2, 0, 0, 0, 3]]


def checkrow(arr, row, n):
    for i in range(0, 9):
        if arr[row][i] == n:
            return False
    return True


def checkcol(arr, col, n):
    for i in range(0, 9):
        if arr[i][col] == n:
            return False
    return True


def checkbox(arr,r,c,n):
    sr = r-r%3
    sc = c-c%3
    for i in range(3):
        for j in range(3):
            if arr[i+sr][j+sc]==n:
                return False
    return True


def checkzeros(arr,index):
    for row in range(0,9):
        for col in range(0,9):
            if arr[row][col]==0:
                index[0] = row
                index[1] = col
                return True
    return False


def draw_grid():
    for i in range(1, 4):
        box = pygame.Rect(0, 150*i, SCREEN_WIDTH, 5)
        pygame.draw.rect(screen, BLACK, box)
    for i in range(1, 4):
        box = pygame.Rect(150 * i, 0, 5, SCREEN_HEIGHT-SCORE_WIDTH)
        pygame.draw.rect(screen, BLACK, box)
    for i in range(1, 10):
        box = pygame.Rect(0, 50 * i, SCREEN_WIDTH, 2)
        pygame.draw.rect(screen, BLACK, box)
    for i in range(1, 10):
        box = pygame.Rect(50 * i, 0, 2, SCREEN_HEIGHT - SCORE_WIDTH)
        pygame.draw.rect(screen, BLACK, box)


def display_numbers():
    global grid
    for i in range(0, 9):
        for j in range(0, 9):
            if main_sudoku[i][j] != 0:
                if grid[i][j] == 1:
                    box = pygame.Rect(50 * j, 50 * i, 50, 50)
                    pygame.draw.rect(screen, GREEN, box, 2)
                number = NUMBERS_FONT.render(str(main_sudoku[i][j]), True, BLACK)
                screen.blit(number, (50*j+25-number.get_width()//2, 50*i+25-number.get_height()//2))


def draw_window():
    global grid
    screen.fill(WHITE)
    draw_grid()
    display_numbers()
    for i in range(0, 9):
        for j in range(0, 9):
            grid[i][j] = 0
    # input_numbers()
    pygame.display.update()


def solvesudoku(main_sudoku):
    global grid
    index = [0,0]
    if not checkzeros(main_sudoku,index):
        return True

    row = index[0]
    col = index[1]

    for num in range(1,10):
        if checkrow(main_sudoku,row,num) and checkcol(main_sudoku,col,num) and checkbox(main_sudoku,row,col,num):
            main_sudoku[row][col] = num
            grid[row][col] = 1
            draw_window()
            pygame.time.delay(5)
            if(solvesudoku(main_sudoku)):
                return True

            main_sudoku[row][col] = 0

    return False


def selected_box(grid):
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 1:
                box = pygame.Rect(50 * col, 50 * row, 50, 50)
                pygame.draw.rect(screen, GREEN, box, 2)


def error():
    screen.fill(BLACK)
    print('1')
    number = ERROR_FONT.render('SOLUTION NOT POSSIBLE', True, WHITE)
    screen.blit(number, (SCREEN_WIDTH//2 - number.get_width() // 2, SCREEN_HEIGHT - number.get_height() // 2))


def main():
    run = True
    global main_sudoku, CURRENT_GRID
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if not solvesudoku(main_sudoku):
                        print('ERROR')
                if event.key == pygame.K_r:
                    main_sudoku = [[5, 0, 0, 0, 1, 0, 0, 0, 4],
                                      [2, 7, 4, 0, 0, 0, 6, 0, 0],
                                      [0, 8, 0, 9, 0, 4, 0, 0, 0],
                                      [8, 1, 0, 4, 6, 0, 3, 0, 2],
                                      [0, 0, 2, 0, 3, 0, 1, 0, 0],
                                      [7, 0, 6, 0, 9, 1, 0, 5, 8],
                                      [0, 0, 0, 5, 0, 3, 0, 1, 0],
                                      [0, 0, 5, 0, 0, 0, 9, 2, 7],
                                      [1, 0, 0, 0, 2, 0, 0, 0, 3]]
                    draw_window()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)
                if x <= 450 and y <= 450:
                    col = x//50
                    row = y//50
                    CURRENT_GRID = [row, col]
                    for i in range(0, 9):
                        for j in range(0, 9):
                            grid[i][j] = 0
                    grid[row][col] = 1
                    selected_box(grid)

        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()
