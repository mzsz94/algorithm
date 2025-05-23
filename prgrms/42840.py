def check_ans(p, ans):
    cnt = 0
    
    if(len(ans)>len(p)):
        p = p*(len(ans)//len(p)+1)
    
    print(p)
    
    for i in range(len(ans)):
        if ans[i] == p[i]:
            cnt+=1
    return cnt

def solution(answers):
    answer = []
    ret = list()
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    ret.append([1,check_ans(p1, answers)])
    ret.append([2,check_ans(p2, answers)])
    ret.append([3,check_ans(p3, answers)])
    ret = sorted(ret, key=lambda x: x[1], reverse = True)
    print(ret)
    for p, cnt in ret:
        if cnt == ret[0][1]:
            answer.append(p)
    
    return answer
