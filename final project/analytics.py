import time
from constraint import *

#in the following I will write some test cases for 
# the different CSP approaches and analyze which ones perform well and which ones do not
    
############################BACKTRACKING##############################################

# Define a CSP problem with 5 variables with domain [1, 100]
problem = Problem()
problem.addVariables(["x1", "x2", "x3", "x4", "x5"], range(1, 50))
problem.addConstraint(AllDifferentConstraint())

# Solve the problem using BacktrackingSolver
start_time = time.time()
solution1 = problem.getSolutions()
elapsed_time = time.time() - start_time
print("Backtracking Search:")
print("Solution: ", solution1)
print("Elapsed Time: ", elapsed_time, "seconds")

#Solve for forward checking
start_time = time.time()
solution2 = problem.getSolutionIter()
elapsed_time = time.time() - start_time
print("Forward Checking:")
print("Solution: ", solution2)
print("Elapsed Time: ", elapsed_time, "seconds")

#solve for constraint propagation
start_time = time.time()
solution3 = problem.getSolutionIter(constraintPropagation=True)
elapsed_time = time.time() - start_time
print("Constraint Propagation:")
print("Solution: ", solution3)
print("Elapsed Time: ", elapsed_time, "seconds")


