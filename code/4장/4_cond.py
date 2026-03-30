# 4_condtionals.py
temp = 16
msg = ""

if temp < 0:
    msg = "Cold"
    elif temp 10:
        msg = "Mild"
    elif temp < 20:
        msg = "Good"
    elif temp < 30:
        msg = "Hot"
    else:
        msg ="Hell"

# 변수 = 참값 if 조선식 else 거짓값 ( 삼항 조건문)

print(msg)

msg = "Let's play" if temp > 15 else "Stay home"
print(msg)

