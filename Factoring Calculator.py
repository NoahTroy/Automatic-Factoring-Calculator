##########################################
#	Written by Noah Troy, 2016	 #
##########################################

#Gather input for the three terms of the polynomial:
print('Please Enter The a, b, and c terms from the polynomial \nyou wish to have factored.\nPlease make sure the terms are from a polynomial in standard form, ie: \nax^2+bx+c\n')
a = input('a-term:\t')
b = input('b-term:\t')
c = input('c-term:\t')

#Convert inputs to integers:
try:
	a = int(a)
	b = int(b)
	c = int(c)
except:
	print('\nThere was an error processing your input. \nPlease make sure all of your terms are valid integers and try again.')
	exit()
	
#Check to make sure the a-term isn't an integer, for if it is, it will cause a ZeroDivisionError, and the input wouldn't be a polynomial, but a linear equation:
if a == 0:
	print('Your a-term is a zero. This means that your equation is linear and not a polynomial, and therefore isn\'t applicable to work with this calculator.')
	exit()
	
	
	
#import the math module for solving the more complicated math (such as finding square roots), and the pickle module for loading and reading (and creating if necessary) the data file containing the powers list. In addition, import os to test for the necessary data file.
import math , pickle , os


#Define a function to find and return the greatest common factor between two numbers:
def FindGCF(Num1 , Num2):
	#Define a function to accept a number, find its ranges, then return a list of its factors:
	def FindFactors(Num):
	#Make sure the number is an integer, before we find its factors:
		try:
			Num = int(Num)
		#If an error occurs, print an error message and stop the code:
		except ValueError as ErrorMessage:
			print('Please make sure the the numbers entered as arguments are valid integers.')
			print('Value Error:\t' , ErrorMessage)
			exit()
		except :
			print('An unknown error has occurred. Please check the validity of your supplied arguments and/or this function\'s code.')
			exit()
		
		#Now that we know the number is an integer, define a factors list:
		Factors = []
		
		#Find the range of the number, in order to cycle through all possible factors, both negative and positive:
		if Num < 0:
			range1 = Num
			range2 = (((Num - Num) - Num) + 1)
		elif Num > 0:
			range1 = ((Num - Num) - Num)
			range2 = (Num + 1)
		else:
			Factors.append(1)
			return Factors
		
		#Find the factors of Num:
		for i in range(range1 , range2):
			#Skip over 0, as to prevent a DivisionByZeroError:
			if i == 0:
				continue
			IsInt = (Num / i)
			if (IsInt == (int(IsInt))):
				Factors.append(i)
		
		#Return the list of factors:
		return Factors


	#Run the function to find the factors for each argument provided:
	FactorsOfNum1 = FindFactors(Num1)		
	FactorsOfNum2 = FindFactors(Num2)
			
	#Declare a common factors variable:
	CommonFactors = []
	
	#Find the common factors between Num1 and Num2:
	for i in FactorsOfNum1:
		if (i in FactorsOfNum2):
			CommonFactors.append(i)
	
	#Assuming that we are being supplied with the numerator and denominator of a fraction, and that the numerator is Num1 and the denominator is Num2, we want to declare a negative GCF if the denominator is a negative number and vice versa [this will still be fine even if the function isn't being used for fraction simplification]:
	if Num2 < 0:
		GCF = CommonFactors[0]
	else:
		GCF = CommonFactors[(len(CommonFactors) - 1)]
	
	#Return the greatest common factor:
	return GCF


#Solve to get one number under the square root:
UnderSqrt = ((b**2)-(4*(a)*(c)))

#Declare variable to assign our result to:
UnderSqrtResult = None

#Check to make sure that the input is an integer, to help weed out any errors later on:
try:
	UnderSqrt = int(UnderSqrt)
except ValueError as ErrorMessage:
	print('\nError Message Geek Speak:\t' , ErrorMessage)
	print('\nLayman Terms: \tYou Must Enter Valid Integers')
	exit()
except:
	print('\nAn Unknown Error Occurred')
	exit()
	
#Check for, and if applicable, remove any negatives:
UnderSqrt = str(UnderSqrt)
HayImaginaryUnit = False
if '-' in UnderSqrt:
	UnderSqrt = int(UnderSqrt)
	UnderSqrt = ((UnderSqrt - UnderSqrt) - UnderSqrt)
	HayImaginaryUnit = True
else:
	UnderSqrt = int(UnderSqrt)


