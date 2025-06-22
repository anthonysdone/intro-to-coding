# ==========================================
# 6: Scientific Computing with Python
# ==========================================

"""
In this module, you will learn about scientific computing with Python, using specialized libraries to solve
mathematical and scientific problems. You will first learn about NumPy for numerical arrays and mathematical
operations, then Matplotlib for creating scientific plots and visualizations, then Pandas for data analysis
and manipulation, then SciPy for advanced scientific computing including linear algebra and differential equations,
and finally apply everything in an epidemic simulation project. Each topic will have explanations, worked examples,
and a mini-project, along with ten exercises and a comprehensive project at the end of the module.
"""

# --------------------------------------------------
# NumPy Arrays and Mathematical Operations
# --------------------------------------------------

"""
NumPy is Python's fundamental package for scientific computing. It provides a powerful array object and
mathematical functions that operate on entire arrays at once. Unlike Python lists, NumPy arrays are
homogeneous (all elements have the same type) and operations are vectorized, meaning they apply to all
elements simultaneously. You create arrays using np.array(), generate sequences with np.linspace() or
np.arange(), and perform mathematical operations like np.sin(), np.cos(), np.exp(), etc. NumPy arrays
support element-wise operations (+, -, *, /) and mathematical functions work on entire arrays efficiently.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd # type: ignore

# Worked Example 1
x = np.linspace(0, 2*np.pi, 100)  # creates 100 points from 0 to 2π
y = np.sin(x)  # computes sine for all x values at once
print("x array has", len(x), "elements")  # prints the size of the array
print("First 5 x values:", x[:5])  # prints first 5 values using slicing
print("Maximum y value:", np.max(y))  # finds maximum value in y array

# Worked Example 2
a = np.array([1, 2, 3, 4, 5])  # creates array from Python list
b = np.array([2, 4, 6, 8, 10])  # creates another array
c = a + b  # element-wise addition: [3, 6, 9, 12, 15]
d = a * b  # element-wise multiplication: [2, 8, 18, 32, 50]
print("a + b =", c)
print("a * b =", d)
print("Sum of all elements in c:", np.sum(c))  # sums all elements

# Worked Example 3
data = np.random.normal(0, 1, 1000)  # generates 1000 random numbers from normal distribution
mean = np.mean(data)  # computes mean of the data
std = np.std(data)  # computes standard deviation
print("Random data statistics:")
print("Mean:", mean, "Standard deviation:", std)
print("Data shape:", data.shape)  # prints dimensions of array

# Practice Problems:
# 1. Create an array of 50 equally spaced points from -10 to 10.
# 2. Compute the square root of all numbers from 1 to 25.
# 3. Create two arrays and compute their dot product using np.dot().
# 4. Generate 500 random numbers and find the 95th percentile.
# 5. Create a 3x3 matrix and compute its determinant using np.linalg.det().

# Mini-Project: Population Growth Analysis
"""
Create a simple population growth model using NumPy. Model exponential and logistic growth patterns
for a city's population over 50 years. Compare the two models and visualize the results.

