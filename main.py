import random
import string
from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

# Simula el tamaño y aspecto de una pantalla móvil (360x640)
Window.size = (360, 640)


class GeneradorInterfaz(BoxLayout):
  contrasena_generada = StringProperty("")

  def generar(self):
    longitud = int(self.ids.slider_longitud.value)

    # Construir el conjunto de caracteres según los filtros seleccionados
    caracteres = ""
    if self.ids.chk_mayus.active:
      caracteres += string.ascii_uppercase
    if self.ids.chk_minus.active:
      caracteres += string.ascii_lowercase
    if self.ids.chk_nums.active:
      caracteres += string.digits
    if self.ids.chk_simbolos.active:
      caracteres += string.punctuation

    # Validación por si desmarcan todas las casillas
    if not caracteres:
      self.contrasena_generada = "Selecciona 1 opción"
      return

    self.contrasena_generada = "".join(
        random.choice(caracteres) for _ in range(longitud)
    )

  def copiar(self):
    if (
        self.contrasena_generada
        and self.contrasena_generada != "Selecciona 1 opción"
    ):
      Clipboard.copy(self.contrasena_generada)


class PasswordGeneratorApp(App):

  def build(self):
    return GeneradorInterfaz()


if __name__ == "__main__":
  PasswordGeneratorApp().run()