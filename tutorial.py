#################################################
#################################################
#PYTHON TUT0RAIL              #AUTHOR: ARUN
#DATE : 02.01.2016
#################################################
#################################################



#################################################
				# STRING
#################################################

# EXAMPLE 1
# =========

# print "All String Methods"
# name = raw_input("Enter Your Input")
# print "Hello",name
# print len(name)
# print type(name)
# print name[0]
# print name[-1]
# print name[1:4]
# print name[3:]
# print name[2:]
# print name[0:10:2] #with step
# print name[::1]
# print name[::-1]
# print name[:]
# print name.lower()
# print name.upper()
# print name.capitalize()
# print name.swapcase()
# print name.title()


#################################################
				# CONDITIONAL STATEMENT	
#################################################

#NO SWITCH IN PYTHON

#IF STATEMENT

# name = raw_input('Enter your Name')
# if len(name) < 4:
# 	print "You are Lazy"
# 	print "Length of the Name is less than four"
# elif len(name) > 10 : 
# 	print "You have a long statement"
# else:
# 	print name

# print "end of if"

#################################################


#WHILE

# name = raw_input('Enter your Name')
# count=0

# while  count<len(name):
# 	 print name[count]
# 	 if name[count]=='i':
# 	 	print 'I'
# 	 print "end of if"
# 	 count=count+1
# print "End Of While"


#################################################

# FOR

# i=1
# for x in range(1,20,i):
# 	print x,x**2,x**3
# 	i=i+1
# for x in range(90,80,-1):
# 	print x

#################################################
				# FUNCTION -#1
#################################################

# EXAMPLE 1
# =========

# def perimeter(radius,pi=3.14):
# 	return 2*pi*radius

# print perimeter(5,3.1456)
# print perimeter(5)
# print perimeter(5,22.0/7)	

# EXAMPLE 2
# =========

# def diff(a,b):
# 	if a>b:
# 		return a-b
# 	else:
# 		return b-a


# print diff(5,3)
# print diff(5,3)


#################################################
		 		# LIST AnD ARRAYS
#################################################

#DEFINITION : 


# EXAMPLE 1
# =========

#Arrays are List

# a=[1,5,8,3,5,9,7]

# print type(a)
# print a[0]
# print a[-1]
# print len(a)
# print sum(a)
# print min(a)
# print max(a)
# print a[2:5]
# print a[::2]

# a.sort()
# print a

# a.reverse()
# print a

# a.append(9)
# print a

# print a.count(5)

# a.remove(9)
# print a

# c=a.pop()
# print c
# print a

# a.extend([7,8,9])
# print a

# a.index(8)

# EXAMPLE 2
# =========

# b = ['hello','are','You',' ']

# b.sort()
# print b

# b.reverse()
# print b

# b.remove(min(b))
# print b

# 'hello' in b

# print True+True  # OUTPUT : 2

#################################################
				# TUPLES
#################################################

# DEFINITION : A TUPLE IS A READ ONLY LIST , IMMUTABLE

# EXAMPLE 1
# =========

# a = (1,5,8,3,5,9,7)

# print type(a)
# print a[0]
# print a[-1]
# print len(a)
# print min(a)
# print max(a)
# print a[2:5]
# print a[::2]

# EXAMPLE 2
# =========

# b=3,4,5
# print type(b) 
# print b.count(4)
# print b.count(3)
# print b[2]
# b[2] =45 # OUTPUT : ERROR [TUPLE DOES NOT SUPPORT ITEM ASSIGNMENT]
# b.append(3) # OUTPUT : ERROR [TUPLE DOES NOT SUPPORT ITEM ASSIGNMENT]
# b.sort() # OUTPUT : ERROR [TUPLE DOES NOT SUPPORT ITEM ASSIGNMENT]


#################################################
				# DICTIONARY
#################################################

# DEFINITION : {'key1':'value1','key2':'value2'} , No Sorting in Dictionary.

# EXAMPLE 1
# =========

# d = {'H':'Hydrogen' ,'O':'Oxygen'};

