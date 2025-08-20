import sys, math
# Libreria de Pyside6 para usar Qt
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class Calculadora(QWidget):
    """
    Clase principal de la calculadora gráfica.

    Hereda de QWidget y proporciona una interfaz gráfica
    para realizar operaciones matemáticas básicas 
    (suma, resta, multiplicación, división, potencia, 
    módulo, factorial, raíz cuadrada) y conversiones
    entre sistemas numéricos (decimal, binario, octal, hexadecimal).

    Attributes:
        txtDisplay (QLineEdit): Campo de texto donde se ingresan los números.

    Methods:
        entrada_datos(tipo: str): Agrega los numeros a la pantalla de la calculadora.
    """

    def __init__(self):
        super().__init__() # Inicializador

        # ---------- Configuraciones basicas para la ventana ----------

        self.setWindowTitle("Calculadora - Modulo 1")
        self.setGeometry(200, 200, 400, 400) # Los valores son: pos_x, pos_y, ancho, alto

        # Establece el maximo tamaño para la ventana.
        self.setFixedSize(400, 400) # Ancho y alto

        # Estilo de la ventana: Ventana Blanco, Letras Negro.
        self.setStyleSheet(
            "background-color: white;" \
            "color: black;" \
            "font-weight: bold;"
            )

        # Entrada de texto
        self.txtDisplay = QLineEdit(self)
        # Establecemos como falso la entrada de texto
        self.txtDisplay.setDisabled(True)
        self.txtDisplay.setFixedSize(380, 50)

        # Establecemos la fuente de la pantalla donde se mostraran los numeros, sera diferente de las demas en la calculadora.
        txt_diplay_font = QFont("Arial", 24)
        self.txtDisplay.setFont(txt_diplay_font)
        # Ajustamos la alineacion del texto a la derecha
        self.txtDisplay.setAlignment(Qt.AlignmentFlag.AlignRight)


        # ---------- Botones de Calculadora ----------

        # ---------- Resultados ----------

        label_hex = QLabel("Hex: ")
        label_dec = QLabel("Dec: ")
        label_oct = QLabel("Oct: ")
        label_bin = QLabel("Bin: ")

        # ---------- Fila 1 ----------

        btn_a = QPushButton("A")
        btn_factorial = QPushButton("n!")
        btn_porcentaje = QPushButton("%")
        btn_ce = QPushButton("C")
        btn_ce.clicked.connect(lambda: self.entrada_datos("clear"))
        btn_retroceso = QPushButton("←")
        btn_retroceso.clicked.connect(lambda: self.entrada_datos("←"))
        

        # ---------- Fila 2 ----------

        btn_b = QPushButton("B")
        btn_log = QPushButton("Log")
        btn_sqrt = QPushButton("√")
        btn_potencia = QPushButton("X" + "\u02b8") # Utilizo unicode para la y en superíndice.
        btn_division = QPushButton("/")


        # ---------- Fila 3 ----------

        btn_c = QPushButton("C")
        btn_7 = QPushButton("7")
        btn_7.clicked.connect(lambda: self.entrada_datos("7"))
        btn_8 = QPushButton("8")
        btn_8.clicked.connect(lambda: self.entrada_datos("8"))
        btn_9 = QPushButton("9")
        btn_9.clicked.connect(lambda: self.entrada_datos("9"))
        btn_multiplicacion = QPushButton("*")


        # ---------- Fila 4 ----------

        btn_d = QPushButton("D")
        btn_4 = QPushButton("4")
        btn_4.clicked.connect(lambda: self.entrada_datos("4"))
        btn_5 = QPushButton("5")
        btn_5.clicked.connect(lambda: self.entrada_datos("5"))
        btn_6 = QPushButton("6")
        btn_6.clicked.connect(lambda: self.entrada_datos("6"))
        btn_resta = QPushButton("-")


        # ---------- Fila 5 ----------

        btn_e = QPushButton("E")
        btn_1 = QPushButton("1")
        btn_1.clicked.connect(lambda: self.entrada_datos("1"))
        btn_2 = QPushButton("2")
        btn_2.clicked.connect(lambda: self.entrada_datos("2"))
        btn_3 = QPushButton("3")
        btn_3.clicked.connect(lambda: self.entrada_datos("3"))
        btn_suma = QPushButton("+")
        

        # ---------- Fila 5 ----------

        btn_f = QPushButton("F")
        btn_mas_igual = QPushButton("+/=")
        btn_0 = QPushButton("0")
        btn_0.clicked.connect(lambda: self.entrada_datos("0"))
        btn_decimal = QPushButton(".")
        btn_igual = QPushButton("=")





        # ---------- Layouts ----------

        # Display Resultado (Display)
        layout = QVBoxLayout()
        layout.addWidget(self.txtDisplay)


        # Resultados Hex, Dec, etc...
        resultados = QVBoxLayout()
        resultados.addWidget(label_hex)
        resultados.addWidget(label_dec)
        resultados.addWidget(label_oct)
        resultados.addWidget(label_bin)
        layout.addLayout(resultados)
        
        
        # Fila 1
        fila_1 = QHBoxLayout()
        fila_1.addWidget(btn_a)
        fila_1.addWidget(btn_factorial)
        fila_1.addWidget(btn_porcentaje)
        fila_1.addWidget(btn_ce)
        fila_1.addWidget(btn_retroceso)
        layout.addLayout(fila_1)


        # Fila 2
        fila_2 = QHBoxLayout()
        fila_2.addWidget(btn_b)
        fila_2.addWidget(btn_log)
        fila_2.addWidget(btn_sqrt)
        fila_2.addWidget(btn_potencia)
        fila_2.addWidget(btn_division)
        layout.addLayout(fila_2)


        # Fila 3
        fila_3 = QHBoxLayout()
        fila_3.addWidget(btn_c)
        fila_3.addWidget(btn_7)
        fila_3.addWidget(btn_8)
        fila_3.addWidget(btn_9)
        fila_3.addWidget(btn_multiplicacion)
        layout.addLayout(fila_3)


        # Fila 4
        fila_4 = QHBoxLayout()
        fila_4.addWidget(btn_d)
        fila_4.addWidget(btn_4)
        fila_4.addWidget(btn_5)
        fila_4.addWidget(btn_6)
        fila_4.addWidget(btn_resta)
        layout.addLayout(fila_4)


        # Fila 5
        fila_5 = QHBoxLayout()
        fila_5.addWidget(btn_e)
        fila_5.addWidget(btn_1)
        fila_5.addWidget(btn_2)
        fila_5.addWidget(btn_3)
        fila_5.addWidget(btn_suma)
        layout.addLayout(fila_5)


        # Fila 6
        fila_6 = QHBoxLayout()
        fila_6.addWidget(btn_f)
        fila_6.addWidget(btn_mas_igual)
        fila_6.addWidget(btn_0)
        fila_6.addWidget(btn_decimal)
        fila_6.addWidget(btn_igual)
        layout.addLayout(fila_6)


        # Se renderiza todo el Layout
        self.setLayout(layout)

    
    def entrada_datos(self, tipo: str):
        """
        Funcion de la clase Calculadora que toma los caracteres de los botones y los muestra en pantalla.

        Args:
            tipo (str): Tipo de operación a realizar. Valores válidos:
                - "clear": Limpia todos los caracteres de la pantalla.
                - "←": Limpia el ultimo caracter de la pantalla.
                - "1, 2, 3...": Escribe los numeros decimales en pantalla.

        Raises:
            ValueError: Si la entrada no es válida o no es numérica o parte de la calculadora.
        """

        new_stack = ""
        text_stack = self.txtDisplay.text()

        try:
            if tipo == "clear":
                new_stack = ""
            elif tipo == "←":
                new_stack = text_stack[:-1] # Quitamos el ultimo carcarter de la cadena. 

            else:
                new_stack = text_stack + tipo
            
            self.txtDisplay.setText(new_stack)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Entrada inválida.\n{e}")


# ---------- Punto de Entrada ----------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec())
