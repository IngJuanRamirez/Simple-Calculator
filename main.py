import sys, math
# Libreria de Pyside6 para usar Qt
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
from PySide6.QtGui import QFont, QFontDatabase
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

        # Cargar la fuente desde la ruta específica
        font_id = QFontDatabase.addApplicationFont("src/fonts/digital-7/digital-7 (mono).ttf")
        
        # Verificar si la fuente se cargó correctamente
        if font_id != -1:
            family = QFontDatabase.applicationFontFamilies(font_id)[0]
            # Establecer la fuente para el display
            txt_display_font = QFont(family, 24)
            self.txtDisplay = QLineEdit(self)
            self.txtDisplay.setFont(txt_display_font)
        else:
            # Si no se pudo cargar, usar una fuente predeterminada
            self.txtDisplay = QLineEdit(self)
            self.txtDisplay.setFont(QFont("Arial", 24))
            print("Error: No se pudo cargar la fuente desde la ruta especificada.")
        
        self.txtDisplay.setAlignment(Qt.AlignmentFlag.AlignRight)
        # Establecemos como falso la entrada de texto
        self.txtDisplay.setDisabled(True)
        self.txtDisplay.setFixedSize(380, 50)

        self.primer_numero = None
        self.operador_actual = ""
        self.esperando_segundo_numero = False

        # ---------- Botones de Calculadora ----------

        # ---------- Resultados ----------

        label_hex = QLabel("Hex: ")
        label_dec = QLabel("Dec: ")
        label_oct = QLabel("Oct: ")
        label_bin = QLabel("Bin: ")
        
        # Display Bin
        self.display_bin = QLineEdit(self)
        self.display_bin.setDisabled(True)
        self.display_bin.setStyleSheet("border: none;")
        
        # Display Hex
        self.display_hex = QLineEdit(self)
        self.display_hex.setDisabled(True)
        self.display_hex.setStyleSheet("border: none;")

        # Display Oct
        self.display_oct = QLineEdit(self)
        self.display_oct.setDisabled(True)
        self.display_oct.setStyleSheet("border: none;")

        # Display Dec
        self.display_dec = QLineEdit(self)
        self.display_dec.setDisabled(True)
        self.display_dec.setStyleSheet("border: none;")

        # ---------- Fila 1 ----------

        btn_a = QPushButton("A")
        btn_factorial = QPushButton("n!")
        btn_factorial.clicked.connect(lambda: self.entrada_datos("factorial"))
        btn_porcentaje = QPushButton("%")
        btn_ce = QPushButton("C")
        btn_retroceso = QPushButton("←")

        # Un color rojo para los botones de borrado.
        btn_ce.setStyleSheet("background-color: red; color: black;")
        btn_retroceso.setStyleSheet("background-color: red; color: black;")

        btn_ce.clicked.connect(lambda: self.entrada_datos("clear"))
        btn_retroceso.clicked.connect(lambda: self.entrada_datos("back"))
        

        # ---------- Fila 2 ----------

        btn_b = QPushButton("B")
        btn_log = QPushButton("Log")
        btn_log.clicked.connect(lambda: self.entrada_datos("log"))
        btn_sqrt = QPushButton("√")
        btn_sqrt.clicked.connect(lambda: self.entrada_datos("sqrt"))
        btn_potencia = QPushButton("X" + "\u02b8") # Utilizo unicode para la y en superíndice.
        btn_potencia.clicked.connect(lambda: self.entrada_datos("**"))
        btn_division = QPushButton("/")
        btn_division.clicked.connect(lambda: self.entrada_datos("/"))


        # ---------- Fila 3 ----------

        btn_c = QPushButton("C")
        btn_7 = QPushButton("7")
        btn_7.clicked.connect(lambda: self.entrada_datos("7"))
        btn_8 = QPushButton("8")
        btn_8.clicked.connect(lambda: self.entrada_datos("8"))
        btn_9 = QPushButton("9")
        btn_9.clicked.connect(lambda: self.entrada_datos("9"))
        btn_multiplicacion = QPushButton("*")
        btn_multiplicacion.clicked.connect(lambda: self.entrada_datos("*"))


        # ---------- Fila 4 ----------

        btn_d = QPushButton("D")
        btn_4 = QPushButton("4")
        btn_4.clicked.connect(lambda: self.entrada_datos("4"))
        btn_5 = QPushButton("5")
        btn_5.clicked.connect(lambda: self.entrada_datos("5"))
        btn_6 = QPushButton("6")
        btn_6.clicked.connect(lambda: self.entrada_datos("6"))
        btn_resta = QPushButton("-")
        btn_resta.clicked.connect(lambda: self.entrada_datos("-"))


        # ---------- Fila 5 ----------

        btn_e = QPushButton("E")
        btn_1 = QPushButton("1")
        btn_1.clicked.connect(lambda: self.entrada_datos("1"))
        btn_2 = QPushButton("2")
        btn_2.clicked.connect(lambda: self.entrada_datos("2"))
        btn_3 = QPushButton("3")
        btn_3.clicked.connect(lambda: self.entrada_datos("3"))
        btn_suma = QPushButton("+")
        btn_suma.clicked.connect(lambda: self.entrada_datos("+"))
        

        # ---------- Fila 5 ----------

        btn_f = QPushButton("F")
        btn_mas_igual = QPushButton("+/=")
        btn_0 = QPushButton("0")
        btn_0.clicked.connect(lambda: self.entrada_datos("0"))
        btn_decimal = QPushButton(".")
        btn_decimal.clicked.connect(lambda: self.entrada_datos("."))
        btn_igual = QPushButton("=")
        btn_igual.clicked.connect(lambda: self.entrada_datos("="))




        # ---------- Layouts ----------

        # Display Resultado (Display)
        layout = QVBoxLayout()
        layout.addWidget(self.txtDisplay)


        # Resultados Hex, Dec, etc...
        resultados = QVBoxLayout()

        # Hex
        hex_result = QHBoxLayout()
        hex_result.addWidget(label_hex)
        hex_result.addWidget(self.display_hex)
        resultados.addLayout(hex_result)
        
        # Dec
        dec_result = QHBoxLayout()
        dec_result.addWidget(label_dec)
        dec_result.addWidget(self.display_dec)
        resultados.addLayout(dec_result)

        # Oct
        oct_result = QHBoxLayout()
        oct_result.addWidget(label_oct)
        oct_result.addWidget(self.display_oct)
        resultados.addLayout(oct_result)

        # Bin
        bin_result = QHBoxLayout()
        bin_result.addWidget(label_bin)
        bin_result.addWidget(self.display_bin)
        resultados.addLayout(bin_result)

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

    
    # Reemplaza tu función entrada_datos por completo con esta versión

    def entrada_datos(self, valor: str):
        """
        Gestiona la entrada de datos y la lógica de una calculadora estándar.
        """
        # Operadores que necesitan dos números (binarios)
        OPERADORES_BINARIOS = ["+", "-", "*", "/", "**", "%"]
        # Operadores que se aplican a un solo número (unarios)
        OPERADORES_UNARIOS = ["sqrt", "factorial", "log"]

        try:
            # --- Lógica para NÚMEROS (0-9) ---
            if valor.isdigit():
                if self.esperando_segundo_numero:
                    self.txtDisplay.setText(valor)
                    self.esperando_segundo_numero = False
                else:
                    if self.txtDisplay.text() == "0":
                        self.txtDisplay.setText(valor)
                    else:
                        self.txtDisplay.setText(self.txtDisplay.text() + valor)

            # --- Lógica para el PUNTO DECIMAL (.) ---
            elif valor == ".":
                if "." not in self.txtDisplay.text():
                    self.txtDisplay.setText(self.txtDisplay.text() + ".")
            
            # --- Lógica para OPERADORES UNARIOS (sqrt, factorial, etc.) ---
            elif valor in OPERADORES_UNARIOS:
                numero_actual = float(self.txtDisplay.text())
                resultado = 0.0

                if valor == "sqrt":
                    if numero_actual < 0:
                        QMessageBox.critical(self, "Error", "Entrada inválida para raíz cuadrada.")
                        return
                    resultado = math.sqrt(numero_actual)
                elif valor == "factorial":
                    if numero_actual < 0 or numero_actual != int(numero_actual):
                        QMessageBox.critical(self, "Error", "Entrada inválida para factorial.")
                        return
                    resultado = float(math.factorial(int(numero_actual)))
                elif valor == "log":
                    if numero_actual <= 0:
                        QMessageBox.critical(self, "Error", "Entrada inválida para logaritmo.")
                        return
                    resultado = math.log10(numero_actual)
                
                self._actualizar_displays(resultado)
                self.esperando_segundo_numero = True

            # --- Lógica para OPERADORES BINARIOS (+, -, *, /, **, %) ---
            elif valor in OPERADORES_BINARIOS:
                if self.primer_numero is not None and not self.esperando_segundo_numero:
                    self.entrada_datos("=")
                
                self.primer_numero = float(self.txtDisplay.text())
                self.operador_actual = valor
                self.esperando_segundo_numero = True

            # --- Lógica para el botón IGUAL (=) ---
            elif valor == "=":
                if self.operador_actual and self.primer_numero is not None:
                    segundo_numero = float(self.txtDisplay.text())
                    resultado = 0.0

                    if self.operador_actual == "+": resultado = self.primer_numero + segundo_numero
                    elif self.operador_actual == "-": resultado = self.primer_numero - segundo_numero
                    elif self.operador_actual == "*": resultado = self.primer_numero * segundo_numero
                    elif self.operador_actual == "**": resultado = self.primer_numero ** segundo_numero
                    elif self.operador_actual == "%": resultado = self.primer_numero % segundo_numero
                    elif self.operador_actual == "/":
                        if segundo_numero == 0:
                            QMessageBox.critical(self, "Error", "No se puede dividir por cero.")
                            return
                        resultado = self.primer_numero / segundo_numero
                    
                    self._actualizar_displays(resultado)
                    self.primer_numero = None
                    self.operador_actual = ""
                    self.esperando_segundo_numero = True

            # --- Lógica para LIMPIAR (C) ---
            elif valor == "clear":
                self.txtDisplay.setText("0")
                self.display_bin.clear()
                self.display_hex.clear()
                self.display_oct.clear()
                self.display_dec.clear()
                self.primer_numero = None
                self.operador_actual = ""
                self.esperando_segundo_numero = False

            # --- Lógica para RETROCESO (←) ---
            elif valor == "back":
                texto_actual = self.txtDisplay.text()
                nuevo_texto = texto_actual[:-1]
                self.txtDisplay.setText(nuevo_texto if nuevo_texto else "0")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error: {e}")
            self.entrada_datos("clear")

    # --- NUEVA FUNCIÓN AUXILIAR ---
    # Añade esta función dentro de tu clase Calculadora

    def _actualizar_displays(self, resultado_numerico: float):
        """Función auxiliar para actualizar todos los displays con un resultado."""
        # Muestra el resultado en el display principal
        if resultado_numerico.is_integer():
            self.txtDisplay.setText(str(int(resultado_numerico)))
        else:
            # Formateamos para evitar exceso de decimales
            self.txtDisplay.setText(f"{resultado_numerico:.10g}")

        # Actualiza los displays de conversión con la parte entera del resultado
        numero_entero_str = str(int(resultado_numerico))
        self.display_bin.setText(self.conversor(numero_entero_str, "bin"))
        self.display_hex.setText(self.conversor(numero_entero_str, "hex"))
        self.display_oct.setText(self.conversor(numero_entero_str, "oct"))
        self.display_dec.setText(self.conversor(numero_entero_str, "dec"))


    def conversor(self, number: str, tipo: str) -> str:
        """
        Convierte un número decimal (en formato string) a otro sistema numérico
        utilizando el algoritmo de división y residuo.
        
        Args:
            number (str): El número en base 10 para convertir.
            tipo (str): El sistema al que se convertirá ("bin", "oct", "hex", "dec").
            
        Returns:
            str: El número convertido en formato de cadena de texto.
        """
        try:
            decimal = int(number)
        except (ValueError, TypeError):
            return "Error"

        # Caso especial: si el número es 0, el resultado es "0" en cualquier base.
        if decimal == 0:
            return "0"

        # --- Conversión a Binario (Base 2) ---
        if tipo == "bin":
            resultado_str = ""
            num_temp = decimal
            while num_temp > 0:
                residuo = num_temp % 2
                resultado_str = str(residuo) + resultado_str
                num_temp //= 2  # División entera
            return resultado_str

        # --- Conversión a Octal (Base 8) ---
        elif tipo == "oct":
            resultado_str = ""
            num_temp = decimal
            while num_temp > 0:
                residuo = num_temp % 8
                resultado_str = str(residuo) + resultado_str
                num_temp //= 8
            return resultado_str

        # --- Conversión a Hexadecimal (Base 16) ---
        elif tipo == "hex":
            # Mapa para los dígitos mayores a 9 (A=10, B=11, etc.)
            mapa_hex = "0123456789ABCDEF"
            resultado_str = ""
            num_temp = decimal
            while num_temp > 0:
                residuo = num_temp % 16
                # Usamos el residuo como índice para obtener el caracter correcto
                resultado_str = mapa_hex[residuo] + resultado_str
                num_temp //= 16
            return resultado_str

        # --- Conversión a Decimal (Base 10) ---
        elif tipo == "dec":
            # No se necesita conversión, ya es un número decimal.
            return str(decimal)
        
        # --- Caso no válido ---
        else:
            return "Tipo no válido"
        

# ---------- Punto de Entrada ----------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec())
