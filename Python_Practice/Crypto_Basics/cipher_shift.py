from multiprocessing import Value
import string
def create_subs(n):
    encoding={}
    decoding={}
    alphabet_size=len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter=string.ascii_uppercase[i]
        subs_letter=string.ascii_uppercase[(i+n)%alphabet_size]
        encoding[letter]=subs_letter
        decoding[subs_letter]=letter
    return encoding, decoding
def encode(message, n):
    encoding, _ =create_subs(n)
    cipher=""
    for letter in message.upper():
        if letter in encoding:
            cipher+=encoding[letter]
        else:
            cipher+=letter
    return cipher
def decode(message, n):
    _, decoding=create_subs(n)
    plain=""
    for letter in message.upper():
        if letter in decoding:
            plain+=decoding[letter]
        else:
            plain+=letter
    return plain
def print_table(subst):
    for key, value in subst.items():
        print(f"{key} -> {value}")
#MAIN PROGRAM
n=1
while True:
    print("\nShift Encoder Decoder")
    print("----------------")
    print(f"\tCurrent Shift: {n}\n")
    print("\t1. Print Encoding/Decoding Tables.")
    print("\t2. Encode Message.")
    print("\t3. Decode Message.")
    print("\t4. Change Shift.")
    print("\t5. Quit.\n")
    choice=input(">> ")
    print()
    if choice=='1':
        encoding, decoding =create_subs(n)
        print("Encoding Table: ")
        print_table(encoding)
        print("Decoding Table: ")
        print_table(decoding)
    elif choice=='2':
        message=input("Enter your message here")
        print("Encoded: ", encode(message, n))
    elif choice=='3':
        message=input("Enter your message here")
        print("Decoded: ", decode(message, n))
    elif choice=='4':
        try:
            new_shift=int(input(f"New Shift (current {n} : )"))
            if new_shift<1:
                print("Shift must be > 0")
            else:
                n=new_shift
        except ValueError:
            print("Invalid Number")
    elif choice=='5':
        print("Exiting....")
        break;
    else:
        print("Invalid Choice!")
