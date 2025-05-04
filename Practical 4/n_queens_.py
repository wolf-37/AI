def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col, n):
    # Check the current column
    for i in range(row):
        if board[i][col]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False
    return True

def solve_n_queens_backtracking(board, row, n):
    if row == n:
        # If all queens are placed, print the solution
        print_board(board)
        return True

    found_solution = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True  # Place the queen

            # Recur to place the rest of the queens
            found_solution = solve_n_queens_backtracking(board, row + 1, n) or found_solution

            # If placing the queen at (row, col) didn't lead to a solution, backtrack
            board[row][col] = False
    return found_solution

def n_queens_backtracking(n):
    board = [[False] * n for _ in range(n)]  # Initialize n x n board with False (no queens placed)
    if not solve_n_queens_backtracking(board, 0, n):
        print("No solution exists.")

def is_safe_branch_and_bound(row, col, cols, diags1, diags2, n):
    return not (cols[col] or diags1[row + col] or diags2[row - col + (n - 1)])

def solve_n_queens_branch_and_bound(row, n, cols, diags1, diags2, board):
    if row == n:
        # If all queens are placed, print the solution
        print_board(board)
        return True
    found_solution = False

    for col in range(n):
        if is_safe_branch_and_bound(row, col, cols, diags1, diags2, n):
            # Place the queen
            board[row][col] = True
            cols[col] = True
            diags1[row + col] = True
            diags2[row - col + (n - 1)] = True

            # Recur to place the rest of the queens
            found_solution = solve_n_queens_branch_and_bound(row + 1, n, cols, diags1, diags2, board) or found_solution
            board[row][col] = False
            cols[col] = False
            diags1[row + col] = False
            diags2[row - col + (n - 1)] = False
    return found_solution

def n_queens_branch_and_bound(n):
    board = [[False] * n for _ in range(n)]  # Initialize n x n board with False (no queens placed)
    cols = [False] * n
    diags1 = [False] * (2 * n - 1)  # For "/" diagonals
    diags2 = [False] * (2 * n - 1)  # For "\" diagonals
    if not solve_n_queens_branch_and_bound(0, n, cols, diags1, diags2, board):
        print("No solution exists.")

# n_queens_backtracking(4)

n_queens_branch_and_bound(4)

