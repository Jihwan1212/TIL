---
contents: 2025년 2월 5일 수요일
tags:
  - Python
---
## 디버깅
1. `print` 함수 활용
    - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 `bisection`으로 나눠서 생각
2. 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
    - `breakpoint`, 변수 조회 등
3. Python tutor 활용 (단순 파이썬 코드인 경우)
4. 뇌 컴파일, 눈 디버깅 등

## 에러
### 문법 에러 (Syntax Error)
프로그램의 구문이 올바르지 않은 경우 발생(프로그램 실행 안됨)
오타, 괄호 및 콜론 누락 등의 문법적 오류

- Invalid syntax (문법 오류)
    ```python
    while  # SyntaxError: invalid syntax
    ```
    
- assign to literal (잘못된 할당)
    ```python
    5 = 3  # SyntaxError: cannot assign to literal
    ```
    
- EOL (End of Line)
```python
print('hello
# SyntaxError: EOL while scanning string literal
```

- EOF (End of File)

```python

print(
# SyntaxError: unexpected EOF while parsing
```

## 예외
프로그램 실행 중에 감지되는 에러

### ZeroDivisionError
: 나누기 또는 모듈로 연산의 두 번째 인자가 `0`일 때 발생

```python
10/0  # ZeroDivisionError: division by zero
```

### NameError

: 지역 또는 전역 이름을 찾을 수 없을 때 발생

```python
print(name_error)
# NameError: name 'name_error' is not defined
```

### TypeError

```python
'2' + 2  # TypeError: can only concatenate str (not "int") to str
```

- 인자 누락

```python

sum()  # TypeError: sum() takes at least 1 positional argument (0 given)
```

- 인자 초과

```python

sum(1, 2, 3)  # TypeError: sum() takes at most 2 arguments (3 given)
```

- 인자 타입 불일치

```python
import random
random.sample(1, 2)
# TypeError: Population must be a sequence. For dicts or set
```

### IndexError
- 시퀀스 인덱스가 범위를 벗어날 때 발생

```python
empty_list = []
empty_list[2]
# IndexError: list index out of range

```

## 예외처리
예외가 발생했을 때 프로그램이 비정상적으로 종료되지 않고, 적절하게 처리할 수 있도록 하는 방법

### 예외처리 사용 구문
- **try**
    - **예외가 발생할 수 있는 코드 작성**
- **except**
    - **예외가 발생했을 때 실행할 코드 작성**
- else (선택사항)
    - 예외가 발생하지 않았을 때 실행할 코드 작성
- finally (선택사항)
    - 예외 발생 여부와 상관없이 항상 실행할 코드 작성

```python
try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유효한 숫자가 아닙니다.')
    
else:
    print(f'결과: {y}')
finally:
    print('프로그램이 종료되었습니다.')
```

### try-except 구조
- `try` 블록 안에는 예외가 발생할 수 있는 코드를 작성
- `except` 블록 안에는 예외가 발생했을 때 처리할 코드를 작성
- 예외가 발생하면 프로그램 흐름은 `try` 블록을 빠져나와 해당 예외에 대응하는 `except` 블록으로 이동

```python
try:
    # 예외가 발생할 수 있는 코드
except 예외:
    # 예외 처리 코드
```

```python
# try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

try:
    num = int(input('숫자입력 : '))
except ValueError:
    print('숫자가 아닙니다.')

# 복수 예외처리
try:
    num = int(input('100을 나눌 값을 입력하세요 : '))
    print(100 / num)
except ValueError:
    print('숫자를 입력하라고')
except ZeroDivisionError:
    print('0으로는 나눌 수 없어')
except:
    print('에러가 발생했습니다.')

```

내장 예외의 상속 계층구조 주의

- 아래와 같이 예외를 작성하면 코드는 2번째 `except` 절에 이후로 도달하지 못함

```python

try:
    num = int(input('100으로 나눌 값을 입력하세요 : '))
    print(100 / num)
except BaseException:
    print('숫자를 넣어주세요.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생하였습니다.')
```

- 내장 예외 클래스는 상속 계층구조를 가짐
    - `except` 절로 분기 시 **반드시 하위 클래스를 먼저 확인 할 수 있도록 작성**해야 함
