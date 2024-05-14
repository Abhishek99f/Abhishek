
import time
import random

print("This is Cricket game")

plist=["Rohit Sharma","Virat Kohli","Surya Kumar Yadav","Kl Rahul","Shivam dubay","Ravindra Jadeja","Ms Dhoni","Kuldeep yadav","Bhuvneswar kumar","Yuvi chahal","Jasprit Bumrah"]
alist = ["David Warner", "Steve Smith", "Aaron Finch", "Glenn Maxwell", "Mitchell Marsh", "Alex Carey", "Marcus Stoinis", "Pat Cummins", "Adam Zampa", "Josh Hazlewood", "Mitchell Starc"]

print(''' 
      Batters
      1. Rohit Sharma
      2. Virat Kohli 
      3. Surya Kumar Yadav
      4. Kl Rahul
      5. Shivam dubay
      6. Ravindra Jadeja
      7. Ms Dhoni
      Bowlers
      8. Kuldeep yadav
      9. Bhuvneswar kumar
      10. Yuvi chahal
      11. Jasprit Bumrah''')

ball = [1,2,3,4,6,"out","Missed"]
aus_weights = {
    "David Warner":  [0.07, 0.16, 0.05, 0.3, 0.2, 0.02, 0.2],
    "Steve Smith": [0.25, 0.125, 0.15, 0.25, 0.1, 0.015, 0.16],
    "Aaron Finch":[0.1, 0.1, 0.1, 0.23, 0.2, 0.02, 0.25],
    "Glenn Maxwell":[0.2, 0.13, 0.1, 0.25, 0.1, 0.02, 0.22],
    "Mitchell Marsh": [0.1, 0.25, 0.1, 0.22, 0.25, 0.03, 0.15],
    "Alex Carey":  [0.2, 0.1, 0.09, 0.2, 0.2, 0.02, 0.19],
    "Marcus Stoinis":  [0.1, 0.2, 0.08, 0.25, 0.2, 0.02, 0.15],
    "Pat Cummins":  [0.1, 0.2, 0.15, 0.1, 0.1, 0.1, 0.35],
    "Adam Zampa": [0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3],
    "Josh Hazlewood":[0.1, 0.1, 0.1, 0.2, 0.1, 0.1, 0.3],
    "Mitchell Starc": [0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.2], 
}

weights = {
    "Rohit Sharma":[0.07, 0.06, 0.05, 0.3, 0.3, 0.02, 0.2],
    "Virat Kohli": [0.2, 0.125, 0.15, 0.25, 0.1, 0.015, 0.16],
    "Surya Kumar Yadav": [0.1, 0.1, 0.1, 0.23, 0.2, 0.02, 0.25],
    "Kl Rahul": [0.2, 0.11, 0.1, 0.25, 0.1, 0.02, 0.22],
    "Shivam dubay": [0.1, 0.15, 0.05, 0.22, 0.3, 0.03, 0.15],
    "Ravindra Jadeja": [0.2, 0.1, 0.13, 0.2, 0.2, 0.02, 0.15],
    "Ms Dhoni": [0.1, 0.1, 0.09, 0.23, 0.3, 0.02, 0.15],
    "Kuldeep yadav": [0.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.3],
    "Bhuvneswar kumar": [0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3],
    "Yuvi chahal": [0.1, 0.1, 0.1, 0.2, 0.1, 0.1, 0.3],
    "Jasprit Bumrah": [0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.2],
}
print("India is batting First")

runs_balls = {player: {"runs": 0, "balls": 0} for player in plist}
nball = 0
player_index = 0
runs = 0

for _ in range(300):
    bowling = 1
    if bowling == 1:
        if player_index >= len(plist):
            print("All out")
            break
        
        choice = random.choices(ball, weights=weights[plist[player_index]])[0]
        nball += 1
        
        if choice == "out":
            print(plist[player_index], "got out")
            runs_balls[plist[player_index]]["balls"] += 1
            time.sleep(1)
            player_index += 1
        elif choice == "Missed":
            print(plist[player_index], "Missed the ball")
            runs_balls[plist[player_index]]["balls"] += 1
        else:
            runs+=choice
            runs_balls[plist[player_index]]["runs"] += choice
            runs_balls[plist[player_index]]["balls"] += 1
            time.sleep(0.1)
            print(plist[player_index], "scored", choice)
    

print("Total runs =", runs)
print("Total balls bowled =", nball)
print("Australian needs",runs+1,"to win ")
print("Australian batting is going to start in 5 seconds")
time.sleep(5)

aruns_balls = {player2: {"runs": 0, "balls": 0} for player2 in alist}
aball = 0
aplayer_index = 0
aruns = 0

for _ in range(300):
    bowling = 1
    if bowling == 1:
        if aplayer_index >= len(alist):
            print("All out")
            break
        
        choice = random.choices(ball, weights=aus_weights[alist[aplayer_index]])[0]
        aball += 1
        
        if choice == "out":
            print(alist[aplayer_index], "got out")
            aruns_balls[alist[aplayer_index]]["balls"] += 1
            time.sleep(1)
            aplayer_index += 1
        elif choice == "Missed":
            print(alist[aplayer_index], "Missed the ball")
            aruns_balls[alist[aplayer_index]]["balls"] += 1
        else:
            aruns+=choice
            aruns_balls[alist[aplayer_index]]["runs"] += choice
            aruns_balls[alist[aplayer_index]]["balls"] += 1
            time.sleep(0.1)
            print(alist[aplayer_index], "scored", choice)
print("Runs and balls faced by each indian player:")
for player, stats in runs_balls.items():
    print(player, "- Runs:", stats["runs"], "- Balls:", stats["balls"])
print(" ")
# Display runs scored and balls faced by each player
print("Runs and balls faced by Australian each player:")
for player2, stats2 in aruns_balls.items():
    print(player2, "- Runs:", stats2["runs"], "- Balls:", stats2["balls"])

print("Total runs =", aruns)
print("Total balls bowled =", aball)

if aruns>runs:
    print("Australia is winner ")
    print("Australian won the match by",aruns-runs,"runs")
else:
    print("India is winner ")
    print("India won the match by",runs-aruns,"runs")