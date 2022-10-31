# class 상속 
# Fourcal 의 모든 기능을 사용 하고 추가적인 기능 추가 하는것도 가능 
from Carculate import FourCal

class MoreFourCal(FourCal):
    # 추가 a^b
    def pow(self):
        result = self.first**self.second
        return result

# class 상속은 기존 클래스의 기능을 확장시킬 때 주로 사용한다.  

a = MoreFourCal(2,3)
# FourCal 의 init 도 쓰이는구만 
print(a.add())
print(a.pow())