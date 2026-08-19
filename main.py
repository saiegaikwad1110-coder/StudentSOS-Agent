from calculator import calculator
from quiz import quiz
from planner import planner
from motivation import motivation
print("===================================")
print("      Welcome to StudentSOS")
print("===================================")

print("\nMenu:")
print("1. Study Assistant")
print("2. Calculator")
print("3. Quiz")
print("4. Study Planner")
print("5. Motivation")
print("6. Exit")

choice = input("\nEnter your choice: ")

if choice == "1":
    print("Study Assistant selected.")
elif choice == "2":
    calculator()
elif choice == "3":
    quiz()
elif choice == "4":
    planner()
elif choice == "5":
    motivation()
elif choice == "6":
    print("Goodbye!")
else:
    print("Invalid choice.")
