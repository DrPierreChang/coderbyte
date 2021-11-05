def QuestionsMarks(strParam):
    first_num = None
    questions_ls = []
    
    # keep only nums and questions, remove letters
    seq = "".join((i for i in strParam
        if i.isdigit() or not i.isalpha()))
    
    tmp_str = ""
    
    # checke every element of string
    for i in seq:
        # we need separete part of string that includes two numbers and qustions between them
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
    
    # when we get all separated parts we need check them for length and sum
    check = False
    for i in questions_ls:
        if (int(i[0]) + int(i[-1])) == 10:
            if len(i) == 5:
                check = True
                continue
            else:
                return False

    if check:
        return True
    else:
        return False

# keep this function call here 
print(QuestionsMarks(input()))
