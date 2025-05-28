from collections import deque

def solution(progresses, speeds):
    answer = []
    q = deque()
    
    tp = 0
    for i, p in enumerate(progresses):
        time = 0
        tp = (100-p) // speeds[i]
        if (100-p)%speeds[i] != 0:
            time += 1
        time += tp
        q.append(time)
    
    p_prv = q.popleft()
    cnt = 0
    time = 0
    while q:
        p_cur = q.popleft()
        # print("p_cur, p_prv, answer", p_cur, p_prv, answer)
        if(p_cur > p_prv):
            p_prv = p_cur
            cnt += 1
            answer.append(cnt)
            cnt = 0
        else:
            cnt += 1
        # print("answer", answer)
        time += 1
        # print("time, prg-1", time, (len(progresses)-1))
        if (time == (len(progresses)-1)):
            answer.append(cnt+1)
    
    
    return answer
