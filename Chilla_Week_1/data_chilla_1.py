import pandas as pd
chilla= pd.read_csv("data_chilla.csv")
print(chilla)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks",color_codes = True)
p = sns.countplot(x="Gender",data=chilla,hue="Age")
p.set_title("Chilla_Participants")
plt.show()