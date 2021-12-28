# def highlight_word(sentence, word):
#     i = sentence.index(word)

#     return(sentence[i].upper())


# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))
w="Have a nice day"
print(w.index("nice")," ",w.count("nice"))
new_w=w.replace("nice","nice".upper())
print(new_w)