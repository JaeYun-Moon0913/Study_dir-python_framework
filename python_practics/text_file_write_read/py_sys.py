# 명령 프롬프트에서 바로 인수로 받기 
import os 
import sys 

pth = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[1:]# argv[0]은 파일 이름 
# 그 뒤 나온것들 list로 만드나 본데? 
# print(type(args)) list로 만드네

f = open(pth + "/text_test.txt","w")
for i in args:
    intxt = i.capitalize()# 대문자 만드는 
    intxt = intxt + '\n'
    f.write(intxt)
f.write(str(args)) # list 형은 안되지만, list를 str로 바꾸니 되네
print(args)
f.close()
    