


with open("devices.txt", "a") as file :
    file.write("192.168.1.1\n192.168.2.2\n192.168.1.3\n")


with open("devices.txt", "r") as file :
    content = file.readline()

for cont in content :
    print(content)