#Load the list of powers if applicable. If the list doesn't exist and/or can't be found, than create the list then load it:
if os.path.isfile('List Of Powers.dat'):
	PowersListFile = open('List Of Powers.dat' , 'rb')
	
	#Make sure that the file wasn't edited or changed to make it unreadable; if it was, present an error and instruct the user to delete the file then restart the calculator:
	try:
		ListOfPowers = pickle.load(PowersListFile)
		PowersListFile.close()
	except pickle.UnpicklingError:
		print('\n\n\nERROR\nDid you open, edit, change, etc. the "List Of Powers.dat" file?\nWe have detected an issue with the file corresponding with unauthorized editing.\nTo fix this error, please delete the file, then restart the calculator and run a test problem.\nWe will then automatically regenerate the data file in the correct format.\nIn the future, please refrain from opening this file, thanks!')
		exit()
	except:
		print('UNKNOWN ERROR\nDid you open, edit, change, etc. the "List Of Powers.dat file?\nWe have detected an issue with the file corresponding with unauthorized editing.\nTo fix this error, please delete the file, then restart the calculator and run a test problem.\nWe will then automatically regenerate the data file in the correct format.\nIn the future, please refrain from opening this file, thanks!')
		exit()
		
else:
	ListOfPowers = []
	for i in range(2 , 100001):
		x = i
		x *= x
		ListOfPowers.append(x)
	PowersListFile = open('List Of Powers.dat' , 'wb')
	pickle.dump(ListOfPowers , PowersListFile)
	PowersListFile.close()
	
	PowersListFile = open('List Of Powers.dat' , 'rb')
	ListOfPowers = pickle.load(PowersListFile)
	PowersListFile.close()
	

#Create a list of quotients that evenly divide up the number under the square root, so that we may later simplify it:
if (UnderSqrt <= 10000000000):
	quotientsthatareints = []
	currentindex = 0
	while ListOfPowers[currentindex] <= UnderSqrt:
		isinteger = UnderSqrt/ListOfPowers[currentindex]
		if isinteger == int(isinteger):
			quotientsthatareints.append(ListOfPowers[currentindex])
		currentindex +=1
else:
	print('\n\nERROR: NUMBER OUT OF RANGE\nThe simplified number under the square root is greater than 10,000,000,000.')
	exit()

#Check to see if the number under the square root can't be simplified; if it can't, than we are done, and can now just assign a variable the answer/result:
if len(quotientsthatareints) == 0:
	#Check for negatives as well, and add the imaginary unit i if necessary:
	if (UnderSqrt == 0):
		UnderSqrtResult = 0
	else:
		if not HayImaginaryUnit:
			UnderSqrt = str(UnderSqrt)
			#If UnderSqrt is equal to 1, just get rid of the square root sign, and let simplification later get rid of the 1:
			if UnderSqrt == '1':
				UnderSqrtResult = (UnderSqrt)
			else:
				UnderSqrtResult = ('√' + UnderSqrt)
		else:
			UnderSqrt = str(UnderSqrt)
			UnderSqrtResult = ('i ' + '√' + UnderSqrt)
			
			
	#We must now declare the divisor here as well, since it can't be simplified either, if the square root can't:
	Divisor = (2*(a))
	#We must also save this original divisor for later as well:
	OriginalDivisor = Divisor
	

