n = int(input())

mask = (1 << n.bit_length()) -1  # bit_length return required bit to write a digit in binary and << bitwise left operator shift 1 left according to value 1<< k
print(n^mask)

