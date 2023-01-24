def pretty_print_optimizer(optimumResult):
    print("Continuous variables:")
    for i in range(len(optimumResult[0])):
        print(f"u{i}: {optimumResult[0][i]}")
    print("Binary variables:")
    for i in range(len(optimumResult[1])):
        print(f"x{i}: {int(optimumResult[1][i])}")
def displayDetail(step,u,x):
    print('############start step %d ##########' % step)
    print("binary variable x is: ",x)
    print("continous variable u is: ",u)

class constrains:
    def __init__(self,Expr,op,Target):
        self.Expr = Expr
        self.op = op
        self.Target = Target
