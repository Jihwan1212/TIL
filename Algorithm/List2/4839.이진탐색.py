# [문제]
# 코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.
# 짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.
# 예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.
# 찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1 <= Pa, Pb < P <=1000
#
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.

# 테스트 케이스 개수 입력
T = int(input())


# 이진 탐색을 수행하는 함수 (재귀 방식)
def binary_search(start, end, key, count=0):
    # 탐색 범위가 유효하지 않으면 탐색 횟수 반환
    if start > end:
        return count

    # 중간값(mid) 계산
    mid = (start + end) // 2

    # 중간값이 찾고자 하는 값(key)과 일치하면 탐색 종료
    if mid == key:
        return count

    # 찾고자 하는 값이 중간값보다 작다면 왼쪽 구간 탐색 (범위: start ~ mid)
    if mid > key:
        return binary_search(start, mid, key, count + 1)

    # 찾고자 하는 값이 중간값보다 크다면 오른쪽 구간 탐색 (범위: mid ~ end)
    return binary_search(mid, end, key, count + 1)


# 각 테스트 케이스에 대해 반복 실행
for tc in range(1, T + 1):
    # P: 전체 페이지 수, Pa: A가 찾을 페이지, Pb: B가 찾을 페이지 입력
    P, Pa, Pb = map(int, input().split())

    # A와 B가 각각 이진 탐색을 수행하여 탐색 횟수 계산
    count_a = binary_search(1, P, Pa)
    count_b = binary_search(1, P, Pb)

    # 탐색 횟수를 비교하여 결과 결정
    # A가 더 빨리 찾으면 'A', B가 더 빨리 찾으면 'B', 같으면 0 출력
    result = 'A' if count_a < count_b else 'B' if count_a > count_b else 0

    # 테스트 케이스 번호와 결과 출력
    print(f'#{tc} {result}')