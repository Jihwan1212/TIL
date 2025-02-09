---
contents: 2025년 2월 3일 월요일
tags:
  - Python
---
## 함수의 구조

- : 을 사용하고 엔터 시, 자동으로 들여쓰기가 될 것
- result 라는 변수에 담아야 결과가 출력될 것
- return문이 없다면 None이 반환됨
	- return의 또 다른 쓰임새
	- 함수를 빠져나가고 싶다면 return을 단독으로 사용
    ```python 
    def say_nick(nick):
    if nick == "바보":
    return print("나의 별명은 %s 입니다." % nick)
    ```

### 위치 인자
- **순서대로 값을 전달해야 함**
- 순서가 바뀌면 의미가 달라질 수 있음
```python
def introduce(name, age):
    print(f"이름: {name}, 나이: {age}")

introduce("Alice", 25)  # 정상 실행
introduce(25, "Alice")  # 순서가 바뀌면 의미가 달라짐
```

### 키워드 인자
```python
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
greet(age=35, name='Dave')  # 안녕하세요, Dave님! 35살이시군요.
```

```python title:'잘못된 예제 (오류 발생)'
greet(age=35, 'Dave')  # 오류: 위치 인자는 키워드 인자 뒤에 올 수 없음
```

### 기본 인자
- 함수 정의에서 **매개변수에 기본값을 할당**
- 함수 호출 시 해당 인자를 전달하지 않으면, **기본값이 자동으로 적용**
```python
def greet(name, age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob')       # 안녕하세요, Bob님! 30살이시군요.
greet('Charlie', 40)  # 안녕하세요, Charlie님! 40살이시군요.
```

