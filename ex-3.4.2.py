user_string = input("Please enter a string:")
to_replace = user_string[0]
if (len(user_string) > 1):
	out_string = user_string[0] + user_string[1:].replace(to_replace, 'e')
else:
	out_string = user_string[0]

print(out_string)