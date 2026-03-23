# -*- coding: utf-8 -*-

"""
Pruebas unitarias de caja blanca 1 al 21.
"""
import unittest

from white_box.class_exercises import (
    authenticate_user,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_shipping_cost,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    check_number_status,
    get_weather_advisory,
    grade_quiz,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
    verify_age,
)


# 1
class TestCheckNumberStatus(unittest.TestCase):
    """
    Pruebas de caja blanca para check_number_status.
    """

    def test_positive_number(self):
        """
        Verifica que un número positivo regrese "Positive".
        """
        self.assertEqual(check_number_status(5), "Positive")

    def test_negative_number(self):
        """
        Verifica que un número negativo regrese "Negative".
        """
        self.assertEqual(check_number_status(-3), "Negative")

    def test_zero(self):
        """
        Verifica que el cero regrese "Zero".
        """
        self.assertEqual(check_number_status(0), "Zero")


# 2
class TestValidatePassword(unittest.TestCase):
    """
    Pruebas de caja blanca para validate_password.
    """

    def test_valid_password(self):
        """
        Verifica que una contraseña que cumple todas las reglas regrese True.
        """
        self.assertTrue(validate_password("Valid123!"))

    def test_too_short(self):
        """
        Verifica que una contraseña de menos de 8 caracteres regrese False.
        """
        self.assertFalse(validate_password("Ab1!"))

    def test_no_uppercase(self):
        """
        Verifica que una contraseña sin mayúscula regrese False.
        """
        self.assertFalse(validate_password("invalid123!"))

    def test_no_lowercase(self):
        """
        Verifica que una contraseña sin minúscula regrese False.
        """
        self.assertFalse(validate_password("INVALID123!"))

    def test_no_digit(self):
        """
        Verifica que una contraseña sin número regrese False.
        """
        self.assertFalse(validate_password("Invalid!!!"))

    def test_no_special_character(self):
        """
        Verifica que una contraseña sin carácter especial regrese False.
        """
        self.assertFalse(validate_password("Invalid123"))

    def test_invalid_special_character(self):
        """
        Verifica que una contraseña con un carácter especial no permitido regrese False.
        """
        self.assertFalse(validate_password("Invalid123?"))


# 3
class TestCalculateTotalDiscount(unittest.TestCase):
    """
    Pruebas de caja blanca para calculate_total_discount.
    """

    def test_no_discount(self):
        """
        Verifica que montos menores a 100 no tengan descuento.
        """
        self.assertEqual(calculate_total_discount(99), 0)

    def test_ten_percent_discount_lower_bound(self):
        """
        Verifica que un monto de exactamente 100 tenga 10% de descuento.
        """
        self.assertEqual(calculate_total_discount(100), 10)

    def test_ten_percent_discount_upper_bound(self):
        """
        Verifica que un monto de exactamente 500 tenga 10% de descuento.
        """
        self.assertEqual(calculate_total_discount(500), 50)

    def test_twenty_percent_discount(self):
        """
        Verifica que montos mayores a 500 tengan 20% de descuento.
        """
        self.assertEqual(calculate_total_discount(1000), 200)


# 4
class TestCalculateOrderTotal(unittest.TestCase):
    """
    Pruebas de caja blanca para calculate_order_total.
    """

    def test_empty_order(self):
        """
        Verifica que una orden vacía regrese 0.
        """
        self.assertEqual(calculate_order_total([]), 0)

    def test_no_discount_quantity(self):
        """
        Verifica que cantidades entre 1 y 5 no tengan descuento.
        """
        self.assertEqual(calculate_order_total([{"quantity": 3, "price": 10}]), 30)

    def test_five_percent_discount_quantity(self):
        """
        Verifica que cantidades entre 6 y 10 tengan 5% de descuento.
        """
        self.assertEqual(calculate_order_total([{"quantity": 6, "price": 10}]), 57.0)

    def test_ten_percent_discount_quantity(self):
        """
        Verifica que cantidades mayores a 10 tengan 10% de descuento.
        """
        self.assertEqual(calculate_order_total([{"quantity": 11, "price": 10}]), 99.0)

    def test_mixed_quantities(self):
        """
        Verifica que cada artículo aplique su descuento correspondiente según la cantidad.
        """
        items = [
            {"quantity": 5, "price": 10},
            {"quantity": 8, "price": 20},
            {"quantity": 12, "price": 5},
        ]
        expected = (5 * 10) + (0.95 * 8 * 20) + (0.9 * 12 * 5)
        self.assertEqual(calculate_order_total(items), expected)


