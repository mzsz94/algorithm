import sys
sys.stdin = open("./algorithm/input.txt",'r')


def min_swaps_to_avoid_collision(n, path1, path2):
    # R(오른쪽) 움직임의 원위치(1-based) 수집
    # p1 = [i+1 for i, c in enumerate(path1) if c == 'R']
    # p2 = [i+1 for i, c in enumerate(path2) if c == 'R']
    
    # R(오른쪽) 움직임의 원위치(0-based) 수집
    # p1 = [0 for _ in range(2*n)]
    # p2 = [0 for _ in range(2*n)]
    p1, p2 = [], []

    for i in range(2*n):
        if path1[i] == 'R':
            p1.append(i+1)
        if path2[i] == 'R':
            p2.append(i+1)
    # print("DBG p1=",p1)
    # print("DBG p2=",p2)
    

    # 차량 1만 R^n U^n 형태로 바꿀 때 비용
    cost1 = sum(abs(p1[i] - (i+1)) for i in range(n))
    
    # 차량 2만 U^n R^n 형태로 바꿀 때 비용
    # (U^n R^n 으로 만들려면 R들은 뒤쪽 n개 위치인 n+1..2n에 있어야 함)
    cost2 = sum(abs(p2[i] - (n + i + 1)) for i in range(n))

    return min(cost1, cost2)


data = sys.stdin.read().split()
n = int(data[0])
path1 = data[1].strip()
path2 = data[2].strip()

result = min_swaps_to_avoid_collision(n, path1, path2)
print(result)