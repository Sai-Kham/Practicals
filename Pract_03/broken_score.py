def main():
    score = float(input("Enter Score: "))
    print(determine_score_condition(score))

def determine_score_condition(score):
    if score < 0 or score > 100:
        return"Invalid Score"
    elif score >= 90:
        return"Excellent"
    elif score >= 50:
        return"Pass"
    else:
        return"Bad"
main()