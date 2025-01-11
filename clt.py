import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def clt(p, size=10000):
    for n, color in zip([10, 100, 1000, 10000], ["red", "yellow", "green", 'blue']):
        np.random.seed(99)
        samples = np.random.binomial(n=n, p=p, size=size)/n
        df = pd.DataFrame({'samples': samples})
        sns.histplot(data = df, x = 'samples', alpha = 0.5, color = color)
        plt.title(f"Sample distribution when n = {n}")
        plt.show()
        
clt(p = 0.25)
