# #동작을 생각한다. 
# 1. 객체를 만들어야 한다. 
# 2. 숫자를 입력 받아야 한다.
# # 기능 
# 3. 더하기 
# 4. 곱하기
# 5. 빼기 
# 6. 나누기 
# 
class FourCal:
    # 2. 숫자를 입력 받는다.
    # def setdata(self, first, second):
    #     self.first = first
    #     self.second = second
    #     # 여기서 self 는 객체 
    #     # 이 후 매개변수는 인수를 각각 받는다. 
    #     # 따라서 FourCal.setdata(a,4,2) 는 
    #     # a = FourCal() : a.setdata(4,2) 와 같다.

    def __init__(self,first,second):
        self.first = first
        self.second = second
        # 생성자를 활용한 방법 
        # 객체가 생성될 때 자동으로 호출되는 메서드를 의미 
        
    # 3. 더하기 기능 
    def add(self):
        result = self.first + self.second
        return result

    # 4. 곱하기 기능 
    def mul(self):
        result = self.first * self.second
        return result

    # 5. 빼기 
    def sub(self):
        result = self.first - self.second
        return result

    # 6. 나누기
    def __delattr__(self, __name: str) -> None:
        result = self.first / self.second
        return result