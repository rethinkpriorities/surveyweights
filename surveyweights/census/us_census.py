US_CENSUS = {'age': {'18-24': 0.1304,
                      '25-44': 0.3505,
                      '45-64': 0.3478,
                      '65+': 0.1713}, # Age from 2010 US Census https://www.census.gov/prod/cen2010/briefs/c2010br-03.pdf

             'education': {'Completed graduate school': 0.1204,
                           'Graduated from college': 0.2128,
                           'Some college, no degree': 0.2777,
                           'Graduated from high school': 0.2832,
                           'Less than high school': 0.1060}, # Education from 2019 ACS https://www.census.gov/data/tables/2019/demo/educational-attainment/cps-detailed-tables.html

             'gender': {'Female': 0.51,
                 'Male': 0.49}, # Gender from 2010 US Census https://www.census.gov/prod/cen2010/briefs/c2010br-03.pdf

             'income': {'Under $15,000': 0.1020,
                        'Between $15,000 and $49,999': 0.2970,
                        'Between $50,000 and $74,999': 0.1720,
                        'Between $75,000 and $99,999': 0.1250,
                        'Between $100,000 and $150,000': 0.1490,
                        'Over $150,000': 0.1550}, # Income from 2019 ACS (p34) https://www.census.gov/content/dam/Census/library/publications/2019/demo/p60-266.pdf

             'race': {'White or Caucasian': 0.6340,
                      'Asian or Asian American': 0.0590,
                      'Black or African American': 0.1340,
                      'Hispanic or Latino': 0.1530,
                      'Other': 0.02}, # Race from 2019 Census estimates https://en.wikipedia.org/wiki/Race_and_ethnicity_in_the_United_States#Racial_categories

             'urban_rural': {'Suburban': 0.5500,
                             'Urban': 0.3100,
                             'Rural': 0.1400}, # Urban-Rural from 2018 Pew https://www.pewsocialtrends.org/2018/05/22/demographic-and-economic-trends-in-urban-suburban-and-rural-communities/

             'region': {'Midwest': 0.2149,
                        'Mountains': 0.0539,
                        'Northeast': 0.1604,
                        'Pacific': 0.1602,
                        'South': 0.2180,
                        'Southwest': 0.0531,
                        'Southeast': 0.1398}, # Regions from 2019 Census estimates https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population

             'vote2016': {'Hillary Clinton': 0.5723,
                          'Donald Trump': 0.3108,
                          'Other': 0.1168} # 2016 US election popular vote as recorded by Wikipedia https://en.wikipedia.org/wiki/2016_United_States_presidential_election

             'left_right': {'Liberal': 0.35,  # Sienna College / NYT poll <https://int.nyt.com/data/documenttools/nyt-siena-poll-methodology-june-2020/f6f533b4d07f4cbe/full.pdf>
                            'Moderate': 0.26,
                            'Conservative': 0.30}}

