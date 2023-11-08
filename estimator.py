###
# RekuFilter : display optimal number of boards I have to buy to receive approximately number
# of filters
# Author     : Pawel Prokop
# License    : General Public License v3
###

import RekuFilter


def estimate(start, end, board_dimension, filter_dimension):
    result = []
    for approx_items_to_order in range(start, end):
        boards_needed, filters = RekuFilter.calculate_optimal_board_count(board_dimension, approx_items_to_order,
                                                                          filter_dimension, False)
        print(boards_needed, filters)

        result.append((boards_needed, filters))
