# BINARY, DECIMAL, HEXADECIMAL

# 1 byte = 8 bits

# 1 nibble = 4 bits

# Hexadecimal Values (base 16; 16 total values -> 0 to f)
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a=10, b=11, c=12, d=13, e=14, f=15

str = "10101010"

def to_decimal(num_string, base):
  digit_list = list(num_string)
  digit_list.reverse()
  value = 0
  for i in range(len(digit_list)):
    print(f"+({int(digit_list[i])} * {base ** i})")
    value += int(digit_list[i]) * (base ** i)
  return value

to_decimal(str, 2)

# Example #1:
# Converting "255" from decimal into binary

# Powers of 2 for Binary: number of instances in the given number
# 128 : 1
# 64  : 1
# 32  : 1
# 16  : 1
# 8   : 1
# 4   : 1
# 2   : 1
# 1   : 1

# 255 - 128 = 127 
# 127 - 64 = 63
# 63 - 32 = 31
# 31 - 16 = 15
# 15 - 8 = 7
# 7 - 4 = 3
# 3 - 2 = 1
# 1 - 1 = 0

# 255 = 0b1111 1111 = 0xFF (hexadecimal)
# 1 + 2 + 4 + 8 = 15 (-> 'F' in hexadecimal values)
# 255 is the highest number that you can represent using bits

# Use this print statement to check your binary->decimal conversions
# print(f"{x}")

# Use this print statement to check your decimal->binary conversions
# print (f"{x:x}")