def gauss(A, B):
    if len(A) == len(A[0]) == len(B):
        l = len(A)
        #print(l) #del
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
                #print(i, A[i][k])
            B[i] /= norm
           # print(i, B[i])
            for j in range(i+1, l):
                koef = A[j][i]
                for k in range(l):
                    A[j][k] -= A[i][k] * koef
                B[j] -= B[i] * koef
        #print(A) #del
        #print(B) #del
        X = []
        for i in range(l):
            X.append(0)
        X[l-1] = B[l-1] / A[l-1][l-1]
        for i in range(l-1, -1, -1):
            for j in range(l):
                X[i] -= A[i][j] * X[j]
            X[i] += B[i]
        return X



def slau_drop_lz(A, B):
    if len(A[0]) > 1:
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                lz = 0
                for k in range(1, len(A[j])):
                    if A[i][k-1] / A[j][k-1] != A[i][k] / A[j][k]:
                        lz += 1

                if B[i] / B[j] != A[i][0] / A[j][0]:
                    lz += 1

                if lz == 0:
                    #print('минус строчка')
                    A.pop(j)
                    B.pop(j)
                    break
    return A, B



S= [[2, 1, 1], [4, 2, 2], [1, 1, 1,], [6, 3, 3]]
s = [2, 4, 6]
#print(gauss(S, s))
print(slau_drop_lz(S, s))
