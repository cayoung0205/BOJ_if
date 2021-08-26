x=int(input())
y=int(input())

if x<-1000 or 1000<x:
    print('다시 입력해주세요')
elif y<-1000 or 1000<y:
    print('다시 입력해주세요')
elif x>0 and y>0:  # x: 양수, y: 양수
    print('1')
elif x<0 and y>0:  # x: 음수, y: 양수
    print('2')
elif x<0 and y<0:  # x: 음수, y: 음수
    print('3')
else:
    print('4')
