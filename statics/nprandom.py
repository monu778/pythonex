import numpy as np
import matplotlib.pyplot as plt

random = np.random.random();

print(random)

np.random.seed(21); #to simulate same random numbers again and again

random_numbers = np.empty(100)

random_numbers = np.random.random(size=4)


print(random_numbers)

def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    # Initialize number of successes: n_success
    n_success = 0


    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number = np.random.random() 

        # If less than p, it's a success so add one to n_success
        if random_number <p:
            n_success+=1

    return n_success
def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n=len(data)

    # x-data for the ECDF: x
    x=np.sort(data)

    # y-data for the ECDF: y
    #Returns an array with evenly spaced elements as per the interval
    y = np.arange(1, n+1) / n

    return x, y


np.random.seed(42)
# Initialize the number of defaults: n_defaults
n_defaults = np.empty(1000)

# Compute the number of defaults
for i in range(1000):
    n_defaults[i] = perform_bernoulli_trials(100,0.05)


# Plot the histogram with default number of bins; label your axes
#_ = plt.hist(n_defaults, normed=True)
#_ = plt.xlabel('number of defaults out of 100 loans')
#_ = plt.ylabel('probability')

# Show the plot
#plt.show()



# Take 10,000 samples out of the binomial distribution: n_defaults

n_defaults=np.random.binomial(n=100,p=0.05,size=10000)
print(n_defaults)
# Compute CDF: x, y
x,y=ecdf(n_defaults)

# Plot the CDF with axis labels
plt.plot(x,y,marker='.',linestyle='none')
plt.xlabel("number of defaults out of 100 loans")
plt.ylabel("CDF")


# Show the plot

plt.show()