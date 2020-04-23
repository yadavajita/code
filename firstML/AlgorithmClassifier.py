from sklearn import tree
from sklearn.linear_model import Perceptron
from sklearn import svm 
from sklearn import neighbors
from sklearn.metrics import accuracy_score
import numpy as np

X_train = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40]]
Y_train = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female']

X_test = [[159, 55, 37], [171, 75, 42], [181, 85, 43]]
Y_test = ['female','male','male']

#print(result.index('male'))
#Decision tree classifier
clf = tree.DecisionTreeClassifier()
clf.fit(X_train,Y_train)
print (clf.predict([[190,70,43]]))

#Perceptron
p = Perceptron()
p.fit(X_train,Y_train)
print(p.predict([[190,70,43]]))

#SVM
s = svm.SVC()
s.fit(X_train,Y_train)
print(s.predict([[190,70,43]]))

#KNN
knn = neighbors.KNeighborsClassifier(5)
knn.fit(X_train,Y_train)
print(knn.predict([[190,70,43]]))


#Determine which algorithm is best
acc_clf = accuracy_score(Y_test,clf.predict(X_test))
acc_p = accuracy_score(Y_test,p.predict(X_test))
acc_s = accuracy_score(Y_test,s.predict(X_test))
acc_knn = accuracy_score(Y_test,knn.predict(X_test))

index = np.argmax([acc_clf,acc_p,acc_s,acc_knn])
classifiers = {0:'DecisionTreeClassifier',1:'Perceptron',2:'SVM',3:'KNN'}
print('Best accuracy algorithm is ',classifiers[index])