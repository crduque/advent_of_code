def sum_2020 ():
    input_file = open("d1-input.txt", "r")
    input_lines = input_file.readlines()
    final_input = []

    for line in input_lines:
        each_line = line.split("\n")
        final_input.append(int(each_line[0]))
    
    result = 0
    
    for num1 in final_input:
        for num2 in final_input:
            if (num1 + num2) == 2020:
                result = num1 * num2

    print(result)   

sum_2020()