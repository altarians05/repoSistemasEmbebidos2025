# Sistemas Embebidos en Raspberry Pi

## Descripción
Este repositorio contiene los códigos de Python desarrollados durante el curso de **Sistemas Embebidos** utilizando **Raspberry Pi**. 

Todos los ejemplos y proyectos se implementan mediante conexión SSH utilizando **PuTTY** para el desarrollo y ejecución remota en la Raspberry Pi.

## Tecnologías Utilizadas
- **Hardware**: Raspberry Pi
- **Lenguaje**: Python 3
- **Conexión**: SSH via PuTTY
- **Sistema Operativo**: Raspberry Pi OS

## Estructura del Repositorio
├── README.md                 # Este archivo
├── 01_basics/               # Ejercicios básicos de Python
├── 02_gpio/                 # Control de GPIO
├── 03_sensors/              # Sensores y periféricos
├── 04_communication/        # Comunicación serial/I2C/SPI
├── 05_projects/             # Proyectos integradores
└── requirements.txt         # Dependencias de Python

## Instrucciones de Configuración

### 1. Conexión SSH con PuTTY
1. Descarga e instala [PuTTY](https://www.putty.org/)
2. Configura la conexión:
   - **Host**: IP de tu Raspberry Pi
   - **Puerto**: 22
   - **Tipo**: SSH
3. Conéctate con usuario `pi` y tu contraseña

### 2. Clonar el Repositorio
git clone https://github.com/[TU-USUARIO]/sistemas-embebidos-rpi.git
cd sistemas-embebidos-rpi

### 3. Instalar Dependencias
bashpip3 install -r requirements.txt

### 4. Ejecutar Ejemplos
# Navega al directorio del ejercicio
cd 01_basics/ejemplo1

# Ejecuta el script
python3 main.py
Ejemplos por Módulo

### Módulo 1: Fundamentos
Variables y estructuras de datos
Funciones y módulos
Manejo de archivos

### Módulo 2: GPIO
Control de LEDs
Botones y entradas digitales
PWM para servomotores

### Módulo 3: Sensores
Sensor de temperatura DHT11/22
Sensor ultrasónico HC-SR04
Acelerómetro MPU6050

### Módulo 4: Comunicación
UART/Serial
I2C
SPI

### Módulo 5: Proyectos
Sistema de monitoreo ambiental
Control remoto por web
Robótica básica

### Contribución
Crea una rama para tus cambios: git checkout -b feature/nombre-ejercicio
Realiza tus commits: git commit -m "Agrega ejercicio X"
Sube los cambios: git push origin feature/nombre-ejercicio
Crea un Pull Request

### Licencia
Este repositorio está bajo licencia MIT. Úsalo libremente para fines educativos.
Contacto

Profesor: Sergio Pinilla Valencia
Curso: Sistemas Embebidos - 2025
Institucion: Universidad de Caldas
Correos: sergio.pinilla@ucaldas.edu.co
