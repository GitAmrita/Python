def addition_without_using_operator(x, y):
   while(True):
       carry_out = x & y
       sum = x ^ y
       x = carry_out << 1
       y = sum
       if not(carry_out):
           return sum


if __name__ == '__main__':
    print addition_without_using_operator(0, 1)