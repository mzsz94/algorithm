import sys

sys.stdin = open("./sujin_love_manjae.txt",'r')
N = int(input())
factory = [list(map(int, input().split(' '))) for _ in range(N)]
print(factory)

def solution(factory):
  """
  factory: List of lists, factory[i][j] == 1 이면
  i번 공장이 j번 부품을 생산할 수 있음.
  모든 공장을 커버(계약)하기 위한 최소 부품 수를 반환.
  """
  N = len(factory)                 # 공장 수
  visited = [0 for _ in range(N)]           # covered[i]: i번 공장 계약 여부
  # parts[i]: i번 공장이 만들 수 있는 부품 번호 리스트
  parts = [[] for _ in range(len(factory))]
  i = 0
  for row_p in factory:
    for no_p, yn  in enumerate(row_p):
      if yn == 1:
        parts[i].append(no_p)
    i += 1

  print("DBG = ")
  print(parts)
  best = [N + 1]                   # 최소 부품 수 (mutable)

  def dfs(used, done):
    if used > best[0]:
      return
    if done == N:
      return
    
    f = 0
    while visited[f]:
      f += 1
    
    for i in parts[f]:
      lst = []
      if not visited[i]:
        if factory[f][i] == 1:
          lst.append(i)
        
        dfs(used+1, done+len(lst))
    
    for i in lst:
      visited[i] = 0


  dfs(0, 0)
  return best[0]

solution(factory)
