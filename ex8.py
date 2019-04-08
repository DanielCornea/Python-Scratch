formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(True, False, True, False))
print(formatter.format(
    "\nOut of the night that covers me\n", 
    "Black as the pit from pole to pole\n",
    "I thank whatever gods may be\n",
    "For my unconquerable soul\n",
))