# 5
class TestCalculateItemsShippingCost(unittest.TestCase):
    """
    Pruebas de caja blanca para calculate_items_shipping_cost.
    """

    def test_standard_light(self):
        """
        Verifica que envío estándar con peso menor o igual a 5 kg cueste $10.
        """
        self.assertEqual(calculate_items_shipping_cost([{"weight": 3}], "standard"), 10)

    def test_standard_medium(self):
        """
        Verifica que envío estándar con peso entre 5 y 10 kg cueste $15.
        """
        self.assertEqual(calculate_items_shipping_cost([{"weight": 7}], "standard"), 15)

    def test_standard_heavy(self):
        """
        Verifica que envío estándar con peso mayor a 10 kg cueste $20.
        """
        self.assertEqual(
            calculate_items_shipping_cost([{"weight": 12}], "standard"), 20
        )

    def test_express_light(self):
        """
        Verifica que envío express con peso menor o igual a 5 kg cueste $20.
        """
        self.assertEqual(calculate_items_shipping_cost([{"weight": 3}], "express"), 20)

    def test_express_medium(self):
        """
        Verifica que envío express con peso entre 5 y 10 kg cueste $30.
        """
        self.assertEqual(calculate_items_shipping_cost([{"weight": 7}], "express"), 30)

    def test_express_heavy(self):
        """
        Verifica que envío express con peso mayor a 10 kg cueste $40.
        """
        self.assertEqual(calculate_items_shipping_cost([{"weight": 12}], "express"), 40)

    def test_invalid_shipping_method(self):
        """
        Verifica que un método de envío inválido lance un ValueError.
        """
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost([{"weight": 3}], "drone")


# 6
class TestValidateLogin(unittest.TestCase):
    """
    Pruebas de caja blanca para validate_login.
    """

    def test_valid_login(self):
        """
        Verifica que un usuario (5-20 chars) y contraseña (8-15 chars) válidos inicien sesión.
        """
        self.assertEqual(validate_login("jorge", "password1"), "Login Successful")

    def test_username_too_short(self):
        """
        Verifica que un usuario con menos de 5 caracteres falle el login.
        """
        self.assertEqual(validate_login("abc", "password1"), "Login Failed")

    def test_username_too_long(self):
        """
        Verifica que un usuario con más de 20 caracteres falle el login.
        """
        self.assertEqual(validate_login("a" * 21, "password1"), "Login Failed")

    def test_password_too_short(self):
        """
        Verifica que una contraseña con menos de 8 caracteres falle el login.
        """
        self.assertEqual(validate_login("jorge", "pass"), "Login Failed")

    def test_password_too_long(self):
        """
        Verifica que una contraseña con más de 15 caracteres falle el login.
        """
        self.assertEqual(validate_login("jorge", "p" * 16), "Login Failed")


