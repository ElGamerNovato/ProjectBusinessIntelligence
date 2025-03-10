# Business Intelligence para Farmacia

## Descripción del Proyecto
Este proyecto implementa un sistema de Business Intelligence (BI) para una farmacia, permitiendo el procesamiento y el análisis de datos desde una base de origen hasta una base de datos destino. Se utiliza el modelo Kimball (modelo estrella) para la organización de los datos, facilitando consultas eficientes y generación de reportes.

## Tecnologías Utilizadas
- **Base de Datos**: MariaDB 🐬
- **Lenguaje de Programación**: Python 🐍
- **Librerías**:
  - Pandas 🐼 (procesamiento de datos)
  - Matplotlib 📊 (visualización de datos)

## Arquitectura del Proyecto
1. **Extracción**: Se obtienen los datos desde la base de origen.
2. **Transformación**: Se limpian y estructuran los datos según el modelo estrella.
3. **Carga**: Los datos procesados se almacenan en la base de datos destino.
4. **Análisis y Visualización**: Se generan informes y gráficos estadísticos utilizando Pandas y Matplotlib.

## Archivos Principales
- `subirDatosModeloEstrella.py` 📂: Se encarga de extraer los datos desde la base de origen y cargarlos en la base de datos destino utilizando el modelo estrella.
- `etl.py` 📊: Ejecuta el proceso de transformación y genera los gráficos estadísticos a partir de los datos almacenados en la base destino.

## Instalación y Configuración
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/ElGamerNovato/ProjectBusinessIntelligence
   cd ProjectBusinessIntelligence
   ```
2. Crear un entorno virtual e instalar dependencias desde `requirements.txt`:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt  # Instalar dependencias generadas con pip freeze
   ```
3. Configurar la conexión a MariaDB en el archivo de configuración correspondiente.

## Uso
1. Subir los datos al modelo estrella:
   ```bash
   python subirDatosModeloEstrella.py
   ```
2. Ejecutar el proceso ETL y generar los gráficos:
   ```bash
   python etl.py
   ```
Los resultados se almacenarán en la base de datos destino y los gráficos se guardarán en la carpeta `GraficosEstadisticos/`.

## Licencia
Este proyecto está bajo la licencia MIT.

