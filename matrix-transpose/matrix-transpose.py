import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    arr_tansp = np.zeros((len(A[0]),len(A)))
    for i,x in enumerate(A):
        for j,y in enumerate(x):
            arr_tansp[j][i] = A[i][j]
    return arr_tansp
    pass