# 7
class TestVerifyAge(unittest.TestCase):
    """
    Pruebas de caja blanca para verify_age.
    """

    def test_eligible_age(self):
        """
        Verifica que una edad entre 18 y 65 sea elegible.
        """
        self.assertEqual(verify_age(30), "Eligible")

    def test_too_young(self):
        """
        Verifica que una edad menor a 18 no sea elegible.
        """
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_too_old(self):
        """
        Verifica que una edad mayor a 65 no sea elegible.
        """
        self.assertEqual(verify_age(66), "Not Eligible")

    def test_boundary_18(self):
        """
        Verifica que exactamente 18 años sea elegible.
        """
        self.assertEqual(verify_age(18), "Eligible")

    def test_boundary_65(self):
        """
        Verifica que exactamente 65 años sea elegible.
        """
        self.assertEqual(verify_age(65), "Eligible")


# 8
class TestCategorizeProduct(unittest.TestCase):
    """
    Pruebas de caja blanca para categorize_product.
    """

    def test_category_a(self):
        """
        Verifica que un precio entre $10 y $50 sea Categoría A.
        """
        self.assertEqual(categorize_product(25), "Category A")

    def test_category_b(self):
        """
        Verifica que un precio entre $51 y $100 sea Categoría B.
        """
        self.assertEqual(categorize_product(75), "Category B")

    def test_category_c(self):
        """
        Verifica que un precio entre $101 y $200 sea Categoría C.
        """
        self.assertEqual(categorize_product(150), "Category C")

    def test_category_d(self):
        """
        Verifica que un precio mayor a $200 sea Categoría D.
        """
        self.assertEqual(categorize_product(250), "Category D")

    def test_below_category_a(self):
        """
        Verifica que un precio menor a $10 caiga en Categoría D (no hay categoría menor).
        """
        self.assertEqual(categorize_product(5), "Category D")


# 9
class TestValidateEmail(unittest.TestCase):
    """
    Pruebas de caja blanca para validate_email.
    """

    def test_valid_email(self):
        """
        Verifica que un correo con formato correcto sea válido.
        """
        self.assertEqual(validate_email("user@example.com"), "Valid Email")

    def test_no_at_symbol(self):
        """
        Verifica que un correo sin @ sea inválido.
        """
        self.assertEqual(validate_email("userexample.com"), "Invalid Email")

    def test_no_dot(self):
        """
        Verifica que un correo sin punto sea inválido.
        """
        self.assertEqual(validate_email("user@examplecom"), "Invalid Email")

    def test_too_short(self):
        """
        Verifica que un correo de menos de 5 caracteres sea inválido.
        """
        self.assertEqual(validate_email("a@b"), "Invalid Email")

    def test_too_long(self):
        """
        Verifica que un correo de más de 50 caracteres sea inválido.
        """
        self.assertEqual(validate_email("a" * 45 + "@b.com"), "Invalid Email")


# 10
class TestCelsiusToFahrenheit(unittest.TestCase):
    """
    Pruebas de caja blanca para celsius_to_fahrenheit.
    """

    def test_freezing_point(self):
        """
        Verifica que 0°C se convierta correctamente a 32°F.
        """
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_boiling_point(self):
        """
        Verifica que 100°C se convierta correctamente a 212°F.
        """
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_negative_temperature(self):
        """
        Verifica que -40°C se convierta correctamente a -40°F.
        """
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

    def test_out_of_range_high(self):
        """
        Verifica que temperaturas mayores a 100°C regresen un mensaje de error.
        """
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")

    def test_out_of_range_low(self):
        """
        Verifica que temperaturas menores a -100°C regresen un mensaje de error.
        """
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")


# 11
class TestValidateCreditCard(unittest.TestCase):
    """
    Pruebas de caja blanca para validate_credit_card.
    """

    def test_valid_13_digits(self):
        """
        Verifica que un número de tarjeta de 13 dígitos sea válido.
        """
        self.assertEqual(validate_credit_card("4111111111111"), "Valid Card")

    def test_valid_16_digits(self):
        """
        Verifica que un número de tarjeta de 16 dígitos sea válido.
        """
        self.assertEqual(validate_credit_card("4111111111111111"), "Valid Card")

    def test_too_short(self):
        """
        Verifica que un número de tarjeta con menos de 13 dígitos sea inválido.
        """
        self.assertEqual(validate_credit_card("411111111111"), "Invalid Card")

    def test_too_long(self):
        """
        Verifica que un número de tarjeta con más de 16 dígitos sea inválido.
        """
        self.assertEqual(validate_credit_card("41111111111111111"), "Invalid Card")

    def test_non_numeric(self):
        """
        Verifica que un número de tarjeta con letras sea inválido.
        """
        self.assertEqual(validate_credit_card("4111abcd11111"), "Invalid Card")


