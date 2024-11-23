import MySQLdb
import sys
import pandas as pd
from datetime import datetime
import locale

#Mis credenciales (con cuidado que te veo)
miusuario='novato'
contraseña='contraseñamariadb'
mihost='localhost'

#Conexión con las bases de datos de origen y destino (estrella)
try:
    conexionDBOrigen=MySQLdb.connect(
            user=miusuario,
            password=contraseña,
            host=mihost,
            database='farmacia')
    print("Conexión exitosa a la base de datos de origen")
except Exception as e:
    print("Error al conectarse a la base de datos de origen", e)
    sys.exit(1)

try:
    conexionDBDestino=MySQLdb.connect(
            user=miusuario,
            password=contraseña,
            host=mihost,
            database='farmaciaETL')
    print("Conexión exitosa a la base de datos de destino")
except Exception as e:
    print("Error al conectarse a la base de datos de destino", e)
    sys.exit(1)

#obtengo los datos de la base de datos origen y los subo a la base de datos destino (Modelo estrella). No quiero tener muchas variables, por eso reutilizaré la misma
try:
    #Creo los cursores de origen y destino, ya que estos me servirán luego
    cursorOrigen=conexionDBOrigen.cursor()
    cursorDestino=conexionDBDestino.cursor()

    cursorDestino.execute("delete from HechosVentas")
    conexionDBDestino.commit()
    #Tabla Producto
    query="select IDproducto, nombre, precio from Producto"
    cursorOrigen.execute(query)
    columns=[desc[0] for desc in cursorOrigen.description]
    data=cursorOrigen.fetchall()
    dfProducto=pd.DataFrame(list(data), columns=columns)
    
    cursorDestino.execute("delete from Producto")
    conexionDBDestino.commit()
    for _, row in dfProducto.iterrows():
        queryInsertar="insert into Producto(IDproducto, nombre, precio) values (%s, %s, %s)"
        cursorDestino.execute(queryInsertar, (row['IDproducto'], row['nombre'], row['precio']))
    conexionDBDestino.commit()
    print("Datos de Producto registrados correctamente")


    #Tabla Empleado
    query="select IDempleado, nombre, documento, sucursal from Empleado"
    cursorOrigen.execute(query)
    columns=[desc[0] for desc in cursorOrigen.description]
    data=cursorOrigen.fetchall()
    dfEmpleado=pd.DataFrame(list(data), columns=columns)
    
    cursorDestino.execute("delete from Empleado")
    conexionDBDestino.commit()
    for _, row in dfEmpleado.iterrows():
        queryInsertar="insert into Empleado(IDempleado, nombre, documento, sucursal) values (%s, %s, %s, %s)"
        cursorDestino.execute(queryInsertar, (row['IDempleado'], row['nombre'], row['documento'], row['sucursal']))
    conexionDBDestino.commit()
    print("Datos de Empleado registrados correctamente")


    #Tabla Proveedor
    query="select IDproveedor, nombre, ruc, direccion from Proveedor"
    cursorOrigen.execute(query)
    columns=[desc[0] for desc in cursorOrigen.description]
    data=cursorOrigen.fetchall()
    dfProveedor=pd.DataFrame(list(data), columns=columns)

    cursorDestino.execute("delete from Proveedor")
    conexionDBDestino.commit()
    for _, row in dfProveedor.iterrows():
        queryInsertar="insert into Proveedor(IDproveedor, nombre, ruc, direccion) values (%s, %s, %s, %s)"
        cursorDestino.execute(queryInsertar, (row['IDproveedor'], row['nombre'], row['ruc'], row['direccion']))
    conexionDBDestino.commit()
    print("Datos de Proveedor registrados correctamente")


    #Tabla Tiempo
    query="select vp.IDventa, v.fecha from Venta_Producto vp inner join Venta v on vp.IDventa=v.IDventa group by v.fecha order by vp.IDventa"
    cursorOrigen.execute(query)
    datos=cursorOrigen.fetchall()
    datos_procesados=[]
    for item in datos:
        IDtiempo=item[0]
        fecha=item[1]
        año=fecha.year
        trimestre=0
        mes=fecha.month
        semana=0
        dia=fecha.day
        dia_de_semana='dia'
        horario='horario'

        if mes>=1 and mes<=3:
            trimestre=1
        if mes>=4 and mes<=6:
            trimestre=2
        if mes>=7 and mes<=9:
            trimestre=3
        if mes>=10 and mes<=12:
            trimestre=4
       
        semana=fecha.isocalendar()[1]

        dia_de_semana=fecha.strftime("%A")
        
        hora=fecha.hour
        if 6<=hora<12:
            horario='mañana'
        elif 12<=hora<20:
            horario='tarde'
        elif 20<=hora<24:
            horario='noche'
        else:
            horario='madrugada'

        datos_procesados.append((IDtiempo, fecha, año, trimestre, mes, semana, dia, dia_de_semana, horario))

    query="insert into Tiempo (IDtiempo, fecha, año, trimestre, mes, semana, dia, dia_de_semana, horario) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursorDestino.execute("delete from Tiempo")
    conexionDBDestino.commit()
    cursorDestino.executemany(query, datos_procesados)
    conexionDBDestino.commit()
    print("Datos de Tiempo insertados correctamente")

    #Tabla Hechos Ventas
    query="select vp.IDventa, prod.IDproveedor, v.IDempleado, vp.IDproducto, prod.precio, vp.cantidad from Venta_Producto vp inner join Producto prod on prod.IDproducto=vp.IDproducto inner join Venta v on vp.IDventa = v.IDventa"
    cursorOrigen.execute(query)
    columns=[desc[0] for desc in cursorOrigen.description]
    data=cursorOrigen.fetchall()
    dfEmpleado=pd.DataFrame(list(data), columns = columns)

    cursorDestino.execute("delete from HechosVentas")
    conexionDBDestino.commit()
    for item in data:
        precio=item[4]
        cantidad=item[5]
        total=round(precio*cantidad,2)
        queryInsertar="insert into HechosVentas(IDtiempo, IDproveedor, IDempleado, IDproducto, precio, cantidad, precio_total) values (%s, %s, %s, %s, %s, %s, %s)"
        cursorDestino.execute(queryInsertar, (item[0], item[1], item[2], item[3], precio, cantidad, total))
    conexionDBDestino.commit()
    print("Datos de HechosVentas insertados correctamente")
    conexionDBOrigen.close()
    conexionDBDestino.close()
except Exception as e:
    print("Error al intentar insertar los datos: ", e)
