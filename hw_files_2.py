with open ('1.txt', 'r') as file1, open('2.txt', 'r') as file2, open ('3.txt', 'r') as file3:
    text1, text2, text3 = file1.readlines(), file2.readlines(), file3.readlines()
   
str_len_list = [len(text1), len(text2), len(text3)]
file_list = [file1.name, file2.name, file3.name]
text_list = [text1, text2, text3]
dict_file = sorted(dict(zip(str_len_list, file_list)).items())
dict_file_text = sorted(dict(zip(str_len_list, text_list)).items())

with open('result.txt', 'w') as file:
    for k in range(len(file_list)):
        file.write(dict_file[k][1] + '\n')
        file.write(str(dict_file[k][0]) + '\n')
        for string in dict_file_text[k][1]:
            file.write(string)
    