import logging
import numpy as np
from numpy.lib.function_base import append
import matplotlib.pyplot as plotter
plotter.style.use('seaborn-pastel')
from random import randint
from matplotlib import rc
from random import randint
from scipy import arange
from pylab import *

# # ECUACIÓN # -> TENT MAP

# # Xn+1 = 
# #       rXn         for Xn<1/2
# #       r(1-Xn)     for Xn>=1/2


# # # Identify the parameter regions that produce meaningful dynamics. 
# # # For the logistic equation we found that the paramter r must be between 0 and 4. This may be different for other maps.

# # 0<Xn<1

# # r values:
# # 1 = r*(1/2)
# # 2 = r

# # 1 = r(1-0.5)
# # 1 = r*(1/2) 
# # 2 = r

# # 0 < r < 2

# ## Calculate fixed points. Estimate their stability. Determine the values of the parameter characterizing the different dynamics.

# # In the region X < 1/2
# # one fixed point 
# # X* = r*X* 
# # X* = 0 

# # In the region X > 1/2
# # X* = r(1-X*) 
# # X*/r = 1 - X*
# # 1 = X*(1/r + 1)
# # X* = r/(r+1)

# # ¿Stability?

# # For 0 < r < 1
# # Fixed point -> X* = 0
# # f'(0) = r < 1
# # Attracting fixed point

# # For 1 < r < 2
# # Fixed point -> X* = r/(r+1)
# # f' (r/(r+1)) = -r < 1
# # Fixed point becomes unestable
# # "Chaotic" region begins

# ## Plot the dynamics of the system for different values of the relevant parameter. 
# ## Try to identify regimes with a stable fixed point, period 2, 4 or other, and chaos.

# def dynamics(t_initial, t_final, Xn_vector, t_vector, Xn, r):
#     while t_initial<t_final:
#         if Xn>=0.5:
#             Xn1=r*(1-Xn)
#         else:
#             Xn1=r*Xn
#         Xn_vector.append(Xn1)
#         t_vector.append(t_initial)

#         t_initial=t_initial+0.1
#         Xn=Xn1
#     return t_vector, Xn_vector

# # When r < 0

# t_initial0=0
# t_final0=7
# Xn_vector0=[]
# t_vector0=[]
# Xn0=0.5
# r0=0.4

# dynamics(t_initial0, t_final0, Xn_vector0, t_vector0, Xn0, r0)

# plotter.plot(t_vector0, Xn_vector0)
# plotter.title('Xn+1 when r<0')
# plotter.xlabel('time')
# plotter.ylabel('Xn+1')
# plotter.show();

# # When r = 1

# t_initial1=0
# t_final1=7
# Xn_vector1=[]
# t_vector1=[]
# Xn1=0.25
# r1=1

# dynamics(t_initial1, t_final1, Xn_vector1, t_vector1, Xn1, r1)

# plotter.plot(t_vector1, Xn_vector1)
# plotter.title('Xn+1 when r=1')
# plotter.xlabel('time')
# plotter.ylabel('Xn+1')
# plotter.show();

# # When r = 1.2

# t_initial2=0
# t_final2=7
# Xn_vector2=[]
# t_vector2=[]
# Xn2=0.5
# r2=1.2

# dynamics(t_initial2, t_final2, Xn_vector2, t_vector2, Xn2, r2)

# plotter.plot(t_vector2, Xn_vector2)
# plotter.title('Xn+1 when r = 1.2')
# plotter.xlabel('time')
# plotter.ylabel('Xn+1')
# plotter.show();

# # When r = 1.4142

# t_initial3=0
# t_final3=7
# Xn_vector3=[]
# t_vector3=[]
# Xn3=0.5
# r3=1.4142

# dynamics(t_initial3, t_final3, Xn_vector3, t_vector3, Xn3, r3)

# plotter.plot(t_vector3, Xn_vector3)
# plotter.title('Xn+1 when r = 1.4142')
# plotter.xlabel('time')
# plotter.ylabel('Xn+1')
# plotter.show();

# # When r = 1.618

# t_initial4=0
# t_final4=7
# Xn_vector4=[]
# t_vector4=[]
# Xn4=0.5
# r4=1.618

# dynamics(t_initial4, t_final4, Xn_vector4, t_vector4, Xn4, r4)

# plotter.plot(t_vector4, Xn_vector4)
# plotter.title('Xn+1 when r = 1.618')
# plotter.xlabel('time')
# plotter.ylabel('Xn+1')
# plotter.show();

# # When r = 2

# t_initial4=0
# t_final4=7
# Xn_vector4=[]
# t_vector4=[]
# Xn4=0.5
# r4=2

