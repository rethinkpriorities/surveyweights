import numpy as np
import pandas as pd

from surveyweights.census.us_census import US_CENSUS, US_CA_CENSUS, US_TX_CENSUS
from surveyweights.census.uk_census import UK_CENSUS


def get_census(census='US'):
    if isinstance(census, dict):
        return census
    if census == 'US':
        return US_CENSUS
    if census == 'US_CA':
        return US_CA_CENSUS
    if census == 'US_TX':
        return US_TX_CENSUS
    elif census == 'UK':
        return UK_CENSUS
    else:
        raise ValueError('{} census not found'.format(census))


def normalize_weights(weights):
    drift = weights.sum() / len(weights)
    return weights * (1 / drift)


def run_weighting_iteration(df, census='US', weigh_on=[], verbose=True):
    errors = []
    all_weights = {}

    if 'weight' not in df.columns:
        df.loc[:, 'weight'] = df[df.columns[0]].transform(lambda x: 1)
    
    census_data = get_census(census)

    if weigh_on == []:
        weigh_on = list(census_data.keys())

    for var in weigh_on:
        if var in df.columns:
            if var in census_data.keys():
                if verbose:
                    print('## {} ##'.format(var))
                    
                data = census_data[var]

                if df[var].isna().sum() > 0:
                    raise ValueError('{} contains NAs which are not allowed for weighting. Please impute or replace with an explicit NA value.'.format(var))

                counts = df[var].value_counts(normalize=True)
                missing_keys = list(set(counts.keys()) - set(data.keys()))
                if missing_keys:
                    data = pd.concat((pd.Series(data) * (1 - counts[missing_keys].sum()),
                                      counts[missing_keys]))
                    data = dict(data)

                prior_weight = df.groupby(var)['weight'].mean()
                weights = normalize_weights(pd.Series(data) / (counts * prior_weight))
                
                if verbose:
                    print(weights)
                    
                all_weights[var] = weights
                error = (df[var].replace(weights).apply(lambda x: np.abs(1 - x)).sum() / df.shape[0])
                errors.append(error)

                if verbose:
                    print('ERROR: {}'.format(error))
                    print('-')
                    print('-')
            elif verbose:
                print('-- WARNING: did not weigh on {} as it is not in census'.format(var))

        elif verbose:
            print('-- WARNING: did not weigh on {} as it is not in survey dataframe'.format(var))
            
            
    total_error = np.array(errors).sum()    
    error_table = sorted([(k,
                           np.array([np.abs(1 - v) for v in vs.values]).max()) for k, vs in all_weights.items()],
                         key=lambda x: x[1],
                         reverse=True)
    error_table = dict(error_table)
    if verbose:
        print(error_table)
        print('TOTAL ERROR: {}'.format(total_error))
        
    return {'errors': errors,
            'error_table': error_table,
            'weights': all_weights,
            'total_error': total_error}


def run_weighting_scheme(df, iters=10, census='US', weigh_on=[], early_terminate=True, verbose=1):
    df.loc[:, 'weight'] = df['age'].transform(lambda x: 1)
    iterx = 1
    weights = None
    last_var = None
    census_data = get_census(census)

    if weigh_on == []:
        weigh_on = list(census_data.keys())

    for var in weigh_on:
        if var in df.columns:
            if var in census_data.keys():
                output = run_weighting_iteration(df,
                                                 census=census,
                                                 weigh_on=weigh_on,
                                                 verbose=(verbose >= 2))

                total_error = output['total_error']

                if not weights and verbose >= 1:
                    print('ITER 1/{} - initialization - ERROR {}'.format(iterx, iters, var, total_error))

                weights = output['weights']
                df.loc[:, 'weight'] = df['weight'] * df[var].astype(str).replace(weights[var])
                df.loc[:, 'weight'] = normalize_weights(df['weight'])

                last_var = var
                iterx += 1
                if verbose >= 1:
                    print('ITER {}/{} - weight {} - ERROR {}'.format(iterx, iters, var, total_error))
            elif verbose >= 1:
                print('-- WARNING: did not weigh on {} as it is not in census'.format(var))
        elif verbose >= 1:
            print('-- WARNING: did not weigh on {} as it is not in survey dataframe'.format(var))
        if iterx > iters:
            break
    
    for i in range(iters - iterx):
        weigh_next = list(output['error_table'].keys())[0]
        if weigh_next == last_var and early_terminate:
            print('-- REACHED LOCAL MINIMUM; EARLY TERMINATION')
            break

        df.loc[:, 'weight'] = df['weight'] * df[weigh_next].astype(str).replace(weights[weigh_next])
        df.loc[:, 'weight'] = normalize_weights(df['weight'])

        output = run_weighting_iteration(df,
                                         census=census,
                                         weigh_on=weigh_on,
                                         verbose=(verbose >= 2))

        weights = output['weights']
        total_error = output['total_error']

        last_var = weigh_next
        iterx += 1

        if verbose >= 1:
            print('ITER {}/{} - weight {} - ERROR {}'.format(iterx,
                                                             iters,
                                                             weigh_next,
                                                             total_error))
        
    max_weight = df['weight'].max()
    min_weight = df['weight'].min()
    if verbose >= 1:
        print('Done - FINAL ERROR {} - MAX WEIGHT {} - MIN WEIGHT {}'.format(total_error,
                                                                             max_weight,
                                                                             min_weight))
    
    df.loc[:, 'weight'] = normalize_weights(df['weight'])

    return {'final_weights': df['weight'],
            'max_weight': max_weight,
            'min_weight': min_weight,
            'final_df': df,
            'error': total_error}

