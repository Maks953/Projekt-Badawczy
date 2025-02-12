import math
import statistics

def solve_SE(x_,y_,x,y):
    a=(y_+x_*x/y)/(x**2/y+y)
    b=(1/y)*(a*x-x_)
    theta = math.atan(b/a)
    A=a/math.cos(math.atan(b/a))
    return(a,b,theta,A)

results = [] 
results.append(solve_SE(3702.1064,-82.1018,-650.1,0.1999))
results.append(solve_SE(3727.8845,-38.1147,-649.2999,2))
results.append(solve_SE(3727.848,-72.0587,-650.1,0.1999))
results.append(solve_SE(3661.9993,-133.9343,-649.7,-0.2999))
results.append(solve_SE(3289.9812,535.9886,-650.2999,1))
results.append(solve_SE(3685.006,-30.1156,-649.5,0.3))
results.append(solve_SE(3737.823,-13.9577,-650.1999,0.0000001))



Thetas=[]
As=[]
for (a,b,theta,A) in results:
    Thetas.append(theta)
    As.append(A)

print(statistics.median(Thetas))
print(statistics.median(As))

