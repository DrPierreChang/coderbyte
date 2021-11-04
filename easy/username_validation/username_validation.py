def CodelandUsernameValidation(strParam):

  if 25 >= len(strParam) >= 4:
    if strParam[0].isalpha():
      if strParam[-1] != "_":
        for letter in strParam:
          if sum([letter.isalpha(), letter.isdigit(), letter == "_"]) == 1:
            return "true"
  return "false"

# keep this function call here 
print(CodelandUsernameValidation(input()))
