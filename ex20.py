from sys import argv 

script, input_file = argv #separate param

#prints all file
def print_all(f): 
    print(f.read())

#goes to 0
def rewind(f):
    f.seek(0)


def print_a_line(line_count, f) :
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewindm kind of like tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)
# rewind(current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += + 1
print_a_line(current_line, current_file) 

current_file.close()