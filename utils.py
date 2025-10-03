"""
Utilidades generales del sistema
Funciones auxiliares para validación, formateo y operaciones comunes
"""

import re
from typing import Any, Dict, List, Optional
from datetime import datetime, date
from enum import Enum

def validate_document_number(document_number: str, document_type: str) -> bool:
    """
    Valida el número de documento según el tipo
    
    Args:
        document_number: Número del documento
        document_type: Tipo de documento
        
    Returns:
        True si el documento es válido, False en caso contrario
    """
    if not document_number or not document_number.strip():
        return False
    
    # Remover espacios y caracteres especiales
    clean_number = re.sub(r'[^0-9]', '', document_number)
    
    # Validaciones específicas por tipo
    if document_type.lower() in ['cc', 'cedula_ciudadania']:
        return 6 <= len(clean_number) <= 12
    elif document_type.lower() in ['ce', 'cedula_extranjeria']:
        return 6 <= len(clean_number) <= 12
    elif document_type.lower() in ['ti', 'tarjeta_identidad']:
        return 10 <= len(clean_number) <= 11
    elif document_type.lower() == 'pasaporte':
        return 6 <= len(document_number) <= 15  # Puede tener letras
    
    return False

def validate_email(email: str, is_institutional: bool = False) -> bool:
    """
    Valida formato de email
    
    Args:
        email: Dirección de email a validar
        is_institutional: Si debe ser email institucional
        
    Returns:
        True si el email es válido
    """
    if not email:
        return False
    
    # Patrón básico de email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_pattern, email):
        return False
    
    # Validar dominio institucional si es requerido
    if is_institutional:
        return email.lower().endswith('@upc.edu.co')
    
    return True

def validate_phone_number(phone: str) -> bool:
    """
    Valida número telefónico colombiano
    
    Args:
        phone: Número telefónico
        
    Returns:
        True si el número es válido
    """
    if not phone:
        return False
    
    # Remover espacios y caracteres especiales
    clean_phone = re.sub(r'[^0-9]', '', phone)
    
    # Validar longitud y formato colombiano
    if len(clean_phone) == 10:
        # Celular: inicia con 3
        return clean_phone.startswith('3')
    elif len(clean_phone) == 7:
        # Teléfono fijo
        return True
    
    return False

def calculate_age(birth_date: date) -> int:
    """
    Calcula la edad basada en la fecha de nacimiento
    
    Args:
        birth_date: Fecha de nacimiento
        
    Returns:
        Edad en años
    """
    today = date.today()
    age = today.year - birth_date.year
    
    # Ajustar si no ha cumplido años este año
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    
    return age

def format_document_number(document_number: str) -> str:
    """
    Formatea el número de documento agregando puntos separadores
    
    Args:
        document_number: Número sin formato
        
    Returns:
        Número formateado
    """
    if not document_number:
        return ""
    
    # Solo formatear números (cédulas)
    clean_number = re.sub(r'[^0-9]', '', document_number)
    
    if len(clean_number) >= 7:
        # Agregar puntos cada 3 dígitos desde la derecha
        formatted = ""
        for i, digit in enumerate(reversed(clean_number)):
            if i > 0 and i % 3 == 0:
                formatted = "." + formatted
            formatted = digit + formatted
        return formatted
    
    return clean_number

def safe_cast(value: Any, target_type: type, default: Any = None) -> Any:
    """
    Convierte un valor a un tipo específico de forma segura
    
    Args:
        value: Valor a convertir
        target_type: Tipo objetivo
        default: Valor por defecto si la conversión falla
        
    Returns:
        Valor convertido o valor por defecto
    """
    try:
        if target_type == bool:
            if isinstance(value, str):
                return value.lower() in ['true', '1', 'si', 'sí', 'yes']
            return bool(value)
        elif target_type == datetime:
            if isinstance(value, str):
                # Intentar varios formatos
                formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y']
                for fmt in formats:
                    try:
                        return datetime.strptime(value, fmt)
                    except ValueError:
                        continue
            return target_type(value)
        else:
            return target_type(value)
    except (ValueError, TypeError):
        return default

def generate_user_code(role: str, document_number: str) -> str:
    """
    Genera un código de usuario único
    
    Args:
        role: Rol del usuario
        document_number: Número de documento
        
    Returns:
        Código único del usuario
    """
    role_prefixes = {
        'estudiante': 'EST',
        'profesor': 'PROF',
        'administrativo': 'ADM',
        'egresado': 'EGR'
    }
    
    prefix = role_prefixes.get(role.lower(), 'USR')
    clean_doc = re.sub(r'[^0-9]', '', document_number)
    
    # Tomar últimos 6 dígitos del documento
    doc_suffix = clean_doc[-6:] if len(clean_doc) >= 6 else clean_doc
    
    return f"{prefix}{doc_suffix}"

def sanitize_string(input_string: str, max_length: Optional[int] = None) -> str:
    """
    Limpia y sanitiza una cadena de texto
    
    Args:
        input_string: Cadena a limpiar
        max_length: Longitud máxima opcional
        
    Returns:
        Cadena limpia
    """
    if not input_string:
        return ""
    
    # Remover espacios extra y caracteres especiales problemáticos
    cleaned = re.sub(r'\s+', ' ', input_string.strip())
    cleaned = re.sub(r'[<>\"\'&]', '', cleaned)
    
    if max_length and len(cleaned) > max_length:
        cleaned = cleaned[:max_length]
    
    return cleaned

def enum_to_dict(enum_class: Enum) -> Dict[str, str]:
    """
    Convierte un Enum a diccionario para serialización
    
    Args:
        enum_class: Clase Enum
        
    Returns:
        Diccionario con valores del enum
    """
    return {item.name: item.value for item in enum_class}

def paginate_results(data: List[Any], page: int = 1, per_page: int = 10) -> Dict[str, Any]:
    """
    Pagina una lista de resultados
    
    Args:
        data: Lista de datos
        page: Página actual (inicia en 1)
        per_page: Elementos por página
        
    Returns:
        Diccionario con datos paginados y metadatos
    """
    total_items = len(data)
    total_pages = (total_items + per_page - 1) // per_page
    
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    
    paginated_data = data[start_index:end_index]
    
    return {
        'data': paginated_data,
        'pagination': {
            'current_page': page,
            'per_page': per_page,
            'total_items': total_items,
            'total_pages': total_pages,
            'has_next': page < total_pages,
            'has_prev': page > 1
        }
    }