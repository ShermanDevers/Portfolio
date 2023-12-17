import time

count_time = int(input("How many seconds long to wait?: "))
for x in range(count_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 60 / 60) % 60
    print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end="")
    time.sleep(1)
