char1, char2= input("Enter two space-separated character:").split()
greater_Val = max (char1, char2,)

asciiVal1 = ord(char1)
asciiVal2 = ord(char2)

print("------------------------------------------------")
print("The character with greater value is: ", greater_Val )
print("------------------------------------------------")

print("This part is optional to include.")
print("Showing ASCII VAlues:")
print(char1, " : ", asciiVal1)
print(char2, " : ", asciiVal2 )
