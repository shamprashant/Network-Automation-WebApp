from netmiko import ConnectHandler
import time

def get_running_config(IP):

	device1 = {
		'device_type': 'cisco_ios',
		'ip': IP,
		'username': 'prashant',
		'password': 'cisco'
	}

	conn = ConnectHandler(**device1)

	print('\nConnected with ', IP)

	print('\nGetting your device configurations.....\n\n\n')
	time.sleep(2)

	conn.send_command('term length 0')
	output = conn.send_command('show run')

	with open('output.txt','w') as file:
		file.write(output)
	print(output)
	output = []

	with open(r'C:\Users\Prashant\Desktop\network_automation\automation\output.txt','r') as read_file:
		Lines = read_file.readlines()
		for line in Lines:
			output.append(line)
	return output
