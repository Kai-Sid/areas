import sys
import math
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QInputDialog
)


class AreaCalculator(QMainWindow):
    """
    Ventana principal de la aplicación que ofrece un menú
    para calcular el área de diferentes figuras geométricas.
    """

    def __init__(self):
        """
        Inicializa la ventana principal y configura el menú.
        """
        super().__init__()
        self.setWindowTitle("Calculadora de Áreas")
        self.setGeometry(100, 100, 400, 300)
        self.setup_menu()

    def setup_menu(self):
        """
        Crea y configura el menú superior con opciones
        para calcular el área de figuras.
        """
        menu_bar = self.menuBar()
        menu_area = menu_bar.addMenu("Calcular Área")

        menu_area.addAction("Círculo", self.area_circulo)
        menu_area.addAction("Triángulo", self.area_triangulo)
        menu_area.addAction("Rectángulo", self.area_rectangulo)
        menu_area.addAction("Cuadrado", self.area_cuadrado)

    def mostrar_resultado(self, figura: str, area: float) -> None:
        """
        Muestra un cuadro de diálogo con el resultado del área calculada.

        :param figura: Nombre de la figura geométrica.
        :param area: Área calculada como número decimal.
        """
        mensaje = f"El área del {figura} es: {area:.2f}"
        QMessageBox.information(self, "Resultado", mensaje)

    def solicitar_valor(self, mensaje: str) -> float:
        """
        Solicita al usuario un valor numérico positivo.

        :param mensaje: Texto descriptivo para el valor requerido.
        :return: Valor ingresado por el usuario o None si se cancela.
        """
        while True:
            valor, confirmado = QInputDialog.getDouble(
                self,
                "Entrada de datos",
                mensaje,
                decimals=2
            )

            if not confirmado:
                return None

            if valor <= 0:
                QMessageBox.warning(
                    self,
                    "Valor inválido",
                    "Por favor ingrese un número positivo mayor que cero."
                )
            else:
                return valor

    def area_circulo(self):
        """
        Calcula el área de un círculo usando el radio ingresado por el usuario.
        """
        radio = self.solicitar_valor("Ingrese el radio del círculo:")
        if radio is not None:
            area = math.pi * radio ** 2
            self.mostrar_resultado("círculo", area)

    def area_triangulo(self):
        """
        Calcula el área de un triángulo a partir de base y altura.
        """
        base = self.solicitar_valor("Ingrese la base del triángulo:")
        altura = self.solicitar_valor("Ingrese la altura del triángulo:")
        if base is not None and altura is not None:
            area = 0.5 * base * altura
            self.mostrar_resultado("triángulo", area)

    def area_rectangulo(self):
        """
        Calcula el área de un rectángulo a partir de base y altura.
        """
        base = self.solicitar_valor("Ingrese la base del rectángulo:")
        altura = self.solicitar_valor("Ingrese la altura del rectángulo:")
        if base is not None and altura is not None:
            area = base * altura
            self.mostrar_resultado("rectángulo", area)

    def area_cuadrado(self):
        """
        Calcula el área de un cuadrado a partir de su lado.
        """
        lado = self.solicitar_valor("Ingrese el lado del cuadrado:")
        if lado is not None:
            area = lado ** 2
            self.mostrar_resultado("cuadrado", area)


def main():
    """
    Punto de entrada de la aplicación.
    Crea y ejecuta la ventana principal.
    """
    app = QApplication(sys.argv)
    ventana = AreaCalculator()
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
