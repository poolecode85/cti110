# Darion Poole
# 04/24/25
# P4HW1
# Score card using loops

score_num = int(input("How many scores do you want to enter?"))
print()

# empty list
scores = []

for num in range(1, score_num + 1):
        # collect scores
    score = float(input("Enter score #" + str(num)+ ":"))
        # Evaluate entry
    while score < 0 or score > 100:
        print("INVALID SCORE ENTERED!!!")
        print("Score should be between 0 and 100")
        score = float(input("Enter score #" + str(num) +" again: "))

    scores.append(score)

print()
        # find lowest score

lowest = min(scores)
scores_modified = scores
        # Drop lowest score
scores_modified.remove(lowest)
        #calculate average

avg = sum(scores_modified)/ len(scores_modified)
print('----------Results----------')
print(f"Lowest Score: {lowest}")
print(f"Modified List: {scores_modified}")
print(f"Scores Average: {avg:.2f}")

if avg >= 90:
    print('Grade: A')
elif avg >= 80:
    print('Grade: B')
elif avg >= 70:
    print('Grade: C')
else:
    print('Grade: F')
print('---------------------------')       

