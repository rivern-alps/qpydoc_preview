import utime    # Importing a Timing Module

print_num = 5   # Define the number of prints

while print_num:
    print("hello world")
    print_num -= 1   # Decrement
    utime.sleep(2)   # Delay in 2 seconds
