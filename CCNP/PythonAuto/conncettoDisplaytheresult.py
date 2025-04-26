from netmiko import ConnectHandler

#Define the networl devices details
device ={

    "device_type": "cisco_ios",  # Adjust based on your device (cisco_nxos, juniper, etc.)
    "host": "192.168.1.1",       # Replace with your device IP
    "username": "admin",         # Replace with your username
    "password": "password123",   # Replace with your password 
}

try:
    print(f"Connecting to {device['host']}...")
    connection= connection = ConnectHandler(**device)

        # Send a command and get the output
    commands = ["show ip interface brief","show version", "show running-config"]
    for cmd in commands:
        output = connection.send_command(commands)
        print(f"Command Output:\n{output}")
    # Close the connection
    connection.disconnect()
    print("Connection closed.")
except Exception as e :
    print(f"An error occured : {e}")

    
