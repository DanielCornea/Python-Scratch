from sys import argv 

script, filename = argv 
file_again = input("> ")

txt = open(filename)

print(f"Here is your file {filename}:")
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = (open(file_again))

print(txt_again.read())

txt.close()
txt_again.close()