def QuestionsMarks(strParam):
    first_num = None
    questions_ls = []
    seq = "".join((i for i in strParam
        if i.isdigit() or not i.isalpha()))
    tmp_str = ""
    for i in seq:
        if i.isdigit():
            if not first_num:
                first_num = i
                tmp_str += i
            else:
                tmp_str += i
                questions_ls.append(tmp_str)
                tmp_str = ""
                first_num = None
        elif not i.isdigit():
            if first_num:
                tmp_str += i
    
    for i in questions_ls:
        if (int(i[0]) + int(i[-1])) >= 10:
            if len(i) == 5:
                continue
            else:
                return False
    
    return True

# keep this function call here 
print(QuestionsMarks(input()))
