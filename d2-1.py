def valid_password ():

    input_file = open("d2-1-input.txt", "r")

    valid_passwords = 0

    for row in input_file:

        each_pw_array = row.split(" ") # ["1-3", "a:", "abdce"]

        min_max = each_pw_array[0].split("-") # ["1", "3"]
        minimum = int(min_max[0]) # 1
        maximum = int(min_max[1]) # 3

        quitting_points = each_pw_array[1].split(":")
        letter = quitting_points[0] # a

        password = each_pw_array[2] # abcde

        how_many = password.count(letter)

        if minimum <= how_many <= maximum:
            valid_passwords += 1

    print(valid_passwords)
    return valid_passwords

valid_password()