### 가변 인자 (args)
[[datastructure#args]]
- **여러 개의 위치 인자를 튜플** 형태로 받음

```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))  # 6
print(add_numbers(10, 20, 30, 40, 50))  # 150
```


### 가변 키워드 인자 (kwargs)
[[datastructure#kwargs]]
- 여러 개의 키워드 인자를 **딕셔너리** 형태로 받음

```python
def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_info(name="Alice", age=25, city="Seoul")
```

|유형|문법|특징|
|---|---|---|
|위치 인자|`f(a, b)`|순서대로 전달|
|키워드 인자|`f(a=1, b=2)`|순서 상관없이 전달 가능|
|기본값 인자|`f(a, b=2)`|기본값을 설정해 생략 가능|
|가변 인자|`f(*args)`|여러 개의 위치 인자 전달 (튜플)|
|가변 키워드 인자|`f(**kwargs)`|여러 개의 키워드 인자 전달 (딕셔너리)|

---
## 재귀함수
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # 120
```

## 내장함수
### map (vs for)
```python title:'map'
numbers = [1, 2, 3, 4]
result = list(map(str, numbers)) #for문 보다 훨신 간결
print(result)  # ['1', '2', '3', '4']
```
```python title:'for'
numbers = [1, 2, 3, 4]
result = []
for num in numbers:
    result.append(str(num))  # 문자열로 변환 후 리스트에 추가
print(result)  # ['1', '2', '3', '4']
```
```python title:'input 사용'
#입력을 공백 기준으로 잘라 리스트로 변환 (기본적으로 문자열 리스트)
numbers = input().split()  # 입력: "1 2 3 4"
print(numbers)  # ['1', '2', '3', '4'] (문자열 리스트)

#입력받은 문자열 리스트를 정수 리스트로 변환
numbers = list(map(int, input().split()))  # 입력: "1 2 3 4"
print(numbers)  # [1, 2, 3, 4] (정수 리스트)
```

### zip 함수
- 여러 개의 iterable(리스트, 튜플 등)을 묶어 각 요소를 튜플로 결합하는 함수
- 결과는 `zip` 객체로 반환되며, `list()`나 `tuple()`로 변환해야 확인 가능
- 각 iterable의 같은 위치에 있는 요소들을 묶어서 튜플로 반환

```python title:'두 개의 리스트 묶기'
girls = ['jane', 'ashley']
boys = ['peter', 'jay']

pair = zip(girls, boys)
print(list(pair))
# [('jane', 'peter'), ('ashley', 'jay')]
# zip(girls, boys): 같은 인덱스에 있는 요소들을 묶어 튜플로 반환
```

```python title:'여러 개의 리스트 요소를 동시에 조회'
kr_scores = [10, 20, 30, 50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]

for student_scores in zip(kr_scores, math_scores, en_scores):
    print(student_scores)
    
    #(10, 20, 40)
		#(20, 40, 20)
		#(30, 50, 30)
		#(50, 70, 50)
```

```python title:'2차원 리스트의 컬럼(열) 요소를 동시에 조회'
scores = [
    [10, 20, 30],
    [40, 30, 39],
    [30, 40, 50]
] # 리스트 안에 리스트가 포함된 형태

for score in zip(*scores)
    print(score)
#zip(*scores) -> zip([10, 20, 30], [40, 30, 39], [30, 40, 50])
```

## 함수의 범위
### **LEGB 규칙 (Scope: 변수의 유효 범위)**
Python에서 변수를 찾을 때 LEGB 규칙을 따름

**LEGB**: 변수를 찾는 순서

1. **Local Scope** (지역 범위)
    - 함수 내부에서 정의된 변수
2. **Enclosed Scope** (내포된 범위)
    - 중첩 함수에서 바깥 함수의 변수
3. **Global Scope** (전역 범위)
    - 스크립트 전체에서 정의된 변수
4. **Built-in Scope** (내장 범위)
    - Python에서 기본 제공하는 내장 함수 및 변수

```python
print(sum)  # 내장 함수 sum
print(sum(range(3)))  # 3

#sum()은 기본적으로 Python 내장 함수(Built-in Scope)
```

```python
sum = 5  # 전역 변수 sum 정의
print(sum)  # 5
print(sum(range(3)))  # TypeError 발생: int 객체는 호출 불가능

#sum을 전역 변수로 선언시 LEGB 규칙에 따라 전역 변수 sum을 먼저 찾음
#기존 sum() 내장 함수는 가려짐 → del sum을 통해 삭제해야 다시 사용 가능
```

```python title:'전역 변수 수정 예제'
#함수 내부에서 전역 변수를 수정하려면 global 키워드 사용
num = 0  # 전역 변수

def increment():
    global num  # 전역 변수 사용 선언
    num += 1

print(num)  # 0
increment()
print(num)  # 1
#global num을 선언해야 함수 내부에서 전역 변수 num을 수정 가능
```

## 스타일 가이드
### 기본형식
- 소문자와 언더스코어 사용
- 동사로 시작하여 함수의 동작 설명
- 약어 사용 지양

```python
# Good

def calculate_total_price(price, tax):
    return price + (price * tax)

```

```python
# Bad

def calc_price(p, t):
    return p + (p * t)
```

### 함수 이름 구성 요소

- 동사 + 명사
    - `save_user()`
- 동사 + 형용사 + 명사
    - `calculate_total_price()`
- get/set 접두사
    - `get_username()`, `set_username()`

### 책임분리
```python

#유효성, 암호화, 이메일 각각 다른 함수 설정
def validate_password(password):
    """비밀번호 유효성 검사"""
    if len(password) < 8:
        raise ValueError('비밀번호는 8자 이상이어야 합니다')

def save_user(user_data):
    """비밀번호 암호화 및 저장"""
    user_data['password'] = hash_password(user_data['password'])
    db.users.insert(user_data)

def send_welcome_email(email):
    """환영 이메일 발송"""
    send_email(email, '가입을 환영합니다!')

# 위 세개 함수를 분리했기에 개별적으로 사용 가능
def process_user_data(user_data):
    validate_password(user_data['password'])
    save_user(user_data)
    send_welcome_email(user_data['email'])
```

## 패킹 언패킹
### `*` 연산자
- **패킹 연산자로 사용될 때**
    - 여러 개의 인자를 하나의 **리스트**나 **튜플**로 묶음
- **언패킹 연산자로 사용될 때**
    - 시퀀스(리스트, 튜플 등)나 반복 가능한 객체를 각각의 요소로 언패킹하여 함수의 인자로 전달

### `**` 연산자
- 언패킹 연산자로 사용될 때
    - 딕셔너리의 키-값 쌍을 개별 키워드 인자로 전달

```python title:'*사용 패킹'
def my_func(*args):
    print(args)  # 모든 인자가 튜플로 묶임

my_func(1, 2, 3, 4)
# 출력: (1, 2, 3, 4)
```
```python
# 변수명을 사용시 **"나머지 모든 값"** 을 리스트로 묶어서 받음
numbers = [1, 2, 3, 4, 5]

a, *b, c = numbers

print(a)  # 1
print(b)  # [2, 3, 4] 
print(c)  # 5
```


```python title:'*사용 언패킹'
numbers = [1, 2, 3, 4]
print(*numbers)
# 출력: 1 2 3 4  (리스트가 개별 요소로 풀림)
```

```python title:'**을 활용한 언패킹 (딕셔너리)'
def print_info(name, age):
    print(f"이름: {name}, 나이: {age}")

person = {"name": "Alice", "age": 25}
print_info(**person)
# 출력: 이름: Alice, 나이: 25
```

```python title:'print 함수에서 임의의 가변 인자를 사용할 수 있는 이유'
# *objects: objects에 전달된 모든 값이 하나의 튜플로 묶여 저장
def my_func(*objects):
    print(objects)        # (1, 2, 3, 4, 5)
    print(type(objects))  # <class 'tuple'>

my_func(1, 2, 3, 4, 5)
# 출력:
# (1, 2, 3, 4, 5)
# <class 'tuple'>
```

## 람다 표현식(with map 함수)
```python title:'일반함수 사용'
def square(x):
    return x**2

squared1 = list(map(square, numbers))
print(squared1)  # [1, 4, 9, 16, 25]
```

- `square()` 함수를 정의하여 `map()` 함수에 전달
- `map(square, numbers)` → `numbers` 리스트의 각 요소에 `square()` 적용

```python title:'람다함수 사용'
squared2 = list(map(lambda x: x**2, numbers))
print(squared2)  # [1, 4, 9, 16, 25]
```

- `lambda x: x**2`를 사용하여 **함수 선언 없이 바로 사용 가능**
- `map(lambda x: x**2, numbers)` → `numbers` 리스트의 각 요소를 제곱

### 람다함수의 특징

| 방식               | 장점                        | 단점                      |
| ---------------- | ------------------------- | ----------------------- |
| 일반 함수 (`def`)    | ✅ 코드 재사용 가능 ✅ 가독성 높음      | ❌ 함수 선언이 필요             |
| 람다 함수 (`lambda`) | ✅ 한 줄로 간결하게 표현 ✅ 코드 길이 감소 | ❌ 재사용 어려움 ❌ 가독성 낮을 수 있음 |
- 일반 함수는 여러 곳에서 재사용할 때 유용
- 람다 함수는 짧고 일회성으로 사용할 때 적합