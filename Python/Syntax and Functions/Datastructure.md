---
tags:
  - Python
contents: 2025년 2월 3일 월요일
---
## 파이썬 특징
- 파이썬은 0부터 숫자를 센다 (** 0:2:1 → 0이상, 2미만, 1간격 )
- 리스트 → 집합 : 중복 제거 용도
- 알고리즘에서는 is보다는 **==**을 자주 사용하게 될 것

### 이스케이프 코드
- `\\n`: 문자열 안에서 줄을 바꿀 때 사용
-  `\\t`: 문자열 사이에 탭 간격을 줄 때 사용
- `\\\\`: `\\`를 그대로 표현할 때 사용
-  `\\'`: 작은따옴표(')를 그대로 표현할 때 사용
-  `\\"`: 큰따옴표(")를 그대로 표현할 때 사용

### print 시 줄 바꿈 대신 한 줄 띄어쓰기
-  print(i, **end=” “**)

### 후행쉼표
```python
# 기존 코드
items = [
    'item1',
    'item2'
]

# 새로운 항목 추가 시, 기존 줄도 수정됨 (diff 발생)
items = [
    'item1',
    'item2',
    'item3'
]
```

```python
# 후행쉼표 사용 시
items = [
    'item1',
    'item2',
]

# 새로운 항목 추가 시, 기존 줄 변경 없음 (diff 최소화)
items = [
    'item1',
    'item2',
    'item3',
]
```

## Mutable VS Immutable
    1. Mutable:
        
        변수 변경가능: [리스트], {딕셔너리}, {집합}
        
    2. Immutable:
        
        변수 변경불가: 정수, 실수, 문자열, (튜플)

## 자료형
### 리스트 자료형
```python
# b를 뽑는 방법
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3][1])
```

### 딕셔너리 자료형
- **순서가 없다**
- 키와 값으로 구성되어있다
- 만들 때 **중괄호**로 만든다
- 키는 고유 (중복을 허용하지 않는다)
    - **키는 불변(Immutable)타입만 가능**
- 값은 어떤 것도 다 포함
- 가변형

```python title:'딕셔너리 생성'
my_dict = {}  # 빈 딕셔너리 생성
y_dict2 = dict()  # dict() 함수를 사용하여 빈 딕셔너리 생성
```

### Set 자료형
- 고유한 요소(Unique Elements):
    - 세트는 고유한 요소만을 저장
    - 중복된 값을 허용X
- **순서 없음**(Unordered):
    - 세트는 순서를 유지하지 않음
    - 요소는 특정 순서로 저장X
- 변경 가능(Mutable):
    - 세트는 변경 가능한 객체, 요소를 추가하거나 삭제가능
    - 그러나 세트 자체는 해시 가능한(immutable) 요소만을 포함
- 사용 사례: **중복을 제거**하거나 **집합 연산**(합집합, 교집합, 차집합 등)을 수행

```python
fruits = {'apple', 'banana', 'cherry'}
fruits.add('apple')  # 중복 추가는 무시됨
print(fruits)  # {'apple', 'banana', 'cherry'}
```


```python title:'set: 중복된 값 제거'
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)

print(unique_numbers)  # {1, 2, 3, 4, 5}
```

```python
#중복 제거 후 리스트로 변환
words = ["apple", "banana", "apple", "cherry"]
unique_words = list(set(words))

print(unique_words)  # ['banana', 'cherry', 'apple']
```
---

### 딕셔너리 vs  세트
- **데이터 저장 방식**
	- 딕셔너리는 키-값 쌍을 저장하고, 세트는 고유한 요소만을 저장
- **순서**
	- 딕셔너리는 삽입 순서를 유지하지만, 세트는 순서를 유지X
- **중복 허용**
	- 딕셔너리는 키가 고유해야 하지만 값은 중복될 수 있음
	- 세트는 모든 요소가 고유
- **사용 사례*
	- 딕셔너리는 키를 통해 값을 빠르게 조회할 때 사용되고, 세트는 중복 제거와 집합 연산에 사용

## 논리연산자
### 단축평가
- 불필요한 연산(and, or)을 피하는 최적화 기법
- and 연산자
	- `A and B` → **A가 거짓이면** B를 확인할 필요 없음 → **A 반환**
	- `A and B` → **A가 참이면** B의 값을 반환
- or 연산자
	- `A or B` → **A가 참이면** B를 확인할 필요 없음 → **A 반환**
	- `A or B` → **A가 거짓이면** B의 값을 반환

```python
vowels = 'aeiou'

print('a' and ('b' in vowels))  # False
print('b' and ('a' in vowels))  # True

print(3 and 5)  # 5 (3이 참이므로 5 반환) 
print(3 and 0)  # 0 (3이 참이지만 0이 거짓이므로 0 반환)
print(0 and 5)  # 0 (0이 거짓이므로 바로 0 반환)
print(0 and 0)  # 0 (0이 거짓이므로 바로 0 반환)

print(5 or 3)  # 5
print(3 or 0)  # 3
print(0 or 3)  # 3
print(0 or 0)  # 0
```

## 여러개의 값을 대변하는 대명사
### args
- 튜플로 묶어 처리
```python
def add_mul(choice, *args):
    if choice == "add":  # choice가 "add"일 경우
        result = 0
        for i in args:
            result = result + i  # 모든 숫자를 더함
    elif choice == "mul":  # choice가 "mul"일 경우
        result = 1
        for i in args:
            result = result * i  # 모든 숫자를 곱함
    return result  # 최종 결과 반환
    
print(add_mul("add", 1, 2, 3, 4))  # 1 + 2 + 3 + 4 = 10
print(add_mul("mul", 1, 2, 3, 4))  # 1 * 2 * 3 * 4 = 24
```

### kwargs
- dictionary로 묶어 처리
```python
def print_info(**kwargs):
    print(kwargs)

print_info(name='Eve', age=30)  # {'name': 'Eve', 'age': 30}
```

## while 문
조건이 True인 동안 계속 반복 실행되는 반복문

```python
# coffee.py

coffee = 10  # 남은 커피 개수

while True:  # 무한 루프 시작
    money = int(input("돈을 넣어 주세요: "))  # 사용자로부터 돈 입력 받기

    if money == 300:  # 정확히 300원을 넣었을 경우
        print("커피를 줍니다.")
        coffee = coffee - 1  # 커피 개수 감소

    elif money > 300:  # 300원 초과를 넣었을 경우
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1  # 커피 개수 감소

    else:  # 돈이 부족한 경우
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)

    if coffee == 0:  # 커피가 다 떨어졌을 경우
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break  # while 문 종료
```

-  `=` vs `==` 차이점

|연산자|의미|사용 예시|
|---|---|---|
|`=`|대입 연산자 (값을 변수에 저장)|`x = 10`|
|`==`|비교 연산자 (두 값이 같은지 확인)|`x == 10`|

- break를 사용하면 **반복문을 강제 종료**
```python
num = 1
while num <= 10:
    print(num)
    if num == 5:  # 특정 조건에서 종료
        break
    num += 1
```

- continue를 사용하면 **특정 조건에서 다음 반복을 진행**
```python
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue  # 3일 때 건너뛰기
    print(num)
```

## for 문
### 기본 구조
```python

for 변수 in iterable:
    실행할 코드
```

- **변수**: 반복할 때마다 iterable 내의 요소가 차례로 할당
- **iterable**: 리스트, 튜플, 문자열, 딕셔너리, 집합 등 반복 가능한 모든 객체가 해당
```python

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

### range() 함수와 for문
- 숫자 범위에 대해 반복 작업을 할 때는 `range()` 함수를 자주 사용
- `range(start, stop, step)` 형태로 사용되며, start부터 stop-1까지 step 간격으로 숫자를 생성
```python
for i in range(5): # 0부터 시작하여 4까지의 숫자를 출력
    print(i)
```

### for문과 다양한 iterable
- 파이썬의 for문은 리스트뿐 아니라 튜플, 문자열, 딕셔너리 등 다양한 iterable 객체에 사용
```python
for char in "Hello":
    print(char)
```

```python
person = {'name': 'Alice', 'age': 25, 'city': 'Seoul'}
for key in person:
    print(key, ":", person[key])
```

혹은, `items()` 메소드를 사용해서 키와 값을 동시에 받을 수도 있습니다:
```python
for key, value in person.items():
    print(key, ":", value)
```

### enumerate() 함수
리스트나 다른 iterable을 순회할 때 인덱스가 필요한 경우, `enumerate()` 함수를 사용하면 인덱스와 값을 동시에 얻을 수 있음

```python title:'인덱스와 함께 리스트 요소 출력하기'
colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")
```

### 반복 제어
- **break**: 반복문을 즉시 종료
```python
for num in range(10):
    if num == 5:
        break
    print(num) # 이 코드는 숫자 5가 되었을 때 반복을 종료
```

- **continue**: 현재 반복의 남은 부분을 건너뛰고 다음 반복으로
```python
for num in range(10):
    if num % 2 == 0:
        continue  # 짝수이면 출력하지 않고 다음 반복으로 넘어감
    print(num) # 짝수인 경우를 건너뛰고 홀수만 출력
```

### for-else 구조
- 파이썬의 for문에는 `else` 절을 추가할 수 있음
- `else` 블록은 for문이 **정상적으로(중간에 break 없이) 완료되었을 때** 실행
```python
for num in range(5):
    print(num)
else:
    print("반복이 모두 완료되었습니다.")

```

- 만약 for문 내부에서 `break`가 발생하면 else 블록은 실행되지 않음

### 요약
- **for문**은 iterable 객체의 요소를 하나씩 순회하면서 작업을 수행
- `range()`를 이용해 숫자 범위를 쉽게 다룰 수
- 다양한 iterable(리스트, 문자열, 딕셔너리 등)에 사용할 수
- `enumerate()`를 이용하면 인덱스와 값을 동시에 사용할 수
- `break`와 `continue`로 반복 제어가 가능하며, `else` 블록으로 반복 종료 후 추가 작업을 수행할 수