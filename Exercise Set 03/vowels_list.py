def extract_vowels(stringname):
    vowels = 'a,e,i,o,u,A,E,I,O,U' 
    vowels_count = []
    for char in stringname:
        if char in vowels:
            vowels_count.append(char)
    return vowels_count

input_string = input("Enter a String: ")
result = extract_vowels(input_string)
print(result)
    