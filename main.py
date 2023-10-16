# install
import numpy as np
import pandas as pd
import streamlit as st

st.title("Streamlit 基礎")
st.write("Hello Wrold")

# set dataframe
df = pd.DataFrame({
    "1nd line" :[1, 2, 3, 4],
    "2nd line" :[10, 20, 30, 40]
})

# active table
# st.dataframe(df)

# decolate active table
# st.dataframe(df.style.highlight_max(axis=0), width=300, height=180)

# stable table
# st.table(df)

# set dataframe
df_ = pd.DataFrame(
    np.random.rand(10, 3),
    columns = ["a", "b", "c"]
)

# line chart
# st.line_chart(df_)

# area chart
# st.area_chart(df_)

# bar chart
# st.bar_chart(df_)

# plot dataflame
_df = pd.DataFrame(
    # random + sinzhuku
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
    columns = ["lat", "lon"]
)


# st.map(_df)

# pillow
from PIL import Image

# picture
img = Image.open("hakarl.jpg")
# st.image(img,caption="hakarl", use_column_width = True)

# check box
if st.checkbox("Show Image"):
    img = Image.open("hakarl.jpg")
    st.image(img,caption="hakarl")

# select box
option = st.sidebar.selectbox(
    "好きな数字を入力してください。",
    list(range(1, 11))
)

"あなたの好きな数字は", option , "です。"

# text input
text = st.sidebar.text_input("あなたの好きなスポーツは")

"あなたの好きなスポーツは:" , text

#slider
condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)
"コンディション:" , condition


import time
latest_iteration = st.empty()
bar = st.progress(0)

# progress per 0.1 
for i in range(100):
    latest_iteration.text(f"Iteration{i + 1}")
    bar.progress(i + 1)
    time.sleep(0.1)
# expander
expander1 = st.expander("質問1")
expander1.write("質問1の回答")

"Done"