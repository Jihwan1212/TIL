# [문제]
# 종이 꽃가루가 들어있는 풍선이 M개씩 N개의 줄에 붙어있고, 어떤 풍선을 터뜨리면 안에 든 종이 꽃가루 개수만큼 상하 좌우의 풍선이 추가로 터지게 되는 게임이 있다.
# 예를 들어 풍선에 든 꽃가루가 1개씩일 때, 가운데 풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다.
# NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면, 한 개의 풍선을 선택했을 때 날릴 수 있는 꽃가루의 합 중 최대값을 출력하는 프로그램을 만드시오.
# (3<=N, M<=100)
#
# 입력
# 첫 줄에 테스트케이스 수 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N과 M, 이후 N줄에 걸쳐 M개씩 풍선에 든 종이 꽃가루 개수가 주어진다.
#
# 출력
# #과 테스트케이스 번호, 빈칸에 이어 종이 꽃가루의 최대 개수를 출력한다.


def max_flower_count(grid, N, M):
    # 방향 이동 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_count = 0

    # 모든 풍선 위치에서 터뜨리기 시도
    for i in range(N):
        for j in range(M):
            initial = grid[i][j]  # 선택한 풍선의 꽃가루 개수
            total = initial  # 총 터지는 꽃가루 개수
            for dx, dy in directions:
                for step in range(1, initial + 1):
                    ni, nj = i + dx * step, j + dy * step
                    if 0 <= ni < N and 0 <= nj < M:
                        total += grid[ni][nj]
            max_count = max(max_count, total)

    return max_count


# 입력 처리
T = int(input().strip())  # 테스트 케이스 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 행(N)과 열(M) 입력
    grid = [list(map(int, input().split())) for _ in range(N)]  # NxM 배열 입력

    result = max_flower_count(grid, N, M)
    print(f"#{tc} {result}")