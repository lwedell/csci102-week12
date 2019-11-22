# csci102-week12
# Liam Wedell
# CSCI 102 - Section B
# Week 12- Part A

def PrintOutput(string):
    print("OUTPUT %s" % string)
    

def LoadFile(file):
    with open(file, 'r') as read_file:
        output_list = []
        contents = read_file.readlines()
        for line in contents:
            if line[-1] == '\n':
                output_list.append(line[:-1])
            else:
                output_list.append(line)
            

        return output_list
    

def UpdateString(a, b, index):
    string_list = list(a)
    
    for i in range(len(a)):
       if i == index:
            string_list[i] = b
            
    new_string = "".join(string_list)
    PrintOutput(new_string)
    

def FindWordCount(l, s):
    count = 0
    for word in l:
        if word == s:
            count += 1

    return count

    
def ScoreFinder(list_1, list_2, string):
    new_string = string.lower()
    new_string = list(new_string)
    new_string[0] = new_string[0].upper()
    new_string = "".join(new_string)
    
    if new_string in list_1:
        index = list_1.index(new_string)
        score = list_2[index]
        print("OUTPUT %s got a score of %d" % (new_string, score))

    else:
        print("OUTPUT player not found")
        

def Union(list_1, list_2):
    new_list = list_1 + list_2
    return new_list
