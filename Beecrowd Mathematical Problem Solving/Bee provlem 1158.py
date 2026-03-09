num = 0
for i in range(int(input())):
     a, b = map(int, input().split())
     for e in range(b):
          if a%2!=0:
               num += (2*e)+a
          else:
               num += (2*e)+a+1
     print(num)




