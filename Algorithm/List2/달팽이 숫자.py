# [문제]
# 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
# 다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

# [제약사항]
#
# 달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)
#
# [입력]
#
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
#
# 각 테스트 케이스에는 N이 주어진다.
#
# [출력]
#
# 각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

def generate_snail_matrix(N):
    # N x N 크기의 2차원 리스트를 0으로 초기화
    matrix = [[0] * N for _ in range(N)]

    # 방향을 나타내는 리스트 (우 → 하 → 좌 → 상 순서)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 시작 위치 (0,0)에서 시작
    x, y, dir_idx = 0, 0, 0

    # 1부터 N*N까지 숫자를 채워넣음
    for num in range(1, N * N + 1):
        matrix[x][y] = num  # 현재 위치에 숫자 저장

        # 다음 위치 계산
        nx, ny = x + directions[dir_idx][0], y + directions[dir_idx][1]

        # 다음 위치가 배열 범위를 벗어나거나 이미 채워진 경우, 방향 전환
        if not (0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 0):
            dir_idx = (dir_idx + 1) % 4  # 방향을 다음으로 변경
            nx, ny = x + directions[dir_idx][0], y + directions[dir_idx][1]

        # 이동
        x, y = nx, ny

    return matrix  # 완성된 달팽이 배열 반환



T = int(input())  # 테스트 케이스 개수 입력
for t in range(1, T + 1):  # 테스트 케이스 개수만큼 반복
    N = int(input())  # 달팽이 배열의 크기 N 입력
    result = generate_snail_matrix(N)  # 달팽이 배열 생성

    # 출력 형식 지정
    print(f"#{t}")
    for row in result:
        print(" ".join(map(str, row)))  # 행을 공백으로 구분하여 출력