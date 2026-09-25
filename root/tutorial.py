state = "coding"

while True:
    if state == "coding":
        print("You're coding!")
        feeling = input("how are you feeling? ")
        if feeling == "tired":
            state = "sleeping"
        elif feeling == "hungry":
            state = "eating"
        else:
            state = "coding"

    elif state == "eating":
        print("you are eating!")
        feeling = input("How are you feeling? ")
        if feeling == "hungry":
            state = "eating"
        elif feeling == "full":
            state = "coding"
        else:
            state = "sleeping"

    elif state == "sleeping":
        print("You're sleeping!")
        feeling = input("How are you feeling? ")
        if feeling == "hungry":
            state = "eating"
        elif feeling == "awake":
            state = "coding"
        else:
            state = "sleeping"