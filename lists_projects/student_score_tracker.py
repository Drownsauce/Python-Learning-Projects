#Travis Delcambre
from functools import reduce

#returns highest score, lowest score, and average_score
def student_stats(scores):
    highest_score = reduce(lambda x, y: y if y[1] > x[1] else x, scores)
    lowest_score = reduce(lambda x, y: y if y[1] < x[1] else x, scores)
    average_score = (sum(x[1] for x in scores) / len(scores))
    return highest_score, lowest_score, average_score

student_scores = []

#While loop to go through all inputs and appends it to students_scores list
while True:
    try:
        student = input("Enter name (or stop): ").strip().lower()
        if student == 'stop':
            break

        score = int(input("Enter Score: "))

        student_scores.append((student.title(), score))
    except ValueError:
        print("Score must be a float!")

#prints the stats
highest, lowest, average = student_stats(student_scores)
print(f"Top score {highest[1]} ({highest[0]})")
print(f"Lowest score {lowest[1]} ({lowest[0]})")
print(f"Average {average:.2f}")
