from django.db import models


class Tour(models.Model):
    name = models.CharField(verbose_name='Тур', max_length=55)
    description = models.TextField()
    duration = models.IntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    image = models.FileField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'

class TourImage(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tour_images')
    images = models.FileField(upload_to='images')

    def __str__(self):
        return self.tour.name

    class Meta:
        verbose_name = 'Тур фото'
        verbose_name_plural = 'Тур фотки'


class Order(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=55)
    surname = models.CharField(verbose_name='Фамилия', max_length=66)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=99)
    email = models.EmailField()
    tour = models.ForeignKey(Tour, verbose_name='тур', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество людей', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'