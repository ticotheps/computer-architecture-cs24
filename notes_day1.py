str = "10101010"
​
def to_decimal(num_string, base):
    digit_list = list(num_string)
    digit_list.reverse()
    value = 0
    for i in range(len(digit_list)):
        print(f"+({int(digit_list[i])} * {base ** i})")
        value += int(digit_list[i]) * (base ** i)
    return value
​
to_decimal(str, 2)

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
# 0

# 255 - 128 = 127 
# 127 - 64 = 63
# 63 - 32 = 31
# 31 - 16 = 15
# 15 - 8 = 7
# 7 - 4 = 3
# 3 - 2 = 1
# 1 - 1 = 0

# xxxx xxxx