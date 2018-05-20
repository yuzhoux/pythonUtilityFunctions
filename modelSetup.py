# these functions cover common tasks in modeling: import, encoding, train-test split and etc. 

#1
"""
this step reads all CSV files from an input data folder
"""
import pandas as pd
import glob, os
os.chdir("./inputdata")
allFiles = glob.glob("*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
	## filter out anything you do not need
    cols = [c for c in df.columns if c.lower()[:3] not in ['col1','col2']]
    df=df[cols].dropna(axis=0,how='any')
    list_.append(df)

frame = pd.concat(list_)


#2
"""
this step applies label encoding and one hot encoding to categorical variables
"""
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
import pickle

categorical_columns=['cat1','cat2']
categorical_values = np.array(frame[categorical_columns])

enc_label = LabelEncoder()
indexed = enc_label.fit_transform(categorical_values[:,0])
filename = 'enc_label_type.sav'
#save this encoder for production use
pickle.dump(enc_label, open(filename, 'wb'))

for i in range(1, categorical_values.shape[1]):
    enc_label = LabelEncoder()
    indexed = np.column_stack((indexed, enc_label.fit_transform(categorical_values[:,i])))
    filename = 'enc_label_'+categorical_columns[i]+'.sav'
    pickle.dump(enc_label, open(filename, 'wb'))

categorical_indexed = indexed.astype(float)

enc_onehot = OneHotEncoder()
categorical_onehot = enc_onehot.fit_transform(categorical_indexed)
filename = 'enc_onehot.sav'
pickle.dump(enc_onehot, open(filename, 'wb'))

cols = [categorical_columns[i] + '_' + str(j) for i in range(0,len(categorical_columns)) for j in range(0,enc_onehot.n_values_[i])]
categorical_onehot_df = pd.DataFrame(categorical_onehot.toarray(),columns=cols)

#append the encoded categorical variables back to original data frame
frame=frame.reset_index(drop=True)
frame[cols]=categorical_onehot_df[cols]

#3
"""
this step splits data into training, test and validation (60%, 20%, 20%)
"""
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, stratify=y_train)

#4
"""
this step saves a chosen model and later loads the chosen model to predict
"""
import pickle

model=a_chosen_model
filename = 'prediction_model.sav'
pickle.dump(model, open(filename, 'wb'))

filename = 'prediction_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
pred=loaded_model.predict(X)