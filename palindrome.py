



#팔린드롬
#입력;문자s
#출력: 회문이면 True, 아니면 False

def palindrome(s):
    #큐,스택 리스트로 정리
    qu = []
    st = []

    #1단계: 문자열의 알파벳 문자를 각각 큐와 스택에 넣음
    for x in s:
        #해당 문자가 알파벳이면(공백,숫자,특수문자 아니면)
        #큐와 스택에 각각 그 문자를 추가
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())

        #2단계: 큐와 스택에 들어있는 문자를 꺼내면서 비교
    while qu:
        if qu.pop(0) != st.pop(): # 큐와 스택에서 꺼낸 문자가 다르면 회문이 아님
            return False

    return True

print(palindrome("Mom"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))