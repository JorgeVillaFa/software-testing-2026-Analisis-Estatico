# -*- coding: utf-8 -*-

"""
Unit tests mejorados para ejercicio 1
"""
import hashlib
import json
import os
import runpy
import sys
import unittest
from unittest.mock import ANY, mock_open, patch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from Example_1 import (
    USER_DATA_FILE,
    generate_password_hash,
    generate_salt,
    load_user_data,
    login,
    main,
    register,
    save_user_data,
)


class TestGenerateSalt(unittest.TestCase):
    """Pruebas para generate_salt"""

    def test_retorna_string(self):
        """Verifica que el salt sea string"""
        self.assertIsInstance(generate_salt(), str)


    def test_longitud_32_caracteres(self):
        """16 bytes en hexadecimal producen 32 caracteres"""
        self.assertEqual(len(generate_salt()), 32)


    def test_solo_contiene_hexadecimal(self):
        """El salt generado debe ser hexadecimal"""
        result = generate_salt()
        self.assertTrue(all(c in "0123456789abcdef" for c in result))


    def test_salts_son_distintos(self):
        """Dos salts consecutivos deben ser distintos"""
        self.assertNotEqual(generate_salt(), generate_salt())


class TestGeneratePasswordHash(unittest.TestCase):
    """Pruebas para generate_password_hash"""

    def test_hash_sha256_correcto(self):
        """El hash debe coincidir con SHA-256(password + salt)"""
        password = "mypassword"
        salt = "mysalt"
        expected = hashlib.sha256(password.encode() + salt.encode()).hexdigest()
        self.assertEqual(generate_password_hash(password, salt), expected)


    def test_hash_es_hexadecimal_de_64_caracteres(self):
        """Un SHA-256 en hexdigest siempre tiene 64 caracteres hex"""
        result = generate_password_hash("test", "salt")
        self.assertEqual(len(result), 64)
        self.assertTrue(all(c in "0123456789abcdef" for c in result))


    def test_mismo_password_y_salt_producen_mismo_hash(self):
        """Misma entrada debe producir el mismo hash"""
        result_1 = generate_password_hash("abc123", "salt1")
        result_2 = generate_password_hash("abc123", "salt1")
        self.assertEqual(result_1, result_2)


    def test_mismo_password_con_distinto_salt_produce_hash_distinto(self):
        """Cambiar el salt debe cambiar el hash"""
        result_1 = generate_password_hash("abc123", "salt1")
        result_2 = generate_password_hash("abc123", "salt2")
        self.assertNotEqual(result_1, result_2)


class TestLoadUserData(unittest.TestCase):
    """Pruebas para load_user_data"""

    @patch("Example_1.os.path.exists", return_value=True)
    def test_carga_datos_cuando_archivo_existe(self, mock_exists):
        """Si el archivo existe, retorna el contenido parseado"""
        data = {"user1": {"password_hash": "abc", "salt": "xyz"}}

        with patch("builtins.open", mock_open(read_data=json.dumps(data))) as mock_file:
            result = load_user_data()

        mock_exists.assert_called_once_with(USER_DATA_FILE)
        mock_file.assert_called_once_with(USER_DATA_FILE, "r")
        self.assertEqual(result, data)


    @patch("Example_1.os.path.exists", return_value=False)
    def test_retorna_dict_vacio_si_no_existe_archivo(self, mock_exists):
        """Si no existe archivo, retorna diccionario vacío"""
        result = load_user_data()

        mock_exists.assert_called_once_with(USER_DATA_FILE)
        self.assertEqual(result, {})


    @patch("Example_1.os.path.exists", return_value=True)
    def test_json_invalido_lanza_json_decode_error(self, mock_exists):
        """Documenta el comportamiento actual con JSON corrupto"""
        with patch("builtins.open", mock_open(read_data="{not valid json")):
            with self.assertRaises(json.JSONDecodeError):
                load_user_data()


