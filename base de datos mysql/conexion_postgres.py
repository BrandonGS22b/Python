import psycopg2

conexion = psycopg2.connect(user='postgres',password='root',host='127.0.0.1',port='3703',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = input('Proporciona el valor id_pesona: ')
            cursor.execute(sentencia, (id_persona,))
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()