Requirements:
- Use exponential growth: P(t) = P₀ * e^(rt) where r is growth rate
- Use logistic growth: P(t) = K / (1 + ((K-P₀)/P₀) * e^(-rt)) where K is carrying capacity
- Create arrays for time (0-50 years), exponential population, and logistic population
- Use realistic parameters: initial population = 10,000, growth rate = 0.03, carrying capacity = 100,000
- Plot both models on the same graph with appropriate labels and legend
- Calculate and print the population difference after 25 and 50 years
"""

# --------------------------------------------------
# Plotting and Visualization with Matplotlib
# --------------------------------------------------

"""
Matplotlib is the primary plotting library for Python, allowing you to create publication-quality figures.
The pyplot interface (imported as plt) provides MATLAB-like plotting commands. You create plots with
plt.plot(), add labels with plt.xlabel() and plt.ylabel(), add titles with plt.title(), and display
with plt.show(). You can customize plots with colors, line styles, markers, and legends. Matplotlib
supports many plot types including line plots, scatter plots, histograms, bar charts, and 3D plots.
Multiple plots can be created using plt.subplot() or plt.figure().
"""

# Worked Example 1
x = np.linspace(-2*np.pi, 2*np.pi, 200)  # creates x values for plotting
y1 = np.sin(x)  # sine function
y2 = np.cos(x)  # cosine function
plt.figure(figsize=(10, 6))  # creates figure with specific size
plt.plot(x, y1, label='sin(x)', color='blue', linewidth=2)  # plots sine with label and styling
plt.plot(x, y2, label='cos(x)', color='red', linestyle='--')  # plots cosine with dashed line
plt.xlabel('x (radians)')  # adds x-axis label
plt.ylabel('y')  # adds y-axis label
plt.title('Trigonometric Functions')  # adds title
plt.legend()  # shows legend
plt.grid(True)  # adds grid
plt.show()  # displays the plot

# Worked Example 2
x = np.random.normal(0, 1, 1000)  # generates random data
y = 2*x + np.random.normal(0, 0.5, 1000)  # creates correlated data with noise
plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.6, s=20)  # creates scatter plot with transparency
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot with Random Data')
plt.show()

# Worked Example 3
data = np.random.exponential(2, 1000)  # generates exponential data
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)  # creates first subplot (1 row, 2 columns, position 1)
plt.hist(data, bins=30, alpha=0.7, color='green')  # creates histogram
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.subplot(1, 2, 2)  # creates second subplot
plt.boxplot(data)  # creates box plot
plt.ylabel('Value')
plt.title('Box Plot')
plt.tight_layout()  # adjusts spacing between subplots
plt.show()

# Practice Problems:
# 1. Plot the function f(x) = x³ - 2x² + x - 1 from x = -2 to 3.
# 2. Create a scatter plot of 100 random (x,y) points and color them by distance from origin.
# 3. Plot multiple exponential functions with different decay constants on the same graph.
# 4. Create a histogram of 1000 random numbers from a uniform distribution.
# 5. Make a pie chart showing the breakdown of your weekly time allocation.

# Mini-Project: Climate Data Visualization
"""
Create a comprehensive climate data visualization dashboard using real-world temperature data.

Requirements:
- Generate synthetic daily temperature data for one year (365 days)
- Include seasonal patterns: base temperature + seasonal variation + random noise
- Create a multi-panel dashboard with:
  1. Time series plot of daily temperatures
  2. Histogram of temperature distribution
  3. Box plot comparing temperatures by season (group data into 4 seasons)
  4. Scatter plot of temperature vs day of year with trend line
- Add proper titles, labels, and color schemes
- Calculate and display statistics: mean, max, min temperatures for each season
- Use subplots to organize all visualizations in a 2x2 grid
"""

# --------------------------------------------------
# Data Analysis with Pandas
# --------------------------------------------------

"""
Pandas is the primary data analysis library for Python, providing data structures and functions for
manipulating structured data. The main data structure is the DataFrame, which is like a spreadsheet
or SQL table with labeled rows and columns. You can read data from files using pd.read_csv(),
pd.read_excel(), etc. DataFrames support filtering with boolean indexing, grouping with groupby(),
and statistical operations like mean(), std(), corr(). You can select columns with df['column'],
filter rows with df[df['column'] > value], and perform operations across groups. Pandas integrates
well with matplotlib for plotting data directly from DataFrames.
"""

# Worked Example 1
# Create sample data
dates = pd.date_range('2023-01-01', periods=100, freq='D')  # creates 100 daily dates
temperature = 20 + 10*np.sin(np.arange(100)/100 * 2*np.pi) + np.random.normal(0, 2, 100)  # seasonal pattern + noise
humidity = 50 + 20*np.cos(np.arange(100)/100 * 2*np.pi) + np.random.normal(0, 5, 100)  # different pattern
df = pd.DataFrame({'date': dates, 'temperature': temperature, 'humidity': humidity})  # creates DataFrame
print("Dataset shape:", df.shape)  # prints dimensions
print("First 5 rows:")
print(df.head())  # prints first 5 rows
print("Statistical summary:")
print(df.describe())  # prints summary statistics

# Worked Example 2
# Data filtering and selection
hot_days = df[df['temperature'] > 25]  # filters rows where temperature > 25
print("Number of hot days:", len(hot_days))
print("Average humidity on hot days:", hot_days['humidity'].mean())
monthly_avg = df.set_index('date').resample('M').mean()  # groups by month and computes averages
print("Monthly averages:")
print(monthly_avg)

# Worked Example 3
# Data visualization with pandas
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
df.plot(x='date', y='temperature', ax=plt.gca(), color='red')  # plots temperature over time
plt.title('Temperature Over Time')
plt.subplot(2, 2, 2)
df.plot(x='date', y='humidity', ax=plt.gca(), color='blue')  # plots humidity over time
plt.title('Humidity Over Time')
plt.subplot(2, 2, 3)
plt.scatter(df['temperature'], df['humidity'], alpha=0.6)  # scatter plot of temp vs humidity
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.title('Temperature vs Humidity')
plt.subplot(2, 2, 4)
df['temperature'].hist(bins=20, alpha=0.7)  # histogram of temperatures
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.title('Temperature Distribution')
plt.tight_layout()
plt.show()

# Practice Problems:
# 1. Create a DataFrame with student names, test scores, and calculate class average.
# 2. Filter data to show only records above a certain threshold.
# 3. Group data by a categorical variable and compute summary statistics.
# 4. Create a correlation matrix and visualize it as a heatmap.
# 5. Read a CSV file and perform basic data cleaning operations.

# Mini-Project: Student Performance Analysis
"""
Analyze student performance data using pandas to identify patterns and insights.