# print type(d)
# print d.keys()
# print d.values()
# print d.items()
# print d['H']   # OUTPUT : Hydrogen
# print d.get('H') # OUTPUT : Hydrogen
# d['C']= 'Carbon' # OUTPUT : Adding an Element
# print d
# del d['H']
# print d
# print type[d.items()]


#################################################
				# PRINTING
#################################################


# EXAMPLE 1
# =========

# print ("Hello World")
# print ("Hello","India")
# print ("{} is a {}".format('water','liquid'))
# print "Average height of indian men is %f" % 1.62 # OUTPUT : 1.620000
# print "Average height of indian men is %d" % 1.62 # OUTPUT : 1
# print "Average height of indian men is %s" % 1.62 # OUTPUT : 1.62

#################################################
				# SET
#################################################

# DEFINITION : COMBINATION OF UNIQUE ELEMENTS

# EXAMPLE 1
# =========

# s1 = {3,4}
# s1.add(2)
# s1.add(3)
# s1.add(4)
# s1.add(5)
# print s1  # OUTPUT :set([2, 3, 4, 5])
# s2 = {3,6,7,8}
# print s2
# u = s1.union(s2)
# i = s1.intersection(s2)
# print u
# print i


#################################################
				# ADVANCED ASSIGNMENTS
#################################################


# EXAMPLE 1
# =========
# a=b=c=2 # OUTPUT : a=2 b=2 c=2

# EXAMPLE 2
# =========
# a,b,c = 2,3,4 # OUTPUT : a=2 b=3 c=4

# EXAMPLE 3 [UNPACKING]
# =====================
# a=[4,5,6]
# x,y,z = a # OUTPUT : x=4 y=5 z=6

# EXAMPLE 4 [SWAPPING]
# ====================
# a=10
# b=5
# a,b=b,a
# print a
# print b

#################################################
				# FUNCTION -#2
#################################################

# EXAMPLE 1
# =========

# def squarecube(x):
# 	return x*x,x**3
# s,c = squarecube(3)
# print s 
# print c

# EXAMPLE 2 [To Handle any number of arguments]
# =============================================

# def add(*args):
# 	print type(args)  # OUTPUT : Tuple
# 	print args
# 	print sum(args)

# add(2,3,4,5)
# add(2,3,4,5,2,3,4,5,2,3,4,5,2,3,4,5)

# EXAMPLE 3
# =========

# def wish(name,age):
# 	print "Hello {} you are {} years old".format(name,age)

# wish('indian',70)
# wish(70,'indian')
# wish(age=50,name='Kenya') #KeyWord Argument Style
# wish('African',80)
# wish() # OUTPUT : Error

# EXAMPLE 4 [Use ** for Passing Elements to Dictionary]
# =====================================================

# def createEmployee(**kwds):
# 	print type(kwds)
# 	print kwds

# createEmployee()
# createEmployee(name='Ramesh')
# createEmployee(name='Ramesh',job='Trainer')
# createEmployee(name='Ramesh',job='Trainer',mobile=987654325)

# EXAMPLE 5
# =========

# g =23
# k =45

# def abc():
# 	g=2
# 	k=3
# 	print locals() #Prints Locals Variables

# abc()
# print globals()
# print g
# print k

# EXAMPLE 6 [Cannot modify global value from function - unless untill Global is Specified to the left of variable]
# ================================================================================================================

# age=10
# def grow():
# 	global age
# 	age=age+1
# grow()
# print age

#################################################
				# ITERATION [LIST]
#################################################

# EXAMPLE 1
# =========

# d=[None,False,2,3.45,'hi',[],(),{},{4,5}]

# for x in d:
# 	print type(x)

#################################################
				# TYPE-CASTING
#################################################

# EXAMPLE 1
# =========

# a=4.5
# b=6

# print int(a)
# print float(b)

# c='hello'
# d='30'

# print int(d)
# print list(c)

# e=(4,5)
# f=[4,5,6]

# print list(e)
# print tuple(f)

# g={'h':'hello','b':'byee','g':'good morning'}
# print list(g)

# EXAMPLE 2
# =========

# a='hyderabad'
# b=[1,2,3,4,55]
# c=(6,4,8,9)
# d= {'H':'Hydrogen' ,'O':'Oxygen'};
# e={4,5,3}

