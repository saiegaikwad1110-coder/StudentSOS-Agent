# Motivational Messages Generator - Inspire students during their study sessions
import random

def motivation():
    # List of motivational messages for students
    messages = [
        "You've got this! Every study session gets you closer to your goal.",
        "Don't give up! Success comes to those who keep trying.",
        "Small steps lead to big achievements. Keep going!",
        "Believe in yourself! You're smarter than you think.",
        "Learning is a journey, not a race. Enjoy the process!",
        "You are capable of amazing things. Now go prove it!",
        "Your hard work today will pay off tomorrow.",
        "Focus on progress, not perfection. You're doing great!",
        "Every expert was once a beginner. Keep learning!",
        "Challenges make you stronger. Embrace them!",
        "You have the power to achieve your dreams. Start now!",
        "Consistency is key. Study a little every day."
    ]
    
    # Pick a random message from the list
    random_message = random.choice(messages)
    
    # Display the motivational message
    print("\n" + "="*55)
    print("✨ MOTIVATIONAL MESSAGE ✨")
    print("="*55)
    print(random_message)
    print("="*55 + "\n")


# This allows the file to be tested independently
if __name__ == "__main__":
    motivation()
