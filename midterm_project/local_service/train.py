import pandas as pd
import numpy as np

from sklearn import multioutput
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor
import pickle

# Parameters

output_file = 'model.bin'

### Parameters for XGBRegressor
n_estimators=500
max_depth=5
learning_rate=0.2
print('parameters are set')



# Data Preperation

df = pd.read_csv('../data/ENB2012_data.csv')
print('Data Loaded.')

print('Data is being prepared')
# Seperate the features and the target variables
X = df.iloc[:,0:-2]
y = np.log(df[['heating', 'cooling']])


# Devide them to training, validation and test parts (60:20:20): 
X_train_full_df, X_test_df, y_train_full_df, y_test = train_test_split(X, y, test_size = 0.20, random_state = 155)
X_train_df, X_val_df, y_train, y_val = train_test_split(X_train_full_df, y_train_full_df, test_size = 0.25, random_state = 155)

# Vectorize feature matrices in the form of dictionary (with renewed indexes):
dv = DictVectorizer(sparse=False)

# Prepare for training
print('Preparing for training')
X_train_df = X_train_df.reset_index(drop=True)
X_train_dict = X_train_df.to_dict(orient='records')
X_train = dv.fit_transform(X_train_dict)

X_val_df = X_val_df.reset_index(drop=True)
X_val_dict = X_val_df.to_dict(orient='records')
X_val = dv.fit_transform(X_val_dict)

X_test_df = X_test_df.reset_index(drop=True)
X_test_dict = X_test_df.to_dict(orient='records')
X_test = dv.fit_transform(X_test_dict)

# Renew the index of target variables
y_train = y_train.reset_index(drop=True)
y_val = y_val.reset_index(drop=True)
y_test = y_test.reset_index(drop=True)
print('Ready for training')

# Training
xgb = XGBRegressor(n_estimators=n_estimators, max_depth=max_depth, learning_rate=learning_rate)
mxgb = multioutput.MultiOutputRegressor(xgb)
mxgb.fit(X_train, y_train)
print('Model is trained')

# Validation
print('Model is being validated')
y_pred = mxgb.predict(X_val)
r2 = np.mean(r2_score(y_val, y_pred))
rmse= np.sqrt(mean_squared_error(y_val,y_pred))
print('Model is validated')
print(f"r2 score: {r2.round(3)}   RMSE: {rmse.round(3)}")


with open(output_file, 'wb') as f_out:
    pickle.dump((dv, mxgb), f_out)

print(f'Model is saved as: {output_file}')