# 12
class TestValidateDate(unittest.TestCase):
    """
    Pruebas de caja blanca para validate_date.
    """

    def test_valid_date(self):
        """
        Verifica que una fecha dentro de los rangos válidos sea aceptada.
        """
        self.assertEqual(validate_date(2000, 6, 15), "Valid Date")

    def test_invalid_year_low(self):
        """
        Verifica que un año menor a 1900 sea inválido.
        """
        self.assertEqual(validate_date(1899, 6, 15), "Invalid Date")

    def test_invalid_year_high(self):
        """
        Verifica que un año mayor a 2100 sea inválido.
        """
        self.assertEqual(validate_date(2101, 6, 15), "Invalid Date")

    def test_invalid_month_low(self):
        """
        Verifica que el mes 0 sea inválido.
        """
        self.assertEqual(validate_date(2000, 0, 15), "Invalid Date")

    def test_invalid_month_high(self):
        """
        Verifica que el mes 13 sea inválido.
        """
        self.assertEqual(validate_date(2000, 13, 15), "Invalid Date")

    def test_invalid_day_low(self):
        """
        Verifica que el día 0 sea inválido.
        """
        self.assertEqual(validate_date(2000, 6, 0), "Invalid Date")

    def test_invalid_day_high(self):
        """
        Verifica que el día 32 sea inválido.
        """
        self.assertEqual(validate_date(2000, 6, 32), "Invalid Date")


# 13
class TestCheckFlightEligibility(unittest.TestCase):
    """
    Pruebas de caja blanca para check_flight_eligibility.
    """

    def test_eligible_by_age(self):
        """
        Verifica que una persona de entre 18 y 65 años pueda reservar sin importar si es viajero frecuente.
        """
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_eligible_frequent_flyer(self):
        """
        Verifica que un viajero frecuente pueda reservar aunque esté fuera del rango de edad.
        """
        self.assertEqual(check_flight_eligibility(70, True), "Eligible to Book")

    def test_not_eligible(self):
        """
        Verifica que alguien fuera del rango de edad y que no es viajero frecuente no pueda reservar.
        """
        self.assertEqual(check_flight_eligibility(16, False), "Not Eligible to Book")

    def test_boundary_age_18(self):
        """
        Verifica que exactamente 18 años sea elegible.
        """
        self.assertEqual(check_flight_eligibility(18, False), "Eligible to Book")

    def test_boundary_age_65(self):
        """
        Verifica que exactamente 65 años sea elegible.
        """
        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")


# 14
class TestValidateUrl(unittest.TestCase):
    """
    Pruebas de caja blanca para validate_url.
    """

    def test_valid_http(self):
        """
        Verifica que una URL con http:// sea válida.
        """
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_valid_https(self):
        """
        Verifica que una URL con https:// sea válida.
        """
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_invalid_prefix(self):
        """
        Verifica que una URL con un prefijo no soportado sea inválida.
        """
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")

    def test_too_long(self):
        """
        Verifica que una URL de más de 255 caracteres sea inválida.
        """
        self.assertEqual(validate_url("http://" + "a" * 250), "Invalid URL")


