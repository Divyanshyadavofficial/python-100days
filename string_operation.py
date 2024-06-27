#strings are immutable 
a= "!!!Divyansh!!!  !!!! yadav"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Divyansh","harsh"))
print(a.split(" "))
blogHeading = "Introduction to python"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50,".")))
print(a.count("Divyansh"))


str1 = "Welcome to the console !!!"
print(str1.endswith("!!!"))

str1 = "his name is Dan. He is an honest man."
print(str1.find("ishh")) # this will return -1 if string is not present
# print(str1.index("sshh")) this will raise an error if string is not present


str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())


str1 = "hello world"
print(str1.islower())

str1 = "We wish you a merry Christmas\n"
print(str1.isprintable())
str1="      "
print(str1.isspace())
str2 = "    "
print(str2.isspace())

str1 = "World Health Organisation"
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())
str1 = "Pyhton is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

str1 = "His name is Dan. Dan ia an honest man."
print(str1.title())