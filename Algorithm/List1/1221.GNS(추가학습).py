# [문제]
# 숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.
# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
# 0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.
# 예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.

# [입력]
# 입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.
# 그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백 문자 후 테스트 케이스의 길이가 주어진다.
# 테스트 케이스의 길이란, 문자열의 글자수가 아닌 단어의 갯수를 말한다.
# 그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.

# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다.

# 숫자 단어와 실제 숫자의 매핑
num_map = {
    "ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
    "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9
}
reverse_map = {v: k for k, v in num_map.items()}  # 숫자 -> 단어 변환용

T = int(input().strip())  # 테스트 케이스 개수 입력

for _ in range(T):
    test_case_info = input().split()  # "#번호 길이" 입력
    test_case_number = test_case_info[0]  # "#1" 같은 테스트 케이스 번호

    words = input().split()  # 숫자 단어 입력
    sorted_numbers = sorted(words, key=lambda word: num_map[word])  # 숫자 순서로 정렬

    sorted_string = " ".join(sorted_numbers)  # 공백으로 구분하여 출력 형식 맞춤
    print(f"{test_case_number} {sorted_string}")  # 결과 출력
