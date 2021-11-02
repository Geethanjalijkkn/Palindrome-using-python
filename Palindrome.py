# 23/10/2021
#Geethanjali
#check the srting is palindrome or not 

while True:
    string = input("Enter the srting you want to check palindrome or not : ")
 
    final = ""
    for i in string:
        #final = final+i
        final = i + final
    if (string == final):
        print(string +" = "+final)
        print("It is palindrome")
    else:
        print(string +" = "+final) 
        print("It is not a palindrome")