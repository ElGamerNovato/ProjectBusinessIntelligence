import pandas as pd
import matplotlib.pyplot as plt
import sys
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

try:
    conn = MySQLdb.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database = os.getenv('DB_NAME_DESTINO'))
    cursor=conn.cursor()
except Exception as e:
    print("Error al conectarse con la base de datos", e)
    sys.exit(1)

#Filtrar la cantidad de ventas que hizo cada empleado
try:
    query="select IDempleado, nombre from Empleado"
    cursor.execute(query)
    empleados_data=cursor.fetchall()
    column_names=[i[0] for i in cursor.description]
    df_empleados=pd.DataFrame(empleados_data, columns=column_names)
    query="select IDempleado, COUNT(*) as cantidad_de_ventas from HechosVentas group by IDempleado"
    cursor.execute(query)
    ventas_por_empleado=cursor.fetchall()
    column_names=[i[0] for i in cursor.description]
    df_ventas_por_empleado=pd.DataFrame(ventas_por_empleado, columns=column_names)
    df_cantidad_ventas_por_empleado=df_empleados.merge(df_ventas_por_empleado, on="IDempleado", how="left").fillna(0)
    df_cantidad_ventas_por_empleado['cantidad_de_ventas']=df_cantidad_ventas_por_empleado['cantidad_de_ventas'].astype(int)
    plt.figure(figsize=(10,6))
    plt.bar(df_cantidad_ventas_por_empleado['nombre'], df_cantidad_ventas_por_empleado['cantidad_de_ventas'], color='blue')
    plt.xlabel('Empleado')
    plt.ylabel('Cantidad de ventas')
    plt.title('Cantidad de ventas realizadas por cada empleado')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('GraficosEstadisticos/VentasPorEmpleado.png')
    plt.close()
    print("Se ha creado la estadística de ventas por empleado")
except Exception as e:
    print("Error al obtener las ventas que hizo cada empleado", e)

#Filtrar el dinero que generó cada empleado
try:
    query="select hv.IDempleado, e.nombre, sum(precio_total) as dinero_generado from HechosVentas hv join Empleado e on hv.IDempleado=e.IDempleado group by e.nombre order by dinero_generado"
    cursor.execute(query)
    dinero_por_empleado=cursor.fetchall()
    column_names=[i[0] for i in cursor.description]
    df_dinero_por_empleado=pd.DataFrame(dinero_por_empleado, columns=column_names)
    #Ingresos numéricos
    fig, ax=plt.subplots()
    barras=ax.bar(df_dinero_por_empleado['nombre'], df_dinero_por_empleado['dinero_generado'])
    ax.bar_label(barras, fmt='%.2f', label_type='edge')
    ax.set_xlabel('Empleado')
    ax.set_ylabel('Ingresos totales')
    ax.set_title('Total de ingresos generados por empleado')
    plt.xticks(rotation=25)
    plt.savefig('GraficosEstadisticos/IngresosPorEmpleado.png')
    plt.close()
    print("Se ha creado el gráfico de la cantidad de ingresos generados por empleado")
    #Porcentaje
    plt.pie(
            df_dinero_por_empleado['dinero_generado'],
            labels=df_dinero_por_empleado['nombre'],
            autopct='%1.1f%%',
            startangle=140)
    plt.title("Porcentaje de ingresos generados por cada empleado")
    plt.savefig('GraficosEstadisticos/PorcentajeIngresosPorEmpleado.png')
    plt.close()
    print("Se ha creado el gráfico del porcentaje de ingresos generados por empleado")
except Exception as e:
    print("Error al crear el gráfico del dinero generado por empleado", e)


