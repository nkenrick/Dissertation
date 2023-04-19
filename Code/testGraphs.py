import pandas as pd
from matplotlib import pyplot as plt
  
columns = ['epsilon', 'Episodes']
df = pd.read_csv('QLearningResultsEpsilon.csv')
print("Contents in csv file:", df)

epsilon = df['epsilon'].tolist()
episodes = df['Episodes'].tolist()

plt.xlabel("Value of (\u03B5)")
plt.ylabel("Average Number of Episodes")
plt.plot(epsilon, episodes)

plt.savefig("QLearningepsilon.png")
plt.show()


