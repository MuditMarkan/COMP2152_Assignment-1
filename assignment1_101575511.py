"""
Author: Mudit Markan
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"        # str
preferred_weight_kg = 20.5         # float
highest_reps = 25                   # int
membership_active = True            # bool

# Step c: Create a dictionary named workout_stats
#tuple values (yoga, running, weightlifting minutes)
# Dictionary with string keys 
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (10, 35, 60),
    "Taylor": (29, 44, 18)
}
# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend in ["Alex", "Jamie", "Taylor"]:
    total = workout_stats[friend][0] + workout_stats[friend][1] + workout_stats[friend][2]
    workout_stats[friend + "_Total"] = total

# Step e: Create a 2D nested list called workout_list
# 2D list where each row is a friend and each column is an activity
workout_list = []
for friend in ["Alex", "Jamie", "Taylor"]:
    workout_list.append(list(workout_stats[friend]))

# Step f: Slice the workout_list
# Extract and print yoga and running for all friends
yoga_running = []
for row in workout_list:
    yoga_running.append(row[:2])
print("Yoga and running minutes for all friends:", yoga_running)

# Extract and print weightlifting for the last two friends
weightlifting_last_two = []
for row in workout_list[-2:]:
    weightlifting_last_two.append(row[2])
print("Weightlifting minutes for the last two friends:", weightlifting_last_two)

# Step g: Check if any friend's total >= 120
for friend in ["Alex", "Jamie", "Taylor"]:
    if workout_stats[friend + "_Total"] >= 120:
        print("Great job staying active, " + friend + "!")

# Step h: User input to look up a friend
friend_name = input("Enter a friend's name: ")

if friend_name in ["Alex", "Jamie", "Taylor"]:
    minutes = workout_stats[friend_name]
    total = workout_stats[friend_name + "_Total"]
    print(friend_name + "'s workout minutes:")
    print("  Yoga: " + str(minutes[0]) + " minutes")
    print("  Running: " + str(minutes[1]) + " minutes")
    print("  Weightlifting: " + str(minutes[2]) + " minutes")
    print("  Total: " + str(total) + " minutes")
else:
    print("Friend " + friend_name + " not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
# Get totals from dictionary
alex_total = workout_stats["Alex_Total"]
jamie_total = workout_stats["Jamie_Total"]
taylor_total = workout_stats["Taylor_Total"]

# Finding the highest total
if alex_total >= jamie_total and alex_total >= taylor_total:
    highest_friend = "Alex"
    highest_total = alex_total
elif jamie_total >= alex_total and jamie_total >= taylor_total:
    highest_friend = "Jamie"
    highest_total = jamie_total
else:
    highest_friend = "Taylor"
    highest_total = taylor_total

# Finding the lowest total
if alex_total <= jamie_total and alex_total <= taylor_total:
    lowest_friend = "Alex"
    lowest_total = alex_total
elif jamie_total <= alex_total and jamie_total <= taylor_total:
    lowest_friend = "Jamie"
    lowest_total = jamie_total
else:
    lowest_friend = "Taylor"
    lowest_total = taylor_total
# Print results
print("Friend with highest total workout minutes: " + highest_friend + " (" + str(highest_total) + " mins)")
print("Friend with lowest total workout minutes: " + lowest_friend + " (" + str(lowest_total) + " mins)")