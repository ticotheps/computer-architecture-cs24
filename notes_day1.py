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

# In general, the `.format` method is considered more modern than the printf `%`
# operator.

x = 123

# Printing a value as decimal

print(x)                     # 123
print("%d" % x)              # 123
print("{:d}".format(x))      # 123

# Printing a value as hex

print(hex(x))                # 0x7b
print("%x" % x)              # 7b
print("%X" % x)              # 7B
print("%04X" % x)            # 007B
print("{:x}".format(x))      # 7b
print("{:X}".format(x))      # 7B
print("{:04x}".format(x))    # 007b

# Printing a value as binary

print("{:b}".format(x))      # 1111011, format method

# Converting a decimal number in a string to a value

s = "1234"; # 1234 is 0x4d2
x = int(s); # Convert base-10 string to value

# Printing a value as decimal and hex

print(x)                     # 1234
print("{:x}".format(x))      # 4d2

# Converting a binary number in a string to a value

s = "100101"   # 0b100101 is 37 is 0x25
x = int(s, 2)  # Convert base-2 string to value

# Printing a value as decimal and hex

print(x)                     # 37
print("{:x}".format(x))      # 25