# dynamics(t_initial4, t_final4, Xn_vector4, t_vector4, Xn4, r4)

# plotter.plot(t_vector4, Xn_vector4)
# plotter.title('Xn+1 when r = 2')
# plotter.xlabel('time')
# plotter.ylabel('Xn+1')
# plotter.show();

## Plot examples of the return map (also cobweb plot or graph for xn+1 versus xn) for different regimes.

# def plot(fx_vector,r, x0, iterations=50):

# # Plot y = x
#     plotter.plot([0, 1.1], [0, 1.1], color="red")

# # Plot f(x) 
#     x = np.linspace(0, 1, 1000)
#     for i in x:
#         if i>=0.5:
#             fx=r*(1-i)
#         else:
#             fx=r*i
#         fx_vector.append(fx)
#     plotter.plot(x, fx_vector, color="black", label="f(x)")

# # Plot f^50(x0)
#     last_x, last_y = x0, 0
#     for _ in range(iterations):
#         if last_x >= 0.5:
#             next_x=r*(1-last_x)
#         else:
#             next_x=r*last_x

# # Plot vertical line 
#         plotter.plot([last_x, last_x], [last_y, next_x], color="blue")

# # Plot horizontal line
#         plotter.plot([last_x, next_x], [next_x, next_x], color="blue")

#         last_x, last_y = next_x, next_x


# # Cobweb Plot r=0.5 and x0=0.5
# fx_vector0=[]
# plot(fx_vector0,0.4,0.5)
# plotter.title("Cobweb Plot: r=0.5")
# plotter.xlabel('Xn')
# plotter.ylabel('Xn+1')
# plotter.show();

# # Cobweb Plot r=1 and x0=0.5
# fx_vector1=[]
# plot(fx_vector1,1,0.5)
# plotter.title("Cobweb Plot: r=1")
# plotter.xlabel('Xn')
# plotter.ylabel('Xn+1')
# plotter.show();

# # Cobweb Plot r=1.2 and x0=0.5
# fx_vector2=[]
# plot(fx_vector2,1.2,0.5)
# plotter.title("Cobweb Plot: r=1.2")
# plotter.xlabel('Xn')
# plotter.ylabel('Xn+1')
# plotter.show();

# # Cobweb Plot r=1.4142 and x0=0.5
# fx_vector3=[]
# plot(fx_vector3,1.4142,0.5)
# plotter.title("Cobweb Plot: r=1.4142")
# plotter.xlabel('Xn')
# plotter.ylabel('Xn+1')
# plotter.show();

# # Cobweb Plot r=1.618 and x0=0.5
# fx_vector4=[]
# plot(fx_vector4,1.618,0.5)
# plotter.title("Cobweb Plot: r=1.618")
# plotter.xlabel('Xn')
# plotter.ylabel('Xn+1')
# plotter.show();

# # Cobweb Plot r=2 and x0=0.5
# fx_vector5=[]
# plot(fx_vector5,2,0.3)
# plotter.title("Cobweb Plot: r=2")
# plotter.xlabel('Xn')
# plotter.ylabel('Xn+1')
# plotter.show();

#Can you solve the equation for period-2 dynamics? Can you try to calculate its stability?

# Xn+2 = F[F(Xn)]
# X*2 = F(2)*(X*2)
# lambda(2)(X*) = [lambda(1)(X*)]^(2)

# Xn+2 = 
#       r(r(1-Xn))=r^(2)(1-Xn)          for Xn<1/2
#       r(1-rXn)                        for Xn>=1/2

#f'(Xn+2)=
#       -r^(2)     for Xn<1/2
#       -r^(2)     for Xn>=1/2

# For 0 < r < 1
# Fixed point -> X* = 0
# f'(0) = -r^(2) < 1

# For 1 < r < 2
# Fixed point -> X* = r/(r+1)
# f' (r/(r+1)) = -r^(2) < 1

# def plot2(fx_vectorA,fx_vectorB,r, x0, iterations=50):

# # Plot y = x
#     plotter.plot([0, 1.1], [0, 1.1], color="red")

# # Plot f(x) 
#     x = np.linspace(0, 1, 1000)
#     for i in x:
#         if i>=0.5:
#             fx1=r*(1-i)
#         else:
#             fx1=r*i
#         fx_vectorA.append(fx1)
#     for i in fx_vectorA:
#         if i>=0.5:
#             fx2=r*(1-i)
#         else:
#             fx2=r*i    
#         fx_vectorB.append(fx2)
#     plotter.plot(x, fx_vectorB, color="black", label="f(x)")

