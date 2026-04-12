• 홀수 달의 15일 또는 짝수 달의 16일이면 "그날"을 출력함.
  ->
  if month == 8 and day == 15:
    print("광복절")
elif (month % 2 == 1 and day == 15) or (month % 2 == 0 and day == 16):
    print("그날")
else:
    print("평일")


3. for 문을 이용해 1~50의 짝수 합을 구하되, 3의 배수는 제외하세요.
   ->
   total = 0

for i in range(2, 51, 2):
    if i % 3 == 0:
        continue
    total += i

print(total)


4. 연습문제 4.3을 while 문으로 해결하세요.
   ->
   total = 0
i = 2

while i <= 50:
    if i % 3 != 0:
        total += i
    i += 2

print(total)
