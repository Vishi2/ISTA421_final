import tkinter as tk
from constraint import *

#insert as default text sections: 
# x:1-2-3,y:4-5-6
# x < y

class App:
    def __init__(self, master):
        self.master = master
        master.title("Constraint Satisfaction Problem Solver")

        # Create input fields for variables and their domains
        self.var_label = tk.Label(master, text="Enter variable names and domains")
        self.var_label.pack()
        self.vars_entry = tk.Entry(master)
        self.vars_entry.pack()

        # Create input fields for constraints
        self.const_label = tk.Label(master, text="Enter constraints")
        self.const_label.pack()
        self.const_entry = tk.Entry(master)
        self.const_entry.pack()

        # Create drop-down menu for search methods
        self.method_label = tk.Label(master, text="Select search method")
        self.method_label.pack()
        self.method_var = tk.StringVar(master)
        self.method_var.set("Backtracking Search")
        self.method_options = ["Backtracking Search", "Forward Checking", "Constraint Propagation"]
        self.method_menu = tk.OptionMenu(master, self.method_var, *self.method_options)
        self.method_menu.pack()

        # Create solve button
        self.solve_button = tk.Button(master, text="Solve", command=self.solve)
        self.solve_button.pack()

        # Create text area to display solutions
        self.result_text = tk.Text(master)
        self.result_text.pack()

    def solve(self):
        vars_input = self.vars_entry.get()
        const_input = self.const_entry.get()
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
        method = self.method_var.get()
        if method == "Backtracking Search":
            solutions = problem.getSolutions()
        elif method == "Forward Checking":
            solutions = problem.getSolutionIter()
        elif method == "Constraint Propagation":
            solutions = problem.getSolutionIter(constraintPropagation=True)


        # Display the solutions in the GUI
        self.result_text.delete(1.0, tk.END)
        for solution in solutions:
            self.result_text.insert(tk.END, str(solution) + "\n")

root = tk.Tk()
app = App(root)
root.mainloop()

