def calc_score(scores, match_count=0):
    # In case of invalid score, skip that particular score and continue counting
    # Iterates through all scores in collection if you don't pass match_count or pass 0
    # You can also pass the number of matches to count (e.g., 10)
    if match_count == 0:
        match_count = len(scores)
    result = 0
    for match_score in scores[:match_count]:
        try:
            x = int(match_score.split(':')[0])
            y = int(match_score.split(':')[1])
            if x < 0 or x > 4 or y < 0 or y > 4:
                print("Points must be >= 0 and <=4  , skipping this score...")
                continue
            diff = x - y
            if diff > 0:
                result += 3
            elif diff == 0:
                result += 1

        # Check for non-integers
        except ValueError:
            print('Non-integer found in score, skipping this score...')
            continue
    return result


# Test
bad_scores = ['a:3', '3:4', '-1:0', '1:4', '2:1']
scores = ['1:3', '3:4', '0:0', '1:4', '2:1']
calc_score(scores)
calc_score(scores, 3)
calc_score(bad_scores)