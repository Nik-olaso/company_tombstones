from django.db import models


class Users(models.Model):
    user_id = models.IntegerField(
        verbose_name="ID пользователя",
        blank=True,
        null=True
    )
    first_name = models.CharField(
        verbose_name="Имя пользователя",
        max_length=200,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        verbose_name="Фамилия пользователя",
        max_length=200,
        blank=True,
        null=True,
    )
    on_admin = models.BooleanField(
        verbose_name="Является ли админом",
        blank=True,
        null=True,
    )

    def str(self):
        return self.title

    objects = models.Manager()


class Tombstone(models.Model):
    tombstone_id = models.IntegerField(
        verbose_name="ID надгробия",
        blank=True,
    )
    create_date = models.DateField(
        verbose_name="Дата создания",
        blank=True,
        null=True,
    )
    user_id = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    user_role = models.CharField(
        max_length=200,
        verbose_name="Роль пользователя",
        blank=True,
        null=True,
    )
    company_name = models.CharField(
        max_length=200,
        verbose_name="Название компании",
        blank=True,
        null=True,
    )
    birth_year = models.DateField(
        verbose_name="Год создания",
        blank=True,
        null=True,
    )
    death_year = models.DateField(
        verbose_name="Год смерти",
        blank=True,
        null=True,
    )
    alternate_name = models.CharField(
        max_length=200,
        verbose_name="Алльтернативное название",
        blank=True,
        null=True,
    )
    link = models.CharField(
        max_length=200,
        verbose_name="Ссылка на компанию",
        blank=True,
        null=True,
    )
    characteristic = models.TextField(
        verbose_name="Характеристики компании",
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name="Описание компании",
        blank=True,
        null=True,
    )
    death_cause = models.TextField(
        verbose_name="Причина смерти компании",
        blank=True,
        null=True,
    )
    count_employee = models.IntegerField(
        verbose_name="Количество сотрудников",
        blank=True,
        null=True,
    )
    revenue = models.IntegerField(
        verbose_name="Доход компании",
        blank=True,
        null=True,
    )
    score_company = models.IntegerField(
        verbose_name="Счет компании",
        blank=True,
        null=True,
    )

    def str(self):
        return self.title

    objects = models.Manager()
