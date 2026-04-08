# -*- coding: utf-8 -*-

"""
Unit tests para ejercicio 2
"""
import os
import runpy
import sys
import unittest
from unittest.mock import call, patch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from Example_2 import Song, SongStore, main


class TestSong(unittest.TestCase):
    """Pruebas para la clase Song"""

    def setUp(self):
        self.song = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", 1975)


    def test_inicializacion(self):
        """Verifica que __init__ asigne correctamente los atributos"""
        self.assertEqual(self.song.title, "Bohemian Rhapsody")
        self.assertEqual(self.song.author, "Queen")
        self.assertEqual(self.song.album, "A Night at the Opera")
        self.assertEqual(self.song.year, 1975)


    @patch("builtins.print")
    def test_display_imprime_los_4_campos_en_orden(self, mock_print):
        """display imprime exactamente los 4 campos esperados"""
        self.song.display()

        mock_print.assert_has_calls(
            [
                call("Title: Bohemian Rhapsody"),
                call("Author: Queen"),
                call("Album: A Night at the Opera"),
                call("Year: 1975"),
            ]
        )
        self.assertEqual(mock_print.call_count, 4)


class TestSongStore(unittest.TestCase):
    """Pruebas para SongStore"""

    def setUp(self):
        self.store = SongStore()
        self.song = Song("Stairway to Heaven", "Led Zeppelin", "Led Zeppelin IV", 1971)


    def test_inicializacion(self):
        """El store inicia con lista vacía"""
        self.assertEqual(self.store.songs, [])


    @patch("builtins.print")
    def test_add_song_agrega_y_confirma(self, mock_print):
        """Agrega una canción al store e imprime confirmación"""
        self.store.add_song(self.song)

        self.assertEqual(len(self.store.songs), 1)
        self.assertIs(self.store.songs[0], self.song)
        mock_print.assert_called_once_with("Song 'Stairway to Heaven' added to the store.")


    @patch("builtins.print")
    def test_display_songs_lista_vacia(self, mock_print):
        """Si no hay canciones, imprime mensaje correspondiente"""
        self.store.display_songs()
        mock_print.assert_called_once_with("No songs in the store.")


    @patch("builtins.print")
    def test_display_songs_con_una_cancion(self, mock_print):
        """Con una canción, imprime encabezado y llama display una vez"""
        self.store.songs.append(self.song)

        with patch.object(self.song, "display") as mock_display:
            self.store.display_songs()

        mock_print.assert_called_once_with("Songs available in the store:")
        mock_display.assert_called_once_with()


    @patch("builtins.print")
    def test_display_songs_con_multiples_canciones(self, mock_print):
        """Con varias canciones, imprime encabezado y muestra todas"""
        song2 = Song("Imagine", "John Lennon", "Imagine", 1971)
        self.store.songs.extend([self.song, song2])

        with patch.object(self.song, "display") as mock_display_1, \
             patch.object(song2, "display") as mock_display_2:
            self.store.display_songs()

        mock_print.assert_called_once_with("Songs available in the store:")
        mock_display_1.assert_called_once_with()
        mock_display_2.assert_called_once_with()


    @patch("builtins.print")
    def test_search_song_no_encontrada(self, mock_print):
        """Si no existe coincidencia, imprime mensaje de no encontrada"""
        self.store.search_song("Unknown Song")
        mock_print.assert_called_once_with("No song found with title 'Unknown Song'.")


    @patch("builtins.print")
    def test_search_song_encontrada(self, mock_print):
        """Si existe una coincidencia, imprime conteo y muestra la canción"""
        self.store.songs.append(self.song)

        with patch.object(self.song, "display") as mock_display:
            self.store.search_song("Stairway to Heaven")

        mock_print.assert_called_once_with("Found 1 song(s) with title 'Stairway to Heaven':")
        mock_display.assert_called_once_with()


    @patch("builtins.print")
    def test_search_song_case_insensitive(self, mock_print):
        """La búsqueda debe ignorar mayúsculas/minúsculas"""
        self.store.songs.append(self.song)

        with patch.object(self.song, "display") as mock_display:
            self.store.search_song("stairway to heaven")

        mock_print.assert_called_once_with("Found 1 song(s) with title 'stairway to heaven':")
        mock_display.assert_called_once_with()


    @patch("builtins.print")
    def test_search_song_multiples_coincidencias(self, mock_print):
        """Si hay varias canciones con el mismo título, debe mostrarlas todas"""
        song2 = Song("Stairway to Heaven", "Heart", "Magazine", 1975)
        self.store.songs.extend([self.song, song2])

        with patch.object(self.song, "display") as mock_display_1, \
             patch.object(song2, "display") as mock_display_2:
            self.store.search_song("Stairway to Heaven")

        mock_print.assert_called_once_with("Found 2 song(s) with title 'Stairway to Heaven':")
        mock_display_1.assert_called_once_with()
        mock_display_2.assert_called_once_with()


    @patch("builtins.print")
    def test_search_song_store_vacio(self, mock_print):
        """Buscar con store vacío también debe responder correctamente"""
        self.store.search_song("Anything")
        mock_print.assert_called_once_with("No song found with title 'Anything'.")


