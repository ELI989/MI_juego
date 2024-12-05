import sqlite3

def mostrar_resultados():
    """Muestra todos los resultados guardados en la base de datos."""
    # Establece conexión con la base de datos
    connection = sqlite3.connect("juego.db")
    cursor = connection.cursor()
    
    # Ejecuta la consulta para obtener todos los resultados
    cursor.execute('SELECT * FROM resultados')
    resultados = cursor.fetchall()
    
    # Imprime cada resultado
    for resultado in resultados:
        print(f'ID: {resultado[0]}, Fecha y Hora: {resultado[3]}, Tiempo Perdido: {resultado[4]} segundos')
    
    # Cierra la conexión
    connection.close()
