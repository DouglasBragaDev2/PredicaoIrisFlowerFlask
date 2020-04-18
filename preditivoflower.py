from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

def preditivoFlower(sepallength, sepalwidth,petallength, petalwidth ):

    iris_dataset = load_iris()

    X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train, y_train)
    X_new = np.array([[sepallength, sepalwidth,petallength, petalwidth]])
    #X_new = np.array([[6.,  2.2, 5.,  1.5]])

    prediction = knn.predict(X_new)
    flower = str(iris_dataset['target_names'][prediction]).replace("[","").replace("]","").replace("'","")    
    
    if flower == "virginica":
        retrHtml = "virginica.png"
    elif flower == "setosa":
        retrHtml = "setosa.png"
    elif flower == "versicolor":
        retrHtml = "versicolor.png"
            
    return retrHtml
    #return str("Predição de tipo de flor: {}".format(iris_dataset['target_names'][prediction])).replace("[","").replace("]","").replace("'","")
    #print("Predicted target name: {}".format(iris_dataset['target_names'][prediction]))