class TestSaveUserData(unittest.TestCase):
    """Pruebas para save_user_data"""

    @patch("Example_1.json.dump")
    @patch("builtins.open", new_callable=mock_open)
    def test_guarda_datos_correctamente(self, mock_file, mock_dump):
        """Abre el archivo correcto y serializa con indent=4"""
        data = {"user1": {"password_hash": "abc", "salt": "xyz"}}

        save_user_data(data)

        mock_file.assert_called_once_with(USER_DATA_FILE, "w")
        mock_dump.assert_called_once_with(data, ANY, indent=4)


    @patch("builtins.open", side_effect=OSError("disk full"))
    def test_error_de_escritura_lanza_os_error(self, mock_open_):
        """Documenta el comportamiento actual cuando open falla"""
        with self.assertRaises(OSError):
            save_user_data({"user1": {}})


class TestRegister(unittest.TestCase):
    """Pruebas para register"""

    @patch("Example_1.save_user_data")
    @patch("builtins.input")
    @patch("Example_1.load_user_data", return_value={"existinguser": {}})
    @patch("builtins.print")
    def test_usuario_ya_existe_no_pide_password_ni_guarda(
        self, mock_print, mock_load, mock_input, mock_save
    ):
        """Si el usuario ya existe, no debe pedir password ni guardar"""
        register("existinguser")

        mock_print.assert_called_once_with(
            "User already exists. Please choose a different username."
        )
        mock_input.assert_not_called()
        mock_save.assert_not_called()


    @patch("Example_1.save_user_data")
    @patch("Example_1.generate_password_hash", return_value="hashed_pw")
    @patch("Example_1.generate_salt", return_value="randomsalt")
    @patch("builtins.input", return_value="mypassword")
    @patch("Example_1.load_user_data", return_value={})
    @patch("builtins.print")
    def test_registro_exitoso(
        self, mock_print, mock_load, mock_input, mock_salt, mock_hash, mock_save
    ):
        """Registro exitoso con verificación estricta de llamadas"""
        register("newuser")

        mock_input.assert_called_once_with("Enter your password: ")
        mock_salt.assert_called_once_with()
        mock_hash.assert_called_once_with("mypassword", "randomsalt")
        mock_save.assert_called_once_with(
            {"newuser": {"password_hash": "hashed_pw", "salt": "randomsalt"}}
        )
        mock_print.assert_called_once_with("User registered successfully.")


    @patch("Example_1.save_user_data")
    @patch("Example_1.generate_password_hash", return_value="hashed_empty")
    @patch("Example_1.generate_salt", return_value="emptysalt")
    @patch("builtins.input", return_value="")
    @patch("Example_1.load_user_data", return_value={})
    @patch("builtins.print")
    def test_registro_con_password_vacio_se_guarda(
        self, mock_print, mock_load, mock_input, mock_salt, mock_hash, mock_save
    ):
        """Documenta que el código actual permite password vacío"""
        register("empty_pass_user")

        mock_hash.assert_called_once_with("", "emptysalt")
        mock_save.assert_called_once_with(
            {"empty_pass_user": {"password_hash": "hashed_empty", "salt": "emptysalt"}}
        )
        mock_print.assert_called_once_with("User registered successfully.")


    @patch("Example_1.save_user_data")
    @patch("Example_1.generate_password_hash", return_value="hash_blank_user")
    @patch("Example_1.generate_salt", return_value="salt_blank_user")
    @patch("builtins.input", return_value="mypassword")
    @patch("Example_1.load_user_data", return_value={})
    @patch("builtins.print")
    def test_registro_con_username_vacio_se_guarda(
        self, mock_print, mock_load, mock_input, mock_salt, mock_hash, mock_save
    ):
        """Documenta que el código actual permite username vacío"""
        register("")

        mock_save.assert_called_once_with(
            {"": {"password_hash": "hash_blank_user", "salt": "salt_blank_user"}}
        )
        mock_print.assert_called_once_with("User registered successfully.")


