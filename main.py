import sys, math
# Libreria de Pyside6 para usar Qt
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtCore import Qt
from functools import partial

# ===================================================================
# CLASE 1: LA FÁBRICA DE LA INTERFAZ (UI)
# Su único trabajo es crear y posicionar los widgets.
# ===================================================================
class UI_Calculator:
    def __init__(self, ventana_principal: QWidget):
        """
        Constructor que recibe la ventana principal (el "chasis")
        para construir la interfaz dentro de ella.
        """
        # --- Creación de todos los widgets (piezas) ---
        self.txtDisplay = QLineEdit("0", ventana_principal)
        self.display_hex = QLineEdit(ventana_principal)
        self.display_dec = QLineEdit(ventana_principal)
        self.display_oct = QLineEdit(ventana_principal)
        self.display_bin = QLineEdit(ventana_principal)
        self.btn_hex = QPushButton("Hex")
        self.btn_dec = QPushButton("Dec")
        self.btn_oct = QPushButton("Oct")
        self.btn_bin = QPushButton("Bin")
        self.btn_a = QPushButton("A")
        self.btn_b = QPushButton("B")
        self.btn_c = QPushButton("C")
        self.btn_d = QPushButton("D")
        self.btn_e = QPushButton("E")
        self.btn_f = QPushButton("F")
        self.btn_0 = QPushButton("0")
        self.btn_1 = QPushButton("1")
        self.btn_2 = QPushButton("2")
        self.btn_3 = QPushButton("3")
        self.btn_4 = QPushButton("4")
        self.btn_5 = QPushButton("5")
        self.btn_6 = QPushButton("6")
        self.btn_7 = QPushButton("7")
        self.btn_8 = QPushButton("8")
        self.btn_9 = QPushButton("9")
        self.btn_decimal = QPushButton(".")
        self.btn_igual = QPushButton("=")
        self.btn_suma = QPushButton("+")
        self.btn_resta = QPushButton("-")
        self.btn_multiplicacion = QPushButton("*")
        self.btn_division = QPushButton("/")
        self.btn_potencia = QPushButton("xʸ")
        self.btn_porcentaje = QPushButton("%")
        self.btn_sqrt = QPushButton("√")
        self.btn_log = QPushButton("Log")
        self.btn_factorial = QPushButton("n!")
        self.btn_ce = QPushButton("C")
        self.btn_retroceso = QPushButton("←")
        self.btn_mas_menos = QPushButton("+/-")

        # --- Agrupación de botones ---
        self.botones_digitos = {
            '0': self.btn_0, '1': self.btn_1, '2': self.btn_2, '3': self.btn_3, '4': self.btn_4,
            '5': self.btn_5, '6': self.btn_6, '7': self.btn_7, '8': self.btn_8, '9': self.btn_9,
            'A': self.btn_a, 'B': self.btn_b, 'C': self.btn_c, 'D': self.btn_d, 'E': self.btn_e, 'F': self.btn_f,
            '.': self.btn_decimal
        }

        # --- Estilos y configuración de widgets ---
        font_id = QFontDatabase.addApplicationFont("src/fonts/digital-7/digital-7 (mono).ttf")
        if font_id != -1:
            family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.txtDisplay.setFont(QFont(family, 28))
        else:
            self.txtDisplay.setFont(QFont("Arial", 24))
            print("Error: No se pudo cargar la fuente.")


        self.txtDisplay.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.txtDisplay.setDisabled(True)
        self.txtDisplay.setFixedSize(380, 50)

        ventana_principal.setStyleSheet(
            "background-color: white;" \
            "color: black;" \
            "font-weight: bold;"
            )

        for btn in [self.btn_hex, self.btn_dec, self.btn_oct, self.btn_bin]:
            btn.setStyleSheet("background-color: #a7c957; color: black;")
        for btn in [self.btn_ce, self.btn_retroceso]:
            btn.setStyleSheet("background-color: #e56b6f; color: black;")

        # --- Organización en Layouts ---
        # 1. Crear UN layout principal que contendrá todo
        main_layout = QVBoxLayout()

        # 2. Añadir el display principal
        main_layout.addWidget(self.txtDisplay)
        
        # 3. Crear el layout para los displays de conversión y añadirlo
        displays_layout = QVBoxLayout()
        for btn, display in [(self.btn_hex, self.display_hex), (self.btn_dec, self.display_dec), (self.btn_oct, self.display_oct), (self.btn_bin, self.display_bin)]:
            row = QHBoxLayout()
            row.addWidget(btn)
            row.addWidget(display)
            display.setDisabled(True)
            display.setStyleSheet("border: none; color: #555;")
            displays_layout.addLayout(row)
        main_layout.addLayout(displays_layout)

        # 4. Crear la parrilla de botones y añadirla
        grid_layout_config = [
            [self.btn_a, self.btn_factorial, self.btn_porcentaje, self.btn_ce, self.btn_retroceso],
            [self.btn_b, self.btn_log, self.btn_sqrt, self.btn_potencia, self.btn_division],
            [self.btn_c, self.btn_7, self.btn_8, self.btn_9, self.btn_multiplicacion],
            [self.btn_d, self.btn_4, self.btn_5, self.btn_6, self.btn_resta],
            [self.btn_e, self.btn_1, self.btn_2, self.btn_3, self.btn_suma],
            [self.btn_f, self.btn_mas_menos, self.btn_0, self.btn_decimal, self.btn_igual]
        ]
        for row_widgets in grid_layout_config:
            row_layout = QHBoxLayout()
            for widget in row_widgets:
                row_layout.addWidget(widget)
            main_layout.addLayout(row_layout)
        
        # 5. Establecer el layout principal en la ventana
        ventana_principal.setLayout(main_layout)

    # Agragado como quality of life.
    def change_mod_color(self, select_mode : str, values : str) -> None:
        # Regresar cualquier cambio al original
        for btn in [self.btn_hex, self.btn_dec, self.btn_oct, self.btn_bin]:
            btn.setStyleSheet("background-color: #a7c957; color: black;")

        #actualizamos los botones de dígitos.
        for digito, boton in self.botones_digitos.items():
            if digito in values:
                # Si el botón es válido, limpia su estilo para que
                # herede el estilo por defecto de la ventana.
                boton.setStyleSheet("")
            else:
                # Si no es válido, lo ponemos gris para que parezca deshabilitado.
                boton.setStyleSheet("background-color: #D1D1D1; color: #black;")


        # Cambio de color en el boton de modo
        if select_mode == "Dec":
            self.btn_dec.setStyleSheet("background-color: blue;")
        elif select_mode == "Bin":
            self.btn_bin.setStyleSheet("background-color: blue;")
        elif select_mode == "Hex":
            self.btn_hex.setStyleSheet("background-color: blue;")
        elif select_mode == "Oct":
            self.btn_oct.setStyleSheet("background-color: blue;")



