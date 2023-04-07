from unittest import TestCase, main
from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart('Shoppy', 100)

    def test_correct_init(self):
        self.assertEqual('Shoppy', self.cart.shop_name)
        self.assertEqual(100, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_shop_name_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.cart = ShoppingCart('shoppy', 100)
        self.assertEqual('Shop must contain only letters and must start with capital letter!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.cart = ShoppingCart('Shoppy1', 100)
        self.assertEqual('Shop must contain only letters and must start with capital letter!', str(ve.exception))

    def test_add_valid(self):
        result = self.cart.add_to_cart('Product1', 5.25)
        self.assertEqual("Product1 product was successfully added to the cart!", result)
        self.assertEqual({'Product1': 5.25}, self.cart.products)
        self.assertEqual(5.25, self.cart.products['Product1'])

    def test_add_invalid_cost_too_much(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart('Product1', 125.00)
        self.assertEqual("Product Product1 cost too much!", str(ve.exception))
        self.assertEqual({}, self.cart.products)

    def test_remove_valid(self):
        self.cart.add_to_cart('Product1', 5.25)
        self.cart.add_to_cart('Product2', 15.25)
        result = self.cart.remove_from_cart('Product1')
        self.assertEqual('Product Product1 was successfully removed from the cart!', result)
        self.assertEqual({'Product2': 15.25}, self.cart.products)

    def test_remove_invalid_no_product_with_this_name(self):
        self.cart.add_to_cart('Product1', 5.25)
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart('Product2')
        self.assertEqual('No product with name Product2 in the cart!', str(ve.exception))
        self.assertEqual({'Product1': 5.25}, self.cart.products)

    def test__add__(self):
        self.cart.add_to_cart('Product1', 5.00)
        other = ShoppingCart('One', 80)
        other.add_to_cart('OtherProduct', 2.50)
        result = self.cart.__add__(other)
        self.assertEqual('ShoppyOne', result.shop_name)
        self.assertEqual(180, result.budget)
        self.assertEqual({'Product1': 5.00, 'OtherProduct': 2.50}, result.products)

    def test_buy_prod_valid(self):
        self.cart.add_to_cart('Product1', 5.25)
        result = self.cart.buy_products()
        self.assertEqual('Products were successfully bought! Total cost: 5.25lv.', result)
        self.assertEqual({'Product1': 5.25}, self.cart.products)
        self.assertEqual(5.25, self.cart.products['Product1'])

    def test_buy_prod_not_enough_money(self):
        self.cart.add_to_cart('Product1', 90.00)
        self.cart.add_to_cart('Product2', 20.00)
        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()
        self.assertEqual('Not enough money to buy the products! Over budget with 10.00lv!', str(ve.exception))


if __name__ == '__main__':
    main()
