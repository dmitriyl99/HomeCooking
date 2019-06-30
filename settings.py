import shelve
from config import basedir
import os
from typing import Optional, Tuple

filename = os.path.join(basedir, 'settings')


def get_delivery_cost() -> tuple:
    """
    Get delivery cost
    :return: (First 3 km, and longer)
    """
    settings = shelve.open(filename)
    if 'delivery_cost' not in settings:
        settings['delivery_cost'] = (3000, 1000)
    value = settings['delivery_cost']
    settings.close()
    return value


def set_delivery_cost(prices: tuple):
    """
    Set delivary prices
    :param prices: (First 3 km, and longer)
    :return: void
    """
    settings = shelve.open(filename)
    settings['delivery_cost'] = prices
    settings.close()


def get_cafe_coordinates() -> Optional[Tuple[float, float]]:
    """
    Cafe coordinates
    :return: (latitude, longitude)
    """
    settings = shelve.open(filename)
    if 'cafe_coordinates' not in settings:
        return None
    value = settings['cafe_coordinates']
    settings.close()
    return value


def set_cafe_coordinates(coordinates: tuple):
    """
    Set cafe coordinates
    :param coordinates: (latitude, longitude)
    :return: void
    """
    settings = shelve.open(filename)
    settings['cafe_coordinates'] = coordinates
    settings.close()


def set_limit_delivery_price(price: int):
    """
    Set limit delivery cost
    :param price: price value
    :return: void
    """
    settings = shelve.open(filename)
    settings['limit_delivery_price'] = price
    settings.close()


def get_limit_delivery_price() -> int:
    """
    Get limit delivery cost or set default value - 15000
    :return: limit delivery price
    """
    settings = shelve.open(filename)
    if 'limit_delivery_price' not in settings:
        settings['limit_delivery_price'] = 15000
    value = settings['limit_delivery_price']
    settings.close()
    return value


def get_trello_settings() -> Optional[Tuple[str, str]]:
    """
    Get Trello settings: board name and list name
    :return: (board name, list name)
    """
    settings = shelve.open(filename)
    if 'trello_settings' not in settings:
        return None
    value = settings['trello_settings']
    settings.close()
    return value


def set_trello_settings(settings: Tuple[str: str]):
    """
    Set Trello configurations
    :param settings: Tuple of (board name, list name)
    :return: void
    """
    settings = shelve.open(filename)
    settings['trello_settings'] = settings
    settings.close()
