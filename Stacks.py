def push():
    global top
    if top == max - 1:  # As soon as we get to the max value we must print "Stack Overflow". It is "max-1" because we're using lists and when top is max it's index is 4.
        print("Stack Overflow")
    else:  # This is when our top value is less than the max, therefore we can continue to push values into the Stack
        ele = int(input("Enter the ele = "))
        top += 1  # We increment first, and then include the value, otherwise we'd just replace the previous value!
        a[top] = ele


def pop():
    global top
    if top == -1: # If the top is -1, then it means there's no values in the stack, therefore we cannot pop anything, therefore "Stack Underflow"
        print("Stack Underflow")
    else:
        print("Deleting .... = ", a[top])
        top -= 1 # We're reducing the stack, such that it seems like the last value has been popped


def display():
    global top
    if top == -1:
        print("Stack is empty...")
    else:
        print("\nElements of stack are: ")
        for i in range(top, -1, -1): # We display from top and decrement till -1. This way our list looks like a stack
            print("| {} |".format(a[i]))
        print()


def peek():
    global top
    print("-------------------------------")
    print("Top most element = ", a[top])
    print("-------------------------------")


max = 5  # Create a max length for the stack, I've chosen 5
a = [0] * max  # Using a list to represent the Stack, therefore we need to initiate all elements and I've chosen "0"
top = -1

# By default, the top of the Stack will always be "-1". It is "-1" because when we add to the stack the top becomes 0, which correctly points to the top.
# If our top value was 0, then when we add to the stack we will point to element 1 which has nothing there.

while True:

    print("Please pick an option:\n"
          "(1) PUSH     (2) POP     (3) PEEK    (4)DISPLAY     (5) EXIT\n")

    menuInput = int(input("Enter the choice  = "))
    if menuInput == 1:
        push()
    elif menuInput == 2:
        pop()
    elif menuInput == 3:
        peek()
    elif menuInput == 4:
        display()
    elif menuInput == 5:
        break
    else:
        print("\ninvalid choice\n")
