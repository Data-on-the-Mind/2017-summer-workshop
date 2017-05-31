
NYC Lottery Data Analysis Scripts
=========
by Ross Otto
ross.otto@mcgill.ca

These scripts constitute the main data analysis pipeline for the study reported in the paper:

Otto, A. R., Fleming, S. M., & Glimcher, P. W. (2016). Unexpected but Incidental Positive Outcomes Predict Real-World Gambling. Psychological Science, 27(3), 299–311. https://doi.org/10.1177/0956797615618366

You will need your own Census API key to query the US Census with the 'load_demographics.py' script. For more information, see: http://www.opengeocode.org/tutorials/USCensusAPI.php

Field codes for the American Community Survey (ACS5) queries used by load_demographics.py are located in data/acs5_codes.txt -- see details in Methods.

Zoning data require the NYC PLUTO dataset 11v1
https://www1.nyc.gov/site/planning/data-maps/open-data/pluto-mappluto-archive.page

The remaining raw data (NYC lottery purchasing, satellite-derived solar irradiance estimates) are available here at https://osf.io/fc463/files/


