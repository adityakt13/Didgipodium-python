def wcount(para):
    words = para.split()
    return len(words)

# calling
print(wcount("Here comes the pain"))

size = wcount("ABCDE ABCDE ERRUHSK jghkhkuh SJDSDJ")
print(size)

data = input("Enter a sentence: ")
size = wcount(data)
print(f"You have entered {size} words.")