# for x in a: print x
# for x in b: print x
# for x in c: print x
# for x in d: print x
# for x in e: print x

# EXAMPLE 3
# =========

# d={'a','apple'}
# e={4,5,3}

# for x in d: print x
# for x in enumerate(e):print x
# for index,value in enumerate(e):print index,value 
# for i,v in enumerate(e):print i,v 


#################################################
				# FILES
#################################################


# EXAMPLE 1 [Modes : [w: WRITE,r: READ, a: APPEND] ]
# ==================================================

# f = open('C:\Users\NEKAR01\Desktop\Certification\Python\ca876.txt','w') # WRITE MODE
# f.write('hello\n')
# f.write	('hi\n')
# k=['ca\n','fidelity\n','Rambo\n','Wells Fargo\n','Cisco\n','Ramon\n']
# f.writelines(k)
# f.close()

# EXAMPLE 2
# =========

# f = open('C:\Users\NEKAR01\Desktop\Certification\Python\ca876.txt','r') # READ MODE
# print f.read()
# f.close()

# EXAMPLE 3
# =========

# f = open('C:\Users\NEKAR01\Desktop\Certification\Python\ca876.txt','r') # READ MODE [Read File Character by Character]
# print f.read(1)
# print f.read(1)
# f.close()

# EXAMPLE 4
# =========

# f = open('C:\Users\NEKAR01\Desktop\Certification\Python\ca876.txt','r') # READ MODE [Read File line by line- First Two lines]
# print (f.readline())
# print (f.readline())
# f.close()

# EXAMPLE 5
# =========

# f = open('C:\Users\NEKAR01\Desktop\Certification\Python\ca876.txt','r') # READ MODE [Read File line by line - All the lines]
# lines = f.readlines()
# print(lines)
# f.close()

# EXAMPLE 6
# =========

# f = open('C:\Users\NEKAR01\Desktop\Certification\Python\ca876.txt','w') 
# lines = f.readlines()
# print(lines)
# f.close()

# EXAMPLE 7
# =========

# f = open('C:\Users\NEKAR01\Desktop\Certification\Python\ca876.txt','w') 
# f.write('this is line one')
# f.close()

# EXAMPLE 8
# =========

# f = open('C:\Users\NEKAR01\Desktop\Certification\Python\ca876.txt','a') 
# f.write('this is a new line')
# f.close()

# EXAMPLE 9
# =========

# f = open('C:\Users\NEKAR01\Desktop\Certification\Python\ca876.txt','r')
# for line in f:
# 	print line, #[, used to stop \n ]
# f.close()

# EXAMPLE 10
# =========

# f = open('C:\Users\NEKAR01\Desktop\Certification\Python\ca876.txt','r')
# for line in f:
# 	print line.rstrip()
# f.close()

#################################################
				# MORE STRING OPERATIONS[SEARCH]
#################################################

# EXAMPLE 1  #Excecute in Console
# ===============================

# a = "Tomorrow is not an Holiday"
# 'not' in a #TRUE

# EXAMPLE 2 []
# =========

# a = "Tomorrow is not an Holiday"

# print 'not' in a
# print 'is' in a
# print 'half' in a

# print a.startswith('Tomorrow')
# print a.startswith('Tom')
# print a.endswith('tom')		
# print a.endswith('y')


#################################################
				# COMMENTS
#################################################

# SINGLE LINE COMMENT

''' THIS IS A MULTI-LINE
 MULTI-LINE COMMENT '''

#################################################
				# Challenge
#################################################

# EXAMPLE 1
# =========

# def getindices(word,char):
# 	j=[]
# 	for idx,chr in enumerate(word):
# 		if chr==char:
# 			j.append(idx)
# 	return j
# print getindices('banana','a')

# Challenge 2
# =========

# Cow is a Domestic animal
# It Gives us Milk
# Cow is a Domestic animal
# Cow is a Domestic animal	

# f = open('C:\Users\NEKAR01\Desktop\Certification\Python\ca876.txt','r') # READ MODE [Read File line by line- First Two lines]

# for line in f:
# 	if line.lower().index('cow')<0:
# 		print line
		
# f.close()		