# 15
class TestCalculateQuantityDiscount(unittest.TestCase):
    """
    Pruebas de caja blanca para calculate_quantity_discount.
    """

    def test_no_discount(self):
        """
        Verifica que cantidades entre 1 y 5 no tengan descuento.
        """
        self.assertEqual(calculate_quantity_discount(3), "No Discount")

    def test_five_percent_discount(self):
        """
        Verifica que cantidades entre 6 y 10 tengan 5% de descuento.
        """
        self.assertEqual(calculate_quantity_discount(8), "5% Discount")

    def test_ten_percent_discount(self):
        """
        Verifica que cantidades mayores a 10 tengan 10% de descuento.
        """
        self.assertEqual(calculate_quantity_discount(15), "10% Discount")

    def test_boundary_5(self):
        """
        Verifica que exactamente 5 unidades no tengan descuento.
        """
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_boundary_6(self):
        """
        Verifica que exactamente 6 unidades tengan 5% de descuento.
        """
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")

    def test_boundary_10(self):
        """
        Verifica que exactamente 10 unidades tengan 5% de descuento.
        """
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_boundary_11(self):
        """
        Verifica que exactamente 11 unidades tengan 10% de descuento.
        """
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")


# 16
class TestCheckFileSize(unittest.TestCase):
    """
    Pruebas de caja blanca para check_file_size.
    """

    def test_valid_size(self):
        """
        Verifica que un tamaño de archivo dentro del límite de 1 MB sea válido.
        """
        self.assertEqual(check_file_size(512000), "Valid File Size")

    def test_zero_bytes(self):
        """
        Verifica que un archivo de 0 bytes sea válido.
        """
        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_exactly_1_mb(self):
        """
        Verifica que exactamente 1 MB (1048576 bytes) sea válido.
        """
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_exceeds_1_mb(self):
        """
        Verifica que un archivo que pasa de 1 MB sea inválido.
        """
        self.assertEqual(check_file_size(1048577), "Invalid File Size")

    def test_negative_size(self):
        """
        Verifica que un tamaño negativo sea inválido.
        """
        self.assertEqual(check_file_size(-1), "Invalid File Size")


# 17
class TestCheckLoanEligibility(unittest.TestCase):
    """
    Pruebas de caja blanca para check_loan_eligibility.
    """

    def test_not_eligible_low_income(self):
        """
        Verifica que un ingreso menor a $30,000 no sea elegible para ningún préstamo.
        """
        self.assertEqual(check_loan_eligibility(20000, 800), "Not Eligible")

    def test_standard_loan_mid_income_high_score(self):
        """
        Verifica que un ingreso medio con score mayor a 700 obtenga un préstamo estándar.
        """
        self.assertEqual(check_loan_eligibility(45000, 750), "Standard Loan")

    def test_secured_loan_mid_income_low_score(self):
        """
        Verifica que un ingreso medio con score de 700 o menos obtenga un préstamo garantizado.
        """
        self.assertEqual(check_loan_eligibility(45000, 680), "Secured Loan")

    def test_premium_loan_high_income_high_score(self):
        """
        Verifica que un ingreso alto con score mayor a 750 obtenga un préstamo premium.
        """
        self.assertEqual(check_loan_eligibility(80000, 800), "Premium Loan")

    def test_standard_loan_high_income_mid_score(self):
        """
        Verifica que un ingreso alto con score de 750 o menos obtenga un préstamo estándar.
        """
        self.assertEqual(check_loan_eligibility(80000, 730), "Standard Loan")

    def test_boundary_income_30000(self):
        """
        Verifica que exactamente $30,000 de ingreso se evalúe como ingreso medio.
        """
        self.assertEqual(check_loan_eligibility(30000, 750), "Standard Loan")

    def test_boundary_income_60000(self):
        """
        Verifica que exactamente $60,000 de ingreso se evalúe como ingreso medio.
        """
        self.assertEqual(check_loan_eligibility(60000, 750), "Standard Loan")


