user_input = input()
password = "This_is_password"

flag = True
for i in range(len(password)):
  if user_input[i] != password[i]:
    flag = False


if flag == True:
  print("パスワードが合っています")
else:
  print("パスワードが間違っています")
