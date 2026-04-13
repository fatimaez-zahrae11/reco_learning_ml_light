# 🎓 Learning Platform Recommender

> An AI-powered system that recommends the best websites to learn a programming language — based on your profile.

---

## 📌 Overview

This project uses **Machine Learning (KMeans clustering)** combined with a **weighted scoring system** to recommend the most suitable learning platforms for each user, based on their programming language, level, budget, format preference and learning goal.

---

## 📸 Screenshot

![App Screenshot](screenshots/app1.png)
![App Screenshot](screenshots/app2.png)
![App Screenshot](screenshots/app3.png)


---

## 🚀 Features

- 🤖 KMeans clustering to group users by learning profile
- 🏆 Weighted scoring system to rank platforms
- 🎨 Clean and modern UI built with Streamlit
- 🗄️ MySQL database with DAO pattern
- 🔒 Secure credentials with `.env` file

---

## 🗂️ Project Structure

```
reco_learning_ml_light/
├── assets/
│   └── abc.svg
├── data/
│   ├── users.csv
│   ├── platforms.csv
│   └── feedback.csv
├── db/
│   ├── connection.py       # MySQL connection
│   ├── users_dao.py        # Load users from DB
│   └── platforms_dao.py    # Load platforms from DB
├── ml/
│   ├── clustering.py       # KMeans clustering
│   ├── recommend.py        # Recommendation engine
│   └── visualize_clusters.py
├── app.py                  # Streamlit app (main entry point)
├── generate_data.py        # Synthetic data generator
├── .env   
|__ .gitignore              # 🔒 secrets (not pushed to GitHub)
└──  README.md
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/fatimaez-zahrae11/reco_learning_ml_light.git
cd reco_learning_ml_light
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure your `.env` file
Create a `.env` file at the root of the project:
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=learning_recommender
```

### 5. Generate sample data
```bash
python generate_data.py
```

### 6. Run the app
```bash
streamlit run app.py
```

---

## 🧠 How the ML works

```
User profile (language, level, format, budget, goal)
        ↓
KMeans Clustering  →  assigns user to a cluster (0, 1 or 2)
        ↓
Weighted Scoring   →  scores each platform against user profile
        ↓
Cluster Bonus      →  extra points based on cluster behavior
        ↓
Top 3 platforms recommended 🏆
```

### Scoring weights

| Criteria   | Weight |
|------------|--------|
| Language   | 3      |
| Level      | 3      |
| Format     | 2      |
| Quality    | 2      |
| Budget     | 1      |

---

## 🛠️ Tech Stack

| Layer      | Technology          |
|------------|---------------------|
| Frontend   | Streamlit           |
| ML         | scikit-learn (KMeans) |
| Database   | MySQL               |
| Language   | Python 3.12         |
| Security   | python-dotenv       |

---

## 📋 Requirements

```
streamlit
pandas
scikit-learn
mysql-connector-python
python-dotenv
matplotlib
```

---

## 👤 Author

Fatima Ez-Zahrae Computer Engineering Student ENSA , Kénitra


## License 

This is a personal project developed independently, aimed at applying and strengthening machine learning skills through hands-on practice.