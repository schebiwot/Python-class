#if else

marks=40
score=56

if score > marks:
    print("you passed")
else:
    print("you failed")

#elif

marks=40
score=40

if score > marks:
    print("you passed with score higher than 40")
elif score==marks:
    print("you passed with score eqaual to 40")
else:
    print("you failed")