#If the number can be simplified, we will follow the process below, to simplify it and return the correct and accurate result:				
else:
	#Find and convert  the biggest divisor to be returned as (possibly only part of) the answer:
	#The index in the list of the greatest divisor found:
	finalindex = (len(quotientsthatareints) - 1)
	#Fetching the biggest divisor using its newfound location and assigning it to a variable:	
	biggestdivisor = quotientsthatareints[finalindex]
	#Simplifying the biggest divisor to its square root (because we are technically taking it out from under the square root), then assigning the simplified divisor to a variable:
	biggestdivisorsimplified = math.sqrt(biggestdivisor)
	biggestdivisorsimplified = int(biggestdivisorsimplified)
	
	#Find the remainder left under the square root:
	remainder = UnderSqrt/biggestdivisor
	remainder = int(remainder)
	
	#Before declaring the final results for under the square root, check to see if the biggestdivisorsimplified can be simplified even further by testing if it is evenly divisable by the Divisor, or if either of them have any common factors they can then be simplified down with:
	Divisor = (2*(a))
	Divisor = int(Divisor)
	#Save the original divisor, before being simplified, for use when solving for the front half of the equation:
	OriginalDivisor = Divisor
	
	#Find the GCF to simplify the Divisor and the biggestdivisorsimplified:
	GCF = FindGCF(biggestdivisorsimplified , Divisor)

	#Now simplify both the Divisor and the biggestdivisorsimplified:
	Divisor = (Divisor / GCF)
	biggestdivisorsimplified = (biggestdivisorsimplified / GCF)
	Divisor = int(Divisor)
	biggestdivisorsimplified = int(biggestdivisorsimplified)
	
	#Assign the final results for under the square root to UnderSqrtResult in the correct format/syntax:
	#If the remainder is a one, get rid of it:
	if remainder == 1:
		#Test to see if the number was negative and we need to add back in an i:
		if not HayImaginaryUnit:
			biggestdivisorsimplified = str(biggestdivisorsimplified)
			UnderSqrtResult = biggestdivisorsimplified
			biggestdivisorsimplified = int(biggestdivisorsimplified)
		else:
			biggestdivisorsimplified = str(biggestdivisorsimplified)
			UnderSqrtResult = (biggestdivisorsimplified + 'i')
			biggestdivisorsimplified = int(biggestdivisorsimplified)
	else:
		if not HayImaginaryUnit:
			biggestdivisorsimplified = str(biggestdivisorsimplified)
			remainder = str(remainder)
			#Check to see if biggestdivisorsimplified is equal to 1; if it is, just get rid of it:
			if biggestdivisorsimplified == '1':
				UnderSqrtResult = ('√' + remainder)
			else:
				UnderSqrtResult = (biggestdivisorsimplified + '√' + remainder)
			biggestdivisorsimplified = int(biggestdivisorsimplified)
			remainder = int(remainder)
		else:
			biggestdivisorsimplified = str(biggestdivisorsimplified)
			remainder = str(remainder)
			
			#Check to see if biggestdivisorsimplified is equal to 1; if it is, just get rid of it:
			if biggestdivisorsimplified == '1':
				UnderSqrtResult = ('i' + '√' + remainder)
			else:
				UnderSqrtResult = (biggestdivisorsimplified + 'i' + '√' + remainder)
			biggestdivisorsimplified = int(biggestdivisorsimplified)
			remainder = int(remainder)

#Now that we've simplified and solved under the square root, let's put the right side of the equation (the side we've solved) into the correct form/syntax:
#Convert the Divisor and UnderSqrtResult to strings for presentation:
UnderSqrtResult = str(UnderSqrtResult)
Divisor = str(Divisor)

#if the Divisor is a 1, just get rid of it:
if (Divisor == '1'):
	#If the UnderSqrtResult is equal to 0, just make the entire RightSideSolveResult 0:
	if UnderSqrtResult == '0':
		RightSideSolveResult = '0'
	else:
		RightSideSolveResult = ('(' + UnderSqrtResult + ')')
else:
	#If the UnderSqrtResult is equal to 0, just make the entire RightSideSolveResult 0:
	if UnderSqrtResult == '0':
		RightSideSolveResult = '0'
	else:
		RightSideSolveResult = ('(' + '(' + UnderSqrtResult + ')' + ' / ' + Divisor + ')')

#Save these values to help with furthur simplification down the road if necessary (Used for later on to add numbers with the same denominators):
try:
	Top = int(UnderSqrtResult)
	CanBeAdded = True
except:
	CanBeAdded = False
Bottom = int(Divisor)




#Now we will simplify the first or left half of the equation:
#Define the Numerator and the Denominator:
Numerator = ((b-b)-b)
Denominator = OriginalDivisor

#Find the GCF between Numerator and Denominator:
GCF = FindGCF(Numerator , Denominator)	

#Now simplify both the Divisor and the biggestdivisorsimplified:
Numerator = (Numerator / GCF)
Denominator = (Denominator / GCF)
Numerator = int(Numerator)
Denominator = int(Denominator)

#Get rid of the fraction if the Numerator can be divided by the Denominator, and leave you with just one integer:
IsThisAnInteger = (Numerator / Denominator)
if IsThisAnInteger == int(IsThisAnInteger):
	IsThisAnInteger = int(IsThisAnInteger)
	IsThisAnInteger = str(IsThisAnInteger)
	FirstSideSolveResult = IsThisAnInteger
else:
	Numerator = str(Numerator)
	Denominator = str(Denominator)
	FirstSideSolveResult = ('(' + Numerator + '/' + Denominator + ')')
	
	

#Now put everything in the correct syntax, then display the results:
#Get rid of half of the equation if that half is equal to 0; there is no need for it:
if ((FirstSideSolveResult == '0') and (RightSideSolveResult != '0')):
	x1 = (RightSideSolveResult)
	x2 = ('-' + RightSideSolveResult)
