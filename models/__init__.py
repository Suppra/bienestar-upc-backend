# Archivo de inicialización del paquete models
"""
Paquete para el Diccionario de Datos - BienestarUPC
Tarea: Alistar primeras variables para cargar en el diccionario

Contiene:
- data_dictionary: Variables del diccionario de datos del sistema
"""

# Importación principal
from .data_dictionary import DataDictionary

__all__ = [
    'DataDictionary'
]

# Información del paquete
__version__ = '1.0.0'
__author__ = 'Equipo Backend - BienestarUPC'
__description__ = 'Variables del diccionario de datos para sistema de bienestar universitario'