from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# master_pwd = input("Please enter the master password: ")
key = load_key()
fer = Fernet(key)

def add():
    user = input("Please enter the user name: ")
    passw = input("Please enter the password: ")

    with open("passwords.txt", "a") as file:
        file.write(user + "|" + fer.encrypt(passw.encode()).decode() + "\n")

    print("Password added successfully!")

def view():
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User name: {user}, Password: {fer.decrypt(passw.encode()).decode()}")

while True:
    mode = input("Would you like to add new user or view existing user or q to quit? (add/view/q) ").lower()
    if mode == "q":
        quit()

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Please enter a valid choice.")
        continue