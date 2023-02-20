import re

# ca?e
# care, cafe, case, cave, ...

p = re.compile("ca.e")
# . : 하나의 문자를 의미
# ^ (^de) : 문자열의 시작 desk, destination | fade (x)
# $ (se$) : 문자열의 끝 case, base | face (x)

def print_match(m):
    # 매치되지 않으면 에러가 발생
    if m:
        print(m.group())
    else:
        print("매칭되지 않음")



# m = p.match("case")
# print_match(m)

m = p.search("good care")
print_match(m)
