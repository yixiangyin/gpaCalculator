import csv
import sys


def main():
    if (len(sys.argv)!=2):
        print("Usage: python3 gpaCalculator.py scores.csv")
        return
    
#   print("Original")
    scores = process(sys.argv[1]) 
    get_average_score(scores)
    get_average_gpa(scores)
    get_WAM_average(scores)

#   print("After adding 2022-S2 result")
#   result_2022S2 = process("score/2022-S2.csv")
#   new_scores = scores | result_2022S2
#   get_average_score(new_scores)
#   get_average_gpa(new_scores)
#   get_WAM_average(new_scores)



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

def get_WAM_average(scores):
    # include the first 6 highest mark
    # COMP course only
    # excluding 1000 level course
    count = 6
    cons_count = count
    
    # l contains a list of course,score pairs
    l = []
    for key in scores:
        # filter out CRS
        if type(scores[key]["score"]) is int:
            l.append((key, scores[key]["score"]))
    l = sorted(l, key=lambda x:x[1], reverse=True)
    sum = 0
    for idx in range(0, len(l)):
        if count == 0:
            break
        cur_course = l[idx][0]
        if cur_course[:4].upper() == "COMP" and cur_course[4] != '1':
            sum += l[idx][1]
            count -= 1 
    if count != 0:
        print("You don't have enough courses to calculate") 
        return
    print(f"Your weighted average mark calculated from the 36 units of courses with the highest marks in cognate disciplines (excluding 1000-level courses): {sum / cons_count}/100")

main()
