# 납세자 타입 입력
p = (str(input('납세자 타입을 입력하세요 : ')))
gr1 = [1,2,3,4]



 

for gr1 in p:
    if int(p) == 1:
        income = int(input('납세할 총 수입을 입력하세요. : '))
    elif income < 0:
        print(income)
    elif income < 8350:
        print('납부하실 세금은 $ ',income * 0.35,'입니다.')
    elif income < 33950:
        print('납부하실 세금은 $ ',income * 0.35, '입니다.')
    elif income < 82250:
        print('납부하실 세금은 $ ',income * 0.35,'입니다.')
    elif income < 171550:
        print('납부하실 세금은 $ ',income * 0.35,'입니다.')
    elif income < 372950:
        print('납부하실 세금은 $ ',income * 0.35,'입니다.')
    else:
        print('$0 입니다.')

