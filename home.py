print("""
====================================================================
             Welcome to Chunkerz0fc's password checker.             
====================================================================
""")

password = input("Please enter your password:  ")
length_fine = len(password) >= 8
lowercase_fine = any(char.islower() for char in password)
uppercase_fine = any(char.isupper() for char in password)
number_fine = any(char.isdigit() for char in password)
special_fine = any(not char.isalnum() for char in password)
