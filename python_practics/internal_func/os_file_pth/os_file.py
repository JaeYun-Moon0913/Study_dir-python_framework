import os 
python_file_pth = os.path.dirname(os.path.abspath(__file__))
# 일정한걸 찾음 
print(python_file_pth)

parent_dir = os.path.dirname(python_file_pth)
print(parent_dir)