# ===================================================================
# CLASE 2: EL INGENIERO / CONTROLADOR
# Contiene la lógica, el estado y conecta los cables.
# ===================================================================
class Calculadora(QWidget):
    def __init__(self):
        super().__init__()

        # --- Configuraciones de la Ventana (el "chasis") ---
        self.setWindowTitle("Calculadora Modular")
        self.setGeometry(200, 200, 400, 400)
        self.setFixedSize(400, 400)

        # --- Lógica y Estado de la Calculadora ---
        self.primer_numero = None
        self.operador_actual = ""
        self.esperando_segundo_numero = False
        self.mode = "Dec"

        # --- El Ingeniero le pide a la Fábrica que construya la UI ---
        self.ui = UI_Calculator(self)

        # --- El Ingeniero conecta los cables ---
        self._conectar_senales()
        
        # --- Establece el estado inicial de la UI ---
        self.cambiar_modo(self.mode)




    ###### Funciones de la calculadora #####
    def _conectar_senales(self):
        """Conecta todos los widgets de la UI a los métodos de esta clase usando partial."""
        # Conexión de dígitos y letras
        for digito, boton in self.ui.botones_digitos.items():
            boton.clicked.connect(partial(self.entrada_datos, digito))

        # Conexiones de operadores y funciones
        self.ui.btn_igual.clicked.connect(partial(self.entrada_datos, "="))
        self.ui.btn_suma.clicked.connect(partial(self.entrada_datos, "+"))
        self.ui.btn_resta.clicked.connect(partial(self.entrada_datos, "-"))
        self.ui.btn_multiplicacion.clicked.connect(partial(self.entrada_datos, "*"))
        self.ui.btn_division.clicked.connect(partial(self.entrada_datos, "/"))
        self.ui.btn_potencia.clicked.connect(partial(self.entrada_datos, "**"))
        self.ui.btn_porcentaje.clicked.connect(partial(self.entrada_datos, "%"))
        self.ui.btn_sqrt.clicked.connect(partial(self.entrada_datos, "sqrt"))
        self.ui.btn_log.clicked.connect(partial(self.entrada_datos, "log"))
        self.ui.btn_factorial.clicked.connect(partial(self.entrada_datos, "factorial"))
        self.ui.btn_ce.clicked.connect(partial(self.entrada_datos, "clear"))
        self.ui.btn_retroceso.clicked.connect(partial(self.entrada_datos, "back"))
        
        # Conexiones de modos
        self.ui.btn_hex.clicked.connect(partial(self.cambiar_modo, "Hex"))
        self.ui.btn_dec.clicked.connect(partial(self.cambiar_modo, "Dec"))
        self.ui.btn_oct.clicked.connect(partial(self.cambiar_modo, "Oct"))
        self.ui.btn_bin.clicked.connect(partial(self.cambiar_modo, "Bin"))

    def cambiar_modo(self, nuevo_modo: str):
        self.mode = nuevo_modo

        if nuevo_modo == "Bin": digitos_validos = "01"
        elif nuevo_modo == "Oct": digitos_validos = "01234567"
        elif nuevo_modo == "Hex": digitos_validos = "0123456789ABCDEF"
        else: digitos_validos = "0123456789."

        for digito, boton in self.ui.botones_digitos.items():
            boton.setEnabled(digito in digitos_validos)
        
        valor_decimal = self.ui.display_dec.text() if self.ui.display_dec.text() else "0"
        self.ui.txtDisplay.setText(self.conversor(valor_decimal, self.mode))

        self.ui.change_mod_color(self.mode, digitos_validos)

    def entrada_datos(self, valor: str):
        """Gestiona toda la entrada de datos y la lógica de cálculo."""
        OPERADORES_BINARIOS = ["+", "-", "*", "/", "**", "%"]
        OPERADORES_UNARIOS = ["sqrt", "factorial", "log"]
        DIGITOS_Y_LETRAS = "0123456789ABCDEF"
        
        try:
            if valor in DIGITOS_Y_LETRAS or valor == ".":
                if self.esperando_segundo_numero:
                    self.ui.txtDisplay.setText(valor)
                    self.esperando_segundo_numero = False
                else:
                    current_text = self.ui.txtDisplay.text()
                    if valor == "." and "." in current_text: return
                    self.ui.txtDisplay.setText(valor if current_text == "0" and valor != "." else current_text + valor)
            
            elif valor in OPERADORES_UNARIOS:
                # --- CORRECCIÓN ---
                # Lee como float en modo Dec, o convierte desde la base en otros modos.
                numero_decimal = 0.0
                if self.mode == "Dec":
                    numero_decimal = float(self.ui.txtDisplay.text())
                else:
                    base = {"Hex": 16, "Oct": 8, "Bin": 2}[self.mode]
                    numero_decimal = float(int(self.ui.txtDisplay.text(), base))
                
                resultado = 0.0
                if valor == "sqrt":
                    if numero_decimal < 0: raise ValueError("Raíz de negativo no válida")
                    resultado = math.sqrt(numero_decimal)
                elif valor == "factorial":
                    if numero_decimal < 0 or numero_decimal != int(numero_decimal): raise ValueError("Factorial no entero o negativo")
                    resultado = float(math.factorial(int(numero_decimal)))
                elif valor == "log":
                    if numero_decimal <= 0: raise ValueError("Logaritmo no positivo")
                    resultado = math.log10(numero_decimal)
                
                self._actualizar_displays(resultado)
                self.esperando_segundo_numero = True

            elif valor in OPERADORES_BINARIOS:
                if self.primer_numero is not None and not self.esperando_segundo_numero:
                    self.entrada_datos("=")
                
                # --- CORRECCIÓN ---
                numero_a_guardar = 0.0
                if self.mode == "Dec":
                    numero_a_guardar = float(self.ui.txtDisplay.text())
                else:
                    base = {"Hex": 16, "Oct": 8, "Bin": 2}[self.mode]
                    numero_a_guardar = float(int(self.ui.txtDisplay.text(), base))
                self.primer_numero = numero_a_guardar
                
                self.operador_actual = valor
                self.esperando_segundo_numero = True

            elif valor == "=":
                if self.operador_actual and self.primer_numero is not None:
                    # --- CORRECCIÓN ---
                    segundo_numero = 0.0
                    if self.mode == "Dec":
                        segundo_numero = float(self.ui.txtDisplay.text())
                    else:
                        base = {"Hex": 16, "Oct": 8, "Bin": 2}[self.mode]
                        segundo_numero = float(int(self.ui.txtDisplay.text(), base))

                    resultado = 0.0
                    if self.operador_actual == "+": resultado = self.primer_numero + segundo_numero
                    elif self.operador_actual == "-": resultado = self.primer_numero - segundo_numero
                    elif self.operador_actual == "*": resultado = self.primer_numero * segundo_numero
                    elif self.operador_actual == "**": resultado = self.primer_numero ** segundo_numero
                    elif self.operador_actual == "%": resultado = self.primer_numero % segundo_numero
                    elif self.operador_actual == "/":
                        if segundo_numero == 0: raise ZeroDivisionError("División por cero")
                        resultado = self.primer_numero / segundo_numero
                    
                    self._actualizar_displays(resultado)
                    self.primer_numero = None
                    self.operador_actual = ""
                    self.esperando_segundo_numero = True

            elif valor == "clear":
                self.ui.txtDisplay.setText("0")
                for display in [self.ui.display_bin, self.ui.display_hex, self.ui.display_oct, self.ui.display_dec]: display.clear()
                self.primer_numero = None
                self.operador_actual = ""
                self.esperando_segundo_numero = False

            elif valor == "back":
                texto_actual = self.ui.txtDisplay.text()
                nuevo_texto = texto_actual[:-1]
                self.ui.txtDisplay.setText(nuevo_texto if nuevo_texto else "0")

        except Exception as e:
            QMessageBox.critical(self, "Error de Cálculo", str(e))
            self.entrada_datos("clear")

    def _actualizar_displays(self, resultado_numerico: float):
        numero_entero_str = str(int(resultado_numerico))
        
        texto_display_principal = self.conversor(numero_entero_str, self.mode)
        
        if not resultado_numerico.is_integer() and self.mode == "Dec":
            self.ui.txtDisplay.setText(f"{resultado_numerico:.10g}")
        else:
            self.ui.txtDisplay.setText(texto_display_principal)

        self.ui.display_bin.setText(self.conversor(numero_entero_str, "bin"))
        self.ui.display_hex.setText(self.conversor(numero_entero_str, "hex"))
        self.ui.display_oct.setText(self.conversor(numero_entero_str, "oct"))
        self.ui.display_dec.setText(numero_entero_str)

    def conversor(self, number_str: str, tipo: str) -> str:
        try:
            decimal = int(number_str)
        except (ValueError, TypeError): return "Error"

        tipo = tipo.lower()

        if decimal == 0: return "0"
        if tipo == "dec": return str(decimal)
        base_map = {"bin": 2, "oct": 8, "hex": 16}
        if tipo not in base_map: return "Tipo no válido"
        base = base_map[tipo]
        mapa_hex = "0123456789ABCDEF"
        resultado_str = ""
        num_temp = decimal
        while num_temp > 0:
            residuo = num_temp % base
            resultado_str = mapa_hex[residuo] + resultado_str
            num_temp //= base
        return resultado_str


# ---------- Punto de Entrada de la Aplicación ----------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec())