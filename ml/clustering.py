
def cluster_users(users_df=None):
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans
    import os
    from db.users_dao import load_users
    if users_df is None: #si aucun dataframe n'est passe e parametre
        users_df = load_users()
    users_df = users_df.copy() # evite de modiffier le dataframe original

    # === Convertir les colonnes categorielles en codes numeriques ===
      #=== KMeans ne fonctionne qu'avec les donnes numeriques
    users_df["level_code"] = users_df["level"].astype("category").cat.codes
    users_df["language_code"] = users_df["language"].astype("category").cat.codes
    users_df["format_code"] = users_df["format"].astype("category").cat.codes
    users_df["budget_code"] = users_df["budget"].astype("category").cat.codes

    # selection des features
    features = ["level_code", "language_code", "format_code", "budget_code"]
    X = users_df[features]
    #=== standarisation des donnes ===
    # why : KKMeans utilise les d.euclidiennes ,sans standarisation les variables avec grandes echelles domineraient
    # ex : si budget_code va de 0 a 1000  et level_code va de 0 a 2 le budget ecraserait le niveau
    X_scaled = StandardScaler().fit_transform(X)

    # application de KMeans
    kmeans = KMeans(n_clusters=3, random_state=42) #random_state=42 : Reproductibilité (mêmes clusters à chaque exécution)
    users_df["cluster"] = kmeans.fit_predict(X_scaled)

    return users_df
