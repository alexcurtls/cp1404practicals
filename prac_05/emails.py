"""
Emails
Estimate time: 30 minutes
Actual time:
"""

email_to_name = {}

def main():
    while True:
        email = input("Email: ")
        user_name = email.split("@", 1)[0]
        if email == "":
            break
        display = extract_display_name(email)
        print(f"Is your name {display}? (Y/n) ")
    # else:
        # name = input("Name: ")
        # email_to_name[email] = name




def extract_display_name(email):
    clean = email.strip()
    user_name = clean.split("@", 1)[0]
    user_name = user_name.replace(".", "_")
    parts = user_name.split("_")
    display = " ".join(parts)
    return display

main()