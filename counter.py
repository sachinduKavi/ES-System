data_file = open("countdata.txt", "r")
max = -20
number_list = []
for record in data_file.readlines():
    number = record[:-1]
    mini_list = number.split(',')
    for num in mini_list:
        num = int(num)
        if num > max and not(num == 99):
            max = num
        number_list.append(num)

print(number_list)
for i in range(max+1):
    con = number_list.count(i)
    print("number " + str(i) + ": " + str(con))

print("number 99" + ": " + str(number_list.count(99)))