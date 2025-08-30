import string
import random
n = int(input("Enter the number of character you want in your password:"))
all_characters = string.ascii_letters + string.digits + string.punctuation
generate_password = "".join(random.choices(all_characters,k=n))
print("Your secure password is:",generate_password)
