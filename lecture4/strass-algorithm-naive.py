#!/usr/bin/python

def strassen(A, B):

    if len(A) == 2 and len(A[0]) == 2 and len(B) == 2 and len(B[0]) == 2:

        p1 = A[0][0] * (B[0][1] - B[1][1])
        p2 = (A[0][0] + A[0][1]) * B[1][1]
        p3 = B[0][0] * (A[1][0] + A[1][1])
        p4 = A[1][1] * (B[1][0] - B[0][0])
        p5 = (A[0][0] + A[1][1]) * (B[0][0] + B[1][1])
        p6 = (A[0][1] - A[1][1]) * (B[1][0] + B[1][1])
        p7 = (A[0][0] - A[1][0]) * (B[0][0] + B[0][1])

        C = [[0,0], [0,0]]
        C[0][0] = p5 + p4 - p2 + p6
        C[0][1] = p1 + p2
        C[1][0] = p3 + p4
        C[1][1] = p1 + p5 - p3 - p7
        return C
    else:
        raise ValueError("Wallah matricen er ikke 2x2")
    
A = [[1,2], [3,4]]
B = [[5,6], [7,8]]

result = strassen(A, B)
for row in result:
    print(row)