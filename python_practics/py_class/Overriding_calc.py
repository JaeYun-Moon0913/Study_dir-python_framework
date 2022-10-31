from Carculate import FourCal

class SafeFourCal(FourCal):
    # 0으로 나누면 오류가 난다. 
    # 이 오류를 제거 하기 위한 수정 본을 만들어 보자. 
    def div(self):
        if self.second == 0:
            return 0 

        else:
            return self.first/self.second
    
    # 이렇게 부모클래스에 있는 메서들를 동일한 이름으로 다시 만드는 것을 
    # 메서드 오버라이딩이다. 

    s = 10 
    # 이런식으로 변수를 주면 어떤 객체든지 
    # s = 10이란 같은 값을 가진다. 
    # SafeFourcal.s = 20 으로 값을 바꿀 수 잇다. 