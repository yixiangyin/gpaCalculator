import csv
import sys


def main():
    if (len(sys.argv)!=2):
        print("Usage: python3 gpaCalculator.py scores.csv")
        return
    
    scores = process(sys.argv[1])
    get_average_score(scores)
    get_average_gpa(scores)


def process(filename):
    scores = {}
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_row = {}
            for field in row:
                # convert to int if possible
                if row[field].isdigit():
                    new_row[field] = int(row[field]) 
                else:
                    new_row[field] = row[field]
            scores[row["course"]] = new_row
    return scores


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
        # pass
        return 'P'
    elif (score < 70):
        # credit
        return 'CR'
    elif (score < 80):
        # distinction
        return 'D'
    else:
        # high distinction
        return 'HD'


def get_average_score(scores):
    sum = 0
    course_count = len(scores)
    for course in scores:
        # don't take CRS into account
        if type(scores[course]["score"]) is int: 
            sum += int(scores[course]["score"])
        else:
            course_count -= 1
    average = round(sum / course_count, 2)
    print(f"Your average score: {average}/100")


main()
