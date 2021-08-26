# 45분 일찍 알람 설정하기
H,M=map(int,input().split())

if H<0 or H>23:
    print('error1')
elif M<0 or M>59:
    print('error2')
elif M-45>=0:
    M=M-45
    print(H,M)
elif M-45<0 and H-1<0:
    M=M-45+60
    H=H-1+24
    print(H,M)
else:
    M=M-45+60
    H=H-1
    print(H,M)