elif ((FirstSideSolveResult != '0') and (RightSideSolveResult == '0')):
	x1 = (FirstSideSolveResult)
	x2 = (FirstSideSolveResult)
elif ((FirstSideSolveResult == '0') and (RightSideSolveResult == '0')):
	x1 = '0'
	x2 = '0'
else:
	#Check to make sure the problem can't be further simplified by adding the numerators if the denominators are the same:
	if (((int(Denominator)) == Bottom) and CanBeAdded):
		SimplifiedNumeratorPos = str(((int(Numerator)) + Top))
		SimplifiedNumeratorNeg = str(((int(Numerator)) - Top))

		#Simplify the fractions down even furthur if possible:
		#First put the negatives in their rightful places:
		if ((Bottom < 0) and ((int(SimplifiedNumeratorPos)) >= 0)):
			Bottom = ((Bottom - Bottom) - Bottom)
			SimplifiedNumeratorPos = int(SimplifiedNumeratorPos)
			SimplifiedNumeratorPos = ((SimplifiedNumeratorPos - SimplifiedNumeratorPos) - SimplifiedNumeratorPos)
		if ((Bottom < 0) and ((int(SimplifiedNumeratorNeg)) >= 0)):
			Bottom = ((Bottom - Bottom) - Bottom)
			SimplifiedNumeratorNeg = int(SimplifiedNumeratorNeg)
			SimplifiedNumeratorNeg = ((SimplifiedNumeratorNeg - SimplifiedNumeratorNeg) - SimplifiedNumeratorNeg)
		if ((Bottom < 0) and ((int(SimplifiedNumeratorPos)) < 0)):
			Bottom = ((Bottom - Bottom) - Bottom)
			SimplifiedNumeratorPos = int(SimplifiedNumeratorPos)
			SimplifiedNumeratorPos = ((SimplifiedNumeratorPos - SimplifiedNumeratorPos) - SimplifiedNumeratorPos)
		
		
		#Find the GCF between SimplifiedNumeratorPos and Bottom, and SimplifiedNumeratorNeg and Bottom:
		#First convert each back into integers:
		SimplifiedNumeratorPos = int(SimplifiedNumeratorPos)
		SimplifiedNumeratorNeg = int(SimplifiedNumeratorNeg)
		
		GCFNumPos = FindGCF(SimplifiedNumeratorPos , Bottom)
		GCFNumNeg = FindGCF(SimplifiedNumeratorNeg , Bottom)	

		#Do the actual simplification:
		SimplifiedNumeratorPos = int((SimplifiedNumeratorPos / GCFNumPos))
		BottomA = Bottom
		BottomA = int((BottomA / GCFNumPos))
		#Eliminate any ones, zeros, or what have you:
		TestIfCanBeSimplifiedFurthur = (SimplifiedNumeratorPos / BottomA)
		if (TestIfCanBeSimplifiedFurthur == int(TestIfCanBeSimplifiedFurthur)):
			x1 = (str(int(TestIfCanBeSimplifiedFurthur)))
		else:
			SimplifiedNumeratorPos = str(SimplifiedNumeratorPos)
			BottomA = str(BottomA)
			x1 = (SimplifiedNumeratorPos + '/' + BottomA)

		#Do the actual simplification:
		SimplifiedNumeratorNeg = int((SimplifiedNumeratorNeg / GCFNumNeg))
		BottomB = Bottom
		BottomB = int((BottomB / GCFNumNeg))
		#Eliminate any ones, zeros, or what have you:
		TestIfCanBeSimplifiedFurthur = (SimplifiedNumeratorNeg / BottomB)
		if (TestIfCanBeSimplifiedFurthur == int(TestIfCanBeSimplifiedFurthur)):
			x2 = (str(int(TestIfCanBeSimplifiedFurthur)))
		else:
			SimplifiedNumeratorNeg = str(SimplifiedNumeratorNeg)
			BottomB = str(BottomB)
			x2 = (SimplifiedNumeratorNeg + '/' + BottomB)

	else:
		x1 = (FirstSideSolveResult + ' + ' + RightSideSolveResult)
		x2 = (FirstSideSolveResult + ' - ' + RightSideSolveResult)
	
#Declare Final Results:
FinalResults = ('x = ' + x1 + '\nx = ' + x2)
print('\n\n\n\nRESULTS:\n\n' , FinalResults , sep = '')
