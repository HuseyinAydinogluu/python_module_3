import sys

print(f" === Player Score Analytics ===")

scores = []

if len(sys.argv) == 1:
    print(f"No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
else:
    i = 1
    while(i < len(sys.argv)):
        try:
            score = int(sys.argv[i])
            scores = scores + [score]
        except:
            print(f"İnvalid parameter: '{sys.argv[i]}'")
        i += 1
    if len(scores) == 0:
        print(f"No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        total_score = sum(scores)
        average_score = total_score / len(scores)
        high_score = max(scores)
        low_score = min(scores)
        score_range = high_score - low_score

        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score}")
        print(f"High score: {high_score}")
        print(f"Low score:: {low_score}")
        print(f"Score range:: {score_range}")


