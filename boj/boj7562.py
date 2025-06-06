from collections import deque
T = int(input())

d = [
[-2,-1], #1
[-1,-2], #1-1
[-2,1], #2
[-1,2], #2-2
[2,1], #3
[1,2], #3-1
[2,-1], #4
[1,-2] #4-1
]


for _ in range(T):
	I = int(input())
	p_cur = list(map(int, input().split(' ')))
	p_target = list(map(int, input().split(' ')))
	
	q = deque() # ===> DON'T FORGET
	
	q.append([p_cur[0],p_cur[1], 0])
	# print(T,I)
	# print(p_cur,p_target)
	
	visited = [[0 for _ in range(I)] for _ in range(I)]
	visited[p_cur[0]][p_cur[1]] = 1
	# print(arr)

	while q:
		r, c, cnt = q.popleft()
		# print("DBG r, c, cnt", r, c, cnt
		if(r == p_target[0] and c == p_target[1]):
			# print(cnt[p_target[0]][p_target[1]])
			print(cnt)
			break
		for dr, dc in d:
			nr, nc = r+dr, c+dc
			if -1 < nr < I and -1 < nc < I:
				if not visited[nr][nc]:
					visited[nr][nc] = 1
					q.append([nr, nc, cnt+1])
