import datetime, textwrap


def ruslankonoz():
	# Open function to avoid errors
	def Open(name, mode):
		try:
			return open(name, mode)
		except:
			print(f"There was an error while opening file {name}")
			return None

	def Read(file):
		# read file and prints it out
		for line in file:
			print(line)
		file.close()  # close the file after use

	def Write(file):
		# write the message into the file
		name = input("What is your name?\n")
		answer = input("Enter your message:\n")

		# Format the message and write it into the file
		file.write(
			f'\t{datetime.datetime.now().strftime("%d/%m/%Y (%H:%M)")}: {name}\n"{textwrap.fill(answer, 100)}"\n\n')
		file.close()  # close the file after use

	# path to the file
	path = "forum.txt"

	# while infinity loop to show the menu after every action
	while True:
		fork = input("What do you to do?\n\t1. Read the messages\n\t2. Write a message\n\t3. Exit\nEnter the number:\n")
		# validating input
		try:
			fork = int(fork)
		except:
			print("Invalid input!\n")
			continue
		# switch for the main functionality
		match fork:
			case 1:
				Read(Open(path, "r"))
			case 2:
				Write(Open(path, "a"))
			case 3:
				print("See you soon!")
				break
			case _:
				print("Invalid input!\n")
				continue


if __name__ == "__main__":
	ruslankonoz()
