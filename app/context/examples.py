ESTIMATION_EXAMPLES = [
    {
        "meeting_summary": (
            "El cliente necesita una plataforma web de gestión de inventario..."
        ),
        "estimation": """
## Estimación de la plataforma de gestión de inventario

### Desglose de tareas

1. Diseño UI/UX: 40 horas
2. Backend API (CRUD inventario): 60 horas
3. Autenticación y roles: 20 horas
4. Dashboard con métricas: 30 horas
5. Testing y QA: 25 horas

**Total estimado: 175 horas**
**Equipo recomendado: 2 desarrolladores full-stack + 1 diseñador UX a tiempo parcial**
**Duración estimada: 6–8 semanas**
""".strip(),
    },
    {
        "meeting_summary": (
            "Una empresa de mantenimiento recibe solicitudes por correo y WhatsApp. "
            "El coordinador las copia en Excel y asigna los trabajos a los técnicos. "
            "El cliente quiere que el personal registre solicitudes con fotos, que "
            "el coordinador las asigne y que cada técnico pueda actualizar su estado "
            "desde el móvil. Ya existe un directorio corporativo para iniciar sesión. "
            "Para la primera entrega se acordó una web adaptable, avisos por correo "
            "en dos momentos (asignación y cierre) y la importación de las solicitudes "
            "abiertas desde un único Excel. Se aplazaron la app nativa y la mensajería "
            "por WhatsApp."
        ),
        "estimation": """
## Estimación del portal de solicitudes de mantenimiento

### Desglose de tareas

1. Taller de alcance, estados y criterios de aceptación: 12 horas
2. Diseño de pantallas para móvil y escritorio: 20 horas
3. Integración con el directorio corporativo y permisos por rol: 24 horas
4. Registro de solicitudes, adjuntos y validaciones: 36 horas
5. Bandeja de trabajo, asignación, filtros e historial de estados: 44 horas
6. Notificaciones por correo para asignación y cierre: 12 horas
7. Importación de solicitudes abiertas y reporte de filas rechazadas: 16 horas
8. Pruebas, despliegue y acompañamiento del piloto: 28 horas

**Subtotal: 192 horas**
**Contingencia: 24 horas para ajustes de permisos y del archivo de importación**
**Total estimado: 216 horas**
**Equipo recomendado: 2 desarrolladores full-stack con dedicación parcial y apoyo puntual de UX y QA**
**Duración estimada: 5–6 semanas**, con una capacidad conjunta de unas 45 horas semanales y una ronda de validación con el coordinador.

### Supuestos y dependencias

- El cliente facilita el acceso de prueba al directorio corporativo y entrega una muestra del Excel durante la primera semana.
- La importación incluye las solicitudes abiertas. El histórico y los adjuntos anteriores quedan fuera del alcance.
- El piloto se considera aceptado cuando un solicitante, un coordinador y un técnico pueden completar una solicitud de principio a fin con sus permisos correspondientes.
""".strip(),
    },
    {
        "meeting_summary": (
            "Una tienda online carga a mano en su ERP los pedidos ya pagados. "
            "El equipo pierde tiempo reconciliando pedidos duplicados y corrigiendo "
            "referencias de productos. La tienda ofrece webhooks y el proveedor del "
            "ERP confirma que puede entregar un entorno de pruebas. El alcance es "
            "enviar los pedidos pagados al ERP, reintentar fallos temporales y "
            "permitir que operaciones reprocese los errores corregidos. Las "
            "devoluciones, la sincronización de stock y los pedidos anteriores "
            "a la puesta en marcha se aplazaron."
        ),
        "estimation": """
## Estimación de la integración entre tienda online y ERP

### Desglose de tareas

1. Revisión de APIs y mapeo de productos, clientes, impuestos y descuentos: 24 horas
2. Recepción, validación y registro de eventos de pedidos pagados: 24 horas
3. Transformación y envío al ERP con control de duplicados: 36 horas
4. Reintentos ante fallos temporales y registro de errores definitivos: 24 horas
5. Vista operativa para consultar y reprocesar pedidos fallidos: 24 horas
6. Pruebas con pedidos representativos y conciliación con operaciones: 32 horas
7. Configuración de alertas, despliegue y traspaso a soporte: 16 horas

**Subtotal: 180 horas**
**Contingencia: 30 horas para diferencias en los datos y el comportamiento real del ERP**
**Total estimado: 210 horas**
**Equipo recomendado: 1 desarrollador de integraciones, con apoyo parcial de QA y operaciones**
**Duración estimada: 6–7 semanas**, con una capacidad conjunta de unas 35–40 horas semanales y una ventana de validación con el proveedor.

### Supuestos y dependencias

- La estimación cubre una tienda, una empresa del ERP y una moneda. El cliente mantiene una correspondencia entre las referencias de ambos sistemas.
- Antes de cerrar el diseño se debe verificar si el ERP puede buscar un pedido por referencia externa. Esa capacidad permite resolver casos en los que el ERP crea el pedido, pero la respuesta se pierde.
- La aceptación incluye comprobar que dos notificaciones del mismo pedido generan un único registro y que un error de datos puede corregirse y reprocesarse.
""".strip(),
    },
    {
        "meeting_summary": (
            "Un equipo BIM prepara paquetes de entrega desde Revit y revisa "
            "manualmente en Excel la codificación y los parámetros obligatorios. "
            "Quieren un complemento que valide el modelo activo, identifique los "
            "elementos con errores y exporte un informe para el coordinador. Las "
            "reglas están en una hoja de cálculo, pero algunos criterios requieren "
            "confirmación y hay modelos antiguos con parámetros incompletos. "
            "Se acordó validar una versión de Revit y tres familias de elementos. "
            "La corrección automática y la publicación en ACC quedan para otra fase."
        ),
        "estimation": """
## Estimación del complemento de validación BIM para Revit

### Desglose de tareas

1. Revisión de reglas con el coordinador BIM y preparación de casos de prueba: 20 horas
2. Configuración del complemento y lectura de elementos del modelo activo: 24 horas
3. Validación de codificación, parámetros obligatorios y valores permitidos: 36 horas
4. Interfaz de resultados y selección de elementos con incidencias en Revit: 28 horas
5. Exportación del informe a Excel con identificador, regla y detalle del error: 16 horas
6. Pruebas en un modelo actual y otro antiguo, incluida la revisión de rendimiento: 28 horas
7. Instalador, documentación breve y piloto con el equipo BIM: 16 horas

**Subtotal: 168 horas**
**Contingencia: 24 horas para variaciones de parámetros y excepciones en modelos antiguos**
**Total estimado: 192 horas**
**Equipo recomendado: 1 desarrollador C# con experiencia en la API de Revit y 1 coordinador BIM a tiempo parcial**
**Duración estimada: 5–6 semanas**, con unas 36–40 horas semanales de capacidad conjunta y disponibilidad del coordinador para resolver excepciones.

### Supuestos y dependencias

- El coordinador entrega dos modelos representativos y aprueba las reglas durante la primera semana.
- La validación se ejecuta sobre los elementos del modelo activo. Los modelos vinculados quedan fuera del alcance inicial.
- La aceptación se verifica con una muestra de elementos válidos e inválidos revisada previamente por el coordinador.
""".strip(),
    },
    {
        "meeting_summary": (
            "Una empresa quiere migrar el flujo de aprobación de gastos de su "
            "aplicación interna antigua a un nuevo portal. El sistema actual "
            "tiene varios años de datos, registros incompletos y reglas de "
            "aprobación poco documentadas. Finanzas necesita conservar el "
            "historial para consultas y continuar las solicitudes abiertas "
            "después del cambio. La primera fase cubre el flujo de gastos, "
            "sus adjuntos y un reporte mensual. Los demás módulos seguirán "
            "operando en la aplicación antigua."
        ),
        "estimation": """
## Estimación de la migración del flujo de aprobación de gastos

### Desglose de tareas

1. Revisión del código actual y validación de las reglas con Finanzas: 32 horas
2. Diseño del flujo, permisos y criterios de aceptación: 24 horas
3. Desarrollo de formularios, aprobaciones, rechazos e historial: 60 horas
4. Consulta del histórico y generación del reporte mensual: 28 horas
5. Scripts de migración para solicitudes, estados y adjuntos: 44 horas
6. Ensayo de migración, conciliación de datos y tratamiento de excepciones: 32 horas
7. Pruebas funcionales y aceptación con Finanzas: 32 horas
8. Corte a producción, plan de reversión y seguimiento inicial: 20 horas

**Subtotal: 272 horas**
**Contingencia: 48 horas para reglas heredadas y problemas de calidad de datos**
**Total estimado: 320 horas**
**Equipo recomendado: 2 desarrolladores, apoyo parcial de QA y un responsable de Finanzas para las validaciones**
**Duración estimada: 7–9 semanas**, con una capacidad conjunta de unas 45–50 horas semanales y una ventana acordada para el corte.

### Supuestos y dependencias

- Finanzas confirma qué estados, adjuntos y campos deben conservarse y decide cómo tratar los registros incompletos.
- Se requiere una copia autorizada de la base de datos y acceso de solo lectura a los adjuntos para ensayar la migración.
- La estimación se revisa al cerrar el análisis inicial. Antes del corte se comparan los conteos por estado y los importes por periodo, y se verifica que las solicitudes abiertas puedan continuar en el portal nuevo.
""".strip(),
    },
]