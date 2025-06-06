def find_primes(num):
  arr = [1 for _ in range(num+1)]
  arr[0], arr[1] = 0, 0
  for i in range(2, int(num**0.5)):
    if arr[i]:
      for j in range(i*i, num+1, i):
        arr[j] = 0
  return arr

lst = list()
set_ans = set()
max_len = 0

def dfs(dep, numbers, visited):
  global lst, set_ans
  if dep >= len(numbers):
      # print(set_ans)
      return
  else:
    for i in range(len(numbers)):
      if not visited[i]:
        visited[i] = 1
        lst.append(numbers[i])
        # print(lst)
        tmp_c = str()
        for c in lst:
          tmp_c += c
          set_ans.add(int(tmp_c))

        dfs(dep+1, numbers, visited)
        visited[i] = 0
        lst.pop()

def solution(numbers):
  answer = 0
  # print(find_primes(11))
  visited = [0 for _ in range(len(numbers))]
  dfs(0, numbers, visited)
  sort_num = sorted(list(set_ans))
  # print(sort_num)
  ans_arr = find_primes(sort_num[-1])
  for n in sort_num:
    if ans_arr[n] == 1:
      answer+=1
  return answer
