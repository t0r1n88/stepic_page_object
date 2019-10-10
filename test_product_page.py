import pytest
from .pages import ProductPage


def guest_can_add_product_to_basket(browser):
	"""
	Тест для тестирования возможности добавления товара в корзину
	"""
	