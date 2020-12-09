from netmiko import ConnectHandler
import time

def check_status(IP):

	device1 = {
		'device_type': 'cisco_ios',
		'ip': IP,
		'username': 'prashant',
		'password': 'cisco'
	}

	conn = ConnectHandler(**device1)

	print('\nConnected with ', IP)

	output = conn.send_command('show ip int brief', use_textfsm = True)

	l = len(output)

	print ('\nList of interfaces which are UP \n')

	for i in range(0,l):
	    if output[i]['status'] == 'up':
	        print (output[i]['intf'] +' ' + output[i]['status'])


	print ('\nList of interfaces which are DOWN \n')
	for i in range(0,l):
	    if output[i]['status'] != 'up':
	        print (output[i]['intf'] + ' ' + output[i]['status'])

	return output


def change_status(IP):

	device1 = {
		'device_type': 'cisco_ios',
		'ip': IP,
		'username': 'prashant',
		'password': 'cisco'
	}

	conn = ConnectHandler(**device1)

	print('\nConnected with ', IP)

	output = conn.send_command('show ip int brief', use_textfsm = True)

	name = output[1]['intf']
	status = output[1]['status']
	print ('\nInterface ' + name + ' status is ' + status )

	if status == 'up':
	    print ('Finishing the script')
	else :
	    print ('making backup interface UP')
	    config_commands = [ 'int fa0/1',
	                        'no shut' ]
	    output = conn.send_config_set(config_commands)
	    print (output)
	    print ('Finished configuration')
