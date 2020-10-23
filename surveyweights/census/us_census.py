US_CENSUS = {'age': {'18-24': 0.1304,
                     '25-44': 0.3505,
                     '45-64': 0.3478,
                     '65+': 0.1713}, # Age from 2010 US Census https://www.census.gov/prod/cen2010/briefs/c2010br-03.pdf

             'education': {'Completed graduate school': 0.1204,
                           'Graduated from college': 0.2128,
                           'Some college, no degree': 0.2777,
                           'Graduated from high school': 0.2832,
                           'Less than high school': 0.1060}, # Education from 2019 ACS https://www.census.gov/data/tables/2019/demo/educational-attainment/cps-detailed-tables.html

             'gender': {'Female': 0.507,
                        'Male': 0.487,
                        'Other': 0.006}, # Male-Female from 2010 US Census https://www.census.gov/prod/cen2010/briefs/c2010br-03.pdf, other from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5227946/

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

			 # Regions follow a custom definition, see `US_REGIONS_MAP`
             'region': {'Midwest': 0.2149,
                        'Mountains': 0.0539,
                        'Northeast': 0.1604,
                        'Pacific': 0.1602,
                        'South': 0.2180,
                        'Southwest': 0.0531,
                        'Southeast': 0.1398}, # Regions from 2019 Census estimates https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population

             'vote2016': {'Hillary Clinton': 0.482,
                          'Donald Trump': 0.461,
                          'Other': 0.057}, # 2016 US election popular vote as recorded by Wikipedia https://en.wikipedia.org/wiki/2016_United_States_presidential_election

             'left_right': {'Liberal': 0.35,  # Sienna College / NYT poll <https://int.nyt.com/data/documenttools/nyt-siena-poll-methodology-june-2020/f6f533b4d07f4cbe/full.pdf>
                            'Moderate': 0.26,
                            'Conservative': 0.30},

             'gss_bible': {'Word of God': 0.31,
                           'Inspired word': 0.473,
                           'Book of fables': 0.217}, # From GSS 2018 https://gssdataexplorer.norc.org/variables/364/vshow

             'gss_trust': {'Can trust': 0.331,
                           'Can\'t be too careful': 0.669 }, # From GSS 2018 https://gssdataexplorer.norc.org/variables/441/vshow

             'gss_spanking': {'Agree': 0.677,
                              'Disagree': 0.323}} # From GSS 2018 https://gssdataexplorer.norc.org/trends/Gender%20&%20Marriage?measure=spanking


US_CA_CENSUS = {'age': {'18-24': 0.136,
                        '25-44': 0.434,
                        '45-64': 0.282,
                        '65+': 0.147}, # Age 2018 US Census https://www.infoplease.com/us/census/california/demographic-statistics

             'education': {'Completed graduate school': 0.13,
                           'Graduated from college': 0.218,
                           'Some college, no degree': 0.285,
                           'Graduated from high school': 0.206,
                           'Less than high school': 0.16}, # Education from https://www.statista.com/statistics/306963/educational-attainment-california

             'gender': {'Female': 0.499,
                        'Male': 0.495,
                        'Other': 0.006}, # Male-Female from 2018 US Census, other from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5227946/

             'income': {'Under $15,000': 0.106,
                        'Between $15,000 and $49,999': 0.2955,
                        'Between $50,000 and $74,999': 0.1652,
                        'Between $75,000 and $99,999': 0.1210,
                        'Between $100,000 and $150,000': 0.1523,
                        'Over $150,000': 0.1597}, # Income from https://statisticalatlas.com/state/California/Household-Income

             'race': {'White or Caucasian': 0.3664,
                      'Asian or Asian American': 0.1452,
                      'Black or African American': 0.0551,
                      'Hispanic or Latino': 0.3929,
                      'Other': 0.0404}, # Race from 2018 Census estimates https://en.wikipedia.org/wiki/File:Ethic_California_Organized_Pie.png

             'vote2016': {'Hillary Clinton': 0.6173,
                          'Donald Trump': 0.3162,
                          'Other': 0.0665}} # 2016 US election popular vote as recorded by Wikipedia https://en.wikipedia.org/wiki/2016_United_States_presidential_election_in_California

US_TX_CENSUS = {'age': {'18-24': 0.109,
                        '25-44': 0.389,
                        '45-64': 0.325,
                        '65+': 0.177}, # Age from 2019 US Census https://www.statista.com/statistics/912205/texas-population-share-age-group/
                                       # 72.7% over 18 per https://en.wikipedia.org/wiki/Demographics_of_Texas

             'education': {'Completed graduate school': 0.108,
                           'Graduated from college': 0.2,
                           'Some college, no degree': 0.287,
                           'Graduated from high school': 0.252,
                           'Less than high school': 0.154}, # Education from https://www.statista.com/statistics/306995/educational-attainment-texas/

             'gender': {'Female': 0.499,
                        'Male': 0.495,
                        'Other': 0.006}, # Male-Female from https://www.census.gov/quickfacts/TX, other from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5227946/

             'income': {'Under $15,000': 0.1186,
                        'Between $15,000 and $49,999': 0.3524,
                        'Between $50,000 and $74,999': 0.1652,
                        'Between $75,000 and $99,999': 0.119,
                        'Between $100,000 and $150,000': 0.1342,
                        'Over $150,000': 0.1106}, # Income from https://statisticalatlas.com/state/Texas/Household-Income

             'race': {'White or Caucasian': 0.4140,
                      'Asian or Asian American': 0.0493,
                      'Black or African American': 0.1188,
                      'Hispanic or Latino': 0.3961,
                      'Other': 0.0218}, # Race from 2018 Census estimates https://en.wikipedia.org/wiki/Demographics_of_Texas

             'vote2016': {'Hillary Clinton': 0.4324,
                          'Donald Trump': 0.5223,
                          'Other': 0.0453}} # 2016 US election popular vote as recorded by Wikipedia https://en.wikipedia.org/wiki/2016_United_States_presidential_election_in_Texas


US_REGIONS_MAP = {'Midwest': ['Illinois', 'Indiana', 'Iowa', 'Michigan', 'Minnesota',
                              'Ohio', 'Pennsylvania', 'Wisconsin'],
                  'Mountains': ['Alaska', 'Idaho', 'Kansas', 'Montana', 'Nebraska',
                                'North Dakota', 'South Dakota', 'Utah', 'Wyoming', 'Oklahoma'],
                  'Northeast': ['Connecticut', 'Delaware', 'District of Columbia (DC)',
                                'Maine', 'Maryland', 'Massachusetts', 'New Hampshire',
                                'New Jersey', 'New York', 'Rhode Island', 'Vermont'],
                  'Pacific': ['California', 'Hawaii', 'Oregon', 'Washington', 'Guam',
                              'Puerto Rico', 'Virgin Islands'],
                  'South': ['Missouri', 'Tennessee', 'Alabama', 'Arkansas', 'Kentucky',
                            'Louisiana', 'Mississippi', 'Texas', 'Virginia', 'West Virginia'],
                  'Southwest': ['Arizona', 'Colorado', 'Nevada', 'New Mexico'],
                  'Southeast': ['Florida', 'Georgia', 'North Carolina', 'South Carolina']}

