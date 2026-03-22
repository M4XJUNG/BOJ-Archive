# 6763 Speed fines are not fine!
a = int(input())
b = int(input())
if b - a >= 31: print("You are speeding and your fine is $500.")
elif 21 <= b - a < 31: print("You are speeding and your fine is $270.")
elif 1 <= b - a < 21: print("You are speeding and your fine is $100.")
else: print("Congratulations, you are within the speed limit!")