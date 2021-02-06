# TentMapLCE.py:
#	Estimate the Lyapunov Characteristic Exponent for the Tent Map.
#   Plot it as a function of the map's control parameter.

# Import modules
# SciPy for the arange function
from scipy import arange
from pylab import *

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

# Setup the plot
# It's numbered 1 and is 8 x 6 inches.
figure(1,(8,6))

# Stuff parameter range into a string via the string formating commands.
TitleString = 'Tent map Lyapunov Characteristic Exponent for a in [%g,%g]' % (plow,phigh)
title(TitleString)

# Label axes
xlabel('Control parameter a')
ylabel('$\lambda$')

# Since the boundary between stability and chaos occurs at LCE = 0, we draw
axhline(0.0,0.0,1.0,color = 'k')

# Set the initial condition used at each parameter value
ic = 0.2

# Establish the arrays to hold the LCE estimates at each parameter value
psweep = [ ] # The parameter values
lce    = [ ] # The LCE values

# The iterates we throw away
nTransients = 100

# The iterations over which we estimate the LCE (more is better)
nIterates = 2500

# This sets how dense the parameter sweep will be
nSteps = 100.0

# Sweep the control parameter over the desired range
for p in arange(plow,phigh,(phigh-plow)/nSteps):

	# Set the initial condition to the reference value
	state = ic

	# Throw away the transient iterations
	# for i in range(nTransients):
	# 	state = TentMap(p,state)

	# Now estimate the LCE over nIterates
	# We start an estimate at a new parameter, must clear previous LCE
	l = 0.0
	for i in range(nIterates):
		state = TentMap(p,state)
		l = log(abs(TentMapDeriv(p,state)))

	# Convert to the per-iteration average
	#l = l / float(nIterates)
	lce.append(l)
	psweep.append(p)

# Plot the list of (p,lce) pairs as lines
plot(psweep, lce, 'r-')

# Use this to save figure as a bitmap png file
#savefig('TentMapLCE', dpi=600)

# Display plot in window
show()