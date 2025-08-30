import string
import random
n = int(input("Enter the number of character you want in your password:"))
generate_password = "".join(random.choices(string.ascii_letters+string.digits,k=n))
print(generate_password)