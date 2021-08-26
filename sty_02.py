score=int(input())

if score<0 or score>100:
    print('점수를 다시 입력하세요')
elif 90<=score<=100:
    print('A')
elif 80<=score<90:
    print('B')
elif 70<=score<80:
    print('C')
elif 60<=score<70:
    print('D')
else:
    print('F')