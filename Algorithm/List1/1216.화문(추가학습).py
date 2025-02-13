# [문제]
# "기러기" 또는 "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
# 주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.
# 위와 같은 글자 판이 주어졌을 때, 길이가 가장 긴 회문은 붉은색 테두리로 표시된 7칸짜리 회문이다.
# 예시의 경우 설명을 위해 글자판의 크기가 100 x 100이 아닌 8 x 8으로 주어졌음에 주의한다.

# [제약사항]
# 각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.
# 글자 판은 무조건 정사각형으로 주어진다.
# ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.
# 가로, 세로 각각에 대해서 직선으로만 판단한다. 즉, 아래 예에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다.

# [입력]
# 각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
# 총 10개의 테스트케이스가 주어진다.

# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 길이를 출력한다.

def is_palindrome(s):
    return s == s[::-1]

def find_max_palindrome(grid, N):
    max_length = 1

    # 가로 방향 회문 검사
    for row in grid:
        for length in range(N, 1, -1):  # 길이를 N부터 2까지 줄여가며 탐색
            for start in range(N - length + 1):
                if is_palindrome(row[start:start + length]):
                    max_length = max(max_length, length)
                    break  # 가장 긴 회문을 찾으면 더 짧은 길이 확인 필요 없음

    # 세로 방향 회문 검사
    for col in range(N):
        col_str = ''.join(grid[row][col] for row in range(N))
        for length in range(N, 1, -1):
            for start in range(N - length + 1):
                if is_palindrome(col_str[start:start + length]):
                    max_length = max(max_length, length)
                    break

    return max_length

# 입력 처리
T = 10  # 테스트 케이스 개수는 10으로 고정
for _ in range(T):
    test_case_num = int(input().strip())  # 테스트 케이스 번호
    grid = [input().strip() for _ in range(100)]  # 100x100 문자판 입력
    max_palindrome_length = find_max_palindrome(grid, 100)
    print(f"#{test_case_num} {max_palindrome_length}")