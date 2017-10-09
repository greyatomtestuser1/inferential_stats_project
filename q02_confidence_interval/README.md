# Find the confidence interval for the population mean given a sample distribution

In the class we calculated the confidence interval for `SalePrice`, lets try and make a similar one for `GrLivArea`, but this time we won't be using the population standard deviation (as it is not available in most cases).

*Note*: when not using the population standard deviation, find confidence interval as:

>$Estimate \pm (z-value) * (Standard Error)$

>$Standard Error = \sigma/\sqrt n$

where $\sigma$ is the sample standard deviation

## Write a function `confidence_interval()` that
* Calculates the Confidence interval for `GrLivArea`

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| sample | DataFrame | compulsory |  | sample data |


### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| lower limit of confidence interval | float | lower(1st) limit of confidence interval returned as a float |
| upper limit of confidence interval | float | upper(2nd) limit of confidence interval returned as a float |