Requirements:
- Create a synthetic dataset with 100 students containing:
  - Student ID, Name, Age, Major, GPA, Study Hours per Week, Attendance %
- Perform comprehensive analysis:
  1. Calculate summary statistics for numerical columns
  2. Find correlations between study hours, attendance, and GPA
  3. Group students by major and compare average GPAs
  4. Identify top 10% and bottom 10% performers
  5. Create categories: "High Performer" (GPA > 3.5), "Average" (2.5-3.5), "Low" (< 2.5)
- Generate visualizations:
  - Bar chart of average GPA by major
  - Scatter plot of study hours vs GPA
  - Histogram of GPA distribution
- Export filtered data (high performers only) to a new CSV file
- Write a summary report with key findings
"""

# --------------------------------------------------
# Advanced Scientific Computing with SciPy
# --------------------------------------------------

"""
SciPy builds on NumPy and provides additional functionality for scientific computing including optimization,
integration, interpolation, signal processing, and solving differential equations. Key modules include
scipy.optimize for finding minima/maxima and solving equations, scipy.integrate for numerical integration,
scipy.interpolate for fitting curves through data points, and scipy.linalg for linear algebra operations.
SciPy functions typically take NumPy arrays as input and return arrays or optimization results. The
library is essential for advanced mathematical computations and scientific simulations.
"""

from scipy import optimize, integrate, interpolate
from scipy.linalg import solve

# Worked Example 1
# Function optimization and root finding
def quadratic(x):
    return x**2 - 4*x + 3  # function with minimum at x=2

x_min = optimize.minimize_scalar(quadratic)  # finds minimum
print("Minimum of quadratic function:")
print("x =", x_min.x, "f(x) =", x_min.fun)

root = optimize.fsolve(quadratic, 0)  # finds root starting from x=0
print("Root of quadratic function:", root[0])

# Worked Example 2
# Numerical integration
def integrand(x):
    return np.exp(-x**2)  # Gaussian function

result, error = integrate.quad(integrand, 0, np.inf)  # integrates from 0 to infinity
print("Integral of exp(-x²) from 0 to ∞:", result)
print("Estimated error:", error)

# Worked Example 3
# Interpolation and curve fitting
x_data = np.array([0, 1, 2, 3, 4, 5])  # data points
y_data = np.array([0, 1, 4, 9, 16, 25])  # y = x²
f_interp = interpolate.interp1d(x_data, y_data, kind='cubic')  # creates interpolation function
x_fine = np.linspace(0, 5, 100)  # fine grid for plotting
y_interp = f_interp(x_fine)  # evaluates interpolation
plt.figure(figsize=(8, 6))
plt.plot(x_data, y_data, 'o', label='Data points', markersize=8)
plt.plot(x_fine, y_interp, '-', label='Cubic interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolation Example')
plt.legend()
plt.grid(True)
plt.show()

# Practice Problems:
# 1. Find the minimum of the function f(x) = x⁴ - 3x³ + 2x² - x + 1.
# 2. Numerically integrate sin(x)/x from 0 to 10.
# 3. Solve the system of equations: 2x + 3y = 7, x - y = 1.
# 4. Fit a polynomial to noisy data and plot the result.
# 5. Use optimization to fit a exponential decay model to data.

# Mini-Project: Radioactive Decay and Growth Models
"""
Model and analyze radioactive decay and bacterial growth using differential equations and optimization.

Requirements:
- Implement radioactive decay model: N(t) = N₀ * e^(-λt)
- Implement bacterial growth model: N(t) = N₀ * e^(kt)
- Generate synthetic "experimental" data with realistic noise
- Use scipy.optimize.curve_fit to estimate parameters from noisy data
- Compare fitted parameters to true values
- Solve the differential equation dN/dt = -λN numerically using scipy.integrate.odeint
- Create visualizations showing:
  1. True models vs fitted models
  2. Residuals (difference between data and fit)
  3. Parameter uncertainty estimates
