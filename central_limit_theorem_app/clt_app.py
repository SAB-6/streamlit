import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("Central Limit Theorem")

binom_dist = np.random.binomial(1, 0.5, 1000)
# st.write(binom_dist)

list_of_means = [np.random.choice(binom_dist, 100, replace=True).mean() for _ in range(10000)]
fig, ax = plt.subplots()
ax = plt.hist(list_of_means, color="brown")
st.pyplot(fig)


