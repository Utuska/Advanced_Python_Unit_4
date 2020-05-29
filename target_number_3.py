from target_number_2 import decorators_logger


# Домашнее задание по теме «Function 2.0 args, kwargs»

@decorators_logger(r'c:\Unit\Adv_py\Unit_1(4)_nam')
def adv_print(*args, **kwargs):

    file_output = open("3.txt", 'wb')
    start = 1
    write = 0
    leng = 0

    for command, item in kwargs.items():
        if command == "max_line":
            leng = int(item)
        if command == "start":
            start = int(item)
        if command == "in_file":
            write = 1

    control_leng = []

    for i in args:
        for j in i:
            if start <= 1:
                control_leng.append(j)
                if len(control_leng) == leng:
                    string = ''.join(control_leng)
                    print(string)
                    file_output.write(string.encode() + '\n'.encode())
                    control_leng.clear()
            else:
                start -= 1
    string = ''.join(control_leng)
    print(string)
    file_output.write(string.encode())


adv_print("Солныхко лучистое улыбнулось весело", max_line=18, start=1)