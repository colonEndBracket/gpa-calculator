cNames = ['Digital Systems Principles','Digital Lab','Physics I','Physics Lab','Discrete Math','Calculus 3']
cGrades = [91,((57*100)/70),60,90,70,60]
cWeights = [3,1,3,1,3,3]
cGPAs = [] #Gets calculated by makeCGPAs()



#Generate cGPAs List with percentage-based GPA
#for i in range(len(cGrades)):
#        cGPAs.append(float(cGrades[i])/20 - 1)

#Generate cGPAs List with scale-based GPA
for i in range(len(cGrades)):
	if cGrades[i] >= 90: #A/4
		cGPAs.append(4)
	elif cGrades[i] >= 80: #B/3
		cGPAs.append(3)
	elif cGrades[i] >= 70: #C/2
		cGPAs.append(2)
	elif cGrades[i] >= 60: #D/1
		cGPAs.append(1)
	else: #F/0
		cGPAs.append(0)

#find longestName string in array
longestName = 0
for i in range(len(cNames)):
	if (len(cNames[i]) > longestName):
		longestName = len(cNames[i])

#find longestGrade string in array
longestGrade = 0
for i in range(len(cGrades)):
	if (len(str(cGrades[i])) > longestGrade):
		longestGrade = len(str(cGrades[i]))

#Make weight total
total = 0
for i in range(len(cWeights)):
    total = total + cWeights[i]

#Find Final GPA
final = 0
for i in range(len(cGrades)):
    final = float(final + cWeights[i]*cGPAs[i])
final = format((final / total),'.2f')

#Output Formatting
labCN = '=Course Name'
labPerc = '%'
labGPA = 'GP='
headLabel = labCN+' '*(longestName-len(labCN)+1)+labPerc+' '*(longestGrade-len(labPerc)+1) + labGPA
finTitle = ' Final GPA: '+str((final))+' '
halfSpacer=(len(headLabel)-len(finTitle))/2
headFinal = "="*(halfSpacer) + finTitle + "="*(halfSpacer)

print(headFinal)
print(headLabel)
for i in range(len(cNames)):
    print(cNames[i] + ' '*(longestName-len(cNames[i])+1) + str(cGrades[i]) + ' '*( longestGrade-len(str(cGrades[i]))+1 ) + str(cGPAs[i]))