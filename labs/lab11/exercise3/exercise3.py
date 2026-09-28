number = int(input())
count = 0
previous_number = number
biggest_jump = 0

while number != 0:
    count += 1

    jump = number - previous_number
    if jump > biggest_jump:
        biggest_jump = jump

    previous_number = number
    number = int(input())

print(count)
print(biggest_jump)
