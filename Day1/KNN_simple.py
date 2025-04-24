import numpy as np
from sklearn.neighbors import KNeighborsClassifier
x=np.array([[1,2],[0,3],[6,8]])
y=np.array([0,0,1])

knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x,y)

new_student=np.array([[7,8]])
print(knn.predict(new_student))