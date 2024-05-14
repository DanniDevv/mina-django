from django.db import models

# Modelo de Usuarios
class Usuarios(models.Model):
    user_id = models.AutoField(primary_key=True)
    codigo_usuario = models.CharField(max_length=10)
    correo = models.EmailField(max_length=100)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo_usuario

# Modelo de Resultados
class Resultados(models.Model):
    resultado_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    intentos = models.IntegerField()
    prueba_id = models.ForeignKey('Prueba', on_delete=models.CASCADE)

    def __str__(self):
        return f"Resultado {self.resultado_id} - Usuario {self.user_id}"

# Modelo de Prueba
class Prueba(models.Model):
    prueba_id = models.AutoField(primary_key=True)
    pregunta = models.TextField()
    respuestas = models.TextField()
    fecha = models.DateField()
    tiempo = models.TimeField()

    def __str__(self):
        return f"Prueba {self.prueba_id} - {self.pregunta[:50]}"

# Modelo de Confirmacion_riesgos
class Confirmacion_riesgos(models.Model):
    confir_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"Confirmacion {self.confir_id} - Usuario {self.user_id}"

# Modelo de EPPs
class EPPs(models.Model):
    epps_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha = models.DateField()
    eplista_id = models.ForeignKey('EPp_Lista', on_delete=models.CASCADE)

    def __str__(self):
        return f"EPPs {self.epps_id} - Usuario {self.user_id}"

# Modelo de EPp_Lista
class EPp_Lista(models.Model):
    eplista_id = models.AutoField(primary_key=True)
    lentes = models.BooleanField()
    casco = models.BooleanField()
    mameluco = models.BooleanField()
    mascarilla = models.BooleanField()
    guantes = models.BooleanField()
    zapatos = models.BooleanField()
    orejeras = models.BooleanField()

    def __str__(self):
        return f"EPlista {self.eplista_id}"
