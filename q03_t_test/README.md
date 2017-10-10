# Hypothesis testing using t-test

In the class we tested if house prices in OldTown are different than the mean price. Lets now check if the Living Area (`GrLivArea`) is significantly different than the mean `GrLivArea` area of the population as well.

* Null Hypothesis: The mean of Living area of houses in OldTown is the same as the population mean.y
* Alternate Hypothesis: The mean of Living area of houses in OldTown is different than the population mean.

Test the above hypothesis at 95% significance level and return True if we do not reject the null hypothesis.

## Write a function `t_statistic()` that
* Returns p-value
* Returns True if we do not reject the null hypothesis and False otherwise

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| df | DataFrame | compulsory |  | IOWA housing dataset |


### Returns:

| Return | dtype | description |
| --- | --- | --- |
| p_value | float | p-value |
| test_result | numpy.bool | result of our t-test(true or false) |
