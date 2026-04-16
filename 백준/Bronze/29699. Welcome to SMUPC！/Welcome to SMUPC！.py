label = "WelcomeToSMUPC"
n = int(input())
len_label = len(label)
n %= len_label 
print(label[n - 1])