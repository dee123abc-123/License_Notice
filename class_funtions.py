class example:    

#example is a class name it can be anything

     def __init__(self, str1, str2):
        self.name1=str1
        self.name2=str2
        self.name3="myself"
     def print_value(self):
         print(self.name1, self.name2, self.name3)
     def display_value(self, str1):
         self.name4=str1
         print(self.name4) 





var=example("hello", "welcome")
var.print_value()
var.display_value("str")
