row_file = open("extract.txt", "r")
# Read file data to variable
data_list = row_file.read().split("|")
print(data_list)
modi_list = []
for sub in data_list:
    if len(sub) > 1:
        modi_list.append(sub.replace(" ", ""))
print(modi_list)
out_file = open("mname.txt", "w")
for i in modi_list:
    try:
        int(i)
        out_file.write(i + "\n")
    except:
        out_file.write(i + "#")