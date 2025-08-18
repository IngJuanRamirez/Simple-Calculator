import sys, math
# Libreria de Pyside6 para usar Qt
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox


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
        lblResultado (QLabel): Etiqueta donde se muestra el resultado.

    Methods:
        operacion(tipo: str): Ejecuta operaciones matemáticas básicas.
        conversion(tipo: str): Convierte entre sistemas numéricos.
    """

    def __init__(self):
        super().__init__() # Inicializador

        # ---------- Configuraciones basicas para la ventana ----------

        self.setWindowTitle("Calculadora - Modulo 1 / Clase 2")
        self.setGeometry(200, 200, 400, 400)
        self.resize

        # Establece el maximo tamaño para la ventana.
        self.setFixedSize(400, 400)

        # Estilo de la ventana: Ventana Blanco, Letras Negro.
        self.setStyleSheet(
            "background-color: white;" \
            "color: black;"
            )

        # Entrada de texto
        self.txtDisplay = QLineEdit(self)

        # Etiqueta de resultados
        self.lblResultado = QLabel("Resultado:", self)




        # ---------- Botones de operaciones básicas ----------

        # Suma
        btnSuma = QPushButton("+")
        btnSuma.clicked.connect(lambda: self.operacion("suma"))

        # Resta
        btnResta = QPushButton("-")
        btnResta.clicked.connect(lambda: self.operacion("resta"))

        # Multipliacion
        btnMult = QPushButton("*")
        btnMult.clicked.connect(lambda: self.operacion("mult"))

        # Division
        btnDiv = QPushButton("/")
        btnDiv.clicked.connect(lambda: self.operacion("div"))

        # Potencia
        btnPot = QPushButton("^")
        btnPot.clicked.connect(lambda: self.operacion("pot"))

        # Modo %
        btnMod = QPushButton("%")
        btnMod.clicked.connect(lambda: self.operacion("mod"))

        # Factorial
        btnFact = QPushButton("n!")
        btnFact.clicked.connect(lambda: self.operacion("fact"))

        # Raiz
        btnSqrt = QPushButton("√")
        btnSqrt.clicked.connect(lambda: self.operacion("sqrt"))




        # ---------- Botones de conversiones ----------

        # Defimal a binario
        btnDecBin = QPushButton("Dec → Bin")
        btnDecBin.clicked.connect(lambda: self.conversion("dec-bin"))

        # Decimal a Octal
        btnDecOct = QPushButton("Dec → Oct")
        btnDecOct.clicked.connect(lambda: self.conversion("dec-oct"))

        # Decimal a Hexadecimal
        btnDecHex = QPushButton("Dec → Hex")
        btnDecHex.clicked.connect(lambda: self.conversion("dec-hex"))

        # Binario a Decimal
        btnBinDec = QPushButton("Bin → Dec")
        btnBinDec.clicked.connect(lambda: self.conversion("bin-dec"))

        # Octal a Decimal
        btnOctDec = QPushButton("Oct → Dec")
        btnOctDec.clicked.connect(lambda: self.conversion("oct-dec"))

        # Hexadecimal a Decimal
        btnHexDec = QPushButton("Hex → Dec")
        btnHexDec.clicked.connect(lambda: self.conversion("hex-dec"))




        # ---------- Layouts ----------

        # Display Resultado (Tanto el Label como el Display)
        layout = QVBoxLayout()
        layout.addWidget(self.txtDisplay)
        layout.addWidget(self.lblResultado)

        # Botones de las operaciones en una fila
        fila1 = QHBoxLayout()
        fila1.addWidget(btnSuma)
        fila1.addWidget(btnResta)
        fila1.addWidget(btnMult)
        fila1.addWidget(btnDiv)
        layout.addLayout(fila1)

        # Botones de Transformacion en otra fila
        fila2 = QHBoxLayout()
        fila2.addWidget(btnPot)
        fila2.addWidget(btnMod)
        fila2.addWidget(btnFact)
        fila2.addWidget(btnSqrt)
        layout.addLayout(fila2)

        # Botones de Conversion en otra fila
        fila3 = QHBoxLayout()
        fila3.addWidget(btnDecBin)
        fila3.addWidget(btnDecOct)
        fila3.addWidget(btnDecHex)
        layout.addLayout(fila3)

        fila4 = QHBoxLayout()
        fila4.addWidget(btnBinDec)
        fila4.addWidget(btnOctDec)
        fila4.addWidget(btnHexDec)
        layout.addLayout(fila4)

        # Se renderiza todo el Layout
        self.setLayout(layout)

    

    # ---------- Funciones de la Clase ----------

    def operacion(self, tipo: str):
        """
        Ejecuta una operación matemática según el tipo especificado.
        Toma los números desde el campo de texto `txtDisplay`, 
        interpreta la entrada y aplica la operación solicitada 
        (suma, resta, multiplicación, división, potencia, módulo, 
        factorial o raíz cuadrada). El resultado se muestra en la 
        interfaz gráfica.
        
        Args:
            tipo (str): Tipo de operación a realizar. Valores válidos:
                - "suma": suma dos números.
                - "resta": resta dos números.
                - "mult": multiplica dos números.
                - "div": divide dos números (lanza error si divisor = 0).
                - "pot": potencia (a ** b).
                - "mod": módulo (a % b).
                - "fact": factorial de un número.
                - "sqrt": raíz cuadrada.
        
        Raises:
            ZeroDivisionError: Si se intenta dividir entre cero.
            ValueError: Si la entrada no es válida o no es numérica.
        
        Returns:
            None: El resultado se muestra en `lblResultado` y en `txtDisplay`.
        """

        try:
            expr = self.txtDisplay.text()
            if tipo == "suma":
                a, b = map(float, expr.split())
                res = a + b
            elif tipo == "resta":
                a, b = map(float, expr.split())
                res = a - b
            elif tipo == "mult":
                a, b = map(float, expr.split())
                res = a * b
            elif tipo == "div":
                a, b = map(float, expr.split())
                if b == 0:
                    raise ZeroDivisionError
                res = a / b
            elif tipo == "pot":
                a, b = map(float, expr.split())
                res = a ** b
            elif tipo == "mod":
                a, b = map(int, expr.split())
                res = a % b
            elif tipo == "fact":
                a = int(expr)
                res = math.factorial(a)
            elif tipo == "sqrt":
                a = float(expr)
                res = math.sqrt(a)
            else:
                res = "Error"

            self.lblResultado.setText(f"Resultado: {res}")
            self.txtDisplay.setText(str(res))

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Entrada inválida.\n{e}")




    def conversion(self, tipo: str):
        """
        Realiza conversiones numéricas entre sistemas de numeración.

        Toma el número ingresado en el cuadro de texto `txtDisplay` y lo 
        convierte al sistema solicitado (binario, octal, hexadecimal o decimal). 
        El resultado se muestra en la interfaz gráfica.

        Args:
            tipo (str): Tipo de conversión a realizar. Valores válidos:
                - "dec-bin": decimal a binario.
                - "dec-oct": decimal a octal.
                - "dec-hex": decimal a hexadecimal.
                - "bin-dec": binario a decimal.
                - "oct-dec": octal a decimal.
                - "hex-dec": hexadecimal a decimal.

        Raises:
            ValueError: Si el número ingresado no corresponde al sistema
            de numeración esperado o no puede convertirse.

        Returns:
            None: El resultado se muestra en `lblResultado` y en `txtDisplay`.
        """

        try:
            expr = self.txtDisplay.text()
            if tipo == "dec-bin":
                n = int(expr)
                res = bin(n)
            elif tipo == "dec-oct":
                n = int(expr)
                res = oct(n)
            elif tipo == "dec-hex":
                n = int(expr)
                res = hex(n)
            elif tipo == "bin-dec":
                res = int(expr, 2)
            elif tipo == "oct-dec":
                res = int(expr, 8)
            elif tipo == "hex-dec":
                res = int(expr, 16)
            else:
                res = "Error"

            self.lblResultado.setText(f"Resultado: {res}")
            self.txtDisplay.setText(str(res))

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Conversión inválida.\n{e}")



# ---------- Punto de Entrada ----------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec())
