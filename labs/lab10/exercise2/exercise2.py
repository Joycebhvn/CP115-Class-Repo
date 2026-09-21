num_days = int(input())
danger_threshold = float(input())
average_temp = 0.0
total_temp = 0.0
danger_days = 0
for day in range (num_days):
    temp = float(input("Temperature: "))
    if temp > danger_threshold:
        danger_days = danger_days + 1
    total_temp = total_temp + temp
average_temp = total_temp / num_days


print(danger_days)
print(f"{average_temp:.1f}")
