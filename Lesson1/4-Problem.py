#Задача «Электронные часы»
n = int(input())
hours = str(n%(60*24)//60)+" "
min = str(n%60)

print(hours+min)
