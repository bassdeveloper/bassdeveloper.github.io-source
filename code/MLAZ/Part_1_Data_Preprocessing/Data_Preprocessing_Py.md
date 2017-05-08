
 # Data Preprocessing Template
 Data pre-processing is an essential step in Machine Learning.


```python
# Importing the libraries 
import numpy as np # Mathematics (Linear Algebra). Makes Python programming like R.
import matplotlib.pyplot as plt # For plotting and viewing graphs from datasets
import pandas as pd # Importing and managing datasets
```


```python
# Importing the dataset
dataset = pd.read_csv('Data.csv') # Read the dataset and store into the 'dataset' variable
print(dataset) # Lets take a look at the dataset
%store dataset
```

       Country   Age   Salary Purchased
    0   France  44.0  72000.0        No
    1    Spain  27.0  48000.0       Yes
    2  Germany  30.0  54000.0        No
    3    Spain  38.0  61000.0        No
    4  Germany  40.0      NaN       Yes
    5   France  35.0  58000.0       Yes
    6    Spain   NaN  52000.0        No
    7   France  48.0  79000.0       Yes
    8  Germany  50.0  83000.0        No
    9   France  37.0  67000.0       Yes
    Stored 'dataset' (DataFrame)



```python
# Create Matrix of Features
#%store -r dataset
X = dataset.iloc[:, :-1].values # All columns except the last one
print("\nThe X variable (dataset) predictor variables \n")
print(X)
y = dataset.iloc[:, 3].values
print("\nThe Y variable (dataset) \n")
print(y)
```

    
    The X variable (dataset) predictor variables 
    
    [['France' 44.0 72000.0]
     ['Spain' 27.0 48000.0]
     ['Germany' 30.0 54000.0]
     ['Spain' 38.0 61000.0]
     ['Germany' 40.0 nan]
     ['France' 35.0 58000.0]
     ['Spain' nan 52000.0]
     ['France' 48.0 79000.0]
     ['Germany' 50.0 83000.0]
     ['France' 37.0 67000.0]]
    
    The Y variable (dataset) 
    
    ['No' 'Yes' 'No' 'No' 'Yes' 'Yes' 'No' 'Yes' 'No' 'Yes']



```python
from sklearn.preprocessing import Imputer # Imputer class helps in data preprocessing. 
# help(Imputer)# Imputation transformer for completing missing values
# Here, we are replacing 'NaN' (missing values) with mean
imputer=Imputer(missing_values='NaN', strategy='mean',axis=0) # Mean is default value. 
imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])
X
```




    array([['France', 44.0, 72000.0],
           ['Spain', 27.0, 48000.0],
           ['Germany', 30.0, 54000.0],
           ['Spain', 38.0, 61000.0],
           ['Germany', 40.0, 63777.77777777778],
           ['France', 35.0, 58000.0],
           ['Spain', 38.77777777777778, 52000.0],
           ['France', 48.0, 79000.0],
           ['Germany', 50.0, 83000.0],
           ['France', 37.0, 67000.0]], dtype=object)




```python

```


```python

```
