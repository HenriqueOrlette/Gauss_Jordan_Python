import numpy as np

#A = np.array([[3.0, 2.0, -4.0], [2.0, 3.0, 3.0], [5.0, -3, 1.0]])
#b = [3.0, 15.0, 14.0]

#print(A, '\n')
#print(b)

#solution_01 = np.linalg.solve(A, b)
#print(solution_01)

# Presença de Singlaridade

A = np.array([[-1.0, 1.0, 2.0], [1.0, 2.0, 1.0], [-2.0, -1.0, 1.0]])
b = np.array([[0.0, 6.0 -6.0]])

try:
    solution_02 = np.linalg.solve(A, b)
    print(solution_02)
except np.linalg.LinAlgError:
    print("LinalgError: MATRIZ SINGULAR")