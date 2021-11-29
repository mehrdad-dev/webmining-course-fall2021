# -*- coding: utf-8 -*-
"""Mabani-web-graph-knn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aDpktq5fWsFdq7Bj6Wl0Ws61hgDnfgQT

# **Web Mining Course Presentation - Fall 2021**
Mehrdad Mohammadian

GitHub repo: https://github.com/mehrdad-dev/webmining-course-fall2021


tips❗

download this jupyter notebook and upload in the google colab
or copy link of this notebook on github, then paste on the `open notebook > github section`.

# **Maximal Clique - Clustring**

NetworkX:  https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.clique.find_cliques.html#networkx.algorithms.clique.find_cliques
"""

from networkx.algorithms import clique
import networkx as nx

G = nx.Graph()
edges_fig_4 = [('p1', 'p2'), ('p1', 'p3'), ('p3', 'p2')]
G.add_edges_from(edges_fig_4)

cliques = clique.find_cliques(G)
for index, clq in enumerate(cliques):
    print( f'Maximal Clique {index+1} ', clq)

"""# **KNN - Classification**"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

"""## **Dataset**"""

wine = datasets.load_wine()
targets = wine.target
data = wine.data

wine.feature_names

wine.target_names

targets

import pandas as pd
df = pd.DataFrame(data)
df.head(10)

"""## **Model Training**"""

X_train, X_test, y_train, y_test = train_test_split(data, targets , test_size=0.3, shuffle=True, random_state=42)

knn_model = KNeighborsClassifier(n_neighbors=7)
knn_model.fit(X_train, y_train)

"""## **Prediction**"""

prediction = knn_model.predict(X_test)

prediction

y_test

print("acc:",metrics.accuracy_score(y_test, prediction))

"""## **GridSearch Example**"""

from sklearn.model_selection import GridSearchCV

parameters = {'n_neighbors':[1,2,3,4,5,6,7,8,9,10]}
grid = GridSearchCV(knn_model, parameters, cv=10, scoring = 'accuracy', verbose=1)
grid.fit(X_train, y_train)

print(grid.best_score_)
print(grid.best_params_)
print(grid.best_estimator_)