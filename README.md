## Surveyweights

Apply Census weighting to survey data.

### Example Usage

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


### Debugging

**Help! The percentages don't sum to 100%!**

If you subset the dataset, you subset the weights too and they will no longer work for the subsetted dataset. To fix this, use `nomalize_weights`:

```Python
# Subset df
subset_df = df[df[var] == subset]

# Look at weighted data (will be wrong and will not sum to 100%!)
print(subset_df[var].value_counts(normalize=True) * subset_df.groupby(var)['weight'].mean() * 100)

# Normalize weights
df['weight'] = nomalize_weights(df['weight'])

# Look at weighted data (it is now fixed and still representative!)
print(subset_df[var].value_counts(normalize=True) * subset_df.groupby(var)['weight'].mean() * 100)
```

**Help! The percentages still don't sum to 100% and I used `normalize_weights`!**

Another issue might be missing values. Try removing those.

```Python
df = df.dropna() # Remove NAs
df['weight'] = nomalize_weights(df['weight']) # Normalize weights

# Look at weighted data (it is now fixed and still representative!)
print(subset_df[var].value_counts(normalize=True) * subset_df.groupby(var)['weight'].mean() * 100)
```

Note that you may prefer to drop NAs just for particular columns of interest, or you may prefer to impute NAs with a particular value.


**Help! Re-running changes my results!**

The results should be deterministic, so re-running should not affect results. However, the weights still might be unstable and running the same weights in a different order could affect results. To fix this, try increasing the number of iterations and turning off early termination. Also, keep in mind that fluctuations of ~0.1 percentage point could be very normal - potentially a larger fluctuation for very small sample sizes.


### Installation

`pip3 install surveyweights`

