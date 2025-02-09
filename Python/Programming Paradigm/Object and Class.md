---
contents: 2025년 2월 5일 수요일
tags:
  - Python
---
## 절차 지향 vs 객체 지향

### 절차 지향
- 데이터를 다시 재사용하거나 하기보다는 처음부터 끝까지 **실행되는 결과물이 중요**
- 위에서 아래로 순차적으로 흐르는 형태 (순차적 명령어 실행)
- 함수 호출의 흐름이 중요
- 데이터와 데이터를 처리하는 함수(절차)가 분리됨 (복잡성 증가, 유지보수 문제)
- "어떤 순서로 처리할까?"를 중심으로 설계

### 객체 지향
- 데이터와 데이터를 처리하는 **메서드(함수)를 하나의 객체(클래스)로 묶음**
- 객체 간 상호작용과 메시지 전달이 중요
- "**어떤 객체가 이 문제를 해결할까**?" 중심으로 설계
- 절차 지향에서는 데이터가 수동적으로 함수에 의해 처리됨
- **객체 지향**에서는 데이터와 관련된 메서드가 함께 묶여 **능동적**으로 기능 수행
- **코드 구조화** 및 **재사용성**을 높이며, **실제 세계를 모델링**하기 쉬움
- 절차 지향과 객체 지향은 대조되는 개념이 아님
- 객체 지향은 **절차 지향의 단점을 보완**하는 방식으로 발전된 프로그래밍 패러다임

### 객체 
1. **속성 (Attribute)**
    - 객체의 상태 또는 데이터를 의미
2. **메서드 (Method)**
    - 객체가 수행하는 행동이나 기능
3. **고유성**
    - 각 객체는 고유한 특성을 가짐

- 객체 지향 프로그래밍(OOP)에서 객체
	- 상태(데이터)를 가지고 있으며, 해당 데이터를 조작하는 행동(메서드)을 수행

## 클래스 

### init메서드
- 생성자 메서드
- 새로운 객체를 만들 때 필요한 초기값을 설정
- **인스턴스 생성 시 자동 호출되는 특별한 메서드**
- `__init__` 이라는 이름의 메서드로 정의
- **인스턴스 변수의 초기화 담당**

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # 인스턴스 속성
        self.age = age    # 인스턴스 속성

    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}, 나이는 {self.age}살입니다.')
```


```python
class Circle:
    pi = 3.14 # 클래스 변수 (모든 Circle 객체가 공유)

    def __init__(self, radius): # 생성자 메서드
        self.radius = radius # 인스턴스 변수

c1 = Circle(1) # 인스턴스 생성
c2 = Circle(2) # 인스턴스 생성

print(c1.radius)  # 1
print(c2.radius)  # 2
print(Circle.pi)  # 3.14 (클래스 변수)
print(c1.pi)  # 3.14 (인스턴스에서도 접근 가능)
```

### 인스턴스
- 클래스가 설계도라면, 인스턴스는 그 설계도로부터 실제로 만든 '개별 물건'
- `Person("Alice", 25)`라고 하면 `Person`이라는 설계도로부터 이름이 **Alice**이고 나이가 **25**인 '사람 객체'가 탄생

```python title:'인스턴스 예시'
p1 = Person('Alice', 25) # Person 클래스를 기반으로 한 인스턴스 생성
p1.introduce()  # "안녕하세요. 저는 Alice, 나이는 25살입니다."

p2 = Person('Bella', 30) # 또 다른 인스턴스 생성
p2.introduce()  # "안녕하세요. 저는 Bella, 나이는 30살입니다."
```

- 클래스와 인스턴스
	- 변수 `name`의 타입은 `str` 클래스
	- 변수 `name`은 `str` 클래스의 **인스턴스**
	- 우리가 사용해왔던 **데이터 타입은 사실 모두 클래스**

## 클래스 메서드
- 클래스 내부에 정의된 함수
- 해당 객체가 어떻게 동작할지를 정의

### 인스턴스 메서드
- **클래스 내부에 정의되는 기본적인 메서드**
- 반드시 **첫 번째 인자로 인스턴스 자신(`self`)을 받아야 함**
- 인스턴스 변수에 접근하여 값을 읽거나 수정 가능

```python
class MyClass:
    def instance_method(self, arg1):
        pass  # 메서드 내부 동작 정의 가능
