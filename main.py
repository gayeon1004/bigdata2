print('hello wolrd')

# import myfunc / 모듈
from myfunc import hello, hello2, add, add2

# 함수를 불러서 사용
hello()
hello2('눈이 아프다')
hello2(2)
add(5,3)
add2(5, 3)
result = add2(5,3) #result가 return 결과값 받음
hello2(result)