
# Decimal to binary

def decimalToBinary(decimal):
    if decimal == 0:
        print("Decimal to binary: 0")
        return
    binaryStr = ''
    while(decimal>0):
        if decimal%2==0:
            binaryStr+='0'
        else:
            binaryStr+='1'
        decimal = decimal//2

    print(f'Decimal to binary {binaryStr[::-1]}')


decimal = int(input("Enter the decimal number:"))
decimalToBinary(decimal)


# Binary to decimal

def binaryToDecimal(binary):
#1000
    pow = 0
    decimal = 0
    for i in binary[::-1]:
        decimal = decimal + (int(i)*(2**pow))
        pow+=1

    print(f'Decimal is {decimal}')


binary = (input("Enter the Binary Number:"))
binary = binary.strip()
binaryToDecimal(binary)