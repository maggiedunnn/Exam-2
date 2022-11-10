#The author is Maggie Dunn
#This is Problem 2 on the programming part of Exam 2
recipe = {"milk" : 1, "flour" : 2.5, "oil" : 0.5, "eggs" : 4, "vanilla extract" : 0.125}
def print_ingredients(d):
    list1 = []
    for item in d:
        list1.append(item)
    list2 = []
    for item in d:
        list2.append(d[item])
    index = 0
    list3 = []
    while index < len(list1):
        list3.append([list1[index], list2[index]])
        index += 1
    list4 = sorted(list3)
    return list4
