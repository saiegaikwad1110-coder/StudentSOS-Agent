def planner():
    print("===== StudentSOS Study Planner =====")

    subject = input("Enter the subject: ")
    hours = float(input("How many hours do you have? "))
    topics = int(input("How many topics do you need to study? "))

    time_per_topic = hours / topics

    print("\nYour Study Plan:")
    print("Subject:", subject)

    for i in range(1, topics + 1):
        print(f"Topic {i}: {time_per_topic:.2f} hours")

if __name__ == "__main__":
    planner()