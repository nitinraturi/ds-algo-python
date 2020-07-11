'''
Question

Convert a decimal number to binary using stack. Return a string representation of binary number
'''

from app import Stack

def convert_int_to_bin(dec_num):
    s = Stack()
    while dec_num > 0:
        rem = dec_num % 2
        s.push(rem)
        dec_num = dec_num // 2

    binary = ""
    while len(s.get_stack()) > 0:
        binary = binary + str(s.pop())

    return binary

print(convert_int_to_bin(74))
print(convert_int_to_bin(25))
print(convert_int_to_bin(26))
print(convert_int_to_bin(94))