import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
import seaborn as sns
import pandas as pd

iris = datasets.load_iris();

print(iris)
df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['species'])
print(df)


versicolor_petal_length = np.array(iris.data[:,1])
setosa_petal_length = np.array(iris.data[:,0])
virginica_petal_length = np.array(iris.data[:,2])

n_data=len(versicolor_petal_length)

print(n_data)
n_bins = np.sqrt(n_data)
n_bins = int(n_bins)

#print (versicolor_petal_length);

sns.set()

# Plot histogram of versicolor petal lengths
#The histogram you just made had ten bins. This is the default of matplotlib. 
#The "square root rule" is a commonly-used rule of thumb for choosing number of bins: 
#choose the number of bins to be the square root of the number of samples'''

#plt.hist(versicolor_petal_length,bins=n_bins)
#sns.swarmplot(x="species", y="petal length (cm)",data=df)
#outliers = q1-1.5IQR
#IQR=q3-q1
sns.boxplot(x='species',y='petal length (cm)',data=df)
# Label the axes

plt.xlabel('species')
plt.ylabel('petal length (cm)')

# Show the plot

plt.show()
#_=plt.xlabel("Petal lenght in (cm)")
#_=plt.ylabel("Count")

# Show histogram



#plt.show()


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


x_set,y_set = ecdf(setosa_petal_length)
x_vers,y_vers = ecdf(versicolor_petal_length)
x_virg,y_virg  = ecdf(virginica_petal_length)
np.mean(versicolor_petal_length)


#plt.plot(x_set,y_set,marker='.',linestyle='none')
#plt.plot(x_vers,y_vers,marker='.',linestyle='none')
#plt.plot(x_virg,y_virg,marker='.',linestyle='none')
# Label the axes
#_ = plt.xlabel('petal length (cm)')
#_= plt.ylabel('ECDF')

#plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')

# Compute percentiles: ptiles_vers
percentiles = np.array([2.5, 25, 50, 75,97.5])

ptiles_vers = np.percentile(versicolor_petal_length,percentiles)
#_ = plt.plot(x_vers, y_vers, '.')
#_ = plt.xlabel('petal length (cm)')
#_ = plt.ylabel('ECDF')

# Overlay percentiles as red diamonds.
#_ = plt.plot(ptiles_vers, percentiles/100, marker='D', color='red',linestyle='none')

# Display the plot
#plt.show()

# Array of differences to mean: differences
differences = versicolor_petal_length-np.mean(versicolor_petal_length)

# Square the differences: diff_sq
diff_sq = differences ** 2;

# Compute the mean square difference: variance_explicit
variance_explicit = np.mean(diff_sq)

# Compute the variance using NumPy: variance_np
variance_np = np.var(versicolor_petal_length)

# Print the results

print(variance_np,variance_explicit)

# Print the square root of the variance

print(np.sqrt(variance))
# Print the standard deviation
print(np.std(versicolor_petal_length))

# Make a scatter plot
plt.plot(versicolor_petal_length,versicolor_petal_width,marker='.',linestyle='none')



# Label the axes
plt.xlabel("petal length(cm)")
plt.ylabel("petal width(cm)")


# Show the result
plt.show()

# Compute the covariance matrix: covariance_matrix
covariance_matrix = np.cov(versicolor_petal_length,versicolor_petal_width)

# Print covariance matrix
print(covariance_matrix)

# Extract covariance of length and width of petals: petal_cov

petal_cov = covariance_matrix[0,1]
# Print the length/width covariance
print (petal_cov)

def pearson_r(x,y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat

    corr_mat = np.corrcoef(x,y)
    # Return entry [0,1]
    return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor: r

r=pearson_r(versicolor_petal_length,versicolor_petal_width)
# Print the result
print(r)



