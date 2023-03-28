from unittest import TestCase, main
from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart('Market', 100)

    def test_correct_init(self):
        self.assertEqual('Market', self.shopping_cart.shop_name)
        self.assertEqual(100, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    # def test_shop_name_valid(self):
    #     self.assertEqual('Market', self.shopping_cart.shop_name)

    def test_shop_name_invalid_should_contains_only_letters_and_start_with_upper(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart('market1', 1000)
        self.assertEqual('Shop must contain only letters and must start with capital letter!', str(ve.exception))

    def test_add_to_cart_valid(self):
        result = self.shopping_cart.add_to_cart('Butter', 5)
        self.assertEqual('Butter product was successfully added to the cart!', result)
        self.assertEqual({'Butter': 5}, self.shopping_cart.products)

    def test_add_to_cart_raises_cost_too_much(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart('Johnnie Walker Blue Label', 400)
        self.assertEqual('Product Johnnie Walker Blue Label cost too much!', str(ve.exception))

    def test_remove_from_cart_valid(self):
        self.shopping_cart.add_to_cart('Meat', 99)
        self.shopping_cart.add_to_cart('Butter', 5)
        result = self.shopping_cart.remove_from_cart('Butter')
        self.assertEqual('Product Butter was successfully removed from the cart!', result)
        self.assertEqual({'Meat': 99}, self.shopping_cart.products)

    def test_remove_from_cart_raises_no_product_with_that_name(self):
        self.shopping_cart.add_to_cart('Butter', 5)
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart('Johnnie Walker Blue Label')
        self.assertEqual('No product with name Johnnie Walker Blue Label in the cart!', str(ve.exception))

    def test_add_method(self):
        first = ShoppingCart('Market', 1000)
        first.add_to_cart('from_first', 1)
        other = ShoppingCart('OtherMarket', 500)
        other.add_to_cart('from_second', 2)
        merged = first.__add__(other)
        self.assertEqual('MarketOtherMarket', merged.shop_name)
        self.assertEqual(1500, merged.budget)
        self.assertEqual({'from_first': 1, 'from_second': 2}, merged.products)

    def test_buy_products_valid(self):
        self.shopping_cart.add_to_cart('Pizzas', 40)
        self.assertEqual('Products were successfully bought! Total cost: 40.00lv.', self.shopping_cart.buy_products())

    def test_buy_products_raises_not_enough_money(self):
        self.shopping_cart.add_to_cart('Johnnie Walker Black Label', 50)
        self.shopping_cart.add_to_cart('Johnnie Walker Green Label', 90)
        self.shopping_cart.add_to_cart('Johnnie Walker Gold Label', 80)
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()
        self.assertEqual('Not enough money to buy the products! Over budget with 120.00lv!', str(ve.exception))


if __name__ == "__main__":
    main()
