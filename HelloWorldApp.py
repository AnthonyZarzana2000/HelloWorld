
# Hello World Application for Course 2023S-SSW567-WS

import datetime

def my_brand(assignment_name):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("=*=*=*= Anthony Zarzana =*=*=*=")
    print()
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*=")
    print()
    print(f"=*=*=*= {assignment_name} =*=*=*=")
    print()
    print(f"=*=*=*= {current_time} =*=*=*=")
    print()

# Call my_brand func before printing Hello, World!
my_brand('Too Setup')

# Print Hello World!
print("Hello World!\n")

my_brand('Hello World Example')
