import sys
import numpy as np

n, m, h = map(int, sys.stdin.readline().split())
X = np.ones((n, m))
W1 = np.triu  (np.ones((m, h)))
W2 = np.triu(np.ones((m, h)))
W3 = np.triu(np.ones((m, h)))
Q = X @ W1
K = X @ W2
V = X @ W3

scores = Q @ K.T
scale = scores / np.sqrt(h)
print(scale)
row_sum = scale.sum(axis=1, keepdims=True)
attn_weights = scale / row_sum
Y = attn_weights @ V
total_sum = np.round(np.sum(Y).astype(int))
print(total_sum)