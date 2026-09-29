# unbreakable.py
# Keeps asking the user for a number until they give one.
# Uses try / except inside a while loop so it never crashes.

while True:
    text = input("Enter a number: ")
    try:
        number = int(text)
        break  # valid input - leave the loop
    except ValueError:
        print("That is not a number. Please try again.")

print("You entered:", number)
