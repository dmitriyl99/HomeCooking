from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, SelectField, BooleanField, \
    PasswordField, FloatField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from flask_wtf.file import FileAllowed
from application.core.models import Dish, DishCategory
from application import trello_client
import settings
from flask_login import current_user


class CategoryForm(FlaskForm):
    name_ru = StringField('Название на русском', validators=[DataRequired('Укажите название категории на русском')])
    name_uz = StringField('Название на узбекском', validators=[DataRequired('Укажите название категории на узбексокм')])
    submit = SubmitField('Сохранить')

    def fill_from_object(self, category: DishCategory):
        self.name_ru.data = category.name
        self.name_uz.data = category.name_uz


class DishForm(FlaskForm):
    name_ru = StringField('Название на русском', validators=[DataRequired('Укажите название блюда на русском')])
    name_uz = StringField('Название на узбекском', validators=[DataRequired('Укажите название блюда на узбексокм')])
    description_ru = TextAreaField('Описание блюда на русском')
    description_uz = TextAreaField('Описание блюда на узбекском')
    category = SelectField('Категория', validators=[DataRequired('Укажите категорию')], coerce=int)
    price = StringField('Цена', validators=[DataRequired('Укажите цену')])
    image = FileField('Изображение',
                      validators=[FileAllowed(['png', 'jpg'],
                                              message='Разрешены только изображения форматов .jpg, .png')])
    delete_image = BooleanField('Удалить изображение')
    submit = SubmitField('Сохранить')

    def fill_from_object(self, dish: Dish):
        self.name_ru.data = dish.name
        self.name_uz.data = dish.name_uz
        self.description_uz.data = dish.description_uz
        self.description_ru.data = dish.description
        self.category.data = dish.category_id
        self.price.data = dish.price

    def validate_price(self, field):
        if not field.data.isdigit():
            raise ValidationError('Укажите числовое значение цены')
        if int(field.data) <= 0:
            raise ValidationError('Цена не может быть отрицательной или равной нулю')


class AdministratorEmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired('Укажите e-mail')])
    password = PasswordField('Пароль', validators=[DataRequired('Для смены e-mail необходима аутентификация')])
    submit = SubmitField('Изменить')

    def fill_from_current_user(self):
        self.email.data = current_user.email

    def validate_password(self, field):
        if not current_user.check_password(field.data):
            raise ValidationError('Указан неверный пароль')


class AdministratorPasswordForm(FlaskForm):
    current_password = PasswordField('Текущий пароль',
                                     validators=[DataRequired('Для смены пароля укажите текущий пароль')])
    new_password = PasswordField('Новый пароль', validators=[DataRequired("Введите новый пароль")])
    password_confirmation = PasswordField('Подтвердите новый пароль',
                                          validators=[EqualTo('new_password', 'Пароли должны совпадать')])
    submit = SubmitField('Изменить')


    def validate_password(self, field):
        if not current_user.check_password(field.data):
            raise ValidationError('Указан неверный пароль')


class DeliveryPriceForm(FlaskForm):
    first_3_km = StringField('Стоимость за первые три киллометра',
                             validators=[DataRequired('Укажите стоимость первых трёх километров')])
    others_km = StringField('Стоимость за остальной путь',
                            validators=[DataRequired('Укажите стоимость за остальные километры')])
    limit_price = StringField('Лимит стоимости доставки',
                              validators=[DataRequired('Укажите лимит цены на доставку')])
    submit = SubmitField('Сохранить')

    def validate_int_value(self, field):
        if not field.data.isdigit():
            raise ValidationError("Стоимость доставки должна быть указана в цифрах")
        value = int(field.data)
        if value <= 0:
            raise ValidationError('Стоимость доставки должна быть больше нуля')

    def fill_from_settings(self):
        delivery_cost = settings.get_delivery_cost()
        self.first_3_km.data = delivery_cost[0]
        self.others_km.data = delivery_cost[1]
        self.limit_price.data = settings.get_limit_delivery_price()
    
    def validate_first_3_km(self, field):
        self.validate_int_value(field)
    
    def validate_others_km(self, field):
        self.validate_int_value(field)
    
    def validate_limit_price(self, field):
        self.validate_int_value(field)


class CafeLocationForm(FlaskForm):
    latitude = FloatField('Широта', validators=[DataRequired("Укажите широту")])
    longitude = FloatField('Долгота', validators=[DataRequired('Укажите долготу')])
    submit = SubmitField('Сохранить')

    def fill_from_settings(self):
        coordinates = settings.get_cafe_coordinates()
        self.latitude.data = coordinates[0]
        self.longitude.data = coordinates[1]


class TrelloSettingsForm(FlaskForm):
    board_name = StringField('Название доски', validators=[DataRequired('Укажите название доски Trello')])
    list_name = StringField('Название списка', validators=[DataRequired('Укажите название списка Trello')])
    submit = SubmitField('Сохранить')

    def validate_board_name(self, field):
        if field.data == '':
            return
        all_boards = trello_client.list_boards(board_filter='open')
        try:
            list(filter(lambda b: b.name == field.data, all_boards))[0]
        except IndexError:
            raise ValidationError('Указанной доски не существует среди открытых')

    def validate_list_name(self, field):
        if self.board_name.data == '' or field.data == '':
            return
        all_boards = trello_client.list_boards(board_filter='open')
        try:
            board = list(filter(lambda b: b.name == self.board_name.data, all_boards))[0]
        except IndexError:
            return
        all_lists = board.open_lists()
        try:
            list(filter(lambda l: l.name == field.data, all_lists))[0]
        except IndexError:
            raise ValidationError('Указанного списка не существует среди открытых в доске %s' % board.name)

    def fill_from_settings(self):
        current_trello_settings = settings.get_trello_settings()
        if not current_trello_settings:
            return
        self.board_name.data = current_trello_settings[0]
        self.list_name.data = current_trello_settings[1]
