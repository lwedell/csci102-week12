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
