
MENU = "(G)et a valid score, (P)rint result, (S)how stars, (Q)uit"

def main():
    """The main menu function"""
    score = get_valid_score()
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_grade(score)
            print(f"Result: {result}")
        elif choice == "S":
            print_asteriks(score)
        choice = input("Choice: ").upper()









def get_valid_score():
    """Get valid score between 0 or 100 inclusive"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid buddy")
        score = int(input("Score: "))
    return score

# :(

def determine_grade(score):
    """Determine grade based on score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_asteriks(score):
    print ("*" * score)

main()