# 標準入力
# 与えられる形式
# a
# b c
# s

a = int(input())
b, c = map(int, input().split())
s = input()

print(a + b + c, s)