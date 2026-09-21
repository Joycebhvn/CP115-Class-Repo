num_rounds = int(input("Number of rounds: "))
total_score = 0.0
for i in range (num_rounds):
    score =  int (input ("score: "))
    if score > 100:
        score = (score * 0.2) + score
        total_score = total_score + score
    else:
        total_score = total_score + score

final_score = total_score
rounds_processed = num_rounds

print(f"{final_score:.1f}")
print(rounds_processed)