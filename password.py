# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確 就印出 "登入成功！"
# 如果不正確 就印出 "密碼錯誤！ 還有＿次機會！"

# 此區學生理解範圍解答
#x = 0
#y = 2
#while x < 3:
#	password = input('請輸入密碼,最多輸入3次:')
#	if password ==  'a123456':
#		print('登入成功！')
#	else:
#		print('密碼錯誤！ 還有' ,y ,'次機會！')
#	x = x+1
#	y = y-1


#老師最佳解答區
password = 'a123456'
i = 3 # 剩餘機會
while True:
	pwd = input('請輸入密碼： ')
	if pwd == password:
		print('登入成功！')
		break #逃出迴圈
	else:
		i = i - 1
		print('密碼錯誤！ 還有' , i, '次機會')
		if i == 0:
			break

