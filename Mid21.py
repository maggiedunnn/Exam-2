#The author is Maggie Dunn
#This is Problem 1 on the programming part of Exam 2
def count_hashtag(string):
    total = 0
    index = 0
    while index < len(string):
        if string[index] == "#":
            total += 1
            index += 1
        else:
            index += 1
    return total
