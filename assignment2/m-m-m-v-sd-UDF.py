def calculate_mean(data):
    return sum(data)/len(data)

def calculate_median(data):
    sorted_data=sorted(data)
    n=len(sorted_data)
    mid=n//2
    if n%2==0:
        median=(sorted_data[mid-1]+sorted_data[mid])/2
    else:
        median=sorted_data[mid]
    return median

def calculate_mode(data):
    frequency={ }
    for num in data:
        frequency[num]=frequency.get(num,0)+1
    mode=max(frequency,key=frequency.get)
    return mode

def calculate_variance(data):
    mean=calculate_mean(data)
    variance=sum((x-mean)**2 for x in data)/(len(data)-1)
    return variance

def calculate_std_deviation(data):
    variance=calculate_variance(data)
    std_deviation=variance**0.5
    return std_deviation

data=[int(x) for x in input("enter a series of number").split()]

mean=calculate_mean(data)
median=calculate_median(data)
mode=calculate_mode(data)
variance=calculate_variance(data)
std_devaition=calculate_std_deviation(data)

print("mean",mean)
print("median",median)
print("mode",mode)
print("variance",variance)
print("sd",std_devaition)