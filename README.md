# BienestarUPC - Diccionario de Datos

**Tarea Backend**: Alistar primeras variables para cargar en el diccionario  
**Proyecto**: Sistema de Bienestar Universitario - Octavo Semestre Ingeniería de Sistemas

## Descripción

Este proyecto define las **primeras variables del diccionario de datos** para el sistema de bienestar universitario.

**Departamentos de Bienestar:**
- **Deporte**: Actividades deportivas y recreativas
- **Cultura**: Danza, teatro, música y actividades artísticas  
- **Ayuda Social**: Asistencia y apoyo a la comunidad universitaria

**Roles de Usuario:**
- Estudiantes, Profesores, Administrativos, Egresados

## Estructura del Proyecto

```
BienestarUPC/
├── models/
│   ├── __init__.py
│   └── data_dictionary.py     # Variables del diccionario de datos
├── main.py                    # Mostrar variables del diccionario
├── config.py                  # Configuraciones básicas
├── utils.py                   # Utilidades de validación
└── README.md                  # Esta documentación
```

## Variables del Diccionario (Según Apuntes UPC)

### 🔹 Variables de Identificación (Normativa UPC + Ley Diversidad Sexual y Género)

**Datos básicos:**
- `tipo_documento`: CC (numérico), CE (alfanumérico), TI (numérico), PAS (alfanumérico)
- `numero_documento`: string (formato según tipo)
- `nombres`: string
- `apellidos`: string
- `fecha_nacimiento`: date
- `domicilio`: string
- `email`: string
- `cel`: string (celular)
- `update_date`: datetime ⭐ **OBLIGATORIO**

**🏳️‍🌈 Diversidad Sexual y Género (OBLIGATORIO por Ley Colombia):**
- `sexo_biologico`: Masculino, Femenino, Intersexual
- `identidad_genero`: Hombre, Mujer, Persona no binaria, Persona de género fluido, Otra, Prefiero no responder ⭐
- `expresion_genero`: Masculina, Femenina, Andrógina, De género fluido, Otra, Prefiero no responder ⭐
- `orientacion_sexual`: Heterosexual, Homosexual, Bisexual, Pansexual, Asexual, Demisexual, Otra, Prefiero no responder ⭐
- `nombre_social`: string (nombre con el que se identifica)
- `pronombres_preferidos`: él/él, ella/ella, elle/elle, otros ⭐
- `autorizacion_datos_sensibles`: boolean ⭐ **OBLIGATORIO**
- `confidencialidad_solicitada`: boolean
- `fecha_autorizacion`: datetime ⭐ **OBLIGATORIO**

### 🔹 Variables por Estamento

**Estudiante:** ⭐ **Obligatorios**: programa_academico, facultad, promedio
- `codigo_estudiante`, `semestre`, `estado_academico`

**Docente:** ⭐ **Obligatorios**: programa_academico, facultad
- `codigo_empleado`, `departamento`, `categoria`, `dedicacion`

**Administrativo:**
- `codigo_empleado`, `area`, `cargo`, `nivel_acceso`, `dependencia`

**Egresado:**
- `programa_academico`, `facultad`, `codigo_egresado`, `año_graduacion`, `estado_vinculacion`

### 🔹 Variables por Área de Bienestar

**Deportes:** ⭐ **Obligatorios**: registro_programa_academico, facultad_inscrito, promedio_academico
- `deportes_upc_disponibles`, `deportes_practicados`, `nivel_actividad`, `seguimiento_administrador`

**Cultura:** ⭐ **Obligatorios**: registro_programa_academico, facultad_inscrito, promedio_academico  
- `actividades_disponibles`: [Danza, Teatro, Música], `nivel_experiencia`, `seguimiento_administrador`

**Ayuda Social:**
- `enlace_vinculacion`, `tipo_asistencia_requerida`, `estado_socioeconomico`, `nivel_urgencia`

**PQRs:**
- `tipo_solicitud`, `descripcion`, `fecha_solicitud`, `estado_pqrs`, `respuesta`

**Informativo:** ⭐ **Obligatorio**: temas_diversidad_inclusion (Ley diversidad sexual y género)
- `podcast_disponibles`, `formato_capsula` (60 seg), `periodicidad_publicacion`

**🏳️‍🌈 Diversidad e Inclusión:** ⭐ **NUEVA ÁREA OBLIGATORIA** (Ley Colombia)
- `poblacion_diferencial`: LGBTIQ+, Afrodescendiente, Indígena, Persona con discapacidad, Víctima del conflicto, Migrante, Adulto mayor
- `necesidades_especiales`, `servicios_inclusion_requeridos`, `participacion_espacios_seguros`
- `reportes_discriminacion`, `acompañamiento_psicosocial`, `ajustes_razonables`
- `sensibilizacion_diversidad`, `grupos_apoyo`, `protocolos_atencion` ⭐
- `seguimiento_inclusion`, `fecha_caracterizacion` ⭐ **OBLIGATORIO**

## Instalación y Uso

### Requisitos
- Python 3.8 o superior
- VS Code (recomendado)

### Configuración
1. Clona o descarga el proyecto
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```

## Uso

### Ejecutar el proyecto:
```bash
python main.py
```

### Uso básico:
```python
from models.data_dictionary import DataDictionary

# Inicializar diccionario
data_dict = DataDictionary()

# Ver todas las variables según normativa UPC
data_dict.show_dictionary_structure()

# Obtener variables por estamento
variables_estudiante = data_dict.get_variables_by_estamento("estudiante")

# Obtener variables por área de bienestar
variables_deportes = data_dict.get_variables_by_area("deportes")

# Obtener variables obligatorias
obligatorias = data_dict.get_obligatory_variables()
```

## Desarrollo

**Tarea específica**: Alistar primeras variables para cargar en el diccionario  
**Rol**: Backend Developer  
**Curso**: Octavo Semestre - Ingeniería de Sistemas  
**Proyecto**: Sistema de Bienestar Universitario  

### Tecnologías
- Python 3.13+
- Programación Orientada a Objetos
- Estructuras de datos

---

### 📋 **Referencias importantes:**
- **Documento base**: "Política de bienestar familiar institucional UPC"
- **Fórmulas de promedio**: Últimas 2 páginas del documento
- **🏳️‍🌈 Normativa obligatoria**: Ley de inclusión diversidad sexual y género Colombia
- **Seguimiento automático**: Variables obligatorias para veto automático por promedio

### 🔒 **Protección de datos sensibles:**
- **Datos sensibles**: Identidad de género, orientación sexual, poblaciones diferenciales
- **Autorización requerida**: Consentimiento explícito para manejo de datos LGBTIQ+
- **Confidencialidad**: Protección especial según solicitud del usuario
- **Caracterización inclusiva**: Obligatoria para cumplimiento normativo

### ⚖️ **Cumplimiento legal:**
- Variables de diversidad sexual y género son **OBLIGATORIAS** por ley colombiana
- Protocolos de atención especializados para poblaciones diferenciales
- Espacios seguros y libres de discriminación
- Seguimiento y caracterización inclusiva

**Nota**: Este proyecto cumple con la Ley de diversidad sexual y género de Colombia y normativa UPC.