calificacion = float(input("Dame una calificacion: "))

print('Dame la asistencia: 1 si asitio o 0 si no asistió')

asistencia = int(input())

if(calificacion > 9.0 and asistencia == 1):
    print("La calificacion es A Excelente con Mencion Honorifica.")
elif((calificacion > 9.0 and asistencia != 1)):
    print("La calificacion es A Excelente.")
elif(calificacion > 8.0 and asistencia == 1):
    print("La calificacion es B Muy bien con Mención.")
elif(calificacion > 8.0 and asistencia != 1):
    print("La calificacion es B Muy bien.")
elif(calificacion == 7.5):
    print("La calificacion es C Bien.")
else:
    print("La calificacion es R Reprobado. Lo siento mucho.")
# Fin del if.

