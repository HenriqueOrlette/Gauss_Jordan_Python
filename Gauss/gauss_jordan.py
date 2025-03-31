#a
matrix = [[2.0, 3.0, 5.0], [4.0, -1.0, 7.0]]
#b
#matrix = [[2.0, 3.0, 1.0, 0.0], [1.0, -2.0, -1.0, 1.0], [1.0, 4.0, 1.0, 2.0]]
#c
#matrix = [[2.0, 2.0, -3.0, 4.0], [1.0, 3.0, 1.0, 11.0], [2.0, 5.0, -4.0, 13.0]]
#d
#matrix = [[1.0, 1.0, 1.0, 1.0], [1.0, -1.0, 1.0, 2.0], [2.0, 2.0, 2.0, 5.0]]
#e
#matrix = [[1.0, 1.0, 1.0, 1.0], [1.0, -1.0, 1.0, 2.0], [2.0, 0.0, 2.0, 3.0]]
#f
#matrix = [[2.0, 1.0, -2.0, 10.0], [3.0, 2.0, 2.0, 1.0], [5.0, 4.0, 3.0, 4.0]]

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

def coef_matrix(augMat):

    # Recuperando as dimensoes da matriz coeficiente
    rows = len(augMat)
    cols = len(augMat[0])
    # Section 2: Cria uma nova matriz de zeros
    MC = zeros_matriz(rows, cols - 1)
    # Section 3: Copia os valores de M para dentro da cópia
    for i in range(rows):
        for j in range(cols - 1):
            MC[i][j] = augMat[i][j]
    return MC

def determinant(AM):

    n = len(AM)
    # Reducao a forma triangular superior
    for fd in range(n):
        if AM[fd][fd] == 0:
            for j in range(fd + 1, n):
                if AM[j][fd] != 0:
                    AM[fd], AM[j] = AM[j], AM[fd]
                break
            else:
    # Se um pivo nao for encontrado, a matriz é singular
                return 0
        for i in range(fd+1, n):
            crScaler = AM[i][fd] / AM[fd][fd] 
            for j in range(n):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
    # Uma vez que temos a forma triangular, calculamos o produto da diagonal principal
    product = 1.0
    for i in range(n):
        product *= AM[i][i]
    return product

def verifica_non_singularidade(A):
    det = determinant(A)
    if det != 0:
        return True
    else:
        raise ArithmeticError("Matriz Singular!")

def GaussJordanMethod(augMat):
    n = len(augMat)
    m = len(augMat[0]) 
    for i in range(n):
    # Verifica se o pivo eh zero e muda a linha se necessario
        if augMat[i][i] == 0:
            for j in range(i + 1, n):
                if augMat[j][i] != 0:
                    augMat[i], augMat[j] = augMat[j], augMat[i]
                break
            else:
        # Se um pivo nao for encontrado, a matriz eh singular
                raise ValueError("Matriz singular!.")
        # Normalizando cada linha
        # L_i <-- L_i/a_ii
        if augMat[i][i] != 1:
            divisor = augMat[i][i]
            for k in range(m):
                augMat[i][k] /= divisor
        else:
            pass
        # Zera as entradas referentes aos pivos
        # L_j <-- L_j - a_ji * L_i
        for j in range(n):
            if i != j:
                coef = augMat[j][i]
                for k in range(m):
                    augMat[j][k] -= coef * augMat[i][k]
            else:
                pass
        print_matriz(augMat)
        print(" ")

def GaussJordan(augMat):
    print("\nCoeficiente:")
    mc = coef_matrix(matrix)
    print_matriz(mc)
    
    try:
        print("\nDeterminante:")
        det = determinant(mc)
        print(det)
        result = verifica_non_singularidade(mc)
        print("\nÉ não singular?")
        print(result)
        print("\nResolução Gauss_Jordan:")
        GaussJordanMethod(matrix)
        print_matriz(matrix)
    except (ArithmeticError, ValueError) as erro:
        print(f"Erro: {erro}") 

GaussJordan(matrix)
