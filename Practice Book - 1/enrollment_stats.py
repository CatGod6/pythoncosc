universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachuesetts Institute of Technology", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500]
]
universities.sort()
tuition = 0
students = 0

for i in range(len(universities)) :
    students += universities[i][1]
    tuition += universities[i][2]
print("Total students : {} \nTotal tuition : {} ".format(students,tuition))

def mean() :
    mean_students = int(students/len(universities))
    mean_tuition = int(tuition/len(universities))
    print("Student mean : {} \nTuition mean : {}".format(mean_students, mean_tuition))

# def median is flawed does not compute correct median. Might be the logic or variable assignments
def median() :
          if len(universities) % 2 == 1:
              i =  int(len(universities) / 2)
          median_students = universities[i][1]
          median_tuition = universities[i][2]
          print("Median students : {} \nMedian tuition : {} ".format(median_students, median_tuition))
""" if len(universities) % 2 == 0 :
 i = int(len(universities) / 2)
 median_students = (universities[i][1] + universities[i-1][1]) / 2
 median_tuition = (universities[i][2] + universities[i-1][2]) / 2
 """

mean()
median()

