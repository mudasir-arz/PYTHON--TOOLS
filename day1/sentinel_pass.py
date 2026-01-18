import secrets
import string
def sentinel_tool():
    print("Sentine Tool v1.0: Security Tool")
    length=16
    chars=string.ascii_letters+string.digits+string.punctuation
    secure_password=''.join(secrets.choice(chars) for _ in range(length))

    print(f"[+] suggested secure key:{secure_password}")
    print("-"*35)

    user_pass= input("[?] Enter a password to audit:")
    #checking for weeknes
    score=0
    if len(user_pass)>=12: score+=1
    if any(c.isdigit() for c in user_pass): score+=1
    if any(c in string.punctuation for c in user_pass): score+=1
    print(f"[*] Audit Result:{score}/3 Strength Points")
    if score<2:
        print(":[!]WARNING: This password is 'very easy' for hackers.")
    else:
        print("[V] PASS: This meets basic strength.")
if __name__=="__main__":
    sentinel_tool()