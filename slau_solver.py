import copy
def gauss(A, B):
    if len(A) == len(A[0]) == len(B):
        l = len(A)
        for i in range(l-1):
            n = i + 1
            while A[i][i] == 0:
                A[i], A[n] = A[n], A[i]
                B[i], B[n] = B[n], B[i]
                if n > l:
                    raise ValueError('At least one of the coefficients of a variable should not be zero')
                n += 1
            norm = A[i][i]
            for k in range(l):
                A[i][k] /= norm
            B[i] /= norm
            for j in range(i+1, l):
                koef = A[j][i]
                for k in range(l):
                    A[j][k] -= A[i][k] * koef
                B[j] -= B[i] * koef
        X = []
        for i in range(l):
            X.append(0)
        if B[l-1] == 0 and A[l-1][l-1] == 0:
            raise ValueError('The system has infinitely many solutions')
        elif B[l-1] != 0 and A[l-1][l-1] == 0:
            raise ValueError('The system has no solution')
        X[l-1] = B[l-1] / A[l-1][l-1]
        for i in range(l-1, -1, -1):
            for j in range(l):
                X[i] -= A[i][j] * X[j]
            X[i] += B[i]
        return X


def slau_drop_null(A, B):
    for i, row in enumerate(A):
        isNull = True
        for element in row:
            if element != 0:
                isNull = False
        if B[i] != 0:
            isNull = False
        if isNull:
            A.pop(i)
            B.pop(i)
    return A, B


def slau_drop_lz(A, B):
    A, B = slau_drop_null(A, B)
    if len(A[0]) > 1:
        for i in range(len(B)-1):
            j = i+1
            while j < len(B):
                isLZ = True
                for k in range(1, len(A[j])):
                    if A[j][k-1] != 0 and A[j][k] != 0 and A[i][k-1] / A[j][k-1] != A[i][k] / A[j][k]:
                        isLZ = False

                if A[i][0] != 0 and B[i] != 0 and B[j] / B[i] != A[j][0] / A[i][0]:
                    isLZ = False

                if isLZ:
                    A.pop(j)
                    B.pop(j)
                else:
                    j += 1
    return A, B


def slau(A, B):
    M = copy.deepcopy(A)
    V = copy.deepcopy(B)
    M, V = slau_drop_lz(M, V)
    if len(M) == len(M[0]) == len(V):
        solution = gauss(M, V)
        return solution
    elif len(M) == len(V) and len(M) < len(M[0]):
        rank = len(M)
        extrank = len(V)
        for i, row in enumerate(M):
            isNull = True
            for element in row:
                if element != 0:
                    isNull = False
            if isNull:
                rank -= 1
        if rank != extrank:
            raise ValueError('The system is underdetermined and has no solution')
        else:
            raise ValueError('The system is underdetermined and has infinitely many solutions')
    elif len(M) == len(V) and len(M) > len(M[0]):
        raise ValueError('The system is overdetermined and has no solution')
    else:
        raise ValueError('Incorrect dimensions')
