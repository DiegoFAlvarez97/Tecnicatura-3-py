import psycopg2 as bd # Esto es para poder conectarnos a Postgre

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')

try:
    conexion.autocommit = False # Con True es mala practica, no deberia estar. Se inicia la transaccion
    cursor = conexion.cursor()
    sentecia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ('Jorge', 'Prol', 'Jprol@mail.com')
    cursor.execute(sentecia, valores)

    sentecia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Juan Carlos', 'Perez', 'juanCarlosPz@mail.com', 1)
    cursor.execute(sentecia, valores)

    conexion.commit() # Hacemos el commit manualmente, SE cierra la transaccion
    print('Termina la transaccion')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()

