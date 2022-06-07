import random
import tkinter
value = random.randint(1, 100)
print("welcome")
print("man yek adad bein 1 ta 100 entekhab kardam. bego on chande?")
shans = int(input("chand shans lazem dari? : "))
while True:
	hads = int(input("hadset chie? : "))
	if hads == value:
		print("afarin! doroste!")
		shans = shans - 1
		input("mamnon az hamrahit")
		break
	elif hads > value:
		print(f"adad man KAMTAR az {hads} hast." )
		shans = shans - 1
		print(  f" {shans} shans barat baghi moonde.")
		if shans == (0):
			print(f"Payan , natonesti , adad {value} bood")
			input("mamnon az hamrahit")
			break

		continue
	elif hads < value:
		print(f"adad man BISHTAR az {hads} hast." )
		shans = shans - 1
		print(  f" {shans} shans barat baghi moonde.")
		if shans == (0):
			print(f"Payan , natonesti , adad {value} bood")
			input("mamnon az hamrahit")
			break

		continue
