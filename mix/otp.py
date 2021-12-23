import random

generate_otp = random.randint(000000, 100000)
username = input("Enter username: ")
print(f"Hello, {username}")
print(f"Here is your OTP for login, {generate_otp}")
password = input("Enter OTP for login: ")

if password == str(generate_otp):
    print("Login Successful")
else:
    print("Login failed")
