
state = "playing hockey"

while True:
    if state == "playing hockey":
        print("Current state: Playing Hockey")
        feeling = input("How are you feeling? (tired / hungry): ").lower()

        if feeling == "tired":
            state = "sleeping"
        elif feeling == "hungry":
            state = "eating"
        else:
            print("Invalid choice, staying in current state.")

    elif state == "eating":
        print("Current state: Eating")
        feeling = input("How are you feeling? (full / ready): ").lower()

        if feeling == "full":
            state = "sleeping"
        elif feeling == "ready":
            state = "playing hockey"
        else:
            print("Invalid choice, staying in current state.")

    elif state == "sleeping":
        print("Current state: Sleeping")
        feeling = input("How are you feeling? (awake / hungry): ").lower()

        if feeling == "awake":
            state = "playing hockey"
        elif feeling == "hungry":
            state = "eating"
        else:
            print("Invalid choice, staying in current state.")

    elif state == "studying":
        print("Current state: Studying")
        feeling = input("How are you feeling? (done / tired): ").lower()

        if feeling == "done":
            state = "playing hockey"
        elif feeling == "tired":
            state = "sleeping"
        else:
            print("Invalid choice, staying in current state.")
