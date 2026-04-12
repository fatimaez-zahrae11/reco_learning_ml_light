import pandas as pd
import random
import os

random.seed(42)

# --- Créer dossier data si nécessaire ---
if not os.path.exists("data"):
    os.makedirs("data")

# --- Génération des utilisateurs ---
users = []
languages = ["Python", "Java", "C++", "JavaScript"]
formats = ["Text", "Video", "Hands-on"]
goals = ["Discovery", "Professional skills", "Certification"]

for i in range(1, 31):
    user = {
        "user_id": i,
        "level": random.choice(["Beginner", "Intermediate", "Advanced"]),
        "language": random.choice(languages),
        "goal": random.choice(goals),
        "format": random.choice(formats),
        "time": random.randint(3, 15),
        "budget": random.choice(["Free", "Paid"])
    }
    users.append(user)

df_users = pd.DataFrame(users)
df_users.to_csv("data/users.csv", index=False)
print("users.csv has been successfully generated!")

# --- Génération des plateformes ---
platforms = [
    {"platform_id": 1, "name": "freeCodeCamp", "language": "Python", "level_min": "Beginner", "level_max": "Advanced",
     "format": "Hands-on", "price": "Free", "certification": 1, "quality": 4.8, "platform_url": "https://www.freecodecamp.org"},

    {"platform_id": 2, "name": "OpenClassrooms", "language": "Python", "level_min": "Beginner", "level_max": "Advanced",
     "format": "Video", "price": "Paid", "certification": 1, "quality": 4.5, "platform_url": "https://openclassrooms.com/fr/"},

    {"platform_id": 3, "name": "Coursera", "language": "Java", "level_min": "Intermediate", "level_max": "Advanced",
     "format": "Video", "price": "Paid", "certification": 1, "quality": 4.6, "platform_url": "https://www.coursera.org/"},

    {"platform_id": 4, "name": "W3Schools", "language": "JavaScript", "level_min": "Beginner", "level_max": "Intermediate",
     "format": "Text", "price": "Free", "certification": 0, "quality": 4.2, "platform_url": "https://www.w3schools.com/"},

    {"platform_id": 5, "name": "CS50 Harvard", "language": "C++", "level_min": "Beginner", "level_max": "Advanced",
     "format": "Video", "price": "Free", "certification": 1, "quality": 4.9, "platform_url": "https://cs50.harvard.edu/x/"},
]

df_platforms = pd.DataFrame(platforms)
df_platforms.to_csv("data/platforms.csv", index=False)
print("platforms.csv has been successfully generated!")
