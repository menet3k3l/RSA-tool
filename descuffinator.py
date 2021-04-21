text = input("Enter deciphered text: ")

text_arr = text.split()

for i in range(len(text_arr)):
    text_arr[i] = text_arr[i][:-1]

text = "".join(text_arr)

#print(text)

count = 0
x = ""
text_arr.clear()
for i in range(len(text)):
    count = count + 1
    x = x + str(text[i])
    if count == 2:
        text_arr.append(x)
        x = ""
        count = 0

print(text_arr)

text_ascii = ""
for letter in text_arr:
    text_ascii = text_ascii + chr(int(letter))

print(text_ascii)