#matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()  # for plot styling
import numpy as np
import requests

from pymongo import MongoClient
# client = MongoClient()
# client = MongoClient('138.197.131.70', 27017)
#
# db = client.busroutes
# collection = db.users
#
#
# post =  {}
# print(list(db.test.find()))
client = MongoClient("localhost", 27017, maxPoolSize=50)
db = client.busroutes
collection = db['users']
cursor = list(collection.find({}))
print(cursor)

data = np.array([ [i['start']['lat'], i['start']['lng'] ]  for i in cursor ])


plt.figure(figsize=(10,5))
from sklearn.datasets.samples_generator import make_blobs

X = data

plt.scatter(X[:, 0], X[:, 1], s=50);

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=40)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')


centers = kmeans.cluster_centers_
plt.xlim([51.0445, 51.047])
plt.ylim([-114.069, -114.0695])


plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);

print(centers.tolist())


destinations = [[51.0452, 114.0811],
[51.0460, 114.0691],
[51.0454, 114.0550],
[51.0479, 114.0619],
[51.0443, 114.0631],
[51.0450, 114.0611]
]
new_list = []

j = 2
k = 3
for i in centers.tolist():
    new_list.append([i] + destinations[j] + destinations[k])
    j+=1
    k+=1
    if j >= len(centers.tolist()):
        j = 0
    if k >= len(centers.tolist()):
        k = 0
print(new_list)

# POST request
r = requests.post('http://localhost:8080/locationRequest', data = {"centers": centers.tolist()})
print(r.content)
