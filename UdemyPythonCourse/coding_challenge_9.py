def student_discount(x):
    return x - 0.1 * x


def additional_discount(x):
    student_dis = student_discount(x)
    return student_dis - 0.05 * student_dis

result = additional_discount(10)
print result
