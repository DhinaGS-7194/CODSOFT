import random
import string

def generate_password(length):
    characters=string.ascii_letters+string.digits
    password=""
    for _ in range(length):
        password+=random.choice(characters)
    return password

length=int(input("Enter the desired password length: "))
generated_password=generate_password(length)
print(f"Password: {generated_password}")

