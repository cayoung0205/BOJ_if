year=int(input())

if year<1 or 4000<year:
    print('다시 입력해주세요')
elif year%4==0 and year%100!=0:
    print(1)
elif year%4==0 and year%400==0:
    print(1)
else:
    print(0)