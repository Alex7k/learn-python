# https://en.wikipedia.org/wiki/Collatz_conjecture

# Rules:
# If number even: divide by 2
# If number odd: multiply by 3 and add 1

samples = 100000
leaderboard = []
for starting_number in range(1, samples):
  # measure how many steps to end up in the 4, 2, 1 loop
  step = 0
  largest_number = starting_number
  number = starting_number
  while True:
    step += 1
    if number % 2 == 0:  # even
      number = number // 2
    else:  # odd
      number = number * 3 + 1
    largest_number = max(largest_number, number)
    # print(number)
    if number == 1:
      # print(f"{starting_number} arrived at loop at step {step} with highest number being {largest_number}")
      leaderboard.append([starting_number, step, largest_number])
      break

print("Leaderboard:")
print("Starting number, achieved step, highest number")
leaderboard.sort(key=lambda x: x[2], reverse=True)
leaderboard_length = min(len(leaderboard), 10)
for i in range(leaderboard_length):
  print(leaderboard[i])
