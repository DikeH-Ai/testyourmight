import string
import secrets
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    if (sum(c.islower() for c in password) >= 3
            and sum(c.isupper() for c in password) >= 3
            and sum(c.isdigit() for c in password) >= 3):
        break


print(password)