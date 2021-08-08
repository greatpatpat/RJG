#HW05

from scipy.optimize import linprog

#equation
#(0.5*X1) + (0.2*X2) <= 10
#(1*X1) + (1*X2) <= 30
# X1, X2 >= 0 

#linprog() solves only minimization (not maximization) problems 
#and doesn’t allow inequality constraints with ≥. 

#obj holds the coefficients from the objective function.
obj = [-2, -3]

#lhs_ineq holds the left-side coefficients from the inequality constraints.
lhs_ineq = [[0.5, 0.2],  # Material A
            [1, 1]]  # Material B

#rhs_ineq holds the right-side coefficients from the inequality constraints.
rhs_ineq = [10,  # Material A
            30]    # Material B

#The next step is to define the bounds for each variable in the same order as the coefficients. In this case, they’re both between zero and positive infinity:
bnd = [(0, float("inf")),  # Bounds of x1
       (0, float("inf"))]  # Bounds of x2

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd,
              method="revised simplex")
print(opt)

#plug the valuse back into one of the equations to check the answer.
print(opt.x)
X1 = opt.x[0]
X2 = opt.x[1]

#equation
MaxZ = 2 * X1 + 3 * X2
print('Maximum profit is',MaxZ)

