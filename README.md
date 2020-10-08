## Surveyweights

Apply Census weighting to survey data.

#### Example Usage

```Python
from surveyweights import run_weighting_scheme, run_weighting_iteration

# Define what to weigh on
weigh_on = ['age', 'education', 'gender', 'income', 'race', 'urban_rural', 'vote2016']

# Run weighting
output = run_weighting_scheme(survey_data, iters=25, weigh_on=weigh_on)

# Get data back with weight column
survey_data = output['final_df']

# See balance of weights 
run_weighting_iteration(survey_data, weigh_on=weigh_on)

# Look at unweighted outcome data
print(survey_data['outcome'].value_counts(normalize=True) * 100)

# Look at weighted outcome data
print(survey_data['outcome'].value_counts(normalize=True) * survey_data.groupby('outcome')['weight'].mean() * 100)
```

