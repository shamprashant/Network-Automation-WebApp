from netmiko import ConnectHandler
import time

def do_backup(IP):

	try:

		device1 = {
			'device_type': 'cisco_ios',
			'ip': IP,
			'username': 'prashant',
			'password': 'cisco'
		}

		conn = ConnectHandler(**device1)

		print('\nConnected with ', IP)

		time.sleep(2)

		conn.send_command('term length 0')
		output = conn.send_command('show run')

		with open(IP + ' backp.txt','w') as file:
			file.write(output)

		output = []
		output.append('Your device backup has been done \n')
		output.append('backup file name: ' + IP + ' backup.txt')
		print('Your device backup has been done \n')
		print('backup file name: ' + IP + ' backup.txt')

	except Exception as e:
		print(e)
	return output