# 18
class TestCalculateShippingCost(unittest.TestCase):
    """
    Pruebas de caja blanca para calculate_shipping_cost.
    """

    def test_small_package(self):
        """
        Verifica que un paquete de hasta 1 kg y dimensiones de hasta 10 cm cueste $5.
        """
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_medium_package(self):
        """
        Verifica que un paquete de 1-5 kg y dimensiones de 11-30 cm cueste $10.
        """
        self.assertEqual(calculate_shipping_cost(3, 20, 20, 20), 10)

    def test_large_package_by_weight(self):
        """
        Verifica que un paquete de más de 5 kg cueste $20.
        """
        self.assertEqual(calculate_shipping_cost(6, 20, 20, 20), 20)

    def test_large_package_by_dimension(self):
        """
        Verifica que un paquete con alguna dimensión mayor a 30 cm cueste $20.
        """
        self.assertEqual(calculate_shipping_cost(3, 31, 20, 20), 20)


# 19
class TestGradeQuiz(unittest.TestCase):
    """
    Pruebas de caja blanca para grade_quiz.
    """

    def test_pass(self):
        """
        Verifica que 7 o más respuestas correctas y 2 o menos incorrectas sea aprobado.
        """
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_conditional_pass(self):
        """
        Verifica que 5 o más correctas y 3 o menos incorrectas (sin cumplir Pass) sea aprobado condicional.
        """
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_fail(self):
        """
        Verifica que no cumplir ninguna condición de aprobación sea reprobado.
        """
        self.assertEqual(grade_quiz(4, 5), "Fail")

    def test_pass_boundary(self):
        """
        Verifica el límite exacto de aprobado: 7 correctas y 2 incorrectas.
        """
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_conditional_pass_boundary(self):
        """
        Verifica el límite exacto de aprobado condicional: 5 correctas y 3 incorrectas.
        """
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")


# 20
class TestAuthenticateUser(unittest.TestCase):
    """
    Pruebas de caja blanca para authenticate_user.
    """

    def test_admin_credentials(self):
        """
        Verifica que el usuario "admin" con contraseña "admin123" regrese "Admin".
        """
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_valid_user(self):
        """
        Verifica que un usuario con 5+ caracteres y contraseña con 8+ caracteres regrese "User".
        """
        self.assertEqual(authenticate_user("jorge", "password1"), "User")

    def test_username_too_short(self):
        """
        Verifica que un usuario con menos de 5 caracteres regrese "Invalid".
        """
        self.assertEqual(authenticate_user("abc", "password1"), "Invalid")

    def test_password_too_short(self):
        """
        Verifica que una contraseña con menos de 8 caracteres regrese "Invalid".
        """
        self.assertEqual(authenticate_user("jorge", "pass"), "Invalid")

    def test_both_too_short(self):
        """
        Verifica que tanto usuario como contraseña cortos regresen "Invalid".
        """
        self.assertEqual(authenticate_user("ab", "123"), "Invalid")


# 21
class TestGetWeatherAdvisory(unittest.TestCase):
    """
    Pruebas de caja blanca para get_weather_advisory.
    """

    def test_high_temp_and_humidity(self):
        """
        Verifica el aviso cuando la temperatura es mayor a 30 y la humedad mayor a 70.
        """
        self.assertEqual(
            get_weather_advisory(35, 80),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_low_temperature(self):
        """
        Verifica el aviso cuando la temperatura es menor a 0.
        """
        self.assertEqual(
            get_weather_advisory(-5, 50),
            "Low Temperature. Bundle Up!",
        )

    def test_no_advisory(self):
        """
        Verifica que condiciones normales no generen ningún aviso.
        """
        self.assertEqual(get_weather_advisory(20, 60), "No Specific Advisory")

    def test_high_temp_low_humidity(self):
        """
        Verifica que temperatura alta sin humedad alta no genere aviso de calor.
        """
        self.assertEqual(get_weather_advisory(35, 60), "No Specific Advisory")


if __name__ == "__main__":
    unittest.main()
