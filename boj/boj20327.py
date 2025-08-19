import sys
sys.stdin = open("boj/input.txt",'r')

N, R = map(int, input().split(' '))
# print(N, R)
N = 1 << N
# print(N, R)
arr = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
# print(arr)

def printArr(arr):
    for row in arr:
        print(*row)
    

def upDownSize(sr, sc, size):
    global arr
    tmp = [arr[row][sc:sc+size] for row in range(sr, sr+size)]
    for r in range(size):
        for c in range(size):
            # print(tmp[size-r-1][c])
            arr[r+sr][c+sc] = tmp[size-r-1][c]
    printArr(arr)



def upDown(lv):
    global arr
    end = len(arr)
    size = 1 << lv
    for sr in range(0, end, size):
        for sc in range(0, end, size):
            upDownSize(sr, sc, size)


for _ in range(R):
    k, l = map(int, input().split(' '))
    # print(k, l)
    if k == 1:
        upDown(l)

