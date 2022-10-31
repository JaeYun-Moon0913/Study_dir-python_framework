# 패키지 
패키지란, 토트를 사용하여 파이썬 모듈을 계층적으로 관리할 수 있게 해준다. 
예를 들어 모듈 이름이 A,B인 경우 A는 패키지 이름이 되고 B는 A 패키지의 B모듈이 된다. 

```
game/      
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/ 
        __init__.py
        run.py
        test.py
```
---

## 가능 하다. 
import game.sound.echo   
from game.sound.echo import echo_test   
from game.sound import echo   


## 불가능 
import game 까지 하고 
game.sound.echo.echo_test() 하면 오류남 
game 디렉토리의 모듈 또는 game 디렉토리의 __init__의.py 에 정의한 것만 참조할 수 있다. 

import a.b.c 라면 가장 마지막 항목 c는 반드시 모듈 또는 패키지여야 한다.   

---
## 1. import * 관한 기능 (__init__py파일 기능)

만약 각 패키지(game,sound,graphic)에 포함된 디렉터리에__init__.py가 없으면 패키지로 인식되지 않는다. --> 단 python3.3부터는 없어도 된다. 있는게 **안전하다고 한다.** 

원래는 __init__파이 파일에 __all__을 해줘야 from game.sound import *이게 되어는데 이제는 안해도 된다. --> python 3.10 ~ 11 
  
```
# 원래는 해줘야 했던것 
# game/sound/__init__.py 
__all__ = ['echo']

```
위 코드를 sound 폴더 init 파일에 추가 했어야 __from game.sound import *__ 이 가능 햇다. 

---

## 패키지 파일안에 있는(game) 다른 파이 파일에 improt 시에   
  

from game.sound.echo import echo_test
from ..sound.echo import echo_test 

..와 game. 과 같다. ..이 graphic 과 sound의 동일 한 깊이에 있으므로 ..은 같은 의미
..은 상위폴더 즉 여기서는 game이다. 
