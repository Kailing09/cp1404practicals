def main():
    score_input = input("Enter your score: ")
    score = get_valid_score(int(score_input))
    menu = """(G)et a new valid score
(P)rint result
(S)how stars
(Q)uit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == "G":
            score_input = int(input("Enter a new score: "))
            score = get_valid_score(score_input)
            print(f"Your score is now {score}")
        elif choice == "P":
            print(determine_score_status(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")

        print(menu)
        choice = input(">>> ").upper()

    print("Farewell and have a great day!")

def get_valid_score(score):
    while not 0 <= score <= 100:
        print("Invalid input; please enter a number between 0 and 100.")
        score = int(input("Enter a score between 0 and 100: "))
    return score

def determine_score_status(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    print("*" * score)

main()
