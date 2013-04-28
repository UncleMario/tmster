def update_calification(student, points):
	student.total_surveys += 1
	student.points += points
	student.calification = student.points / student.total_surveys
	student.save()