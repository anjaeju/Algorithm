import numpy as np

def matmul(a, b):
    if a.shape[1] != b.shape[0]:
        print('The shapes of matrices are not matched.')

    tmp = np.zeros((a.shape[0], b.shape[1]))
    
    for i in range(a.shape[0]):                 
        tmp[i] = a[i][0] * b[0] + a[i][1] * b[1]

    print(tmp)
        
if __name__=='__main__'

    a = np.arange(0, 10)
    a = a.reshape(-1, 2)

    b = np. arange(10, 20)
    b = b.reshape(2, -1)
    print(a)
    print(b)

    res = matmul(a, b)
    print(res)