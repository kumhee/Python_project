from flask import Blueprint, render_template, send_file
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from io import BytesIO
import matplotlib
matplotlib.use("Agg")

score = Blueprint('score', __name__)

@score.route('/page4')
def page4():
    return render_template('page4.html')

# 로지스틱회귀 모델링
def logistic():
    df = pd.read_csv('./data/LogisticRegressionData.csv')
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    reg = LogisticRegression()
    reg.fit(X_train, y_train)
    return reg, X_train, y_train


def sigmoid(reg, x):
    m = reg.coef_
    b = reg.intercept_
    y = m * x + b
    P = 1 / (1 + (np.exp(-y)))
    P = P.reshape(-1)
    return P

# 로지스틱회귀 그래프 출력
@score.route('/logistic/graph')
def logistic_graph():
    X_train = logistic()[1]
    y_train = logistic()[2]
    reg = logistic()[0]
    
    X_range = np.arange(min(X_train), max(X_train), 0.1)
    
    plt.figure(figsize=(8, 5), dpi=80)
    plt.scatter(X_train, y_train, color='blue')
    plt.plot(X_range, np.full(len(X_range), 0.5), color='red')
    plt.plot(X_range, sigmoid(reg, X_range), color='green')
    plt.xlabel('hours')
    plt.ylabel('p')
    
    img = BytesIO()
    plt.savefig(img, format='png', dpi=50)
    img.seek(0)
    return send_file(img, mimetype='image/png')

# 로지스틱회귀 합격률
@score.route('/logistic/<hour>')
def logistic_result(hour):
    hour = float(hour)
    reg = logistic()[0]
    pred = reg.predict_proba([[hour]])
    return str(pred[0, 1])

# K-평균 페이지
@score.route('/page5')
def page5():
    return render_template('page5.html')

#K-평균그래프
@score.route('/kmean/graph/<k>')
def kmean_graph(k):
    K = int(k)
    df = pd.read_csv('./data/KMeansData.csv')
    X = df.iloc[:, :].values
    
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X = sc.fit_transform(X)
    
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=K, random_state=0, n_init=10)
    group = kmeans.fit_predict(X)
    centers = kmeans.cluster_centers_
    
    X_org = sc.inverse_transform(X)
    centers_org = sc.inverse_transform(centers)
    
    plt.figure(figsize=(10, 10), dpi=50)
    for cluster in range(K):
        plt.scatter(X[group == cluster, 0], X[group == cluster, 1], s=100, ec='black')
        plt.scatter(centers[cluster,0], centers[cluster, 1], s=300, ec='black', color='yellow', marker='s')
        plt.text(centers[cluster, 0], centers[cluster,1], cluster, va='center', ha='center')
    plt.xlabel('hours')
    plt.ylabel('score')
    
    img = BytesIO()
    plt.savefig(img, format='png', dpi=50)
    img.seek(0)
    return send_file(img, mimetype='image/png')