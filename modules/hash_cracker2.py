import hashlib
from colorama import init, Fore
init()

GREEN = Fore.GREEN
Mag   = Fore.MAGENTA
RESET = Fore.RESET
BLUE  = Fore.BLUE
print(f"{Mag}**************HASH CRACKER******************")
print("""
1. md5
2. sha1
3. sha256
4. sha512
5. sha3 256
""")
anan = input(": ")
if anan == "1":
    pass_found = 0                                       
    input_hash = input("Enter the hashed password: ")
    p = input("\nDo you want to use a custom wordlist? (y or n) :")
    if p == "y":
        pass_doc = input("Please enter the path of the wordlist: ")
    if p == "n":
        pass_doc = "wordlist.txt"
    try:
        pass_file = open(pass_doc, 'r')              
    except:
        print("Error:")
        print(pass_doc, "is not found.\nPlease give the path of file correctly.\n") 
        quit()
    for word in pass_file:
        enc_word = word.encode('utf-8')
        hash_word = hashlib.md5(enc_word.strip())     
        digest = hash_word.hexdigest()         
        if digest == input_hash:
            print(f"{GREEN}Password found.\nThe password is: {RESET}", word)   
            pass_found = 1
            break
    if not pass_found:
        print("Password is not found in the", pass_doc, "file")   
        print('\n')
    print("***************************************")
if anan == "2":
    pass_found = 0                                       
    input_hash = input("Enter the hashed password: ")
    pass_doc = input("\nPlease enter the path of the password wordlist: :")
    try:
        pass_file = open(pass_doc, 'r')              
    except:
        print("Error:")
        print(pass_doc, "is not found.\nPlease give the path of file correctly.\n") 
        quit()
    for word in pass_file:
        enc_word = word.encode('utf-8')
        hash_word = hashlib.sha1(enc_word.strip())     
        digest = hash_word.hexdigest()         
        if digest == input_hash:
            print(f"{GREEN}Password found.\nThe password is: {RESET}", word)   
            pass_found = 1
            break
    if not pass_found:
        print("Password is not found in the", pass_doc, "file")   
        print('\n')
    print("***************************************")
if anan == "3":
    pass_found = 0                                       
    input_hash = input("Enter the hashed password: ")
    pass_doc = input("\nPlease enter the path of the password wordlist: :")
    try:
        pass_file = open(pass_doc, 'r')              
    except:
        print("Error:")
        print(pass_doc, "is not found.\nPlease give the path of file correctly.\n") 
        quit()
    for word in pass_file:
        enc_word = word.encode('utf-8')
        hash_word = hashlib.sha256(enc_word.strip())     
        digest = hash_word.hexdigest()         
        if digest == input_hash:
            print(f"{GREEN}Password found.\nThe password is: {RESET}", word)   
            pass_found = 1
            break
    if not pass_found:
        print("Password is not found in the", pass_doc, "file")   
        print('\n')
    print("***************************************")
if anan == "4":
    pass_found = 0                                       
    input_hash = input("Enter the hashed password: ")
    pass_doc = input("\nPlease enter the path of the password wordlist: :")
    try:
        pass_file = open(pass_doc, 'r')              
    except:
        print("Error:")
        print(pass_doc, "is not found.\nPlease give the path of file correctly.\n") 
        quit()
    for word in pass_file:
        enc_word = word.encode('utf-8')
        hash_word = hashlib.sha512(enc_word.strip())     
        digest = hash_word.hexdigest()         
        if digest == input_hash:
            print(f"{GREEN}Password found.\nThe password is: {RESET}", word)   
            pass_found = 1
            break
    if not pass_found:
        print("Password is not found in the", pass_doc, "file")   
        print('\n')
    print("***************************************")
if anan == "5":
    pass_found = 0                                       
    input_hash = input("Enter the hashed password: ")
    pass_doc = input("\nPlease enter the path of the password wordlist: :")
    try:
        pass_file = open(pass_doc, 'r')              
    except:
        print("Error:")
        print(pass_doc, "is not found.\nPlease give the path of file correctly.\n") 
        quit()
    for word in pass_file:
        enc_word = word.encode('utf-8')
        hash_word = hashlib.sha3_256(enc_word.strip())     
        digest = hash_word.hexdigest()         
        if digest == input_hash:
            print(f"{GREEN}Password found.\nThe password is: {RESET}", word)   
            pass_found = 1
            break
    if not pass_found:
        print("Password is not found in the", pass_doc, "file")   
        print('\n')
    print("***************************************")