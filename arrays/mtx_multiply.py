import numpy as np

def mtx_multiply():
    '''
    Lets user input define two matrices and multiply them.
    '''
    n,m,k = map(int, raw_input().split())

    a = np.zeros((n,m))
    b = np.zeros((m, k))

    for row_idx in range(n):
        row = map(int, raw_input().split())
        a[row_idx] = row

    for row_idx in range(m):
        row = map(int, raw_input().split())
        b[row_idx] = row

    c = np.zeros((n,k))
    for row_idx in range(n):
        row = a[row_idx]
        for col_idx in range(k):
            col = b[:,col_idx]
            c[row_idx, col_idx] = row_col_multiply(row, col)

    print_mtx(c, n, k)

def row_col_multiply(row, col):
    if len(row) != len(col):
        return 0
    n = len(row)
    total = 0
    for idx in range(n):
        total += row[idx] * col[idx]
    return total

def print_mtx(mtx, num_row, num_col):
    for row_idx in range(num_row):
        row = ""
        for col_idx in range(num_col):
            row += str(int(mtx[row_idx, col_idx])) + " "
        print row
