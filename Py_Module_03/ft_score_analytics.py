import sys

print("=== Player Score Analytics ===")

scores = []

for argument in sys.argv[1:]:
    try:
        score = int(argument)
        scores.append(score)
    except ValueError:
        print(f"Invalid parameter: '{argument}'")

if len(scores) == 0:
    print(
        "No scores provided. Usage: "
        "python3 ft_score_analytics.py <score1> <score2> ...\n"
    )
else:
    total = sum(scores)
    average = total / len(scores)
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}\n")
