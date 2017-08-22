def file_handling(file_name):
    file1 = open(file_name, 'w')
    lines = ["test", "best", "rest", "zest"]
    file1.writelines(lines)
    file1.close()
    file1 = open(file_name, 'r')
    content = file1.read()
    print content
    file1.close()
    file1 = open(file_name, 'a')
    file1.write("nest")
    file1.close()

file_handling("demo.txt")