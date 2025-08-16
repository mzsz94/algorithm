import sys
import copy
sys.stdin = open("./algorithm/strawberry/input.txt",'r')

N, M, R = map(int, sys.stdin.readline().split(' '))
# print(N, M, R)
arr = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
# print(arr)
# tmp = [[0] * M for _ in range(N)]


def rotate(tmp, sr,sc,n,m):
  global arr
  for _ in range(min(n,m)//2):
    # print(min(n,m)//2)
    er, ec = n-sr-1, m-sc-1
    # print("er,ec,sr,sc=",er, ec, sr, sc)
    lst = []
    for c in range(sc+1,ec+1):
      lst.append(tmp[sr][c])
    # print(lst)
    for c in range(len(lst)):
      arr[sr][sc+c] = lst[c]
      # print(arr[0][:])
    # print(arr[0][:])

    # print(arr)
    lst = []
    for r in range(sr+1, er+1):
      lst.append(tmp[r][ec])
    # print(lst)
    for r in range(len(lst)):
      arr[sr+r][ec] = lst[r]
    
    # print(arr)
    
    lst = []
    for c in range(ec):
      lst.append(tmp[er][c])
    for c in range(sc+1, ec+1):
      arr[er][c] = lst[c-1]
    # print(arr)
  
    lst = []
    # print(tmp)
    for r in range(er):
      lst.append(tmp[r][sc])
    for r in range(sr+1, er+1):
      arr[r][sc] = lst[r-1]
    # print(arr)
    lst = tmp[sr][sc]
    arr[sr+1][sc] = lst
    # print(arr)

    sr+=1
    sc+=1

#main
sr, sc = 0, 0
n, m = N, M
R = R%((N+M)*2-2)
for _ in range(R):
  tmp = copy.deepcopy(arr)
  # for i in range(N):
    # for j in range(M):
      # tmp[i][j] = arr[i][j]
  rotate(tmp, sr, sc, n, m)

for row in arr:
  print(*row)