from netmiko import ConnectHandler
import sys
import time
from automation_app import get_config
from automation_app import backup
from automation_app import status

def change_status():
	pass

def exit():
	print('\nBye!')
	sys.exit(0)

def do_required_task(choice,IP):
	choice = int(choice)
	output = ''
	if choice == 1:
		output = get_config.get_running_config(IP)
	if choice == 2:
		output = backup.do_backup(IP)
	if choice == 3:
		output = status.check_status(IP)
	if choice == 4:
		output = status.change_status(IP)
		
	return output
