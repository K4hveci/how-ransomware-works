# how-ransomware-works
 A basic ransomware to learn what is ransomware and how it is working.

# What is a Ransomware:
Ransomware is a program that enrypts your files, hacker wants money and you should pay to save/use your files.
This ransomware uses "fernet" to encrypt and decrypt and stores key to a file named "ransomkey.key" so you will have the key.
To make this ransomware safer, this program runs at a certain directory and doesn't go to upper or lower directories.

# How to try:
If you want to try this ransomware, create a directory and in that folder create a normal txt file and write down somethings to that folder.
Move ```ransom.py``` to that directory and run.
Now you will see that txt file is encrypted and there is a key file.
Now move ```ransomdecoder.py``` to that directory and run it to decrypt your file.