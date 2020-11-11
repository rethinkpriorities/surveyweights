## v0.3

* Fixed a bug where `max_weight` and `min_weight` would not be populated if `verbose=False`

## v0.2

* California census data can be accessed via `census='US_CA'`
* Texas census data can be accessed via `census='US_TX'`
* Custom census cwn be defined via passed dict (`census=custom_dict`)
* Early termination can be disabled by passing `early_terminate=False` to `run_weighting_scheme`
