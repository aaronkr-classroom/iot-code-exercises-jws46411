# 4_loops.py
cars =['Tesla', 'Hyundai', 'KIa', 'Honda', 'Ford']
    
# 리스트 컴프리헨션을 이용하여 리스트 만들기 ( 짝수일 때)
prices = [i**2 for i range (1,13) if i % 2 == 0]

for car in cars:
    print(f"My new car is {car}!")
    
for price in prices:
    print(f"it cost ${price},000!")