```

- `self`는 인스턴스 자체를 의미
- `self` 대신 다른 이름을 사용할 수 있지만 **일반적으로 사용하지 않음**(일관성을 위해 `self`를 사용하는 것이 권장됨)

- **`self` 동작 원리**
	- 인스턴스 메서드의 **첫 번째 인자는 반드시 인스턴스 자기 자신**
	- 메서드는 객체를 통해 호출되지만, 내부적으로는 클래스의 메서드로 변환됨

```python
class Person:
    def __init__(self, name):
        self.name = name  # 인스턴스 변수 초기화

    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}입니다.')

p = Person('Alice')
p.introduce() # "안녕하세요. 저는 Alice입니다."
```

- **문자열의 `upper()` 메서드**
	- `'hello'`라는 **문자열 객체**가 `upper()` 메서드를 호출하는 것처럼 보이지만, 실제로는 `str` 클래스의 메서드가 실행
	- 즉, **객체 지향 방식**의 단축형 표현

```python
print('hello'.upper())  # HELLO
```

```python
# 위 코드는 내부적으로 다음과 같이 동작
print(str.upper('hello'))  # HELLO
```

### 클래스메서드
- 클래스에서 호출하는 메서드
- 클래스 변수 조작 또는 클래스 레벨의 동작 수행
- `@classmethod` 데코레이터 사용
- 첫 번째 인자로 클래스 자체(`cls`)를 받음

- 클래스 메서드 구조

```python
class MyClass:
    @classmethod
    def class_method(cls, arg1, ...):
        pass
```

- `cls`는 클래스 자체를 참조하는 인자
- `cls`를 사용해 클래스 변수 변경 또는 읽기 가능

- 클래스 메서드 활용 예제

```python
class Person:
    population = 0  # 클래스 변수

    def __init__(self, name):
        self.name = name
        Person.increase_population()  # 클래스 메서드 호출

    @classmethod
    def increase_population(cls):
        cls.population += 1  # 클래스 변수 증가

person1 = Person("Alice")
person2 = Person("Bella")

print(Person.population)  # 2
```

- 동작 원리
	- `Person.population`은 클래스 변수로, 모든 인스턴스가 공유
	- `increase_population()`이 실행될 때마다 `population` 증가
	- 인스턴스가 생성될 때(`__init__` 실행) 클래스 메서드 호출 → `population` 증가

### 스태틱 메서드

스태틱 메서드 개념

- 클래스, 인스턴스와 독립적으로 동작하는 메서드
- `@staticmethod` 데코레이터를 사용하여 정의
- 자동으로 전달받는 인자 없음 (`self`나 `cls`를 받지 않음)
- 클래스나 인스턴스 속성에 직접 접근하지 않는, 일반적인 도우미 함수 역할

스태틱 메서드 구조

```python
class MyClass:
    @staticmethod
    def static_method(arg1, ...):
        pass
```

- `@staticmethod`를 사용하면 클래스 내부에 정의되지만, 클래스나 인스턴스에 의존하지 않는 독립적인 함수를 만들 수 있음

- 스태틱 메서드 예시

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 5))  # 8
```

- `MathUtils.add(3, 5)` 호출 시 **클래스나 인스턴스와 관계없이 독립적으로 실행**
- `add()` 메서드는 클래스 변수나 인스턴스 변수를 사용하지 않으므로 **스태틱 메서드로 정의하는 것이 적절함**
- `@staticmethod`를 사용하면 클래스 내부에서 **독립적인 함수 정의 가능**
- `self`나 `cls`를 받지 않으며, 클래스 속성에 접근하지 않음
- 클래스의 일부이지만, **클래스나 인스턴스의 상태와 관계없는 기능을 수행할 때 사용**

### 메서드 비교

|구분|특징|첫 번째 인자|
|---|---|---|
|**인스턴스 메서드**|개별 객체(인스턴스)와 관련된 기능 수행|`self`|
|**클래스 메서드**|클래스 자체와 관련된 기능 수행|`cls`|
|**정적 메서드**|클래스와 무관한 독립적인 기능 수행|없음|
- **클래스가 사용해야 할 것**
    - 클래스 메서드
    - 스태틱 메서드
- **인스턴스가 사용해야 할 것**
    - 인스턴스 메서드

```python
class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'

instance = MyClass()

print(instance.instance_method())  # ('instance method', <__main__.MyClass object at 0x0000...>)
print(instance.class_method())  # ('class method', <class '__main__.MyClass'>)
print(instance.static_method())  # 'static method'
```