class TestLogin(unittest.TestCase):
    """Pruebas para login"""

    @patch("Example_1.generate_password_hash")
    @patch("Example_1.load_user_data", return_value={})
    @patch("builtins.print")
    def test_usuario_no_existe(self, mock_print, mock_load, mock_hash):
        """Si el usuario no existe, no se debe generar hash"""
        login("nouser", "pass")

        mock_print.assert_called_once_with(
            "User does not exist. Please register first."
        )
        mock_hash.assert_not_called()


    @patch("Example_1.generate_password_hash", return_value="correct_hash")
    @patch(
        "Example_1.load_user_data",
        return_value={"user1": {"password_hash": "correct_hash", "salt": "somesalt"}},
    )
    @patch("builtins.print")
    def test_login_exitoso(self, mock_print, mock_load, mock_hash):
        """Login exitoso con password correcta"""
        login("user1", "mypassword")

        mock_hash.assert_called_once_with("mypassword", "somesalt")
        mock_print.assert_called_once_with("Login successful!")


    @patch("Example_1.generate_password_hash", return_value="wrong_hash")
    @patch(
        "Example_1.load_user_data",
        return_value={"user1": {"password_hash": "correct_hash", "salt": "somesalt"}},
    )
    @patch("builtins.print")
    def test_login_password_incorrecta(self, mock_print, mock_load, mock_hash):
        """Login fallido con password incorrecta"""
        login("user1", "wrongpassword")

        mock_hash.assert_called_once_with("wrongpassword", "somesalt")
        mock_print.assert_called_once_with("Invalid password. Please try again.")


    @patch("Example_1.generate_password_hash", return_value="empty_hash")
    @patch(
        "Example_1.load_user_data",
        return_value={"": {"password_hash": "empty_hash", "salt": "emptysalt"}},
    )
    @patch("builtins.print")
    def test_login_con_username_vacio_funciona_segun_datos_almacenados(
        self, mock_print, mock_load, mock_hash
    ):
        """Documenta que username/password vacíos funcionan si existen en datos"""
        login("", "")

        mock_hash.assert_called_once_with("", "emptysalt")
        mock_print.assert_called_once_with("Login successful!")


class TestMain(unittest.TestCase):
    """Pruebas para main"""

    @patch("Example_1.register")
    @patch("builtins.input", side_effect=["1", "testuser", "3"])
    @patch("builtins.print")
    def test_opcion_1_llama_register(self, mock_print, mock_input, mock_register):
        """Opción 1: solicita username y llama a register"""
        main()

        mock_register.assert_called_once_with("testuser")
        mock_print.assert_any_call("Exiting...")


    @patch("Example_1.login")
    @patch("builtins.input", side_effect=["2", "testuser", "testpass", "3"])
    @patch("builtins.print")
    def test_opcion_2_llama_login(self, mock_print, mock_input, mock_login):
        """Opción 2: solicita username y password, luego llama a login"""
        main()

        mock_login.assert_called_once_with("testuser", "testpass")
        mock_print.assert_any_call("Exiting...")


    @patch("Example_1.register")
    @patch("Example_1.login")
    @patch(
        "builtins.input",
        side_effect=["1", "newuser", "2", "newuser", "newpass", "3"],
    )
    @patch("builtins.print")
    def test_main_registra_y_luego_login_en_misma_sesion(
        self, mock_print, mock_input, mock_login, mock_register
    ):
        """registrar y luego login en la misma ejecución"""
        main()

        mock_register.assert_called_once_with("newuser")
        mock_login.assert_called_once_with("newuser", "newpass")
        mock_print.assert_any_call("Exiting...")


    @patch("builtins.input", side_effect=["3"])
    @patch("builtins.print")
    def test_opcion_3_sale_del_loop(self, mock_print, mock_input):
        """Opción 3: sale del programa"""
        main()
        mock_print.assert_any_call("Exiting...")


    @patch("builtins.input", side_effect=["invalid", "3"])
    @patch("builtins.print")
    def test_opcion_invalida(self, mock_print, mock_input):
        """Opción inválida: muestra error y luego sale"""
        main()
        mock_print.assert_any_call("Invalid choice. Please try again.")
        mock_print.assert_any_call("Exiting...")


    @patch("builtins.input", side_effect=["3"])
    @patch("builtins.print")
    def test_bloque_if_name_main(self, mock_print, mock_input):
        """Ejecuta el archivo como __main__ para cubrir el bloque final"""
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Example_1.py")
        runpy.run_path(file_path, run_name="__main__")
        mock_print.assert_any_call("Exiting...")


if __name__ == "__main__":
    unittest.main()