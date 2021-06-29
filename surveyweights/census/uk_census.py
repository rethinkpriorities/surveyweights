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

             'education': {'No qualifications': 0.23,
                           'Level 1 qualifications': 0.14,
                           'Level 2 qualifications': 0.15,
                           'Apprenticeship': 0.03,
                           'Level 3 qualifications': 0.12,
                           'Level 4 qualifications and above': 0.27,
                           'Other qualifications': 0.06}, # https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/bulletins/keystatisticsandquickstatisticsforlocalauthoritiesintheunitedkingdom/2013-12-04

             'region': {'North East': 0.04,
                        'North West': 0.1098,
                        'Yorkshire And The Humber': 0.0824,
                        'East Midlands': 0.0725,
                        'West Midlands': 0.0889,
                        'East': 0.0935,
                        'London': 0.1342,
                        'South East': 0.1374,
                        'South West': 0.0844,
                        'Wales': 0.0472,
                        'Scotland': 0.0815,
                        'Northern Ireland': 0.0283},

             'gender': {'Female': 0.507,
                        'Male': 0.487,
                        'Other': 0.006}, # Male-Female from https://www.ethnicity-facts-figures.service.gov.uk/uk-population-by-ethnicity/demographics/male-and-female-populations/latest, other from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5227946/

             'income': {'Less than £15,000': 0.12,
					    '£15,000 to £20,000': 0.21,
					    '£20,000 and £30,000': 0.29,
                        '£30,000 to £50,000': 0.24,
                        '£50,000 to £70,000': 0.07,
                        '£70,000 to £100,000': 0.04,
                        'More than £100,000': 0.03},

             'vote_brexit': {'Remain': 0.4811,
                             'Leave': 0.5189}, # https://en.wikipedia.org/wiki/2016_United_Kingdom_European_Union_membership_referendum

             'vote2019': {'Conservative': 0.436,
                          'Labour': 0.321,
                          'SNP': 0.039, 
                          'Lib Dem': 0.116,
                          'Other': 0.088}} # 2019 UK election popular vote as recorded by Wikipedia https://en.wikipedia.org/wiki/2019_United_Kingdom_general_election
