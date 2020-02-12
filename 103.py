'''
문자열과 내장함수
'''

msg = "It is Time"
# print(msg.upper())
# print(msg.lower())
# print(msg)
# tmp = msg.upper()
# print(tmp)
# print(tmp.find('T'))  #처음으로 나온 T의 인덱스번호를 반환하는듯
# print(tmp.count('T'))
# print(tmp)
# print(msg[:2])  #2번 전까지 추출
# print(msg[3:5])  #3~4까지
# print(len(msg))  #길이라서 그냥 1부터 세는건가
# for i in range(len(msg)):
#     print(msg[i], end = ' ')
# print()



for x in msg:
    print(x, end = ' ')
print()

for x in msg:
    if x.isupper():
        print(x, end = ' ')
print()

for x in msg:
    if x.islower():
        print(x, end = ' ')
print()

for x in msg:
    if x.isalpha():
        print(x, end = ' ')
print()

tmp = 'AZ'
for x in tmp:ㄴ
    print(ord(x))  #아스키코드

tmp = 'az'
for x in tmp:
    print(ord(x))
    
tmp = 66
print(chr(tmp))    #아스키코드로 몇번이 무슨알파벳인지 알려줌