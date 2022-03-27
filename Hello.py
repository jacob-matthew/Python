#Testing out Pythonista 3
#
#
import time
def main():
  
	name = input("Enter Your name: ")
	if (name) == "Raely":
		print("Hello!  I love you with all my heart!")
	if (name)	== 'Myles':
			print('Hey little homie I love You!')
	else: 
		print("Hello Bitch! Go Away!! ")
		time.sleep(3)
	restart = input('Do you want to restart?')
	if (restart) == 'y':
		main()
	else:
		print('Goodbye!')
		
main()
