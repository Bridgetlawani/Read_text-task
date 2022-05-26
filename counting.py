# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here
    file = open(filename, 'r')
    text = file.read()
    file.close()
    # return "Hello World"
    print(text)

    return text


read_file_content('./story.txt')


# return file.read()

#


def count_words():
    text = read_file_content("./story.txt").split(" ")
    # print(text)
    # [assignment] Add your code here

    #wd = {}
    words = {}
    for word in text:
        words[word] = words.get(word, 0) + 1
 
    print(words)

    return words


count_words()
