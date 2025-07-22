import sys
sys.stdin = open("./input.txt",'r')

N = int(input())

lst = list(map(int, input().split(' ')))

lst_num = list(enumerate(lst))
print("DBG lst_num= ",lst_num)

lst_p =[]
lst_p = sorted(lst_num, key=lambda x: x[1])
print("DBG lst_p=",lst_p)


tot_work = []

for i in range(N):
    tot_work.append(lst_p[i][1])

sum_work = 0
for i in range(1,N):    
    sum_work += lst_p[i-1][1]
    tot_work[i] += sum_work
    #ans_work = tot_work[i]+lst_p[i-1][1]

    
print(sum(tot_work))
