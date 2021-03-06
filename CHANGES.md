## v0.6

* Adds `vote_brexit` (2016 Brexit vote), `income`, `education`, and `region` to the list of weights for the UK census.

## v0.5

* Adds `vote2020` to the list of weights for the US national census.

## v0.4

* Fixed a bug where NAs in the dataset would make the package crash. Now it raises an error message.

## v0.3

* `get_census` can now be used to view the census data.
* Fixed a bug where `max_weight` and `min_weight` would not be populated if `verbose=False`

## v0.2

* California census data can be accessed via `census='US_CA'`
* Texas census data can be accessed via `census='US_TX'`
* Custom census cwn be defined via passed dict (`census=custom_dict`)
* Early termination can be disabled by passing `early_terminate=False` to `run_weighting_scheme`
