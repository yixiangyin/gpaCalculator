import csv
import sys
def main():
    if (len(sys.argv)!=2):
        print("Usage: python3 gpaCalculator.py scores.csv")
        return
    
    scores = {}
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_row = {}
            for field in row:
                if row[field].isdigit():
                    new_row[field] = int(row[field]) 
                else:
                    new_row[field] = row[field]
            scores[row["course"]] = new_row
    
    get_average_score(scores)
    get_average_gpa(scores)
def get_average_gpa(scores):
    # weighted grade point score
    wgps = 0
    unit = 0
    for course in scores:
        score = scores[course]["score"]
        if type(score) is int:
            ng = get_numeric_grade(score)
            wgps += ng * scores[course]["unit"]
            unit += scores[course]["unit"]
    gpa = round(wgps/unit, 2)
    print(f"Your GPA: {gpa}/7")

def get_numeric_grade(score):
    if (score < 50):
        # fail
        return 0
    elif (score < 60):
        return 4
    elif (score < 70):
        return 5
    elif (score < 80):
        return 6
    else:
        return 7
def get_grade(score):
    if (score < 50):
        # fail
        return 'F'
    elif (score < 60):
        return 'P'
    elif (score < 70):
        return 'CR'
    elif (score < 80):
        return 'D'
    else:
        return 'HD'
def get_average_score(scores):
    sum = 0
    # without CRS
    course_count = len(scores)
    for course in scores:
        if scores[course]["score"] != "CRS":
            sum += int(scores[course]["score"])
        else:
            course_count -= 1
    average = round(sum / course_count, 2)
    print(f"Your average score: {average}/100")


main()
