###
# RekuFilter : display optimal number of boards I have to buy to receive approximately number
# of filters
# Author     : Pawel Prokop
# License    : General Public License v3
###

import unittest
import RekuFilter


class TestsRekuFilter(unittest.TestCase):

    BOARD_HEIGHT = 64
    BOARD_WIDTH = 160
    FILTER_HEIGHT = 39
    FILTER_WIDTH = 28

    def test_RekufilterCalculate_OK(self):
        board_dimension = (self.BOARD_WIDTH, self.BOARD_HEIGHT)
        filter_dimension = (self.FILTER_WIDTH, self.FILTER_HEIGHT)
        approx_items_to_order = 40
        boards_needed, filters = RekuFilter.calculate_optimal_board_count(board_dimension, approx_items_to_order,
                                                                          filter_dimension, False)
        self.assertEqual(5, boards_needed)
        self.assertEqual(42, filters)

    def test_RekufilterCalculate_OK_1_filters_fit(self):
        board_dimension = (self.BOARD_WIDTH, self.BOARD_HEIGHT)
        filter_dimension = (self.FILTER_WIDTH, self.FILTER_HEIGHT)
        approx_items_to_order = 1
        boards_needed, filters = RekuFilter.calculate_optimal_board_count(board_dimension, approx_items_to_order,
                                                                          filter_dimension, False)

        self.assertEqual(1, boards_needed)
        self.assertEqual(6, filters)

    def test_RekufilterCalculate_OK_128_filters_fit(self):
        board_dimension = (self.BOARD_WIDTH, self.BOARD_HEIGHT)
        filter_dimension = (self.FILTER_WIDTH, self.FILTER_HEIGHT)
        approx_items_to_order = 128
        boards_needed, filters = RekuFilter.calculate_optimal_board_count(board_dimension, approx_items_to_order,
                                                                          filter_dimension, False)

        self.assertEqual(15, boards_needed)
        self.assertEqual(134, filters)
