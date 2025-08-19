# 🏮 Tent Map Dynamics in Python

This repository contains Python scripts to simulate and analyze the Tent Map, a simple yet powerful discrete-time dynamical system often used in chaos theory. The code includes simulations, visualizations, bifurcation diagrams, and Lyapunov exponent calculations.

## ✨ Features

🧮 Tent Map Definition
The Tent Map is defined as:

𝑥
𝑛
+
1
=
{
𝑟
 
𝑥
𝑛
	
if 
𝑥
𝑛
<
0.5


𝑟
 
(
1
−
𝑥
𝑛
)
	
if 
𝑥
𝑛
≥
0.5
x
n+1
	​

={
rx
n
	​

r(1−x
n
	​

)
	​

if x
n
	​

<0.5
if x
n
	​

≥0.5
	​


where 
𝑟
r is the control parameter.

⏱ Time Evolution / Dynamics
Simulates the evolution of the Tent Map over time for different initial conditions and parameter values 
𝑟
r.

## 🌀 Cobweb Plots
Illustrates the iteration of the Tent Map visually, showing convergence, cycles, or chaos.

## 📊 Bifurcation Diagram
Plots the long-term behavior as a function of the control parameter 
𝑟
r, revealing periodic windows and chaotic regimes.

## 🔥 Lyapunov Exponent Calculation
Quantifies chaos: positive Lyapunov exponents indicate chaotic behavior.

🛠 Requirements

Python 3.x

NumPy

Matplotlib

Install dependencies with:

pip install numpy matplotlib

## 🚀 Usage

Run dynamics simulation
Update initial conditions and 
𝑟
r values in the script:

r_values = [0.4, 1, 1.2, 1.4142, 1.618, 2]
X0_values = [0.5, 0.25, 0.5, 0.5, 0.5, 0.3]


Cobweb plots

cobweb_plot(r=1.618, x0=0.5)


Bifurcation diagram

valor_r = np.linspace(0, 2, 5000)
Xo = 0.5


Lyapunov exponent

plow, phigh = 0.01, 2.0
nIterates = 2500
nSteps = 100

## 🌟 Visual Examples

## 📈 Time series plots: show convergence or chaotic behavior.

## 🌀 Cobweb plots: reveal iterative behavior.

## 📊 Bifurcation diagram: shows period doubling and chaos.

## 🔥 Lyapunov exponent plot: highlights chaotic parameter ranges.
