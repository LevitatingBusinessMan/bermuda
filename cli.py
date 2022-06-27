#!/usr/bin/python
import pwinput

print("""
  __     ___  _     _   __ 
 (_  |_|  |  |_)   / \ (_  
 __) | | _|_ |     \_/ __) 
""")

print("Please login to continue:")

password = ""
while password != "COLOMBUS":
	password = pwinput.pwinput()
	if password != "COLOMBUS":
		print("Wrong password, please try again.")


#Clear screen sequence
print(chr(27)+'[2j')
print('\033c')
print('\x1bc', end="")

print("Welcome to SHIP OS v2.4.1")
print("Type \"help\" for a list of commands")

def helpf(args):
	print("Commands:")
	for command_name in commands:
		print(f"{command_name}: {commands[command_name]['description']}")

ship_info = {
	"speed": 4, #speed in knots
	"course": 200, #course/heading in degrees
}

def show_info(args):
	print(f"Current speed: {ship_info['speed']} knots")
	print(f"Current course: {ship_info['course']} degrees")

def set_course(args):
	try:
		new_course = int(args)
		print(f"Setting course to {new_course} degrees")
		ship_info['course'] = new_course
	except:
		print("Invalid course")

def errorf(args):
	print("Ship OS memory error 0x4f4e25")
	print("Failed to execute command")

commands = {
	"help": {
		"description": "Show a list of commands",
		"run": helpf
	},
	"set_course": {
		"description": "Set ship course",
		"run": set_course
	},
	"set_speed": {
		"description": "Set ship speed",
		"run": errorf
	},
	"info": {
		"description": "Show ship statistics",
		"run": show_info
	}
}

while True:
	print("\033[92mship-os> \033[0m", end="")
	input_s = input()
	command_name = input_s.split(" ").pop(0)
	args = "".join(input_s.split(" ")[1:])
	if command_name in commands:
		commands[command_name]["run"](args)
	else:
		print(f"The command {command_name} is invalid. Please type \"help\" to see a list of commands.")
