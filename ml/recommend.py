import pandas as pd
import os
from ml.clustering import cluster_users

# ================= PATHS =================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# ================= LOAD PLATFORMS =================
from db.platforms_dao import load_platforms
platforms = load_platforms()


# ================= WEIGHTS =================
WEIGHTS = {
    "language": 3,
    "level": 3,
    "format": 2,
    "budget": 1,
    "quality": 2
}

# ================= CLUSTER BONUS =================
def cluster_bonus(user, platform):
    # Cluster 0 → préfère hands-on
    if user["cluster"] == 0 and platform["format"] == "Hands-on":
        return 1.0

    # Cluster 1 → cherche certification
    if user["cluster"] == 1 and platform["certification"] == 1:
        return 1.0

    # Cluster 2 → sensible à la qualité
    if user["cluster"] == 2 and platform["quality"] >= 4.5:
        return 1.0

    return 0.0

# ================= SCORE FUNCTION =================
def compute_score(user, platform):
    score = 0.0

    # Language
    if user["language"] == platform["language"]:
        score += WEIGHTS["language"]

    # Level
    levels_order = ["Beginner", "Intermediate", "Advanced"]
    user_level_index = levels_order.index(user["level"])
    platform_min_index = levels_order.index(platform["level_min"])
    platform_max_index = levels_order.index(platform["level_max"])

    if platform_min_index <= user_level_index <= platform_max_index:
        score += WEIGHTS["level"]

    # Format
    if user["format"] == platform["format"]:
        score += WEIGHTS["format"]

    # Budget
    if user["budget"] == platform["price"]:
        score += WEIGHTS["budget"]

    # Quality (normalized)
    score += (platform["quality"] / 5) * WEIGHTS["quality"]

    # ML bonus
    score += cluster_bonus(user, platform)

    return round(score, 2)

# ================= RECOMMEND =================
def recommend(user_id, users_df=None, top_k=3):

    if users_df is None:
        users_df = cluster_users()

    user_row = users_df[users_df["user_id"] == user_id]

    if user_row.empty:
        raise ValueError(f"user_id {user_id} not found")

    user = user_row.iloc[0]

    results = []
    for _, platform in platforms.iterrows():
        results.append({
            "platform": platform["name"],
            "score": compute_score(user, platform),
            "platform_url": platform["platform_url"]
        })

    return (
        pd.DataFrame(results)
        .sort_values(by="score", ascending=False)
        .head(top_k)
    )
