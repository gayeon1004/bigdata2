#함수를 만들어 봅시다
def hello():
    print('함수안에서 헬로 월드')

def hello2(msg):
    print('받은 메세지를 함수안에서 출력')
    print(f'받은 메세지:{msg}')

def add(num1, num2):
    print(num1 + num2)

# 출력하지 않고 전달은 return
def add2(num1, num2):
    return num1 + num2