class Employer():
    def __init__(self, name, sales, bonushrs, basesalary):
        # Initialize the Employer object with the provided parameters
        self.name = name
        self.sales = sales
        self.bonushrs = bonushrs
        self.basesalary = basesalary
    
    def info(self):
        # Display information about the employee
        print(" Name is {}..bonushrs is {}. Sales are {} Base salary is {}."
            .format( self.name, self.bonushrs, self.sales, self.basesalary))
    
    # The following method is commented out because it's not implemented in the code
    # def calculateNetSalary():

# Create instances of the Employer class
emp1 = Employer("soulaiman", 1000, 0, 0)
emp2 = Employer("abdelrahim", 3000, 10, 0)

# Display information about each employee
emp1.info()
emp2.info()