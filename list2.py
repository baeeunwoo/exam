

a = (23, 12, 36, 53, 19)
if all(50 > x for x in a):  #모두가 다 참이어야한다
    print("YES")
else:
    print("NO")

if any(11 > x for x in a):  # 한번이라도 참이면 o
    print("YES")
else:
    print("NO")