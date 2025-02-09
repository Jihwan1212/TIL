---
contents: 2025년 2월 4일 화요일
tags:
  - Python
---
메서드: 객체(클래스)에 속한 함수

## 딕셔너리 관련 메서드
[[datastructure#딕셔너리]]
### clear
```python
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person)  # {}
```
### get
```python
person = {'name': 'Alice', 'age': 25}

print(person.get('name')) # Alice
print(person.get('country')) # None
print(person.get('country', 'Unknown')) # Unknown
print(person['country']) # KeyError: 'country'
```
### keys, values, items
|메서드|설명|반환 값 예시 (`dict_items` 형태)|
|---|---|---|
|`.items()`|키-값 쌍 반환|`[('key1', 'value1'), ('key2', 'value2')]`|
|`.keys()`|키만 반환|`['key1', 'key2', 'key3']`|
|`.values()`|값만 반환|`['value1', 'value2', 'value3']`|

```python
# keys(), values(), items() 들의 공통점: 딕셔너리에 있는 특별한 view 객체
# 원본 객체의 실시간 상태를 반영

person = {'name': 'Alice', 'age': 25, 'gender': 'Female'}

print(person.keys()) 
print(person.items()) 
print(person.values()) 

print(type(person.keys())) # <class 'dict_keys'>
print(type(person.items())) # <class 'dict_items'>
print(type(person.values())) # <class 'dict_values'>
```
### setdefault
- setdefault(key, **default_value**) 메서드
	- 딕셔너리에 특정 키가 존재하면 해당 값을 반환
	- 없으면 기본값(default_value)을 추가한 후 반환

```python
student = {'name': 'isaac'}
print(student.setdefault('age', 20)) # 키가 없으면 추가
print(student) # {'name': 'isaac', 'age': 20}
print(student.setdefault('name', 'kim')) #'name' 키가 이미 존재, 'isaac'을 그대로 반환
```
## 세트 관련 메서드 
[[datastructure#Set {a,b,c}]]
### remove
- 세트에서 지정된 요소를 제거
- 요소가 없을 때: **제거하려는 요소가 세트에 없으면 KeyError** **예외**를 발생
- 사용 사례: **요소가 반드시 존재**할 것으로 예상되는 경우에 사용

    ```python
    fruits = {'apple', 'banana', 'cherry'}
    fruits.remove('banana')
    print(fruits)  # {'apple', 'cherry'}
    fruits.remove('orange')  # KeyError: 'orange'
    ```
### discard
- 세트에서 지정된 요소를 제거
- 요소가 없을 때: 제거하려는 요소가 세트에 없어도 *예외를 발생시키지 않음*
- 사용 사례: *요소가 존재하지 않을 수도 있는 경우* 에 사용

    ```python
    fruits = {'apple', 'banana', 'cherry'}
    fruits.discard('banana')
    print(fruits)  # {'apple', 'cherry'}
    fruits.discard('orange')  # 아무런 에러도 발생하지 않음
    print(fruits)  # {'apple', 'cherry'}
    ```
### pop
- 기능: 세트에서 임의의 요소를 제거하고 **그 요소를 반환**
- 요소가 없을 때: **세트가 비어 있으면 KeyError 예외**를 발생
- 사용 사례: 세트에서 임의의 요소를 제거하고 그 값을 알고 싶을 때 사용

    ```python
    fruits = {'apple', 'banana', 'cherry'}
    removed_fruit = fruits.pop()
    print(removed_fruit)  # 임의의 요소 (예: 'apple')
    print(fruits)  # 남은 요소 (예: {'banana', 'cherry'})
    
    fruits = set() # 빈 집합 생성
    fruits.pop()  # KeyError: 'pop from an empty set'
    ```

### 요약
- **`remove()`**: 요소를 제거, 요소가 없으면 `KeyError`를 발생시킵니다.
- **`discard()`**: 요소를 제거, 요소가 없어도 예외를 발생시키지 않습니다.
- **`pop()`**: 임의의 요소를 제거하고 반환, 세트가 비어 있으면 `KeyError`를 발생
## 문자열 관련 메서드
### replace
- 문자열의 특정 부분을 새로운 문자열로 치환
    - `text.replace('old', 'new')` → 문자열 내 모든 `old`를 `new`로 변경
    - `text.replace('old', 'new', count)` → 앞에서부터 `count`번만 변경

```python
text = 'Hello, world! world world'
new_text1 = text.replace('world', 'Python')
new_text2 = text.replace('world', 'Python', 1)
    
print(new_text1)  # Hello, Python! Python Python
print(new_text2)  # Hello, Python! world world
```

### strip
- 문자열의 앞뒤 특정 문자(기본값: 공백)를 제거

```python
text = "  Hello, World!  " 
print(text.strip())  # "Hello, World!" (양쪽 공백 제거)
```

### split
- 특정 구분자를 기준으로 문자열을 나누어 리스트로 반환
    - `split(sep)` → `sep`을 기준으로 문자열을 나누어 **리스트** 반환
    - `split()` → 공백(스페이스, 탭, 개행 등)을 기준으로 자동 분할

    ```python
    text = 'Hello, world!'
    words1 = text.split(',')
    words2 = text.split()
    
    print(words1)  # ['Hello', ' world!']
    print(words2)  # ['Hello,', 'world!']
    ```
    
### join
- 리스트 등의 문자열 요소를 특정 구분자로 연결
    - `'separator'.join(iterable)` → 리스트나 튜플 등의 문자열 요소를 특정 구분자(`separator`)로 연결하여 하나의 문자열 반환
    - 예: `'-'.join(['a', 'b', 'c'])` → `'a-b-c'`

    ```python
    words = ['Hello', 'world!']
    text = '-'.join(words)
    print(text)  # 'Hello-world!'
    ```
## 리스트 관련 메서드
###  append() 메서드 설명

```python
my_list = [1, 2, 3]
my_list.append(4) # 원본 자체를 변경
print(my_list) # [1, 2, 3, 4]
```

### extend() 메서드 설명

```python
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6] 

# += 연산자와 같은 기능 수행 (my_list += [4, 5, 6] 도 동일한 결과)
```

### insert() 메서드 설명

```python
my_list = [1, 2, 3]
my_list.insert(1, 5) # 리스트의 인덱스 i 위치에 값 x를 삽입
print(my_list)  # [1, 5, 2, 3]
```

### remove() 메서드 설명

```python
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2) # remove(x) → 리스트에서 가장 **왼쪽에 있는** x를 제거
print(my_list)  # [1, 3, 2, 2, 2]
# x가 리스트에 없으면 ValueError 발생
```

### pop() 메서드 설명

```python
my_list = [1, 2, 3, 4, 5]

item1 = my_list.pop() # 마지막 항목을 제거하고 반환
item2 = my_list.pop(0) # **인덱스 i에 있는 항목**을 제거하고 반환

print(item1)  # 5
print(item2)  # 1
print(my_list)  # [2, 3, 4]
# 인덱스가 범위를 벗어나면 IndexError 발생
```

### clear() 메서드 설명

```python
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []
# 리스트 자체는 그대로 유지되며 길이만 0이 됨
```

### reverse() 메서드

```python
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()

print(my_list.reverse())  # None 
# reverse()는 리스트 자체를 뒤집지만 반환값은 None
print(my_list)  # [9, 1, 8, 2, 3, 1]
```

```python
# 리스트를 뒤집은 새로운 리스트를 반환받고 싶다면 [::-1]을 사용
reversed_list = my_list[::-1]
print(reversed_list)
```

### sort() 메서드
- 기본적으로 오름차순 정렬, reverse=True 옵션으로 내림차순 가능
	- sort() → 리스트를 오름차순으로 정렬
- sort(**reverse=True**) → 리스트를 **내림차순**으로 정렬
- sort()는 리스트 자체를 정렬하며 **반환값이 None**
- 정렬된 **새로운 리스트를 반환**받고 싶다면 **sorted()** 사용

```python
# 예제 리스트
numbers = [5, 2, 9, 1, 5, 6]

# 리스트 자체를 오름차순 정렬 (sort())
numbers.sort()
print("오름차순 정렬:", numbers)  # [1, 2, 5, 5, 6, 9]

# 리스트 자체를 내림차순 정렬 (sort(reverse=True))
numbers.sort(reverse=True)
print("내림차순 정렬:", numbers)  # [9, 6, 5, 5, 2, 1]

# 정렬된 새로운 리스트를 반환 (sorted())
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print("새로운 정렬된 리스트:", sorted_numbers)  # [1, 2, 5, 5, 6, 9]
print("원본 리스트:", numbers)  # [5, 2, 9, 1, 5, 6] (변경 없음)
```

## 기타 메서드
### find() vs index()
- find(): 찾는 문자가 없으면 -1 반환
- index(): 찾는 문자가 없으면 ValueError 발생

```python
print('banana'.find('n'))  # 2
print('banana'.find('z'))  # -1
```

```python
print('banana'.index('a'))  # 1
print('banana'.index('z'))  # ValueError: substring not found
```

### isupper() vs islower():
- **is** 로 시작하는 함수는 **불리언**(참, 거짓) 형태
- isupper(): 문자열이 모두 대문자이면 True, 아니면 False
- islower(): 문자열이 모두 소문자이면 True, 아니면 False
- 대문자와 소문자가 섞여 있으면 둘 다 False 

```python
string1 = "HELLO"
string2 = "Hello"

print(string1.isupper())  # True
print(string2.isupper())  # False
print(string1.islower())  # False
print(string2.islower())  # False
```

### isalpha()
- 문자열이 **알파벳 문자(A-Z, a-z)만 포함**하면 True, 아니면 False

```python
string1 = "Hello"
string2 = "123heis98576ssh"

print(string1.isalpha())  # True
print(string2.isalpha())  # False
```

## 메서드 체이닝

```python
# 1. 단계별로 실행하기
text = 'heLLo, woRld!'
step1 = text.swapcase() 
# swapcase() → 대문자는 소문자로, 소문자는 대문자로 변환
print('1단계 결과:', step1)  # HELlO, WOrLD!

step2 = step1.replace('l', 'z')
print('2단계 결과:', step2)  # HEzzO, WOrLD!

# 2. 메서드 체이닝 (위와 동일한 결과)
new_text = text.swapcase().replace('l', 'z')
print('최종 결과:', new_text)  # HEzzO, WOrLD!
```

```python title:'리스트에서의 메서드 체이닝 예시'
# copy()로 리스트를 복사 후, sorted() 함수로 정렬
numbers = [3, 1, 4, 1, 5, 9, 2]
result = numbers.copy().sort()

print(numbers)  # [3, 1, 4, 1, 5, 9, 2] (원본은 변경되지 않음)
print(result)   # None (sort() 메서드는 None을 반환하기 때문)

# 올바른 체이닝 예시
sorted_numbers = sorted(numbers.copy())
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]

# [[복사#얕은 복사 Shallow Copy]]
# [[메서드#sort() 메서드]]
```

### 메서드 체이닝 주의사항
- 모든 메서드가 체이닝을 지원하는 것은 아님
	- **메서드가 객체를 반환할 때만 체이닝 가능**
	- None을 반환하는 메서드는 메서드 체이닝이 불가능
    - 리스트의 **append()**, **sort()**
    - 메서드 체이닝을 사용할 때는 각 메서드의 반환 값을 잘 이해하고 있어야 함

```python title:'체이닝이 가능한 예시'
text = "hello world"
result = text.upper().replace("HELLO", "HI")
print(result)  # HI WORLD
```

```python title:'체이닝이 불가능한 예시 (None 반환)'
numbers = [3, 1, 4, 1, 5]
sorted_numbers = numbers.sort().reverse()  # 오류 발생 (sort()는 None 반환)
```

```python title:'해결방법'
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers, reverse=True)  # 올바른 체이닝
print(sorted_numbers)  # [5, 4, 3, 1, 1]
```