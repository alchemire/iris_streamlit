import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# load dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# target
df["target"] = iris.target

# math >> name
df.loc[df["target"] == 0, "target"] = "setosa"
df.loc[df["target"] == 1, "target"] = "versicolor"
df.loc[df["target"] == 2, "target"] = "verginica"

# model
x = iris.data[:, [0, 2]]
y = iris.target

# Logistic
clf = LogisticRegression()
clf.fit(x, y)

# sidebar
st.sidebar.header("Input feature")

sepalValue = st.sidebar.slider("sepal length(cm)", min_value=0.0, max_value=10.0, step=0.1)
petalValue = st.sidebar.slider("petal length(cm)", min_value=0.0, max_value=10.0, step=0.1)

# main panel
st.title("Iris Classifier")
st.write("## Input Value")

#input data
value_df = pd.DataFrame([], columns=["data", "sepal length(cm)", "petal length(cm)"])
record = pd.DataFrame(["data", sepalValue, petalValue], index=value_df.columns).T
value_df = pd.concat([value_df, record], ignore_index=True)
value_df.set_index("data", inplace=True)

# input is
st.write(value_df)

# prediction dataframe
pred_probs = clf.predict_proba(value_df)
pred_df = pd.DataFrame(pred_probs, columns=["setona", "versicolor", "virginica"], index=["probability"])

st.write("## Prediction")
st.write(pred_df)

# print prediction
name = pred_df.idxmax(axis=1).tolist()
st.write("## Result")
st.write("このアイリスはきっと", str(name[0]), "です。")