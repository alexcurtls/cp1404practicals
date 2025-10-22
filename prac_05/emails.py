"""
Emails
Estimate time: 30 minutes
Actual time: 90 minutes
This program made me rethink my degree choices
"""

# email_to_name = {}

def main():
    """Main function for storing name and email in a dictionary"""
    email_to_name = {}
    while True:
        email = input("Email: ").strip()
        if email == "":
            break
        display = extract_display_name(email)
        response = input(f"Is your name {display}? (Y/n) ").strip().lower()
        if response in {"y",""}:
            name = display
            email_to_name[email] = name
        else:
            name = input("Name: ").strip()
            email_to_name[email] = name
    for email, name in email_to_name.items():
        print(f"{name} ({email})")



def extract_display_name(email):
    """Extracts the email name and converts it into a normal name"""
    clean = email.strip()
    user_name = clean.split("@", 1)[0]
    user_name = user_name.replace(".", "_")
    parts = user_name.split("_")
    display = " ".join(parts)
    return display

main()