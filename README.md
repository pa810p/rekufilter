# Rekufilter - knapsack problem

Shortly, Rekufilter has been written to calculate optimal number of boards that can encapsulate
given number of filters.


Filter mate is sold in as a roll of height equal 160cm. Man pays for multiple of 1 m² area of mate. Dimension of 1 m² of
the mate is then 160cm x 64cm. So the customer can buy n * (160cm x 64cm) sections (later named boards for convenience).
Customer needs filter mate to prepare filters to his recuperation aggregate. Each filter dimensions for his aggregate
is 39cm x 28cm.

The question is: how many square meters (boards) should customer order to prepare optimal number of filters -
(having as little cuttings as possible)? And another question: how to cut the mate?

:bulb: Above, it's a description of an issue that recufilter can solve, this application can be used to calculate
other things like:
- how many leaflets can be printed on paper sheet or roll
- how many pallets can be placed inside a truck

## Requirements
- Python3
- pygame
- rectpack

## Usage

### Configuration
See Configuration Section in recufilter.py and fill required dimensions of board, filter and number of filters
````shell
$ vim recufilter.py
````
````python
# FILTER is a rectangle of filter mat that fit's recuperator.
FILTER_HEIGHT = 39
FILTER_WIDTH = 28

# BOARD is a rectangle of filter mat that is sold by dealer.
BOARD_HEIGHT = 64
BOARD_WIDTH = 160

# APPROX is an approximate number of filters that I will need in next several months.
APPROX_FILTERS = 40
````
### Run
````shell
$ python3 rekufilter.py
````
or if you use virtual environment for the project with installed required libraries:
````shell
$ ./venv/bin/python3 rekufilter.py
````
Depending on Configuration Section results can be like these:
````
####################################
Boards needed: .............. 5
Filters planned: ............ 40
Total area: ................. 51200
Filters area: ............... 45864
Wasted area: ................ 5336
Optimal number of filters: .. 42
####################################
````

````
####################################
Boards needed: .............. 1
Filters planned: ............ 1
Total area: ................. 10240
Filters area: ............... 6552
Wasted area: ................ 3688
Optimal number of filters: .. 6
####################################
````
