import random

def result():
    money = 1000
    while money:
        gamble = input('big or small')
        gamble=gamble.strip()
        gresult = rand()
        #print('gresult',gresult)
        #print(type(gresult))
        #print(type(gamble))
        if money <= 0:
            print('钱不够了！')
            break
        else:
            if gamble == gresult :
                money = money + 1000
                print('你赢了，还剩{}'.format(money))
            else:
                money = money - 500
                print('你输了，还剩{}'.format(money))
def dice():
    return result

def rand():
    result = dice()
    #print(result)
    if 0<result<4 :
        print('本次{}为小'.format(result))
        return 'small'
    else :
        print('本次{}为大'.format(result))
        return 'big'

result()