class TestMain(unittest.TestCase):
    """Pruebas para main"""

    @patch("builtins.input", side_effect=["1", "4"])
    @patch("builtins.print")
    def test_opcion_1_display_songs(self, mock_print, mock_input):
        """Opción 1: muestra canciones con store vacío"""
        main()
        mock_print.assert_any_call("No songs in the store.")
        mock_print.assert_any_call("Exiting...")


    @patch("builtins.input", side_effect=["2", "Stairway to Heaven", "4"])
    @patch("builtins.print")
    def test_opcion_2_search_song(self, mock_print, mock_input):
        """Opción 2: busca canción en store vacío"""
        main()
        mock_print.assert_any_call("No song found with title 'Stairway to Heaven'.")
        mock_print.assert_any_call("Exiting...")


    @patch("builtins.input", side_effect=["3", "MySong", "MyAuthor", "MyAlbum", "2020", "4"])
    @patch("builtins.print")
    def test_opcion_3_add_song(self, mock_print, mock_input):
        """Opción 3: agrega una canción correctamente"""
        main()
        mock_print.assert_any_call("Song 'MySong' added to the store.")
        mock_print.assert_any_call("Exiting...")


    @patch("builtins.input", side_effect=["3", "MySong", "MyAuthor", "MyAlbum", "2020", "1", "4"])
    @patch("builtins.print")
    def test_main_add_y_despues_mostrar_misma_sesion(self, mock_print, mock_input):
        """Agrega una canción y luego la muestra en la misma ejecución"""
        main()

        mock_print.assert_any_call("Song 'MySong' added to the store.")
        mock_print.assert_any_call("Songs available in the store:")
        mock_print.assert_any_call("Title: MySong")
        mock_print.assert_any_call("Author: MyAuthor")
        mock_print.assert_any_call("Album: MyAlbum")
        mock_print.assert_any_call("Year: 2020")


    @patch("builtins.input", side_effect=["3", "MySong", "MyAuthor", "MyAlbum", "2020", "2", "mysong", "4"])
    @patch("builtins.print")
    def test_main_add_y_despues_buscar_misma_sesion(self, mock_print, mock_input):
        """Agrega una canción y luego la busca en la misma ejecución"""
        main()

        mock_print.assert_any_call("Song 'MySong' added to the store.")
        mock_print.assert_any_call("Found 1 song(s) with title 'mysong':")
        mock_print.assert_any_call("Title: MySong")


    @patch("builtins.input", side_effect=["4"])
    @patch("builtins.print")
    def test_opcion_4_sale_del_loop(self, mock_print, mock_input):
        """Opción 4: sale del programa"""
        main()
        mock_print.assert_any_call("Exiting...")


    @patch("builtins.input", side_effect=["invalid", "4"])
    @patch("builtins.print")
    def test_opcion_invalida(self, mock_print, mock_input):
        """Opción inválida: imprime error y continúa hasta salir"""
        main()
        mock_print.assert_any_call("Invalid choice. Please try again.")
        mock_print.assert_any_call("Exiting...")


    @patch("builtins.input", side_effect=["3", "MySong", "MyAuthor", "MyAlbum", "abc"])
    def test_opcion_3_year_invalido_lanza_value_error(self, mock_input):
        """Documenta el comportamiento actual cuando year no es entero"""
        with self.assertRaises(ValueError):
            main()


    @patch("builtins.input", side_effect=["4"])
    @patch("builtins.print")
    def test_bloque_if_name_main(self, mock_print, mock_input):
        """Ejecuta el archivo como __main__ para cubrir el bloque final"""
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Example_2.py")
        runpy.run_path(file_path, run_name="__main__")
        mock_print.assert_any_call("Exiting...")


if __name__ == "__main__":
    unittest.main()