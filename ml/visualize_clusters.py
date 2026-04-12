import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Charger les utilisateurs
users = pd.read_csv(r"C:\Users\Lenovo\reco_learning_ml_light\data\users.csv")

# Colonnes utilisées pour le clustering
features = users[[
    "niveau",
    "langage",
    "objectif",
    "format",
    "temps",
    "budget"
]]

# Normalisation
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
users["cluster"] = kmeans.fit_predict(X_scaled)

# Réduction de dimension (2D)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Visualisation
plt.figure()
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=users["cluster"])
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.title("Visualisation des clusters d'utilisateurs")
plt.show()
