# [문제]
# ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
#
# 회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
# [입력]
#
#
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
#
# 다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
#
# 다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.
#
#
#
# [출력]
#
#
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

def find_palindrome():
    T = int(input())  # 테스트 케이스 개수 입력

    for tc in range(1, T + 1):
        N, M = map(int, input().split())  # NxN 글자판 크기와 회문의 길이 M 입력
        board = [input() for _ in range(N)]  # 글자판 입력 받기

        # 가로 방향 회문 찾기
        for row in board:
            for start in range(N - M + 1):  # 가능한 시작 위치를 순회
                substring = row[start:start + M]  # M 길이의 부분 문자열 추출
                if substring == substring[::-1]:  # 회문인지 확인
                    print(f"#{tc} {substring}")  # 결과 출력
                    break  # 회문을 찾았으므로 반복 종료
            else:
                continue  # 내부 루프가 break되지 않았을 경우 계속 진행
            break  # 외부 루프도 종료
        else:
            # 세로 방향 회문 찾기
            for col in range(N):  # 열을 순회하며 세로 방향 탐색
                for start in range(N - M + 1):  # 가능한 시작 위치를 순회
                    substring = ''.join(board[row][col] for row in range(start, start + M))  # 세로 방향 부분 문자열 추출
                    if substring == substring[::-1]:  # 회문인지 확인
                        print(f"#{tc} {substring}")  # 결과 출력
                        break  # 회문을 찾았으므로 반복 종료
                else:
                    continue  # 내부 루프가 break되지 않았을 경우 계속 진행
                break  # 외부 루프도 종료


# 실행
find_palindrome()  # 함수 호출