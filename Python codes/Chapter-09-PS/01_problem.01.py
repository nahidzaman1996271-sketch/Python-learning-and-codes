'''
Write a program to read the text from a given file 'poem.txt' and find out whether
if contains the word 'twinkle'.
'''

f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")

else:
    print("The word twinkle is not in the content")

f.close()