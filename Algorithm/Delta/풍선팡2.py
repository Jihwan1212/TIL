# [문제]
# 종이 꽃가루가 들어있는 풍선이 NxM 크기의 격자판에 붙어있는데, 어떤 풍선을 터뜨리면 상하좌우의 풍선이 추가로 터진다고 한다.
# 다음의 경우 가운데 풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다.
# NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면, 한 개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는 꽃가루 수 중 최대값을 출력하는 프로그램을 만드시오.
# (3<=N, M<=100)
#
# 입력
# 첫 줄에 테스트케이스 수 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N과 M, 이후 N줄에 걸쳐 M개씩 풍선에 든 종이 꽃가루 개수가 주어진다.
#
# 출력
# #과 테스트케이스 번호, 빈칸에 이어 종이 꽃가루의 최대 개수를 출력한다.


def max_flower_count(T):
    results = []
    for tc in range(1, T + 1):
        N, M = map(int, input().split())  # 격자 크기 N x M 입력
        grid = [list(map(int, input().split())) for _ in range(N)]  # 꽃가루 개수 격자 입력

        max_flowers = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향

        for i in range(N):
            for j in range(M):
                flower_sum = grid[i][j]  # 현재 풍선을 터뜨릴 때의 꽃가루 개수

                # 상하좌우 풍선이 추가로 터짐
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < N and 0 <= nj < M:
                        flower_sum += grid[ni][nj]

                max_flowers = max(max_flowers, flower_sum)

        results.append(f"#{tc} {max_flowers}")

    return results


# 입력 받기
T = int(input().strip())  # 테스트 케이스 개수
output = max_flower_count(T)

# 결과 출력
for line in output:
    print(line)