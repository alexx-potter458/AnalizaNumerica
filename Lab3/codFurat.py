import math

def f(x): 
    power = -x**2
    return x + (math.e**power)*math.cos(x)

def SecantaF(x0,x1,N):
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break
        
        x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
        print('%d, %.10f and  %.4e' % (step, x2, f(x2)))
        #print("%d\t %.10f\t %.4e" %(N, x1, np.abs(x1 - x0) / np.abs(x0)))
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step > N:
            print('Not Convergent!')
            break
        
        condition = step<11
    print('\n Required root is: %0.8f' % x2)



SecantaF(-1,1,10)

def falsePosition(x0,x1,N):
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break
        
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        print('%d, %.10f ,%.4e' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
             x1 = x2
        else:
             x0 = x2
        step = step + 1
        
        if step > N:
            print('Not Convergent!')
            break
        
        condition = step<11
    print('\n Required root is: %0.8f' % x2)
    
falsePosition(-1,1,10)