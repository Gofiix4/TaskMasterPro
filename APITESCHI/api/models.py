from django.db import models

# Create your models here.
class Genero(models.Model):
    idGenero = models.AutoField(primary_key=True,db_column='idGenero')
    tipoGenero = models.TextField(db_column='tipoGenero')
    class Meta:
        db_table='Generos'

class Alumno(models.Model):
    idAlumno = models.IntegerField(primary_key=True,db_column='idAlumno')
    nameAlumno = models.CharField(max_length=100,db_column='nameAlumno')
    class Meta:
        db_table='Alumnos'

class alumno_has_genero(models.Model):
    idalumno_has_genero = models.AutoField(primary_key=True,default=1,db_column='idalumno_has_genero')
    fk_alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE,db_column='fk_alumno')
    fk_genero = models.ForeignKey(Genero,on_delete=models.CASCADE,db_column='fk_genero')
    class Meta:
        db_table='alumno_has_genero'

class Usuarios(models.Model):
    idUsuario = models.AutoField(primary_key=True,db_column='idUsuario')
    Nombre = models.CharField(max_length=45,default='nombre',db_column='Nombre')
    ApellidoP = models.CharField(max_length=45,default='apellidop',db_column='ApellidoP')
    ApellidoM = models.CharField(max_length=45,default='apellidom',db_column='ApellidoM')
    Fecha_nacimiento = models.DateField(default='2000/01/01',db_column='Fecha_nacimiento')
    Telefono = models.IntegerField(default=0,db_column='Telefono')
    Correo = models.EmailField(max_length=50,default='algo@algo.algo',db_column='Correo')
    Contrasena = models.CharField(max_length=64,default='contra123',db_column='Contrasena')
    class Meta:
        db_table='Usuarios'

class Tareas(models.Model):
    idTarea = models.AutoField(primary_key=True,db_column='idTarea')
    Titulo = models.CharField(max_length=50,default='Titulo',db_column='Titulo')
    Descripcion = models.CharField(max_length=200,default='Descripcion',db_column='Descripcion')
    Fecha_creacion = models.DateField(default='2000-01-01',db_column='Fecha_creacion')
    Fecha_vencimiento = models.DateField(default='2000-01-01',db_column='Fecha_vencimiento')
    Status = models.CharField(max_length=15,default='Pendiente',db_column='Status')
    Prioridad = models.CharField(max_length=10,default='Baja',db_column='Prioridad')
    fk_Usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE,db_column='fk_Usuario')
    class Meta:
        db_table='Tareas'

class Lista_tareas(models.Model):
    idLista = models.AutoField(primary_key=True,db_column='idLista')
    Nombre = models.CharField(max_length=45,default='Nombre',db_column='Nombre')
    Descripcion = models.CharField(max_length=200,default='Descripcion',db_column='Descripcion')
    fk_Usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE,db_column='fk_Usuario')
    class Meta:
        db_table='Lista_tareas'

class Listas_has_tareas(models.Model):
    idListas_has_tareas = models.AutoField(primary_key=True,default=1,db_column='idListas_has_tareas')
    fk_Lista = models.ForeignKey(Lista_tareas,on_delete=models.CASCADE,db_column='fk_Lista')
    fk_Tarea = models.ForeignKey(Tareas,on_delete=models.CASCADE,db_column='fk_Tarea')
    class Meta:
        db_table='Listas_has_tareas'

class Etiquetas(models.Model):
    idEtiqueta = models.AutoField(primary_key=True,db_column='idEtiqueta')
    Nombre = models.CharField(max_length=20,default='Nombre',db_column='Nombre')
    Descripcion = models.CharField(max_length=100,default='Descripcion',db_column='Descripcion')
    class Meta:
        db_table='Etiquetas'

class Tareas_has_etiquetas(models.Model):
    idTareas_has_etiquetas = models.AutoField(primary_key=True,default=1,db_column='idTareas_has_etiquetas')
    fk_Tarea = models.ForeignKey(Tareas,on_delete=models.CASCADE,db_column='fk_Tarea')
    fk_Etiqueta = models.ForeignKey(Etiquetas,on_delete=models.CASCADE,db_column='fk_Etiqueta')
    class Meta:
        db_table='Tareas_has_etiquetas'