import pandas as pd
import plotly.express as px

# 1. Cargar los datos del Excel
# Cambia 'datos_empresa.xlsx' por el nombre de tu archivo
# Asegúrate de que el Excel esté en la misma carpeta que este script
nombre_archivo = 'datos_empresa.xlsx' 

try:
    df = pd.read_excel('datos_empresa.xlsx')
    print("✅ Excel cargado con éxito")
    
    # 2. Procesamiento básico (Ejemplo: Agrupar ventas por categoría)
    # Supongamos que tu Excel tiene columnas: 'Categoria' y 'Ventas'
    resumen = df.groupby('clientes')['ventas'].sum().reset_index()

    # 3. Crear gráfico sofisticado (Gráfico de barras interactivo)
    fig = px.bar(
        resumen, 
        x='clientes', 
        y='ventas',
        title="Reporte Corporativo: Ventas por Categoría",
        text_auto='.2s', # Muestra valores sobre las barras
        template='plotly_dark' # Estilo oscuro y profesional
    )

    # 4. Personalización estética
    fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                      marker_line_width=1.5, opacity=0.6)

    # 5. Guardar y mostrar
    fig.show() # Abre el gráfico en tu navegador
    # fig.write_html("reporte_interactivo.html") # Esto genera un archivo para enviar por correo

except FileNotFoundError:
    print(f"❌ Error: No encontré el archivo '{nombre_archivo}'")
    