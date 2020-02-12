



def palindrome(s):
    qu = []
    st = []

    #1
    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())

    #2
    while qu:
        if qu.pop(0) != st.pop():
            return False

    return True

print(palindrome("MoM"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam"))