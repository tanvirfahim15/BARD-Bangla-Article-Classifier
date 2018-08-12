import numpy as np
from sklearn.cross_validation import train_test_split
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from sklearn import svm
from sklearn import naive_bayes
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold


df = pd.read_csv('trainset.csv',sep=',', header=None)
arr = np.array(df)
y = arr[:, 0]
X = arr[:, 1:]

F = open('workfile', 'w')
kf = KFold(n_splits=10, shuffle=True, random_state=1337)
for train_index, test_index in kf.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    clf = naive_bayes.GaussianNB()
    clf.fit(X_train, y_train)
    predict_test = clf.predict(X_test)
    error_count = 0
    error_set = {}
    for i in range(y_test.__len__()):
        if predict_test[i] != y_test[i]:
          error_count = error_count+1
        if y_test[i] not in error_set:
            error_set[y_test[i]]=1
        else:
            error_set[y_test[i]] = error_set[y_test[i]]+1

    print('Accuracy:'+str((1-(error_count/y_test.__len__()))*100)+'%')
    print('Error:'+str(error_count/y_test.__len__()*100)+'%')
    print()

    report=classification_report(y_test, predict_test)
    print(report)
    F.write(report)

