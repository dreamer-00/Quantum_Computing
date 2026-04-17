import string
def create_shift_substitutions(n):
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
    encoding, _ =create_shift_substitutions(n)
    cipher = ""
    for letter in message.upper():
        if letter in encoding:
            cipher+=encoding[letter]
        else:
            cipher+=letter
    return cipher
def decode(message, n):
    _, decoding = create_shift_substitutions(n)
    plain=""
    for letter in message.upper():
        if letter in decoding:
            plain+=decoding[letter]
        else:
            plain+=letter
    return plain
print(encode("vatsal", 25))
print(decode("YDWVDO", 25))
WORDS = {
    "THE", "AND", "IS", "HELLO", "WORLD", "THIS", "YOU", "ARE",
    "TO", "OF", "IN", "IT", "THAT", "FOR", "ON", "WITH", "AS"
}
def decode(message, shift):
    result=""
    for c in message:
        if c.isalpha():
            result+=chr((ord(c)-ord('A')-shift)%26 +ord('A'))
        else:
            result+=c
    return result
def score_text(text, word_set):
    text=text.upper()
    score=0
    for word in word_set:
        if word in text:
            score+=1
    return score
def crack_caeser(ciphertext):
    best_shift=0
    best_score=-1
    best_message=""
    for shift in range(26):
        decoded=decode(ciphertext, shift)
        score=score_text(decoded, WORDS)
        if score>best_score:
            best_score=score
            best_shift=shift
            best_message=decoded
    return best_shift, best_message
cipher="TQXXA IADXP, U MY TQDQ FA DGXQ KAGD RGOWUZS IADXP, KAG XAEQDE"
shift, message=crack_caeser(cipher)
print("Best Shift: ", shift)
print("Decoded Message: ", message)
