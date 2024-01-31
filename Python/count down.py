import time



                                                                             
print("  oooooooo8                                    o8        oooo                                         ooooooooooo o88                                        ")
print("o888     88   ooooooo  oooo  oooo  oo oooooo o888oo ooooo888   ooooooo  oooo  o  oooo oo oooooo       88  888  88 oooo  oo ooo oooo   ooooooooo8 oo oooooo   ")
print("888         888     888 888   888   888   888 888 888    888 888     888 888 888 888   888   888          888      888   888 888 888 888oooooo8   888    888 ")
print("888o     oo 888     888 888   888   888   888 888 888    888 888     888  888888888    888   888          888      888   888 888 888 888          888        ")
print(" 888oooo88    88ooo88    888o88 8o o888o o888o 888o 88ooo888o  88ooo88     88   88    o888o o888o        o888o    o888o o888 888 888o  88oooo888 o888o       ")

print()
print()
print()
print()
print()
count_time = int(input("How many seconds long to wait?: "))

for x in range(count_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 60 / 60) % 60
    print(f"\r                                                          {hours:02}:{minutes:02}:{seconds:02}", end="")
    time.sleep(1)
print()