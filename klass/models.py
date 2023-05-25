from django.db import models
from .utils import validate_phone_number

# Create your models here.

class Subject(models.Model): 
      name = models.CharField(max_length=100, verbose_name="название урока")
      
      def __str__(self):
            return self.name
      
class Teacher(models.Model): 
      firstname = models.CharField(max_length=100, verbose_name="имя")
      lastname = models.CharField(max_length=100, verbose_name="фамилия")
      email = models.EmailField(max_length=100, verbose_name="email",
                                    help_text = "Введите ваш email")
      phone = models.CharField(max_length=100, verbose_name="телефон",
                               validators=[validate_phone_number],)
      adress = models.CharField(max_length=100, verbose_name="адресс")
      subject = models.ForeignKey(Subject, on_delete=models.PROTECT,
                                  verbose_name="урок")
      created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистраций")
      
      @property # Обьединение модели 
      def full_name(self):
            return f"{self.firstname} {self.lastname}"
      
      def __str__(self) -> str: # Отображение модели
            return self.lastname + " " + self.firstname + " " 
      
      class Meta: # Метаданные модели
            verbose_name = "Преподаватель"
            verbose_name_plural = "Преподаватели"
            
      
class Klass(models.Model): 
      number = models.PositiveSmallIntegerField(verbose_name="Номер класса")
      teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT,
                                  verbose_name="преподаватель")
      
      def __str__(self) -> str: # Отображение модели
            return f"Номер класса: {self.number} | {self.teacher}"
      
      class Meta: # Метаданные модели
            verbose_name = "Класс"
            verbose_name_plural = "Классы"
            
            
class Student(models.Model):
      firstname = models.CharField(max_length=100, verbose_name="имя")
      lastname = models.CharField(max_length=100, verbose_name="фамилия")
      email = models.EmailField(max_length=100, verbose_name="email",
                                    help_text = "Введите ваш email")
      phone = models.CharField(max_length=100, verbose_name="телефон")
      adress = models.CharField(max_length=100, verbose_name="адресс")
      teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT,
                                  verbose_name="Преподаватель")
      
      
      @property # Обьединение модели 
      def full_name(self):
            return f"{self.firstname} {self.lastname}"
      
      def __str__(self) -> str: # Отображение модели
            return self.lastname + " " + self.firstname + " | "   + self.teacher
      
      class Meta: # Метаданные модели
            verbose_name = "Ученик(ца)"
            verbose_name_plural = "Ученики(цы)"