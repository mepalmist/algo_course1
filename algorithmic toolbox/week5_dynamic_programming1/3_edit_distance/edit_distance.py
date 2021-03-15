# Uses python3
def edit_distance(s, t):
    l_min = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]


    for i in range(0, len(s)+1):
        for j in range(0, len(t)+1):
            if i == 0:
                l_min[i][j] = j
            elif j == 0:
                l_min[i][j] = i

            elif s[i-1] == t[j-1]:
                l_min[i][j] = l_min[i-1][j-1]
            else:
                l_min[i][j] = 1 + min(l_min[i-1][j], l_min[i][j-1], l_min[i-1][j-1])


    return l_min[len(s)][len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
