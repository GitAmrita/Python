import re


pattern = r"eggs(bacon)*"
string = "test"
if re.match(pattern, string):
    print 1
else:
    print 0






