import csv
from netmiko import ConnectHandler


def load_devices_from_csv(file_path):
    """
    Load network device configurations from a CSV file.
    """
    devices = []
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            devices.append(row)
    return devices


def connect_and_execute(device, commands):
    """
    Connect to a network device and execute commands.
    """
    try:
        print(f"Connecting to {device['host']}...")
        connection = ConnectHandler(**device)
        
        for cmd in commands:
            output = connection.send_command(cmd)
            print(f"Output for '{cmd}' on {device['host']}:\n{output}")

        connection.disconnect()
        print(f"Connection to {device['host']} closed.\n")

    except Exception as e:
        with open("ESaver.txt", "a") as file:
              file.write(str(e)+"\n")

with open("devices.txt", "r") as file :
    content = file.readlines()

for cont in content :
    print(cont.strip())

       

def main():
    # Load devices from CSV
    devices = load_devices_from_csv("devices.csv")
    commands = ["show ip interface brief", "show version", "show running-config"]

    # Execute commands on each device
    for device in devices:
        connect_and_execute(device, commands)


if __name__ == "__main__":
    main()
