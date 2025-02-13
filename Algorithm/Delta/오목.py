# [문제]
# N X N 크기의 판이 있다. 판의 각 칸에는 돌이 있거나 없을 수 있다. 돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램을 작성하라.
#
#
#
# [입력]
#
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
#
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(5 ≤ N ≤ 20)이 주어진다.
#
# 다음 N개의 줄의 각 줄에는 길이 N인 문자열이 주어진다. 각 문자는 ‘o’또는 ‘.’으로, ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸을 의미한다.
#
#
#
# [출력]
#
# 각 테스트 케이스 마다 돌이 다섯 개 이상 연속한 부분이 있으면 “YES”를, 아니면 “NO”를 출력한다

def check_five_in_a_row(board, N):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # 하, 우, 우하향, 좌하향

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for dx, dy in directions:
                    count = 1
                    x, y = i + dx, j + dy
                    while 0 <= x < N and 0 <= y < N and board[x][y] == 'o':
                        count += 1
                        if count >= 5:
                            return "YES"
                        x += dx
                        y += dy
    return "NO"


def main():
    test_cases = int(input().strip())

    for t in range(1, test_cases + 1):
        N = int(input().strip())
        board = [input().strip() for _ in range(N)]
        result = check_five_in_a_row(board, N)
        print(f"#{t} {result}")


if __name__ == "__main__":
    main()
