class mark(object): #class: introduce each mark

	def __init__(grade, code_portfolio, poster_presentation, final_exam):
		grade.CP=code_portfolio
		grade.PP=poster_presentation
		grade.FE=final_exam #def __init__:determine each mark
	def All(grade):
		Total=grade.CP*0.4+grade.PP*0.3+grade.FE*0.3
		return Total #calculate and determine the whole mark
Ye_Yaxuan=mark(98,95,100) #input each mark
print(mark.All(Ye_Yaxuan)) #output the whole mark
