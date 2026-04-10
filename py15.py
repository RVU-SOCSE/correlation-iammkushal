import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('C:/Users/RVUW241/Downloads/laptops.csv.csv')

corr_matrix = df.corr(numeric_only=True)

print("Correlation Matrix:\n", corr_matrix)


plt.figure(figsize=(10, 6))

sns.heatmap(corr_matrix, 
            annot=True,       # show values
            cmap='coolwarm',  # color style
            fmt=".2f")        # 2 decimal points

plt.title("Correlation Heatmap")
plt.show()
