max = 7
min = 2.5
mean = 4
this_course = 1.5
crude_course = 3.5 
crude = 5

#A difference between this course and  the min
difference = 100*(min-this_course)/min
print(f'the difference is: {difference:4.2f}%')
# between this course and the max
difference = 100*(max-this_course)/max
print(f'the difference about the max is: {difference:4.2f}%')
# between this course and the mean
difference = 100*(mean-this_course)/mean
print(f'the difference about the mean is: {difference:4.2f}%')

#B  percentage of garbage time 
trash_mean = 100*(crude-mean)/crude
print(f'The result of trash time is: {trash_mean:4.2f}%')
trash_act = 100*(crude_course-this_course)/crude_course
print(f'The result of this course trash is: {trash_act:4.2f}%')

#C convertion from regular video to this coruse and vicevversa
this_course_to_regular = 10*mean/this_course
regular_to_this_course = 10*this_course/mean
print(f'The result of convertions are: \nThis course to regular: {this_course_to_regular:4.2f}hrs\nRegular to this course: {regular_to_this_course:4.2f}hrs')