# [문제]
# 보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
# N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
# 예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
# 10 1 9 2 8 3 7 4 6 5
# 주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
#
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100
#
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.

def special_sort(arr):
    # 리스트를 큰 숫자부터 작은 숫자 순으로 정렬 (내림차순)
    arr.sort(reverse=True)

    # 정렬된 숫자를 특별한 순서로 배치할 새 리스트 생성
    result = []

    # 왼쪽(큰 숫자)과 오른쪽(작은 숫자)를 가리킬 두 개의 인덱스 설정
    left, right = 0, len(arr) - 1

    # 최대 10개의 숫자를 선택해야 하므로 반복문 실행
    while left <= right and len(result) < 10:
        # 먼저 가장 큰 숫자를 추가
        if left <= right:
            result.append(arr[left])
            left += 1  # 다음 큰 숫자를 가리키도록 이동

        # 그다음 가장 작은 숫자를 추가
        if left <= right and len(result) < 10:
            result.append(arr[right])
            right -= 1  # 다음 작은 숫자를 가리키도록 이동

    return result


# 입력 받기
T = int(input())  # 테스트 케이스 개수 입력
for t in range(1, T + 1):
    N = int(input())  # 정수의 개수 입력
    arr = list(map(int, input().split()))  # 입력된 숫자들을 리스트로 변환
    result = special_sort(arr)  # 특별한 정렬 함수 실행

    # 결과 출력 (테스트 케이스 번호와 함께)
    print(f"#{t} {' '.join(map(str, result))}")
