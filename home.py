print("""
============================================================================
             Welcome to Chunkerz0fc's password creator checker.             
============================================================================
""")

while True:
    password = input("Make sure to include Uppercase,lowercase,numbers and symbol characters, aswell as being atleast 8 characters long  \nPlease create your new password:")

    length_fine = len(password) >= 8
    lowercase_fine = any(char.islower() for char in password)
    uppercase_fine = any(char.isupper() for char in password)
    number_fine = any(char.isdigit() for char in password)
    special_fine = any(not char.isalnum() for char in password)

    if all([length_fine, lowercase_fine, uppercase_fine, number_fine, special_fine]):
        print("\n Password accepted.")
        break
   
    if length_fine == False:
        print("Password must be 8 characters or longer. \n")
    if lowercase_fine == False:
        print("Password must contain lowercase charcters. \n")
    if uppercase_fine == False:
        print("Password must contain uppercase characters. \n")
    if number_fine == False:
        print("Password must include atleast oen number. \n")
    if special_fine == False:
        print("Password must include atleast one special character. \n")

    
