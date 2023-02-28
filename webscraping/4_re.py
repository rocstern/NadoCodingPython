import re

# ca?e
# care, cafe, case, cave
# caae, cabe, cace, cade, ....


# 패턴을 컴파일함
# 변수 petern에 ca.e 라는 규칙이 적용됨
pattern = re.compile("ca.e")

# . 하나의 문자를 의미
# ^ 문자열 시작을 의미
# $ 문자열 종료를 의미

def print_match(m):
    if m:
        print("m.group() : ", m.group())  # 일치하는 문자열 반환
        print("m.string : ", m.string)  # 입력받은 문자열
        print("m.start() : ", m.start())  # 일치하는 문자열의 시작 index
        print("m.end() : ", m.end())      # 일치하는 문자열의 끝 index
        print("m.span() : ", m.span())      # 일치하는 문자열의 끝 index
    else:
        print("매칭이 되지 않음")

# match 주어진 문자열의 처음부터 일치하는지 확인
# m = pettern.match("good care")

# search 주어진 문자열 중에 일치하는게 있는지 확인
# m = pettern.search("good care")

# print_match(m)

# findall 일치하는 모든것을 리스트 형태로 전달
lst = pattern.findall("care cafe ceed bike cake")
print(lst)


# 정규식 쓰는 법
# 1. pattern = re.compile("원하는 형태")
# 2. match = pattern.match("비교할 문자열)
# 3. search = pattern.search("비교할 문자열)
# 4. lst = pattern.findallß("비교할 문자열)

