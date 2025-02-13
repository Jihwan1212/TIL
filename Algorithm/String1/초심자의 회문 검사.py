# [문제]
# "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
#
# 단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.
# [입력]
#
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
#
# 각 테스트 케이스의 첫 번째 줄에 하나의 단어가 주어진다.
#
#
# [출력]
#
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
#
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

def is_palindrome(s):
    return s == s[::-1]  # 단어가 회문인지 확인하는 함수


def find_palindrome():
    T = int(input().strip())  # 테스트 케이스 개수 입력

    for tc in range(1, T + 1):
        word = input().strip()  # 테스트 케이스의 단어 입력 (공백 제거)
        result = 1 if is_palindrome(word) else 0  # 회문이면 1, 아니면 0
        print(f"#{tc} {result}")  # 결과 출력


# 실행
find_palindrome()  # 함수 호출
