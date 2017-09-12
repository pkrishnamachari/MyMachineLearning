import csv  # For importing data from the CSV file

import numpy as np  # Import numpy function

# Define array to hold the congruent and incongruent data read from the file

congruentData = []
incongruentData = []

# open the input file stored as CSV file in the folder

with open('input.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        congruentData.append(row[1])
        incongruentData.append(row[2])
# Remove the empty string from the array

    while '' in congruentData:
        congruentData.remove('')

    while '' in incongruentData:
        incongruentData.remove('')
# Storing the data in array for easy manipulation

congruentData = np.array(congruentData[1:], dtype=np.float)
incongruentData = np.array(incongruentData[1:], dtype=np.float)

# Caculate the statistical parameters for the sample data - mean, variance, "
#                standard deviation, sample size and degrees of freedom

# For congruent data
mean_congruent = np.mean(congruentData)
stdev_congruent = np.std(congruentData)
var_congruent = np.var(congruentData)
ncong = congruentData.size
congdof = ncong - 1

# For incongruent data

mean_incongruent = np.mean(incongruentData)
stdev_incongruent = np.std(incongruentData)
var_incongruent = np.var(incongruentData)
nincong = incongruentData.size
incongdof = nincong - 1

# code for the t test for the statistics


tstats = (mean_congruent - mean_incongruent)/np.sqrt(var_congruent/ncong +
                                                     var_incongruent/nincong)

# calculate the R2 value

dof = incongdof + congdof
R2 = tstats**2/(tstats**2 + dof)

# calculate Cohen's d

d = np.sqrt(var_congruent/ncong + var_incongruent/nincong)
# print all the relevant information as output

print("STATISTICAL PARAMETERS \n")
print ("For congruent data")
print("Mean: ", mean_congruent)
print("Standard Deviation ", stdev_congruent)
print("For Incongruent Data")
print("Mean: ", mean_incongruent)
print("Standard Deviation ", stdev_incongruent)
print("\n")

print("STATISTCAL TEST PARAMETERS \n")
print("t statistics: ", tstats)
print("Coeficient of determination (R2): ", R2)
print("Cohen's d: ", d)

