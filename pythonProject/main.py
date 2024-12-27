x = int(input())
sum = 0
while x != 0:
    R = x % 10
    x = x // 10
    sum = sum + R

print(sum)