# # Xn+2, r=0.5
# fx_vector6=[]
# fx_vector7=[]
# plot2(fx_vector6,fx_vector7,0.5,0.5)
# plotter.title("Second generation with r=0.5 ")
# plotter.xlabel('Xn')
# plotter.ylabel('Xn+2')
# plotter.show();

# # # Xn+2, r=1
# fx_vector8=[]
# fx_vector9=[]
# plot2(fx_vector8,fx_vector9,1,0.5)
# plotter.title("Second generation with r=1 ")
# plotter.xlabel('Xn')
# plotter.ylabel('Xn+2')
# plotter.show();

# # Xn+2, r=1.2
# fx_vector10=[]
# fx_vector11=[]
# plot2(fx_vector10,fx_vector11,1.2,0.5)
# plotter.title("Second generation with r=1.2 ")
# plotter.xlabel('Xn')
# plotter.ylabel('Xn+2')
# plotter.show();

# # Xn+2, r=1.4142
# fx_vector12=[]
# fx_vector13=[]
# plot2(fx_vector12,fx_vector13,1.4142,0.5)
# plotter.title("Second generation with r=1.4142 ")
# plotter.xlabel('Xn')
# plotter.ylabel('Xn+2')
# plotter.show();

# # Xn+2, r=1.618
# fx_vector14=[]
# fx_vector15=[]
# plot2(fx_vector14,fx_vector15,1.618,0.5)
# plotter.title("Second generation with r=1.618 ")
# plotter.xlabel('Xn')
# plotter.ylabel('Xn+2')
# plotter.show();

# # Xn+2, r=2
# fx_vector16=[]
# fx_vector17=[]
# plot2(fx_vector16,fx_vector17,2,0.5)
# plotter.title("Second generation with r=2 ")
# plotter.xlabel('Xn')
# plotter.ylabel('Xn+2')
# plotter.show();

# # Plot the bifurcation diagram (discard transients and represent values of xn for a number of time-steps at each value of r).

# def logistic_iteration(N, xinicial, r):
#     logistic=0
#     for i in range(N):
#         if xinicial<0.5:
#             logistic=r*xinicial
#         else:
#             logistic=r*(1-xinicial)
#         xinicial = logistic
#     return logistic
    
# valor_r = list(np.linspace(0, 2, 50000))
# valor_f=[]
# eje_r=[]

# N = 2000
# Xo = 0.5

# for elems in valor_r:
#     #print(elems)
#     log = 0
#     log = logistic_iteration(randint(100, N), Xo, elems)
#     valor_f.append(log)
#     eje_r.append(elems)

# plotter.scatter(eje_r, valor_f,c="plum",s=0.25)
# plotter.title("Bifurcation diagram of tent map ")
# plotter.xlabel('r')
# plotter.ylabel('Xn+1')
# plotter.show();

# Calculate the Lyapunov exponent for different values of r (advanced)

# Define the Tent map's function, a in [0,2]
def TentMap(a,x):
	if x < 0.5:
		return a * x
	else:
		return a - a * x

# Define the Tent map's derivative
def TentMapDeriv(a,x):
	if x < 0.5:
		return a
	else:
		return -a

# Setup parameter range, hacemos esto porque a debe estar entre algo mayor que 0 y menor de 2, ya que el logaritmo no funciona con 0
plow  = 0.01
phigh = 2.0

# Stuff parameter range into a string via the string formating commands.
TitleString = 'Tent map: Lyapunov Exponent' # for a in [%g,%g]' % (plow,phigh)
title(TitleString)

# Label axes
xlabel('r, maximum fecundity')
ylabel('$\lambda$')

# Since the boundary between stability and chaos occurs at LCE = 0, we draw
axhline(0.0,0.0,1.0,color = 'red')

# Set the initial condition used at each parameter value
ic = 0.5

# Establish the arrays to hold the LCE estimates at each parameter value
psweep = [ ] # The parameter values
lce    = [ ] # The LCE values

# The iterations over which we estimate the LCE (more is better)
nIterates = 2500

# This sets how dense the parameter sweep will be
nSteps = 100.0

# Sweep the control parameter over the desired range
for p in arange(plow,phigh,(phigh-plow)/nSteps):

	# Set the initial condition to the reference value
	state = ic

	# Now estimate the LCE over nIterates
	# We start an estimate at a new parameter, must clear previous LCE
	l = 0.0
	for i in range(nIterates):
		state = TentMap(p,state)
		l = log(abs(TentMapDeriv(p,state)))

	# Convert to the per-iteration average
	lce.append(l)
	psweep.append(p)

# Plot the list of (p,lce) pairs as lines
plot(psweep, lce, 'k-')

# Display plot in window
show()



