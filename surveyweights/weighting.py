import numpy as np
import pandas as pd

from surveyweights.census.us_census import US_CENSUS


def get_census(country='US'):
    if country == 'US':
        return US_CENSUS
    else:
        return None


def run_weighting_iteration(df, country='US', verbose=True):
    errors = []
    all_weights = {}

    if 'weight' not in df.columns:
        df['weight'] = df[df.columns[0]].transform(lambda x: 1)
    
    census = get_census(country)

    for var, data in census.items():
        if var in df.columns:
            if verbose:
                print('## {} ##'.format(var))
                
            weights = pd.Series(data) / (df[var].value_counts(normalize=True) * df.groupby(var)['weight'].mean())
            
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
            print('-- WARNING: did not weigh on {} as it is not present'.format(var))
            
            
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


def run_weighting_scheme(df, iters=10, country='US', verbose=True):
    df['weight'] = df['age'].transform(lambda x: 1)
    output = run_weighting_iteration(df, verbose=False)
    weights = output['weights']
    total_error = output['total_error']
    iterx = 1
    
    if verbose:
        print('ITER {}/{} - initialization - ERROR {}'.format(iterx, iters, total_error))
    
    census = get_census(country)

    for var in census.keys():
        if var in df.columns:
            df['weight'] = df['weight'] * df[var].astype(str).replace(weights[var])
            output = run_weighting_iteration(df, country=country, verbose=False)
            weights = output['weights']
            total_error = output['total_error']
            iterx += 1
            if verbose:
                print('ITER {}/{} - weight {} - ERROR {}'.format(iterx, iters, var, total_error))
        elif verbose:
            print('-- WARNING: did not weigh on {} as it is not present'.format(var))
    
    for i in range(iters - iterx):
        weigh_on = list(output['error_table'].keys())[0]
        df['weight'] = df['weight'] * df[weigh_on].astype(str).replace(weights[weigh_on])
        output = run_weighting_iteration(df, country=country, verbose=False)
        weights = output['weights']
        total_error = output['total_error']
        iterx += 1
        if verbose:
            print('ITER {}/{} - weight {} - ERROR {}'.format(iterx, iters, weigh_on, total_error))
        
    if verbose:
        max_weight = df['weight'].max()
        min_weight = df['weight'].min()
        print('Done - FINAL ERROR {} - MAX WEIGHT {} - MIN WEIGHT {}'.format(total_error, max_weight, min_weight))
    
    return {'final_weights': df['weight'],
            'max_weight': max_weight,
            'min_weight': min_weight,
            'final_df': df,
            'error': total_error}

