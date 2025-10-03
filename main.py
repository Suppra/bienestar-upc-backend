#!/usr/bin/env python3
"""
Sistema de Bienestar Universitario - BienestarUPC
Backend - Diccionario de Datos

Tarea: Alistar primeras variables para cargar en el diccionario
Proyecto octavo semestre - Ingeniería de Sistemas
"""

# Importar solo el diccionario de datos
from models.data_dictionary import DataDictionary

def main():
    """Mostrar las variables del diccionario de datos"""
    print("=== BienestarUPC - Variables del Diccionario ===")
    print("Backend: Alistar primeras variables para cargar en el diccionario")
    print()
    
    # Inicializar diccionario de datos
    data_dict = DataDictionary()
    
    # Mostrar estructura de variables
    print("📋 ESTRUCTURA DEL DICCIONARIO DE DATOS:")
    print()
    data_dict.show_dictionary_structure()
    
    print("\n✅ Variables del diccionario listas para implementación")

if __name__ == "__main__":
    main()