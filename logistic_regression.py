# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import dataset
dataset = pd.read_csv('Dataset\Social_Network_Ads.csv')
dataset.head()
dataset.info()
dataset.columns
dataset.describe()
print(f"{dataset.head()} {dataset.describe()}", end=" ")
# we have no missing values and the data looks like in good structure so will proceed with further steps
missing_data = dataset.isnull()
print(missing_data)
print(missing_data.value_counts())


# check the corelation between variables
# use pivot tables
df_pvot = pd.pivot_table(data=dataset, index=['Purchased'])
df_pvot

#df_pvot.plot(kind='bar')
#sns.boxplot(x="Age", y='EstimatedSalary', data=dataset)


# separate dependent and independent variables .i.e X and Y
X = dataset.iloc[:, :-1].values  # x variables
type(X)
print("check the dimension of array", X.ndim)
print(X[0:4])

Y = dataset.iloc[:, -1].values  # Y variable(Target variable)
Y[0:4]
print("Check the dimension of array", Y.ndim)

# Step 3 is to divide the dataset into training and test dataset
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30, random_state=0)
type(X_train)
# checking the test and train dataset size and dimension
X_train.shape
X_test.shape
Y_train.shape
Y_test.shape
X_train
Y_train

# Feature scaling
# Very important to transform data to normlization
# sklearn.preprocessing is used for preprocessing data one of step is
# scalling the data .i.e (x-mean(x))/ std(X). for normalization
dataset.head()
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  # create instance of Standardparser class
# scale X train and x test data

X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

# check the data now for X
X_train[0:5]
X_test[0:5]

y = dataset['Purchased']
x = dataset['Age']
plt.scatter(x, y)

plt.title("Scatter Plot to check Age and Purchased")
plt.xlabel("AGE")
plt.ylabel("Purchased")

# from scikit-learn import logistic regression model and use methods fit fit the model and use predict for preicting the results for test data or new data.
from sklearn.linear_model import LogisticRegression
model1 = LogisticRegression(random_state=0)
print(model1.fit(X_train,Y_train))

print("Predict values for test data")
print("Predicting new values as per model1", model1.predict(sc.transform([[30,87000]])))

X_test.shape

y_pred = model1.predict(X_test)
print("results for test data\n", y_pred)
type(y_pred)
y_pred.shape
###################################
# Checking something
#####
# checking the dimesnions of y-prediction and shape, it is 120 by 1 D (120 rows 1 column)
# y_predict hold fitted y values(predicted values) for test data
print(y_pred.reshape(len(y_pred),1))
# Same with y-test which holds observed Y values of Y_test
print(Y_test.reshape(len(Y_test),1))

# concatenate both fitted and observed target variables.

#merged = np.concatenate((y_pred.reshape(len(y_pred),1),Y_test.reshape(len(Y_test),1), 1)
# concatinate used to join two arrays of same shape concatenate(a1,a2, 0or1) 0 = first 1 complete array the 2nd array, 1 means side by side.
merged = np.concatenate((y_pred.reshape(len(y_pred),1), Y_test.reshape(len(Y_test),1)),1)
print(merged)
merged.shape

# Confusion Matrix : A table describes performance of classification models for test data set. we use scikit learn matrix library for this purpose

from sklearn.metrics import confusion_matrix
conf_matrix = confusion_matrix(Y_test, y_pred) # gives confusion matrix composed of TP, FN, FP, TN
print(conf_matrix) #


# Calculate the accuracy of the model
# Accuracy is nothing but recall or sensitivity or True-Positive rate = [TP+TN/Total number of observations]
# Accuracy is calculated using scikit learn accuracy library
from sklearn.metrics import accuracy_score
accuracy_model1 =accuracy_score(Y_test, y_pred)
print(accuracy_model1) # wow we have 0.89 accuracy score


# we can also find the F-Score : F-score is nothing but average of recsll and precision F1 = 2 * (precision * recall) / (precision + recall)
from sklearn.metrics import f1_score
fscore= f1_score(Y_test, y_pred, average='macro')
print(fscore)

# Visualizing the result for Training Set
from matplotlib.colors import ListedColormap
X_set, y_set = sc.inverse_transform(X_train), Y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 10, stop = X_set[:, 0].max() + 10, step = 0.25),
                     np.arange(start = X_set[:, 1].min() - 1000, stop = X_set[:, 1].max() + 1000, step = 0.25))
plt.contourf(X1, X2, model1.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()