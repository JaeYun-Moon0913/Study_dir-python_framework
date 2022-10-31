# 입력 받고 파일 만드는 파이썬 파일 
# 단어장 만들기 

# 경로에 대한 부분 확실히 공부 하자. 
import os 
#pth = os.getcwd() # 현재 디렉토리 
# 어디서 시작하느냐에 따라 다름 python 터미널은 이 파일의 포더의 
# 상위 폴더에서 시작해서 그 폴더 위치가 찍힘 

# cmd 창에서는 py 파일 폴더에서 시작해서 이 파일이 있는 폴더가 찍힘

pth = os.path.dirname(os.path.abspath(__file__))
file_name = 'vocabulary.txt'

result_pth = os.path.join(pth,file_name)

print(result_pth)

word = input("please input word  : ")
word_meaning = input("please input word meaning : ")

word_line = word + ' : ' + word_meaning


f = open(result_pth,"w")
f.write(word_line)

f.close()