#Filtrar los productos más vendidos por día en la semana anterior
try:
    #Lunes
    semana_anterior=(datetime.now().isocalendar()[1])-1
    query="select hv.IDproducto, p.nombre, hv.cantidad, t.dia_de_semana, t.semana from HechosVentas hv join Tiempo t on t.IDtiempo=hv.IDtiempo join Producto p on p.IDproducto=hv.IDproducto where semana=%s and dia_de_semana=%s group by hv.IDproducto order by cantidad desc"
    cursor.execute(query, (semana_anterior, "Monday"))
    productos_lunes=cursor.fetchall()
    column_names=[i[0] for i in cursor.description]
    df_productos_lunes=pd.DataFrame(productos_lunes, columns =column_names)
    df_productos_lunes=df_productos_lunes.head()
    fig,ax=plt.subplots()
    barras=ax.bar(df_productos_lunes['nombre'], df_productos_lunes['cantidad'])
    ax.bar_label(barras, fmt='%d', label_type='edge')
    ax.set_xlabel('Producto')
    ax.set_ylabel('Ventas')
    ax.set_title('Productos más vendidos el Lunes de la semana anterior')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('GraficosEstadisticos/DiasDeSemana/lunesAnterior.png')
    plt.close()

    #Martes
    query="select hv.IDproducto, p.nombre, hv.cantidad, t.dia_de_semana, t.semana from HechosVentas hv join Tiempo t on t.IDtiempo=hv.IDtiempo join Producto p on p.IDproducto=hv.IDproducto where semana=%s and dia_de_semana=%s group by hv.IDproducto order by cantidad desc"
    cursor.execute(query, (semana_anterior, "Tuesday"))
    productos_lunes=cursor.fetchall()
    df_productos_lunes=pd.DataFrame(productos_lunes, columns =column_names)
    df_productos_lunes=df_productos_lunes.head()
    fig,ax=plt.subplots()
    barras=ax.bar(df_productos_lunes['nombre'], df_productos_lunes['cantidad'])
    ax.set_xlabel('Producto')
    ax.set_ylabel('Ventas')
    ax.set_title('Productos más vendidos el Martes de la semana anterior')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('GraficosEstadisticos/DiasDeSemana/martesAnterior.png')
    plt.close()

    #Miercoles
    query="select hv.IDproducto, p.nombre, hv.cantidad, t.dia_de_semana, t.semana from HechosVentas hv join Tiempo t on t.IDtiempo=hv.IDtiempo join Producto p on p.IDproducto=hv.IDproducto where semana=%s and dia_de_semana=%s group by hv.IDproducto order by cantidad desc"
    cursor.execute(query, (semana_anterior, "Wednesday"))
    productos_lunes=cursor.fetchall()
    df_productos_lunes=pd.DataFrame(productos_lunes, columns =column_names)
    df_productos_lunes=df_productos_lunes.head()
    fig,ax=plt.subplots()
    barras=ax.bar(df_productos_lunes['nombre'], df_productos_lunes['cantidad'])
    ax.set_xlabel('Producto')
    ax.set_ylabel('Ventas')
    ax.set_title('Productos más vendidos el Miércoles de la semana anterior')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('GraficosEstadisticos/DiasDeSemana/miercolesAnterior.png')
    plt.close()

    #Jueves
    query="select hv.IDproducto, p.nombre, hv.cantidad, t.dia_de_semana, t.semana from HechosVentas hv join Tiempo t on t.IDtiempo=hv.IDtiempo join Producto p on p.IDproducto=hv.IDproducto where semana=%s and dia_de_semana=%s group by hv.IDproducto order by cantidad desc"
    cursor.execute(query, (semana_anterior, "Thursday"))
    productos_lunes=cursor.fetchall()
    column_names=[i[0] for i in cursor.description]
    df_productos_lunes=pd.DataFrame(productos_lunes, columns =column_names)
    df_productos_lunes=df_productos_lunes.head()
    fig,ax=plt.subplots()
    barras=ax.bar(df_productos_lunes['nombre'], df_productos_lunes['cantidad'])
    ax.set_xlabel('Producto')
    ax.set_ylabel('Ventas')
    ax.set_title('Productos más vendidos el Jueves de la semana anterior')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('GraficosEstadisticos/DiasDeSemana/juevesAnterior.png')
    plt.close()

    #Viernes
    query="select hv.IDproducto, p.nombre, hv.cantidad, t.dia_de_semana, t.semana from HechosVentas hv join Tiempo t on t.IDtiempo=hv.IDtiempo join Producto p on p.IDproducto=hv.IDproducto where semana=%s and dia_de_semana=%s group by hv.IDproducto order by cantidad desc"
    cursor.execute(query, (semana_anterior, "Friday"))
    productos_lunes=cursor.fetchall()
    column_names=[i[0] for i in cursor.description]
    df_productos_lunes=pd.DataFrame(productos_lunes, columns =column_names)
    df_productos_lunes=df_productos_lunes.head()
    fig,ax=plt.subplots()
    barras=ax.bar(df_productos_lunes['nombre'], df_productos_lunes['cantidad'])
    ax.set_xlabel('Producto')
    ax.set_ylabel('Ventas')
    ax.set_title('Productos más vendidos el Viernes de la semana anterior')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('GraficosEstadisticos/DiasDeSemana/viernesAnterior.png')
    plt.close()

    #Sabado
    query="select hv.IDproducto, p.nombre, hv.cantidad, t.dia_de_semana, t.semana from HechosVentas hv join Tiempo t on t.IDtiempo=hv.IDtiempo join Producto p on p.IDproducto=hv.IDproducto where semana=%s and dia_de_semana=%s group by hv.IDproducto order by cantidad desc"
    cursor.execute(query, (semana_anterior, "Saturday"))
    productos_lunes=cursor.fetchall()
    column_names=[i[0] for i in cursor.description]
    df_productos_lunes=pd.DataFrame(productos_lunes, columns =column_names)
    df_productos_lunes=df_productos_lunes.head()
    fig,ax=plt.subplots()
    barras=ax.bar(df_productos_lunes['nombre'], df_productos_lunes['cantidad'])
    ax.set_xlabel('Producto')
    ax.set_ylabel('Ventas')
    ax.set_title('Productos más vendidos el Sábado de la semana anterior')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('GraficosEstadisticos/DiasDeSemana/sabadoAnterior.png')
    plt.close()

    #Domingo
    query="select hv.IDproducto, p.nombre, hv.cantidad, t.dia_de_semana, t.semana from HechosVentas hv join Tiempo t on t.IDtiempo=hv.IDtiempo join Producto p on p.IDproducto=hv.IDproducto where semana=%s and dia_de_semana=%s group by hv.IDproducto order by cantidad desc"
    cursor.execute(query, (semana_anterior, "Sunday"))
    productos_lunes=cursor.fetchall()
    column_names=[i[0] for i in cursor.description]
    df_productos_lunes=pd.DataFrame(productos_lunes, columns =column_names)
    df_productos_lunes=df_productos_lunes.head()
    fig,ax=plt.subplots()
    barras=ax.bar(df_productos_lunes['nombre'], df_productos_lunes['cantidad'])
    ax.set_xlabel('Producto')
    ax.set_ylabel('Ventas')
    ax.set_title('Productos más vendidos el Domingo de la semana anterior')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('GraficosEstadisticos/DiasDeSemana/domingoAnterior.png')
    plt.close()
    
    print("Se han creado los gráficos de los productos más vendidos cada día de la semana anterior")

except Exception as e:
    print("Error al crear gráficos de productos más vendidos por día", e)
