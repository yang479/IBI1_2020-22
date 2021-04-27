class mark(object):

	def __init__(grade, code_portfolio, poster_presentation, final_exam):
		grade.CP=code_portfolio
		grade.PP=poster_presentation
		grade.FE=final_exam
	def All(grade):
		Total=grade.CP*0.4+grade.PP*0.3+grade.FE*0.3
		return Total
Ye_Yaxuan=mark(98,95,100)
print(mark.All(Ye_Yaxuan))
