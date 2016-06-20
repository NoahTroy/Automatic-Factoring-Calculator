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
	
	
	
#import the math module for solving the more complicated math (such as finding square roots), and the pickle module for loading and reading (and creating if necessary) the data file containing the powers list. In addition, import os to test for the necessary data file.
import math , pickle , os

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
	ListOfPowers = pickle.load(PowersListFile)
	PowersListFile.close()
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
			UnderSqrtResult = ('√' + UnderSqrt)
		else:
			UnderSqrt = str(UnderSqrt)
			UnderSqrtResult = ('i ' + '√' + UnderSqrt)
			
			
	#We must now declare the divisor here as well, since it can't be simplified either, if the square root can't:
	Divisor = (2*(a))
	#We must also save this original divisor for later as well:
	OriginalDivisor = Divisor
	

#If the number can be simplified, than we will follow the process below,to simplify it and return the correct and accurate result:				
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
	
	#Find the correct range for the divisor, depending on whether or not it is negative:
	if (Divisor > 0):
		range1 = 1
		range2 = (Divisor + 1)
	elif (Divisor < 0):
		range1 = Divisor
		range2 = ((Divisor - Divisor) - Divisor)
	else:
		##############################################FIX##############################################
		print('YOUR A-TERM IS A ZERO, THIS IS UNACCEPTABLE AT THE MOMENT AND HAS CRASHED MY CALCULATOR!!!')
		exit()
		##############################################FIX##############################################
	
	#Define a list of factors for the divisors, and also a common factors list:
	FactorsForDivisor = []
	FactorsForbiggestdivisorsimplified = []
	CommonFactors = []
	#Factors of Divisor
	for i in range(range1 , range2):
		if i == 0:
			continue
		CurrentDivisor = (Divisor / i)
		if (CurrentDivisor == (int(CurrentDivisor))):
			FactorsForDivisor.append(i)
	#Factors of biggestdivisorsimplified:
	for i in range(1 , (biggestdivisorsimplified + 1)):
		CurrentDivisor2 = (biggestdivisorsimplified / i)
		if (CurrentDivisor2 == (int(CurrentDivisor2))):
			FactorsForbiggestdivisorsimplified.append(i)

		#Find the common factors:
	for i in FactorsForDivisor:
		if (i in FactorsForbiggestdivisorsimplified):
			CommonFactors.append(i)
	#Find the greatest common factor:
	GCFindex = (len(CommonFactors) - 1)
	if GCFindex >= 0:
		GCF = CommonFactors[GCFindex]
	else:
		GCF = -1

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
			UnderSqrtResult = (biggestdivisorsimplified + '√' + remainder)
			biggestdivisorsimplified = int(biggestdivisorsimplified)
			remainder = int(remainder)
		else:
			biggestdivisorsimplified = str(biggestdivisorsimplified)
			remainder = str(remainder)
			UnderSqrtResult = (biggestdivisorsimplified + 'i' + '√' + remainder)
			biggestdivisorsimplified = int(biggestdivisorsimplified)
			remainder = int(remainder)

#Now that we've simplified and solved under the square root, let's put the right side of the equation (the side we've solved) into the correct form/syntax:
#Convert the Divisor and UnderSqrtResult to strings for presentation:
UnderSqrtResult = str(UnderSqrtResult)
Divisor = str(Divisor)
#If the UnderSqrtResult is equal to 0, just make the entire RightSideSolveResult 0:
if UnderSqrtResult == '0':
	RightSideSolveResult = '0'
else:
	RightSideSolveResult = ('(' + UnderSqrtResult + '/' + Divisor + ')')




#Now we will simplify he first or left half of the equation:
#Define the Numerator and the Denominator:
Numerator = ((b-b)-b)
Denominator = OriginalDivisor

#Define a list of factors for the Numerator and the Denominator:
FactorsForNumerator = []
FactorsForDenominator = []
CommonFactors = []

#Find the ranges for the Numerator and Denominator:
if Numerator < 0:
	range1 = Numerator
	range2 = ((Numerator - Numerator) - Numerator)
elif Numerator > 0:
	range1 = ((Numerator - Numerator) - Numerator)
	range2 = Numerator
else:
	######################################FIX######################################
	print('NO SUPPORT YET!!!!!! GO AWAY!!!!!!!')
	exit()
	######################################FIX######################################
if Denominator < 0:
	range1b = Denominator
	range2b = ((Denominator - Denominator) - Denominator)
elif Denominator > 0:
	range1b = ((Denominator - Denominator) - Denominator)
	range2b = Denominator
else:
	######################################FIX######################################
	print('NO SUPPORT YET!!!!!! GO AWAY!!!!!!!')
	exit()
	######################################FIX######################################

#Factors of Numerator:
for i in range(range1 , range2):
	if i == 0:
		continue
	CurrentNumerator = (Numerator / i)
	if (CurrentNumerator == (int(CurrentNumerator))):
		FactorsForNumerator.append(i)
#Factors of Denominator:
for i in range(range1b , range2b):
	if i == 0:
		continue
	CurrentDenominator = (Denominator / i)
	if (CurrentDenominator == (int(CurrentDenominator))):
		FactorsForDenominator.append(i)
		
	#Find the common factors:
for i in FactorsForNumerator:
	if (i in FactorsForDenominator):
		CommonFactors.append(i)
#Find the greatest common factor:
GCFa = CommonFactors[(len(CommonFactors) - 1)]
GCFb = CommonFactors[0]
#Make sure we find the factor's absolute value, and judge it as greatest because of that:
#Convert all possible GCFs to positive numbers, to help determine their absolute values:
if GCFb < 0:
	GCFb2 = ((GCFb - GCFb) - GCFb)
else:
	GCFb2 = GCFb
if GCFa < 0:
	GCFa2 = ((GCFa - GCFa) - GCFa)
else:
	GCFa2 = GCFa
#Determine which has the greatest absolute value, an assign it as the GCF:
if GCFa2 > GCFb2:
	GCF = GCFa
else:
	GCF = GCFb

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
else:
	x1 = '0'
	x2 = '0'
	
#Declare Final Results:
FinalResults = ('x = ' + x1 + '\nx = ' + x2)
print('\n\n\n\nRESULTS:\n\n' , FinalResults , sep = '' , end = '')
