# 🎓 Student Performance Prediction using Machine Learning

## Overview

This project predicts a student's **Writing Score** using **Math Score** and **Reading Score** with the **Linear Regression** algorithm.

The project also includes a **Flask web application** where users can enter scores and receive predictions through a browser interface.

---

## Features

✔ Data preprocessing
✔ Label Encoding
✔ Train-Test Split
✔ Linear Regression Model
✔ Score Prediction
✔ Flask Web Application
✔ Responsive HTML/CSS UI
✔ Model Saving using Pickle

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Flask
* HTML
* CSS
* Pickle

---

## Project Structure

```text
student-performance-machine-learning-project/

│── app.py
│── model.pkl
│── student performance (1).ipynb
│── README.md

├── templates
│     └── index.html

├── static
│     └── style.css

├── dataset
│     └── StudentsPerformance.csv
```

---

## Machine Learning Workflow

### Load Dataset

```python
df = pd.read_csv("StudentsPerformance.csv")
```

### Data Preprocessing

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df["gender"] = le.fit_transform(df["gender"])
```

### Feature Selection

```python
X = df[['math score', 'reading score']]
y = df['writing score']
```

### Split Data

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

### Train Model

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)
```

### Save Model

```python
import pickle

pickle.dump(model, open("model.pkl", "wb"))
```

---

## Run Flask Application

Install packages:

```bash
pip install flask pandas scikit-learn
```

Run project:

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Prediction Example

Input:

```text
Math Score = 80
Reading Score = 90
```

Output:

```text
Predicted Writing Score = 88
```

---

## Future Improvements

* Add multiple ML algorithms
* Deploy application online
* Add charts and analytics
* User login system

---

## Author

Surekha Lenka
