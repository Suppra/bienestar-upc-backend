"""
Archivo de configuración principal del sistema
Contiene constantes y configuraciones globales
"""

import os
from typing import Dict, Any

# Configuración de la base de datos (placeholder - ajustar según necesidades)
DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "bienestar_upc"),
    "username": os.getenv("DB_USER", "bienestar_user"),
    "password": os.getenv("DB_PASSWORD", ""),
}

# Configuración del sistema
SYSTEM_CONFIG = {
    "name": "Sistema de Bienestar Universitario - BienestarUPC",
    "version": "1.0.0",
    "environment": os.getenv("ENVIRONMENT", "development"),
    "debug": os.getenv("DEBUG", "True").lower() == "true",
    "timezone": "America/Bogota",
    "language": "es",
}

# Configuración de roles y permisos
ROLES_CONFIG = {
    "estudiante": {
        "default_permissions": ["read_own_profile", "update_own_profile", "request_assistance"],
        "restricted_actions": ["admin_functions", "manage_users"]
    },
    "profesor": {
        "default_permissions": ["read_own_profile", "update_own_profile", "view_student_activities"],
        "restricted_actions": ["admin_functions", "financial_operations"]
    },
    "administrativo": {
        "default_permissions": ["manage_assistance", "generate_reports", "manage_activities"],
        "restricted_actions": ["system_admin"]
    },
    "egresado": {
        "default_permissions": ["read_own_profile", "update_own_profile", "alumni_services"],
        "restricted_actions": ["admin_functions", "current_student_services"]
    }
}

# Configuración de límites y validaciones
VALIDATION_RULES = {
    "documento_minimo_length": 7,
    "documento_maximo_length": 12,
    "edad_minima": 16,
    "edad_maxima": 100,
    "telefono_regex": r"^[0-9]{10}$",
    "email_institucional_domain": "@upc.edu.co"
}

# Configuración de servicios externos (placeholder)
EXTERNAL_SERVICES = {
    "email_service": {
        "enabled": True,
        "smtp_server": os.getenv("SMTP_SERVER", ""),
        "smtp_port": int(os.getenv("SMTP_PORT", "587")),
    },
    "sms_service": {
        "enabled": False,
        "provider": "twilio",
        "api_key": os.getenv("SMS_API_KEY", "")
    }
}

# Configuración de logging
LOGGING_CONFIG = {
    "level": os.getenv("LOG_LEVEL", "INFO"),
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file_path": os.getenv("LOG_FILE", "logs/bienestar_upc.log")
}

def get_config(section: str) -> Dict[str, Any]:
    """
    Obtiene una sección específica de la configuración
    
    Args:
        section: Nombre de la sección de configuración
        
    Returns:
        Diccionario con la configuración solicitada
    """
    config_sections = {
        "database": DATABASE_CONFIG,
        "system": SYSTEM_CONFIG,
        "roles": ROLES_CONFIG,
        "validation": VALIDATION_RULES,
        "external": EXTERNAL_SERVICES,
        "logging": LOGGING_CONFIG
    }
    
    return config_sections.get(section, {})