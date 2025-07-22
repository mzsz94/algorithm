def can_equalize(kills, assists):
    n = len(kills)
    max_kill = max(kills)
    need = [max_kill - k for k in kills]
    total_ops = sum(need)
    new_assists_sum = sum(assists) + total_ops

    # 각 assists 값을 동일하게 만들 수 있는지 확인
    if new_assists_sum % n != 0:
        return [kills, assists]

    # 각 플레이어의 assists 값이 모두 target이 되도록 분배가 가능한지 확인
    # 실제로는 분배가 항상 가능 (총합만 맞추면 됨, 누구에게 몇 번 몰아주던 상관 없음)
    target = new_assists_sum // n

    # 단, 각 assists[i]가 target을 넘는지(즉, 더 올려야 하는지)는 문제 조건상 상관없음
    return [max_kill, target]


print(can_equalize([4,2,3], [1,0,2]))   # [5,2]
print(can_equalize([1000], [0]))       # [1000,0]
print(can_equalize([6,4], [2,0]))       # [6,4]