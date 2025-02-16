# Write a program covers data manipulation techniques such as 
# handling missing data and computing summary statistics.

import pandas as pd

population_dict = {
	'California': 38332521,
	'Texas': 26448193,
	'New York': 19651127,
	'Illinois': 12882135
}
population = pd.Series(population_dict)

area_dict = {
	'California': 423967,
	'New York': 141297,
	'Florida': 170312,
	'Illinois': 149995
}
area = pd.Series(area_dict)

states = pd.DataFrame({'population': population,'area': area})
print(states)
print("--------------")
# removing null values
#states = states.dropna()
#print(states)

# adjusting null values
states = pd.DataFrame({'population': population,'area': area})
states = states.fillna({
	'population': states['population'].mean(),
	'area': states['area'].median()
	})
print(states)

print(states.describe())
