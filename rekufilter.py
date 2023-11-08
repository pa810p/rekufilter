###
# RekuFilter : display optimal number of boards I have to buy to receive approximately number
# of filters
# Author     : Pawel Prokop
# License    : General Public License v3
###

import RekuFilter

#########################
# Configuration Section #
#########################
# FILTER is a rectangle of filter mat that fit's recuperator.
FILTER_HEIGHT = 39
FILTER_WIDTH = 28

# BOARD is a rectangle of filter mat that is sold by dealer.
BOARD_HEIGHT = 64
BOARD_WIDTH = 160

# APPROX is an approximate number of filters that I will need in next several months.
APPROX_FILTERS = 1
#########################

if __name__ == "__main__":
    board_dimension = (BOARD_WIDTH, BOARD_HEIGHT)
    filter_dimension = (FILTER_WIDTH, FILTER_HEIGHT)

    RekuFilter.calculate_optimal_board_count(board_dimension, APPROX_FILTERS, filter_dimension, True)
