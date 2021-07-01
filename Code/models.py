from sklearn import  linear_model
from sklearn import metrics
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB

 
def Bayes(X_train, y_train, X_test):
	reg=linear_model.BayesianRidge()
	reg_=reg.fit(X_train, y_train)
	y_pred = reg.predict(X_test)
	return (X_test,y_pred)

