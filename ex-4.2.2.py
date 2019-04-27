#
# Detect polindrom without using loops
#
input_str = input("Enter your string: ")
# stripdown spaces (according to requirements)
stripped_input = input_str.replace(" ","")
if (stripped_input == stripped_input[::-1]):
    print("OK")
else:
    print("NOT")