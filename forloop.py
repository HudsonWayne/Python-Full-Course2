import time

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
    
    if seconds == 0:
        print("Welcome to mufakose!")