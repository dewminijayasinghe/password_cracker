#simple password cracker using python

import hashlib
from urllib.request import urlopen


#read the words from url

def readwords(url):
    try:
        wordfile = urlopen(url).read()
    except Exception as e:
        print("There is an error in the words of the wordlist", e)
        exit()
    return wordfile


 #decode the password using hash characters
 
def decodewords(password):
    results = hashlib.sha1(password.encode())
    return results.hexdigest()
 
 #bruteforce attack to the password


def attack(guesspassword,actualpassword):
    for pas in guesspassword:
        if decodewords(pas) == actualpassword:
            print("Your password is: ",pas,"\nChange it, its not secure and easy to attack...")
            exit()

           
url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
original_password = input("Enter the password: ")
actualpassword = decodewords(original_password)
 
wordlist = readwords(url).decode('UTF-8')
guesspassword = wordlist.split('\n')
 

attack(guesspassword,actualpassword)

print("Hey! I couldn't guess this password, so its secure :) ")

            



