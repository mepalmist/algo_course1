# Uses python3
import sys
import numpy as np

def optimal_weight(W, w):
    # write your code here

    arr = np.zeros(shape=(len(w), W + 1), dtype=int)

    for j in range(0, len(w)):
        for i in range(1, W + 1):
            if w[j] > i:
                arr[j, i] = arr[j - 1, i]
            else:
                arr[j, i] = max(w[j] + arr[j - 1, i - w[j]], arr[j - 1, i])
    return arr[len(w) - 1, W]

if __name__ == '__main__':
    input = sys.stdin.read()
#    input = input()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
