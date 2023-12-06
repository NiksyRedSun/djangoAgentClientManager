from django.db import models

# Create your models here.


class Agent(models.Model):

    class Membership(models.IntegerChoices):
        OUT = 0, 'исключен'
        IN = 1, 'состоит в организации'
    membership_choices_dict = dict(Membership.choices)


    class Status(models.IntegerChoices):
        DEATH = 0, 'мертв'
        ALIVE = 1, 'жив'
    status_choices_dict = dict(Status.choices)


    class EquipmentLevel(models.IntegerChoices):
        FIRST = 1, 'ножи, дубинки и скрытое огнестрельное оружие'
        SECOND = 2, 'пистолеты, кастеты и компактные пистолеты-пулеметы'
        THIRD = 3, 'полуавтоматические винтовки, топоры и дымовые гранаты'
        FOURTH = 4, 'снайперские винтовки, широкие клинки и метательные ножи'
        FIFTH = 5, 'штурмовые винтовки, бронебойные дротики и дробовики'
        SIXTH = 6, 'специальные винтовки с подавлением звука, ядовитые стрелы и технологически продвинутые маскировочные устройства'
    equipment_level_choices_dict = dict(EquipmentLevel.choices)



    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    membership = models.BooleanField(choices=Membership.choices, default=Membership.IN)
    start_membership = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(choices=Status.choices, default=Status.ALIVE)
    money = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    equipment_level = models.IntegerField(choices=EquipmentLevel.choices, default=EquipmentLevel.FIRST)

    objects = models.Manager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}, возраст: {self.age}, деньги: {self.money}, опыт: {self.exp},\n' \
               f'статус: {self.status_choices_dict[self.status]}, членство: {self.membership_choices_dict[self.membership]},\n' \
               f'уровень снаряжения: {self.equipment_level_choices_dict[self.equipment_level]}'




class Client(models.Model):

    class Status(models.IntegerChoices):
        DEATH = 0, 'мертв'
        ALIVE = 1, 'жив'
    status_choices_dict = dict(Status.choices)


    class SecurityLevel(models.IntegerChoices):
        FIRST = 1, 'цель с минимальной охраной, неосведомлена о возможной опасности'
        SECOND = 2, 'цель, которая может иметь небольшую охрану, но её легко обойти'
        THIRD = 3, 'цель, защищена опытной охраной и базовыми техническими средствами'
        FOURTH = 4, 'цель с высокой степенью защиты, включая физическую, электронную и техническую безопасность'
        FIFTH = 5, 'цель, охраняемая профессиональными телохранителями, современными системами безопасности и тщательной разведкой'
        SIXTH = 6, 'высокопоставленная личность, государственного значения, с максимальной защитой, ' \
                   'включая военные силы, секретные службы и высокотехнологичные системы безопасности'
    security_level_choices_dict = dict(SecurityLevel.choices)


    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    price = models.IntegerField(default=500)
    exp = models.IntegerField(default=500)
    security_level = models.IntegerField(choices=SecurityLevel.choices, default=SecurityLevel.FIRST)
    status = models.BooleanField(choices=Status.choices, default=Status.ALIVE)
    killed_by = models.OneToOneField(Agent, on_delete=models.DO_NOTHING, blank=True, null=True)
    death_time = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}, возраст: {self.age}, ' \
               f'награда: {self.price}, опыт за убийство: {self.exp}, статус: {self.status_choices_dict[self.status]},\n' \
               f'уровень защиты: {self.security_level_choices_dict[self.security_level]}'