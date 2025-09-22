import sys
from collections import defaultdict
d = defaultdict(int)
str = input()
n = int(input())
for _ in range(n):
    word, score = input().split()
    score = int(score)
    d[word] = score

m = int(input())
for _ in range(m):
    word1, word2, score = input().split()
    score = int(score)
    d[word1+word2] = max(d[word1+word2], score)

way = []
ans = -1e9
def dfs(s):
    global ans
    cur = 0
    if s == '':
        for w in range(len(way)):
            cur += d[way[w]]
        if w + 1 < len(way) and d[way[w]+way[w+1]] != 0:
            cur += d[way[w]+way[w+1]]
        # print(cur)
        ans = max(ans, cur)
        return ans
    for word, score in d.items():
        if s.startswith(word):
            way.append(word)
            dfs(s[len(word):])
            way.pop()
    return 0
dfs(str)
print(ans if ans != -1e9 else 0)