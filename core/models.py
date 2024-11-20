from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    category = models.CharField(max_length=100)
    harvest_date = models.DateField()

    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    location = models.CharField(max_length=255)
    update_date = models.DateTimeField(auto_now=True)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Inventario de {self.Product.name}"
    
class Sales(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    quantity = models.IntegerField()
    total_price = models.FloatField()
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta de {self.quantity} unidades de {self.Product.name}"

class RegistrationWeight(models.Model):
    id = models.AutoField(primary_key=True)
    weight = models.FloatField()
    date = models.DateField()
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Registro de peso: {self.weight} kg para {self.Product.name}"

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    creation_date = models.DateField()
    details = models.TextField()

    def __str__(self):
        return f"Reporte {self.type} creado el {self.creation_date}"

class alert(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    date = models.DateField()
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Alerta: {self.mensaje} para {self.Product.name}"
