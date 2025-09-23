"""
CP1404 - Menus
"""



name = input("Name: ")
print("(H)ello (G)oodbye (Q)uit")
choice = input("Choice: ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid Choice")
    choice = input("Choice: ").upper()
print("Finished.")

