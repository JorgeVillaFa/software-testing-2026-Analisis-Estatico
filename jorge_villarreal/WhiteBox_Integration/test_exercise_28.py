# -*- coding: utf-8 -*-

"""
Pruebas unitarias de caja blanca para el ejercicio 28: Product y ShoppingCart.
"""
import unittest
from unittest.mock import patch

from white_box.class_exercises import Product, ShoppingCart


class TestProduct(unittest.TestCase):
    """
    Pruebas para la clase Product.
    """

    def setUp(self):
        self.product = Product("Laptop", 999.99)

    def test_inicializa_correctamente(self):
        """
        Verifica que el producto se cree con el nombre y precio correctos.
        """
        self.assertEqual(self.product.name, "Laptop")
        self.assertEqual(self.product.price, 999.99)

    @patch("builtins.print")
    def test_view_product_imprime_bien(self, mock_print):
        """
        Verifica que view_product imprima el nombre y precio del producto.
        """
        self.product.view_product()
        mock_print.assert_called_with(
            f"The product {self.product.name} has a price of {self.product.price}"
        )

    def test_view_product_regresa_mensaje(self):
        """
        Verifica que view_product regrese el mensaje correcto como string.
        """
        msg = self.product.view_product()
        self.assertEqual(
            msg,
            f"The product {self.product.name} has a price of {self.product.price}",
        )


class TestShoppingCart(unittest.TestCase):
    """
    Pruebas para la clase ShoppingCart.
    """

    def setUp(self):
        self.cart = ShoppingCart()
        self.product_a = Product("Laptop", 999.99)
        self.product_b = Product("Mouse", 29.99)

    def test_carrito_empieza_vacio(self):
        """
        Verifica que el carrito arranque sin productos.
        """
        self.assertEqual(self.cart.items, [])

    def test_agregar_producto_nuevo(self):
        """
        Verifica que agregar un producto nuevo lo añada al carrito con la cantidad correcta.
        """
        self.cart.add_product(self.product_a, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["product"], self.product_a)
        self.assertEqual(self.cart.items[0]["quantity"], 2)

    def test_agregar_producto_existente_incrementa_cantidad(self):
        """
        Verifica que agregar un producto que ya está en el carrito sume la cantidad en lugar de duplicarlo.
        """
        self.cart.add_product(self.product_a, 1)
        self.cart.add_product(self.product_a, 3)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 4)

    def test_agregar_cantidad_por_defecto(self):
        """
        Verifica que agregar un producto sin especificar cantidad use 1 por defecto.
        """
        self.cart.add_product(self.product_a)
        self.assertEqual(self.cart.items[0]["quantity"], 1)

    def test_agregar_multiples_productos_distintos(self):
        """
        Verifica que se puedan agregar varios productos diferentes al carrito.
        """
        self.cart.add_product(self.product_a, 1)
        self.cart.add_product(self.product_b, 2)
        self.assertEqual(len(self.cart.items), 2)

    def test_quitar_producto_reduce_cantidad(self):
        """
        Verifica que quitar menos unidades de las que hay solo reduzca la cantidad.
        """
        self.cart.add_product(self.product_a, 5)
        self.cart.remove_product(self.product_a, 2)
        self.assertEqual(self.cart.items[0]["quantity"], 3)

    def test_quitar_producto_lo_elimina_cuando_cantidad_es_igual(self):
        """
        Verifica que quitar exactamente las unidades disponibles elimine el producto del carrito.
        """
        self.cart.add_product(self.product_a, 3)
        self.cart.remove_product(self.product_a, 3)
        self.assertEqual(len(self.cart.items), 0)

    def test_quitar_producto_lo_elimina_cuando_cantidad_excede(self):
        """
        Verifica que quitar más unidades de las disponibles también elimine el producto del carrito.
        """
        self.cart.add_product(self.product_a, 2)
        self.cart.remove_product(self.product_a, 10)
        self.assertEqual(len(self.cart.items), 0)

    def test_quitar_producto_que_no_existe_no_rompe_nada(self):
        """
        Verifica que intentar quitar un producto que no está en el carrito no cause errores.
        """
        self.cart.add_product(self.product_a, 2)
        self.cart.remove_product(self.product_b, 1)
        self.assertEqual(len(self.cart.items), 1)

    @patch("builtins.print")
    def test_view_cart_imprime_productos(self, mock_print):
        """
        Verifica que view_cart imprima los productos del carrito correctamente.
        """
        self.cart.add_product(self.product_a, 2)
        self.cart.view_cart()
        mock_print.assert_called_with(
            f"2 x {self.product_a.name} - ${self.product_a.price * 2}"
        )

    @patch("builtins.print")
    def test_checkout_calcula_total_correcto(self, mock_print):
        """
        Verifica que checkout imprima el total correcto al finalizar la compra.
        """
        self.cart.add_product(self.product_a, 1)
        self.cart.add_product(self.product_b, 2)
        self.cart.checkout()
        expected_total = self.product_a.price * 1 + self.product_b.price * 2
        mock_print.assert_any_call(f"Total: ${expected_total}")
        mock_print.assert_any_call("Checkout completed. Thank you for shopping!")

    @patch("builtins.print")
    def test_checkout_carrito_vacio(self, mock_print):
        """
        Verifica que hacer checkout con el carrito vacío imprima total de $0.
        """
        self.cart.checkout()
        mock_print.assert_any_call("Total: $0")
        mock_print.assert_any_call("Checkout completed. Thank you for shopping!")


if __name__ == "__main__":
    unittest.main()
