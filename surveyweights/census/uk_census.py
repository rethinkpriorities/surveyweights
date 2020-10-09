UK_CENSUS = {'age': {'18-24': 0.094,
                     '25-29': 0.068,
                     '30-34': 0.066,
                     '35-39': 0.067,
                     '40-44': 0.073,
                     '45-49': 0.073,
                     '50-54': 0.064,
                     '55-59': 0.057,
                     '60-64': 0.060,
                     '65-69': 0.048,
                     '70-74': 0.039,
                     '75+': 0.078}, # https://www.ethnicity-facts-figures.service.gov.uk/uk-population-by-ethnicity/demographics/age-groups/latest

             # TODO:
             # 'education': {'Completed graduate school': 0.1204,
             #               'Graduated from college': 0.2128,
             #               'Some college, no degree': 0.2777,
             #               'Graduated from high school': 0.2832,
             #               'Less than high school': 0.1060}, # Education from 2019 ACS https://www.census.gov/data/tables/2019/demo/educational-attainment/cps-detailed-tables.html

             'gender': {'Female': 0.507,
                        'Male': 0.487,
                        'Other': 0.006}, # Male-Female from https://www.ethnicity-facts-figures.service.gov.uk/uk-population-by-ethnicity/demographics/male-and-female-populations/latest, other from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5227946/

             # TODO:
             # 'income': {'Under $15,000': 0.1020,
             #            'Between $15,000 and $49,999': 0.2970,
             #            'Between $50,000 and $74,999': 0.1720,
             #            'Between $75,000 and $99,999': 0.1250,
             #            'Between $100,000 and $150,000': 0.1490,
             #            'Over $150,000': 0.1550}, # Income from 2019 ACS (p34) https://www.census.gov/content/dam/Census/library/publications/2019/demo/p60-266.pdf

             'vote2019': {'Conservative': 0.436,
                          'Labour': 0.321,
                          'SNP': 0.039, 
                          'Lib Dem': 0.116,
                          'Other': 0.088}} # 2019 UK election popular vote as recorded by Wikipedia https://en.wikipedia.org/wiki/2019_United_Kingdom_general_election
