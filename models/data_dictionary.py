"""
Diccionario de datos - Variables para Bienestar Universitario UPC
Tarea: Alistar primeras variables para cargar en el diccionario

Áreas de Bienestar:
- Deportes
- Cultura  
- Ayuda Social
- PQRs
- Informativo (Podcast)

Estamentos: Estudiantes, Administrativos, Docentes, Egresados
Basado en: Política de bienestar familiar institucional UPC
"""

class DataDictionary:
    """Diccionario de variables para el sistema de bienestar universitario UPC"""
    
    def __init__(self):
        """Inicializa las variables del diccionario de datos según apuntes de clase"""
        
        # Variables de identificación (según normativa UPC + Ley diversidad sexual y género Colombia)
        self.identificacion_variables = {
            "tipo_documento": ["CC", "CE", "TI", "PAS"],  # CC: numérico, CE: alfanumérico, TI: numérico, PAS: alfanumérico
            "numero_documento": "string",  # Formato según tipo
            "nombres": "string",
            "apellidos": "string",
            
            # DIVERSIDAD SEXUAL Y GÉNERO (Ley Colombia) - OBLIGATORIO
            "sexo_biologico": ["Masculino", "Femenino", "Intersexual"],  # Sexo asignado al nacer
            "identidad_genero": [
                "Hombre", "Mujer", "Persona no binaria", "Persona de género fluido",
                "Otra identidad de género", "Prefiero no responder"
            ],  # Identidad de género autopercibida
            "expresion_genero": [
                "Masculina", "Femenina", "Andrógina", "De género fluido", 
                "Otra expresión", "Prefiero no responder"
            ],  # Expresión de género
            "orientacion_sexual": [
                "Heterosexual", "Homosexual", "Bisexual", "Pansexual", 
                "Asexual", "Demisexual", "Otra orientación", "Prefiero no responder"
            ],  # Orientación sexual
            "nombre_social": "string",  # Nombre con el que se identifica (opcional)
            "pronombres_preferidos": [
                "él/él", "ella/ella", "elle/elle", "ellos/ellas", 
                "otros pronombres", "sin pronombres específicos"
            ],  # Pronombres preferidos
            
            # DATOS PERSONALES BÁSICOS
            "fecha_nacimiento": "date",
            "domicilio": "string",
            "email": "string",
            "cel": "string",  # Celular (no teléfono)
            "update_date": "datetime",  # Campo obligatorio
            
            # CONFIDENCIALIDAD Y PROTECCIÓN DE DATOS
            "autorizacion_datos_sensibles": "boolean",  # Autorización para manejo de datos sensibles
            "confidencialidad_solicitada": "boolean",  # Si solicita confidencialidad especial
            "fecha_autorizacion": "datetime"  # Fecha de autorización de datos
        }
        
        # Variables por estamento (no roles)
        self.estamentos_variables = {
            "estudiante": {
                "programa_academico": "string",  # Obligatorio: Registro por programa académico
                "facultad": "string",  # Obligatorio: Estar en la Facultad inscrito
                "promedio": "float",  # Obligatorio: Para seguimiento automático
                "codigo_estudiante": "string",
                "semestre": "integer",
                "estado_academico": "string"
            },
            "docente": {  # No profesor, es docente
                "programa_academico": "string",  # Registro por programa académico
                "facultad": "string",
                "codigo_empleado": "string",
                "departamento": "string",
                "categoria": "string",
                "dedicacion": "string"
            },
            "administrativo": {
                "codigo_empleado": "string",
                "area": "string",
                "cargo": "string",
                "nivel_acceso": "string",
                "dependencia": "string"
            },
            "egresado": {
                "programa_academico": "string",  # Programa del que egresó
                "facultad": "string",
                "codigo_egresado": "string",
                "año_graduacion": "integer",
                "estado_vinculacion": "string"
            }
        }
        
        # Variables por área de bienestar
        self.areas_bienestar_variables = {
            "deportes": {
                "deportes_upc_disponibles": "array",  # Deportes que ofrece la UPC
                "deportes_practicados": "array",
                "registro_programa_academico": "string",  # Obligatorio
                "facultad_inscrito": "string",  # Obligatorio
                "promedio_academico": "float",  # Para veto automático
                "nivel_actividad": "string",
                "frecuencia_semanal": "integer",
                "seguimiento_administrador": "string",  # Para veto automático
                "estado_participacion": "string"
            },
            "cultura": {
                "actividades_disponibles": ["Danza", "Teatro", "Música"],  # Ejemplos específicos
                "actividades_practicadas": "array",
                "registro_programa_academico": "string",  # Obligatorio
                "facultad_inscrito": "string",  # Obligatorio
                "promedio_academico": "float",  # Para veto automático
                "nivel_experiencia": "string",
                "seguimiento_administrador": "string",  # Para veto automático
                "participacion_eventos": "array"
            },
            "ayuda_social": {
                "enlace_vinculacion": "string",  # Enlace para vinculación
                "tipo_asistencia_requerida": "array",
                "estado_socioeconomico": "string",
                "nivel_urgencia": "string",
                "documentos_soporte": "array"
            },
            "pqrs": {
                "tipo_solicitud": "string",
                "descripcion": "text",
                "fecha_solicitud": "datetime",
                "estado_pqrs": "string",
                "respuesta": "text",
                "fecha_respuesta": "datetime"
            },
            "informativo": {
                "podcast_disponibles": "array",
                "formato_capsula": "string",  # Formato: 60 segundos
                "periodicidad_publicacion": "string",
                "temas_diversidad_inclusion": "array",  # Obligatorio: Ley inclusión diversidad sexual y género
                "fecha_publicacion": "datetime"
            },
            
            # NUEVA ÁREA: DIVERSIDAD E INCLUSIÓN (Obligatorio por Ley)
            "diversidad_inclusion": {
                "poblacion_diferencial": [
                    "LGBTIQ+", "Afrodescendiente", "Indígena", "Persona con discapacidad",
                    "Víctima del conflicto", "Migrante", "Adulto mayor", "Ninguna", "Prefiero no responder"
                ],  # Poblaciones diferenciales
                "necesidades_especiales": "array",  # Necesidades específicas de apoyo
                "servicios_inclusion_requeridos": "array",  # Servicios de inclusión necesarios
                "participacion_espacios_seguros": "boolean",  # Participación en espacios seguros LGBTIQ+
                "reportes_discriminacion": "array",  # Reportes de discriminación
                "acompañamiento_psicosocial": "boolean",  # Requiere acompañamiento
                "ajustes_razonables": "array",  # Ajustes razonables requeridos
                "sensibilizacion_diversidad": "boolean",  # Participación en sensibilización
                "grupos_apoyo": "array",  # Grupos de apoyo disponibles
                "protocolos_atencion": "array",  # Protocolos de atención especializados
                "seguimiento_inclusion": "string",  # Estado de seguimiento inclusivo
                "fecha_caracterizacion": "datetime"  # Fecha de caracterización inclusiva
            }
        }
    
    def show_dictionary_structure(self):
        """Muestra la estructura completa del diccionario de variables según apuntes UPC"""
        
        print("🔹 VARIABLES DE IDENTIFICACIÓN (Normativa UPC):")
        for variable, tipo in self.identificacion_variables.items():
            if isinstance(tipo, list):
                print(f"   {variable}: {tipo}")
            else:
                print(f"   {variable}: {tipo}")
        
        print("\n🔹 VARIABLES POR ESTAMENTO:")
        for estamento, variables in self.estamentos_variables.items():
            print(f"   📂 {estamento.upper()}:")
            for variable, tipo in variables.items():
                if variable in ["programa_academico", "facultad", "promedio"]:
                    print(f"      {variable}: {tipo} ⭐ OBLIGATORIO")
                else:
                    print(f"      {variable}: {tipo}")
        
        print("\n🔹 VARIABLES POR ÁREA DE BIENESTAR:")
        for area, variables in self.areas_bienestar_variables.items():
            print(f"   📂 {area.upper()}:")
            for variable, tipo in variables.items():
                if isinstance(tipo, list) and variable == "actividades_disponibles":
                    print(f"      {variable}: {tipo} (Ejemplos)")
                elif "obligatorio" in variable.lower() or "programa_academico" in variable or "promedio" in variable:
                    print(f"      {variable}: {tipo} ⭐")
                else:
                    print(f"      {variable}: {tipo}")
        
        print("\n📋 NOTAS IMPORTANTES:")
        print("   ⭐ Variables obligatorias para seguimiento automático")
        print("   📄 Consultar: 'Política de bienestar familiar institucional UPC'")
        print("   📊 Fórmulas de promedio: últimas 2 páginas del documento")
        print("   🏳️‍🌈 OBLIGATORIO: Ley inclusión diversidad sexual y género Colombia")
        print("   🔒 Datos sensibles: Requieren autorización explícita del usuario")
        print("   ⚖️  Protección especial: Variables de identidad de género y orientación sexual")
        print("   📋 Caracterización inclusiva: Obligatoria para todas las personas usuarias")
    
    def get_variables_by_estamento(self, estamento):
        """Obtiene las variables específicas de un estamento"""
        base_vars = {**self.identificacion_variables}
        estamento_vars = self.estamentos_variables.get(estamento, {})
        return {**base_vars, **estamento_vars}
    
    def get_variables_by_area(self, area):
        """Obtiene las variables específicas de un área de bienestar"""
        return self.areas_bienestar_variables.get(area, {})
    
    def get_obligatory_variables(self):
        """Retorna las variables obligatorias del sistema según Ley de diversidad sexual y género"""
        return {
            "identificacion_obligatoria": [
                "tipo_documento", "numero_documento", "nombres", "apellidos", 
                "fecha_nacimiento", "email", "cel", "update_date"
            ],
            "diversidad_genero_obligatorio": [
                "sexo_biologico", "identidad_genero", "expresion_genero", "orientacion_sexual",
                "pronombres_preferidos", "autorizacion_datos_sensibles", "fecha_autorizacion"
            ],  # Obligatorio por Ley de diversidad sexual y género
            "por_estamento_obligatorio": ["programa_academico", "facultad", "promedio"],
            "areas_deportes_cultura": ["registro_programa_academico", "facultad_inscrito", "promedio_academico"],
            "informativo_obligatorio": ["temas_diversidad_inclusion"],
            "inclusion_obligatoria": [
                "poblacion_diferencial", "fecha_caracterizacion", "protocolos_atencion"
            ]  # Obligatorio para cumplimiento normativo
        }
    
    def get_all_variables(self):
        """Retorna todas las variables del diccionario organizadas según UPC"""
        return {
            "identificacion": self.identificacion_variables,
            "estamentos": self.estamentos_variables,
            "areas_bienestar": self.areas_bienestar_variables,
            "obligatorias": self.get_obligatory_variables()
        }