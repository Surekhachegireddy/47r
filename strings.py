
#whether the string is lower case, uppercase and number
character=input("Enter character:")
code=ord(character)
if code>=65 and code<=90:
    print(character,"is uppercase")
elif code>=97 and code<=122:
    print(character,"is lowercase")
elif code>=48 and code<=57:
    print(character,"is number")
else:
    print("Not an uppercase, lowercase & number")



    #write a function to convert vowel charecters into the next charecter
    def vowel(name):
    secret=" "
    for i in range(len(name)):
        code=ord(name[i])
        if name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u':
            secret+=chr(code+1)
        else:
            secret+=name[i]
        return secret
    print(vowel("Surekha"))