### 매직 메서드
- Double underscore(`__`)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
- 인스턴스 메서드
- `__str__`메서드는 **객체를 사람이 읽기 쉬운 문자열 형태로 반환**하는 역할을 합니다.
- print() 함수를 호출할 때 자동으로 실행되며, 반환된 문자열이 출력됩니다.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'원의 반지름: {self.radius}'

c1 = Circle(10)
c2 = Circle(1)

print(c1)  # 원의 반지름: 10
print(c2)  # 원의 반지름: 1
```

## 상속
- 한 클래스(부모)의 속성과 메서드를 다른 클래스(자식)가 물려받는 것

### 상속이 필요한 이유

- 코드 재사용
    - 상속을 통해 기존 클래스의 속성과 메서드를 재사용
    - 기존 클래스를 수정하지 않고도 기능을 확장
- 계층 구조
    - 상속을 통해 클래스들 간의 계층 구조를 형성
    - 클래스 간의 관계를 표현, 더 구체적인 클래스를 만듦
- 유지 보수의 용이성
    - 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지 보수가 용이해짐
    - 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있음

```python
class Animal:
    def eat(self):
        print('먹는 중')

class Dog(Animal): # Animal의 특성을 물려받음
    def bark(self):
        print('멍멍')

my_dog = Dog() # 부모 클래스(Animal) 메서드 사용 가능

my_dog.bark()  # 멍멍
my_dog.eat()  # 먹는 중
```

### 메서드 오버라이딩

```python
class Animal:
    def eat(self):
        print('Animal이 먹는 중')

class Dog(Animal):
    # 부모 클래스(Animal)의 eat 메서드를 재정의(오버라이딩)
    def eat(self):
        print('Dog가 먹는 중')

my_dog = Dog()

my_dog.eat()  # Dog가 먹는 중

```

### 다중상속
- 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것
- 상속받은 모든 클래스의 요소를 활용 가능
- 중복된 속성이나 메서드가 있는 경우 **상속 순서에 의해 결정**

    ```python
    class Person:
        def __init__(self, name):
            self.name = name
    
        def greeting(self):
            return f'안녕, {self.name}'
    
    class Mom(Person):
        gene = 'XX'
    
        def swim(self):
            return '엄마가 수영'
    
    class Dad(Person):
        gene = 'XY'
    
        def walk(self):
            return '아빠가 걷기'
    ```
    
    ```python
    class FirstChild(Dad, Mom):
        def swim(self):
            return '첫째가 수영'
    
        def cry(self):
            return '첫째가 응애'
    
    baby1 = FirstChild('아가')
    
    print(baby1.cry())   # 첫째가 응애
    print(baby1.swim())  # 첫째가 수영
    print(baby1.walk())  # 아빠가 걷기
    print(baby1.gene)    # ?? XY (상속 순서에 따라 Dad의 gene 값이 적용됨)
    ```

### super
- 부모 클래스(또는 상위 클래스)의 메서드를 호출하기 위해 사용하는 내장 함수
- 다중 상속 상황에서 특히 유용
- **MRO**를 따르기에 부모 클래스를 가진 자식 클래스에서 다음에 호출해야 할 부모 메서드를 순서대로 호출할 수 있게 함

### MRO (Method Resolution Order)
- 파이썬이 메서드를 찾는 순서에 대한 규칙
- 메서드 결정 순서

- 다이아몬드 문제 (The diamond problem)
	- 두 클래스 B와 C가 A에서 상속되고, 클래스 D가 B와 C 모두에서 상속될 때 발생하는 모호함
	- B와 C가 재정의한 메서드가 A에 있고, D가 이를 재정의하지 않은 경우라면
	- **D는 B의 메서드 중 어떤 버전을 상속하는가? 아니면 C의 메서드 버전을 상속하는가?**

- 파이썬에서의 해결책
	- **MRO(Method Resolution Order)** 알고리즘을 사용하여 클래스 목록을 생성
	- 부모 클래스로부터 상속된 속성들의 검색을 **깊이 우선**, **왼쪽에서 오른쪽** 순서로 진행하며,계층 구조에서 **겹치는 같은 클래스를 두 번 검색하지 않음**
	- 따라서, 속성이 **D에서 발견되지 않으면 → B에서 찾고, B에서도 없으면 → C에서 찾고**,이런 식으로 진행됨

```python title:'단일 상속'

class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # super()를 통해 Person의 __init__ 메서드 호출
        super().__init__(name, age, number, email)
        self.student_id = student_id
```
        
```python title:'super를 사용하지 않았을 때'
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id
```



