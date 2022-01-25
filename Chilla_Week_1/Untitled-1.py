import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks",color_codes=True)

kashti=sns.load_dataset("titanic")
# print(kashti)
# Basic plot
p = sns.countplot(x="sex",data=kashti,hue="class") # Coount plot for two variable we use "hue")
p.set_title("Titanic_Count ") # We are telling python that when plot is made then give it a title
plt.show()
