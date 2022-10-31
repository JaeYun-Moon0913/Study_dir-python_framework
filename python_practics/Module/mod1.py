def add(a,b):
    return a+b

def sub(a,b):
    return a-b 

# import mod1 : 단순히 가져오는 
# mod1.add() 이렇게 사용 
# from mod1 import * 
# 하면 add() 를 바로 사용 가능 

if __name__ =="__main__": 
    # 위 조건문을 하지 않으면, 
    # import 할 때 밑에 줄이 실행 된다. 
    # 확인 용으로 쓰면 된다.

    # import 경우 __name__에는 mod1 이라는 값이 들어간다.
    print(add(1,4)) 