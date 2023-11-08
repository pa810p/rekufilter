###
# RekuFilter : display optimal number of boards I have to buy to receive approximately number
# of filters
# Author     : Pawel Prokop
# License    : General Public License v3
###

from pygame.rect import Rect
from rectpack import newPacker
from math import ceil

import pygame
from pygame.locals import QUIT
import sys

INCREASE_FACTOR = 1.2


def calculate_optimal_board_count(board, filters_to_order, filter_dimension, visualize=False):
    """
    Calculates optimal number of boards needed to encapsulate filters to order
    :param board: (width, height)
    :param filters_to_order: number of filters we need to order
    :param filter_dimension: (width, height)
    :param visualize: true if visualization of filter arrangement should be displayed
    :return: boards needed to encapsulate filters and number of encapsulated filters
    """
    boards_needed, extended_board_dimension = calculate_boards_needed(board, filters_to_order, filter_dimension)

    current_filters = 1
    packer = newPacker()
    packer.add_bin(*extended_board_dimension)
    last_pack = []

    while (current_filters * (filter_dimension[0]*filter_dimension[1])
           < (extended_board_dimension[0]*extended_board_dimension[1])):
        packer.add_rect(*(filter_dimension[0], filter_dimension[1]))
        packer.pack()
        if len(last_pack) == len(packer[0]):
            break

        last_pack = packer[0]
        current_filters = len(packer[0])+1

    if visualize:
        visualize_result(filters_to_order, filter_dimension, extended_board_dimension, boards_needed, last_pack)
    return boards_needed, len(last_pack)


def calculate_boards_needed(board, items_to_order, filter_dimension):
    """
    Calculates how many boards is needed to encapsulate given number of filters
    :param board: (width, height)
    :param items_to_order: number of filters we need to order
    :param filter_dimension: (width_height)
    :return: number of boards needed to encapsulate filters and total dimension of these boards
    """
    filter_area = filter_dimension[0] * filter_dimension[1]
    board_area = board[0] * board[1]

    approx_filter_area_needed = filter_area * items_to_order
    approx_boards_needed = ceil(approx_filter_area_needed / board_area)

    filters = 0

    while filters < items_to_order:
        packer = newPacker()
        for _ in range(0, items_to_order):
            packer.add_rect(*(filter_dimension[0], filter_dimension[1]))

        extended_board_dimension = (board[0], (approx_boards_needed * board[1]))
        packer.add_bin(*extended_board_dimension)
        packer.pack()

        filters = len(packer[0])
        approx_boards_needed += 1

    return approx_boards_needed-1, extended_board_dimension


def visualize_result(filters_to_order, filter_dimension, board, boards_needed, packer):
    """
    Visualizes arrangement of filters on board using pygame engine and exit
    :param filters_to_order: number of given filters to order
    :param filter_dimension: (width, height) of a filter
    :param board: (widht, height)
    :param boards_needed: number of the boards
    :param packer: list of filters arranged to the board
    :return: None
    """
    total = board[0]*board[1]
    filters = len(packer)*filter_dimension[0]*filter_dimension[1]

    print("####################################")
    print(f'Boards needed: .............. {boards_needed}')
    print(f'Filters planned: ............ {filters_to_order}')
    print(f'Total area: ................. {total}')
    print(f'Filters area: ............... {filters}')
    print(f'Wasted area: ................ {total - filters}')
    print(f'Optimal number of filters: .. {len(packer)}')
    print("####################################")

    pygame.init()
    pygame.display.set_caption('RekuFilter')
    display_surface = pygame.display.set_mode((board[0], board[1]))
    while True:
        for filter_item in packer.rect_list():
            pygame.draw.rect(display_surface, pygame.Color(0, 0, 0),
                             Rect(filter_item[0], filter_item[1], filter_item[2], filter_item[3]))
            pygame.draw.rect(display_surface, pygame.Color(255, 255, 255),
                             Rect(filter_item[0] + 1, filter_item[1] + 1, filter_item[2] - 2, filter_item[3] - 2))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

                sys.exit()
        pygame.display.update()
