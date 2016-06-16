#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def noise():
    return random.randint(-7, 7)

def main():
    M = 9
    N = 2000
    A = [-0.13, 0.2, -0.31, -0.2, -0.18, -0.2, 0.3, 0.1, -0.25]
    X = [-5, 2, 3, -6, -2, -7, 2, -5, -4]
    print(A)

    for n in range(M, N):
        xk = 0.0
        for k in range(M):
            xk += A[k] * X[n-k-1] + noise()
        X.append( xk )

    for i in range( len(X) ):
        print(X[i])


if __name__ == '__main__':
    main()
