import sys
sys.stdin = open("input.txt",'r')

op = list(map(str, input()))
#print(op)
sign,lst_num = [],[]
num = 0
carry = 0
op = op[::-1]

for c in op:
    #print(num)
    if c == '-':
        sign += [-1]
        lst_num.append(num)
        num = 0
        carry = 0
    elif c == '+':
        sign += [1]
        lst_num.append(num)
        num = 0
        carry = 0
    else:
        num += 10**(carry)*int(c)
        carry += 1
lst_num.append(num)

# cal
sign = sign[::-1]
lst_num = lst_num[::-1]
print(sign)
print(lst_num)
ans = lst_num[0]

operand = 1
for i in range(len(sign)):
    if sign[i] == -1:
        operand = -1
    ans += operand * lst_num[i+1]

print(ans)
