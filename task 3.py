import random
characters= ['A','B','C','D','E','F','G','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','+','-','|','<','>','/','?','~']
print("\n_______Welcone to Password Generator_______")
length= int(input("\nMention the length of your password: "))
password= " "
for i in range(1,length+1):
    char= random.choice(characters)
    password+=char
print("Your generated password is: ", password)