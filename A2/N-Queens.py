n = input()
board = [[0 for i in xrange(n)] for j in xrange(n)]


def is_attacked(x, y):
    for i in xrange(n):
        if board[x][i] or board[i][y]:
            return True

    i, j = x - 1, y + 1
    while 0 <= i and j < n:
        if board[i][j] == 1:
            return True
        i -= 1
        j += 1

    i, j = x - 1, y - 1
    while 0 <= i and 0 <= j:
        if board[i][j] == 1:
            return True
        i -= 1
        j -= 1

    i, j = x + 1, y - 1
    while i < n and 0 <= j:
        if board[i][j] == 1:
            return True
        i += 1
        j -= 1

    i, j = x + 1, y + 1
    while i < n and j < n:
        if board[i][j] == 1:
            return True
        i += 1
        j += 1
    return False


def N_Queens(N, z):
    if N == 0: return True
    for i in xrange(z, z + 1):
        for j in xrange(n):
            if is_attacked(i, j):
                continue
            board[i][j] = 1
            if N_Queens(N - 1, i + 1):
                return True
            board[i][j] = 0
    return False


if N_Queens(n, 0):
    for i in xrange(n):
        for j in xrange(n):
            print board[i][j],
        print
else:
    print "Not possible"