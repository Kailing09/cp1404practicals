import random

def determine_score_status(score):
    """Determine the status of the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def main():
    user_score = float(input("Enter score: "))
    print(determine_score_status(user_score))

    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f}")
    print(determine_score_status(random_score))

main()
