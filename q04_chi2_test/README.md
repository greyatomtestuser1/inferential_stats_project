# Chi-Square test of Independence

Perform a chi-square test to test independence of variables `LandSlope` and `SalePrice` in the IOWA housing dataset. `SalePrice` isn't a categorical variable, but we can divide it into three categories - High, medium, low using pandas qcut [function](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.qcut.html).

## Write a function `chi2_test()` that
* Returns the p-value and the Boolean result of Chi2-test

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| df | DataFrame | compulsory |  | IOWA housing dataset |


### Returns:

| Return | dtype | description |
| --- | --- | --- |
| test_result | tuple | p-value and result of our chi2-test(true or false) |
