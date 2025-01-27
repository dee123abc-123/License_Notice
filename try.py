class bio:                                    #class
	def __init__(self, str1, str2):           #init is a contructor of the class, automatically called when new intance of class is created, str1,2 are parameters
		self.a=str1
		self.b=str2
		self.c="29"
	def company(self):
		print("the employee name is " + self.a)
		print("the employee company is " + self.b)
		print("employee age is " + self.c)
		
var=bio("deepak", "lovelocal")                #creates instance of class
var.company()                                 #calls the already initialised method

var1=bio("rahul", "infosys")
var1.company()
