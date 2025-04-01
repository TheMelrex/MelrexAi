import ast,os

#بارگزاری اطلاعات قبلی
digits = ast.literal_eval(open("DigitsWord.txt","r").read())
digits_data = ast.literal_eval(open("Digitsdata.txt").read())
rev_digits = {v:k for k,v in digits.items()}


text = ""
number = 0

#حذف کل لاین های خالی
while 60 in digits_data:
	digits_data.remove(60)
	number += 1
	print(number,end="\r")
if number > 0:
	with open("Digitsdata.txt","w") as file:
		file.write(str(digits_data))
		
answer = input("\n(1) Change to english,(2) See All characters: ")

if answer == "1":
	#ساخت کلمات با ارقام
	for num in digits_data:
		trans = rev_digits[num]
		text += trans
		print(text,end="\r")
elif answer == "2":
	print(len(digits_data))