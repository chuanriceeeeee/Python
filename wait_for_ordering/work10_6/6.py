def countWords(text):
    textList=text.split()
    return len(textList)
text=input("Input a sentence:\n")
print(f"Words' number is {countWords(text)}")

