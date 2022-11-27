# gpa calculator for [ANU policy](https://www.anu.edu.au/students/program-administration/assessments-exams/grade-point-average-gpa)
## install
- git clone this repo
## usage
- cd into the local repo
- python3 gpaCalculator.py score.csv

## format
- You should put your marks in a csv(comma seperated) file. 
- The  csv file should contain 3 columns:
	- course contains the course code
	- score contains the score out of 100 OR CRS
	- unit contains unit for each course
- An example csv file:
```
course,score,unit
COMP2420,76,6
MATH1005,82,6
COMP2100,70,6
COMP2300,77,6
MATH1014,76,6
PHYS1201,CRS,6
COMP1110,CRS,6
COMP1730,89,6
COMP1100,CRS,6
PSYC1003,CRS,6
MATH1115,71,6
PHYS1101,CRS,6
COMP3310,61,6
COMP3703,53,6
COMP2620,74,6
COMP4450,65,6
COMP2310,67,6
COMP2120,71,6
COMP1600,89,6
COMP2700,73,6
```