##----------------------------------------------------------
## Libraries
##----------------------------------------------------------

import pandas as pd
import os

##----------------------------------------------------------
## Read dataset
##----------------------------------------------------------

data=pd.read_csv('data\Human_Resources.csv')

##----------------------------------------------------------
## Data quality check
##----------------------------------------------------------

#check data type
data.dtypes

#check missing value
data.isnull().sum()

#check central value
data.describe().transpose()

#check duplicated row
data[data.duplicated()].transpose()



