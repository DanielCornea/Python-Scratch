name = 'Zed A. Shaw'
age = 35
height = 74 # inches 
weight = 180 # lbs 
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}")
print(f"He's {height} inches tall")
print(f"He's {weight} pounds heavy")
print("Actually that is not too heavy")
print("He's got {eyes} eyes and {hair} hair")
print(f"His teeth are usually {teeth} depending on the coffee")

# This line is tricky, try to get exactly right
total = age + height + weight
print(f"If I add {age}, {height* 2.54} and {weight} I get {total}")