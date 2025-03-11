def print_matriz(M, decimals = 3):
    for row in M:
        print([round(x, decimals)+0 for x in row])

def zeros_matriz(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len (M[-1]) < cols:
            M[-1].append(0.0)
    return M

def GaussJordan(augMat):
    n = len(augMat)
    m = len(augMat[0])

    # Normalizar cada linha
    # L_i <- L_i/a_ii
    for i in range (n):
        # Verificar se o pivo pode ser definido ou não
        if augMat [i][i] == 0:
            for j in range(i + 1, n):
                if augMat[j][i] != 0:
                    augMat[i], augMat[j] = augMat[j], augMat[i]
                    break
                else:
                    # Caso não encontre linha com valor diferente de zero temos uma singularidade
                    raise ValueError("Matriz Singular")


        if augMat[i][i] != 1:
            divisor = augMat[i][i]
            for k in range(m):
                augMat[i][k] /= divisor
        else:
            pass

        # Zerando as entradas do pivô
        # L_j <- L_j - a_ji * L_i
        for j in range(n):
            if i != j:
                coef = augMat[j][i]
                for k in range(m):
                    augMat[j][k] -= coef * augMat[i][k]
            else:
                pass

    print_matriz(augMat)

matriz = [
    [0.0, 2.0, -4.0, 3.0], 
    [2.0, 3.0, 3.0, 15.0], 
    [5.0, -3.0, 1.0, 14.0]
]

GaussJordan(matriz)