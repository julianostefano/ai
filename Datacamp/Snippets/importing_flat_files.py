# Open a file as read-only and bind it to file
with open('moby_dick.txt', mode='r') as file:
  	# Print it
    print(file.read())


# Read & print the first 3 lines
with open('moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

