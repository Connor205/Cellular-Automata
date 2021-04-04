from graphics import *
import numpy as np
import random

window_width = 20000
window_height = 1000
cell_size = 10


def main():
    win = GraphWin("Cellular Automota",
                   window_width,
                   window_height,
                   autoflush=False)
    grid = generate_grid(0.65, 100, 50)
    # print(np.array(grid))
    render_grid(grid, win)
    win.update()
    cont = True
    while cont:
        key = win.checkKey()
        if key == 'a':
            grid = automota_pass(grid)
            render_grid(grid, win)
            win.update()
        clicked = win.checkMouse()
        if clicked:
            cont = False
    win.close()


def generate_grid(bias: float = 0.5,
                  width: int = 100,
                  height: int = 50) -> list:
    """Generates a grid of 1s and 0s based on random noise. 
    The lower the bias the less white space, the higher the value the more walls

    Args:
        bias (int, optional): Bias towards open. Defaults to 0.5:float.
        width (int, optional): width of grid. Defaults to 100:int.
        height (int, optional): height of grid. Defaults to 50:int.

    Returns:
        Grid: A randomly generated grid
    """
    grid = [[None for x in range(width)] for y in range(height)]
    for row in range(height):
        for col in range(width):
            generated_val = random.random()
            grid[row][col] = generated_val < bias
    print(np.array(grid))
    return grid


def render_grid(grid: list, win: GraphWin):
    """Renders the grid to the given GraphWin.

    Args:
        grid (list[list[boolean]]): a boolean grid
        win (GraphWin): the graphical window to draw on
    """
    height = len(grid)
    width = len(grid[0])
    for row in range(height):
        for col in range(width):
            cell = Rectangle(
                Point(col * cell_size, row * cell_size),
                Point(col * cell_size + cell_size,
                      row * cell_size + cell_size))
            if grid[row][col]:
                cell.setFill('white')
            else:
                cell.setFill('grey')
            cell.setOutline("")
            cell.draw(win)


def coord_in_range(row: int, col: int, grid: list):
    return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])


def automota_pass(grid):
    height = len(grid)
    width = len(grid[0])
    new_grid = [[None for x in range(width)] for y in range(height)]
    for row in range(height):
        for col in range(width):
            trues = 0
            if coord_in_range(row, col, grid) and grid[row][col]:
                trues += 1
            row -= 1
            col -= 1
            # Upper left
            if coord_in_range(row, col, grid) and grid[row][col]:
                trues += 1
            col += 1
            if coord_in_range(row, col, grid) and grid[row][col]:
                trues += 1
            col += 1
            if coord_in_range(row, col, grid) and grid[row][col]:
                trues += 1
            row += 1
            if coord_in_range(row, col, grid) and grid[row][col]:
                trues += 1
            row += 1
            if coord_in_range(row, col, grid) and grid[row][col]:
                trues += 1
            col -= 1
            if coord_in_range(row, col, grid) and grid[row][col]:
                trues += 1
            col -= 1
            if coord_in_range(row, col, grid) and grid[row][col]:
                trues += 1
            row -= 1
            if coord_in_range(row, col, grid) and grid[row][col]:
                trues += 1
            col += 1
            new_grid[row][col] = trues > 4
    return new_grid


main()
