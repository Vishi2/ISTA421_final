from constraint import *

# Define the problem
problem = Problem()

# Add variables
variables = ['Western Australia', 'Northern Territory', 'South Australia', 'Queensland', 'New South Wales', 'Victoria', 'Tasmania']
colors = ['red', 'green', 'blue']
problem.addVariables(variables, colors)

# Add constraints
problem.addConstraint(lambda x, y: x != y, ['Western Australia', 'Northern Territory'])
problem.addConstraint(lambda x, y: x != y, ['Western Australia', 'South Australia'])
problem.addConstraint(lambda x, y: x != y, ['South Australia', 'Northern Territory'])
problem.addConstraint(lambda x, y: x != y, ['Queensland', 'Northern Territory'])
problem.addConstraint(lambda x, y: x != y, ['Queensland', 'South Australia'])
problem.addConstraint(lambda x, y: x != y, ['Queensland', 'New South Wales'])
problem.addConstraint(lambda x, y: x != y, ['New South Wales', 'South Australia'])
problem.addConstraint(lambda x, y: x != y, ['Victoria', 'South Australia'])
problem.addConstraint(lambda x, y: x != y, ['Victoria', 'New South Wales'])
problem.addConstraint(lambda x, y: x != y, ['Victoria', 'Tasmania'])

# Solve the problem using each solver and print the solutions
method = "Backtracking Search"

if method == "Backtracking Search":
    solutions = problem.getSolutions()
elif method == "Forward Checking":
    solutions = problem.getSolutionIter()
elif method == "Constraint Propagation":
    solutions = problem.getSolutionIter(constraintPropagation=True)

if solutions is not None:
    print(solutions)
else:
    print("No solution found")
