# Programmers Level1 문제 1 of 2
def solution(s):
    if s.lower().count('p') == s.lower().count('y'):
        return True
    else :
        return False

# Programmers Level1 문제 2 of 2
def solution2(seoul):
    answer = '김서방은 {}에 있다'.format(seoul.index("Kim"))
    return answer