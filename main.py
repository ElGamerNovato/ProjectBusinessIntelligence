import MySQLdb 
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

conn=MySQLdb.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME_ORIGEN'))

cursor=conn.cursor()


#Filtrar por fecha. Ventas la última semana
query="select * from Venta order by fecha;"
hoy=datetime.today()
fecha_hace_7_dias= hoy - timedelta(days=7)
cursor.execute(query)
nombre_columnas = [i[0] for i in cursor.description]
ventas_data = cursor.fetchall()
df_ventas = pd.DataFrame(ventas_data, columns=nombre_columnas)
df_ventas['fecha'] = pd.to_datetime(df_ventas['fecha'])
df_ventas_ultima_semana = df_ventas[(df_ventas['fecha'] >= fecha_hace_7_dias) & (df_ventas['fecha'] <= hoy)]
print("VENTAS REALIZADAS LA ÚLTIMA SEMANA")
print(df_ventas_ultima_semana)

#Filtrar qué productos se venden más a ciertas horas del día
query = "select Venta_Producto.IDproducto, Venta_Producto.cantidad, Venta.fecha from Venta join Venta_Producto on Venta.IDventa=Venta_Producto.IDventa"
cursor.execute(query)
nombre_columnas=[i[0] for i in cursor.description]
ventas_horas_data = cursor.fetchall()
df_ventas_horas = pd.DataFrame(ventas_horas_data, columns = nombre_columnas)
df_ventas_horas['fecha'] = pd.to_datetime(df_ventas_horas['fecha'])
df_ventas_horas['hora'] = df_ventas_horas['fecha'].dt.hour
def categorizar_hora(hora):
    if 6<=hora<12:
        return 'Mañana'
    elif 12<=hora<18:
        return 'Tarde'
    elif 18<=hora<=22:
        return 'Noche'
    else:
        return 'Madrugada'
df_ventas_horas['rango_horario']=df_ventas_horas['hora'].apply(categorizar_hora)
ventas_por_hora=df_ventas_horas.groupby(['IDproducto', 'rango_horario'])['cantidad'].sum().reset_index()
print(ventas_por_hora)

#Filtrar la cantidad de ventas que hizo cada empleado

#Obtenemos los empleados
query="select IDempleado, nombre from Empleado"
cursor.execute(query)
empleados_data=cursor.fetchall()
column_names=[i[0] for i in cursor.description]
df_empleados=pd.DataFrame(empleados_data, columns=column_names)
#Buscamos las ventas de cada empleado
query="select IDempleado, COUNT(*) as cantidad_de_ventas from Venta group by IDempleado"
cursor.execute(query)
ventas_por_empleado=cursor.fetchall()
nombre_columnas=[i[0] for i in cursor.description]
df_ventas_por_empleado=pd.DataFrame(ventas_por_empleado, columns=nombre_columnas)
df_cantidad_ventas_por_empleado=df_empleados.merge(df_ventas_por_empleado, on="IDempleado", how="left").fillna(0)
df_cantidad_ventas_por_empleado['cantidad_de_ventas'] = df_cantidad_ventas_por_empleado['cantidad_de_ventas'].astype(int)

#Filtrar cuánto dinero logró vender cada empleado
query = "SELECT Empleado.IDempleado, Empleado.nombre, SUM(Venta_Producto.precio * Venta_Producto.cantidad) AS total_ventas FROM Empleado JOIN Venta ON Empleado.IDempleado = Venta.IDempleado JOIN Venta_Producto ON Venta.IDventa = Venta_Producto.IDventa GROUP BY Empleado.IDempleado, Empleado.nombre;"
cursor.execute(query)
nombre_columnas=[i[0] for i in cursor.description]
df_dinero_ventas_por_empleado=pd.DataFrame(cursor.fetchall(), columns = nombre_columnas)

cursor.close()
conn.close()

#MOSTRANDO DATOS USANDO MATPLOTLIB

#Primero, muestro el dinero que generó cada empleado
plt.figure(figsize=(10,6))
print(df_dinero_ventas_por_empleado)
plt.bar(df_dinero_ventas_por_empleado['nombre'], df_dinero_ventas_por_empleado['total_ventas'], color='skyblue')
plt.xlabel('Empleado')
plt.ylabel('Total de dinero')
plt.title('Total de Dinero recaudado por Empleado en Ventas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/home/novato/Projects/BusinessIntelligence/ETL/dinero_por_empleado.png')

print("CANTIDAD DE VENTAS POR EMPLEADO")
print(df_cantidad_ventas_por_empleado)
print("CANTIDAD DE DINERO RECAUDADO POR CADA EMPLEADO")
print(df_dinero_ventas_por_empleado)
