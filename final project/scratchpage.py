import tkinter as tk
from constraint import *


# Get input from the user

vars_input = "x:1-2-3, y:3-4-5"
const_input = "x < y"
variables = []
# Parse input and create problem object
problem = Problem()
vars_list = vars_input.split(",")
for var in vars_list:
    name, domain = var.strip().split(":")
    #print(name)
    #print(type(name))
    domain_list = domain.split("-")
    domain_tuple = tuple(map(int, domain_list))
    #print(domain_tuple)
    problem.addVariable(str(name), list(domain_tuple))

    globals()[name] = list(domain_tuple)
    variables.append(name)


const_list = const_input.split(",")
prefix = "lambda "
constraint = ""
for const in const_list:
    constraint = const.strip()
    iter = 0
    for var in variables:
        if iter == 0: 
            constraint = var + ":" + constraint 
            print(constraint)
        else:
            constraint = var + ", " + constraint
            print(constraint)
        iter += 1
    
    constraint = prefix + constraint
    print(constraint)
    temp = FunctionConstraint(eval(constraint))
    problem.addConstraint(FunctionConstraint(eval(constraint)))

# Solve the problem using the selected search method
method = "Backtracking Search"
if method == "Backtracking Search":
    solutions = problem.getSolutions()
elif method == "Forward Checking":
    solutions = problem.getSolutionIter()
elif method == "Constraint Propagation":
    solutions = problem.getSolutionIter(constraintPropagation=True)

print(solutions)
