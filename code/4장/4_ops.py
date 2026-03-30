    #4_operators.py
a = 132
b = 45

fmt0 = '{:<10}'		#변수 + 공백 10개 까지
fmt1 = '0b{:08b} ox{:02x} {:3}' # 0b________ 8개 2진법, 0x__ 16진법 2개,

#bit and &
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))

n = 30
print('-'*n)

print(fmt0.format('a & b'), fmt1.format(a&b, a&b, a&b))

#bit Xor ^
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))
print('-' * n)
print(fmt0.format('a ^ b'), fmt1.format(a^b,a^b,a^b))
        
#bit not ~
print("\nbit NOT ~")
print(fmt0.format('a'), fmt1.format(a,a,a))
print('-' * n)
print(fmt0.format('~a'), fmt1.format(~a&0xff,~a&0xff,~a&0xff))
      

#bit 왼쪽 쉬프트 <<
print("\nbit 왼쪽 쉬프트 <")
print(fmt0.format('a'), fmt1.format(a,a,a))
print('-' * n)
print(fmt0.format('~a'), fmt1.format(~a<<2&0xFF,~a<<2&0xFF,~a<<2&0xFF))

#bit 오른쪽 쉬프트 >>
print("\nbit 오른쪽  쉬프트 >")
print(fmt0.format('a'), fmt1.format(a,a,a))
print('-' * n)
print(fmt0.format('~a'), fmt1.format(~a>>2&0xFF,~a>>2&0xFF,~a>>2&0xFF))