- Calculate half-life for radioactive decay and doubling time for bacterial growth
- Perform sensitivity analysis: how do results change with different noise levels?
"""

# --------------------------------------------------
# Linear Algebra and Differential Equations
# --------------------------------------------------

"""
Linear algebra and differential equations are fundamental tools in scientific computing. Linear algebra
deals with systems of linear equations, matrix operations, and vector spaces, while differential equations
model how quantities change over time. SciPy provides powerful tools for both: scipy.linalg for linear
algebra operations like solving systems, eigenvalue problems, and matrix decompositions, and scipy.integrate
for solving ordinary differential equations (ODEs) and partial differential equations (PDEs). These tools
are essential for modeling physical systems, engineering problems, and biological processes.
"""

from scipy.linalg import solve, eigvals, svd
from scipy.integrate import odeint, solve_ivp

# Worked Example 1: Solving linear systems and eigenvalue problems
# System of equations: 3x + 2y - z = 1, 2x - 2y + 4z = 0, -x + 0.5y - z = 0
A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])  # coefficient matrix
b = np.array([1, 0, 0])  # right-hand side vector
x = solve(A, b)  # solve Ax = b
print("Solution to linear system:", x)
print("Verification (Ax - b should be ~0):", np.dot(A, x) - b)

# Eigenvalue analysis
eigenvalues = eigvals(A)  # find eigenvalues
print("Eigenvalues of matrix A:", eigenvalues)

# Worked Example 2: Solving ordinary differential equations
# Example: exponential decay dy/dt = -ky, y(0) = y0
def exponential_decay(y, t, k):
    """ODE function: dy/dt = -ky"""
    return -k * y

y0 = 100  # initial condition
k = 0.1   # decay constant
t = np.linspace(0, 50, 100)  # time points
y_solution = odeint(exponential_decay, y0, t, args=(k,))  # solve ODE

plt.figure(figsize=(10, 6))
plt.plot(t, y_solution, 'b-', label='Numerical solution')
plt.plot(t, y0 * np.exp(-k * t), 'r--', label='Analytical solution')
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('Exponential Decay: dy/dt = -ky')
plt.legend()
plt.grid(True)
plt.show()

# Worked Example 3: Coupled differential equations (predator-prey model)
def predator_prey(state, t, alpha, beta, gamma, delta):
    """
    Lotka-Volterra predator-prey model:
    dx/dt = alpha*x - beta*x*y    (prey equation)
    dy/dt = gamma*x*y - delta*y   (predator equation)
    """
    x, y = state
    dxdt = alpha * x - beta * x * y
    dydt = gamma * x * y - delta * y
    return [dxdt, dydt]

# Parameters and initial conditions
alpha, beta, gamma, delta = 1.0, 0.5, 0.5, 1.0  # model parameters
initial_state = [10, 10]  # initial prey and predator populations
t = np.linspace(0, 20, 1000)  # time points

# Solve the system
solution = odeint(predator_prey, initial_state, t, args=(alpha, beta, gamma, delta))
prey, predators = solution.T

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t, prey, 'b-', label='Prey')
plt.plot(t, predators, 'r-', label='Predators')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Predator-Prey Dynamics')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(prey, predators, 'g-')
plt.xlabel('Prey Population')
plt.ylabel('Predator Population')
plt.title('Phase Portrait')
plt.grid(True)
plt.tight_layout()
plt.show()

# Mini-Project: Spring-Mass-Damper System Analysis
"""
Analyze a spring-mass-damper system using linear algebra and differential equations.

The system is governed by: m*d²x/dt² + c*dx/dt + k*x = F(t)
where m=mass, c=damping, k=spring constant, F(t)=external force

Requirements:
1. Convert to first-order system: [dx/dt, dv/dt] = [v, (F(t) - c*v - k*x)/m]
2. Analyze three cases:
   - Underdamped (c² < 4mk): oscillatory with decay
   - Critically damped (c² = 4mk): fastest return to equilibrium
   - Overdamped (c² > 4mk): slow return without oscillation
3. For each case:
   - Solve the differential equation numerically
   - Calculate natural frequency and damping ratio
   - Find eigenvalues of the system matrix
   - Plot displacement vs time and phase portrait (position vs velocity)
4. Apply step force input: F(t) = F₀ for t > 0
5. Compare analytical solutions (where available) with numerical results
6. Create animation showing mass motion for underdamped case
7. Analyze frequency response: how does the system respond to sinusoidal inputs?

System parameters to test:
- Mass: m = 1 kg
- Spring constants: k = 4, 16, 64 N/m (giving different natural frequencies)
- Damping: vary c to achieve under/critical/over-damped responses
- Force: step input of 10 N
"""