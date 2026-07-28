import numpy as np
import statistics as stats
data=[10,15,20,25,30,35,40,45,50,55]

#mean
mean=np.mean(data)
print(f"mean: {mean}")

#median
median=np.median(data)
print(f"Median: {median}")

#mode
mode=np.mode(data)
print(f"mode: {mode}")

#standard_deviation
std_dev=np.std(data)
print(f"std deviation: {std_dev}")

#variance
variance=np.variance(data)
print(f"vairiance:{variance}")