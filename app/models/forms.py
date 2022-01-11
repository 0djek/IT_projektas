from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, TextAreaField, BooleanField, IntegerField, DecimalField, FormField, FieldList, Form, HiddenField, SelectField
from wtforms.validators import InputRequired, EqualTo, Email, ValidationError, Length, Optional, NumberRange
import database_python as db


class FilterItemForm(Form):
    item = DecimalField("item", validators=[Optional(), NumberRange(min=0, message="Mažiausias įmanomas skaičius yra %(min)s")])
    unit = StringField("unit", validators=[Optional()])
    hidden_seo = HiddenField("seo_title", validators=[Optional()])


class FilterForm(FlaskForm):
    items = FieldList(FormField(FilterItemForm))
    search = SubmitField("Ieškoti")


class RegisterForm(FlaskForm):
    username = StringField("Slapyvardis", validators=[InputRequired("Prašome įvesti norimą vartotojo vardą."), Length(min=5, max=20, message="Ilgis turi būti tarp %(min)s ir %(max)s simbolių")])
    password = PasswordField("Slaptažodis", validators=[InputRequired("Prašome įvesti norimą naudoti slaptažodį."), Length(min=5, max=12, message="Ilgis turi būti tarp %(min)s ir %(max)s simbolių")])
    password_repeat = PasswordField("Pakartoti slaptažodį", validators=[InputRequired("Prašome įvesti slaptažodį dar kartą."), EqualTo("password", "Privalo atitikti slaptažodžio lauką."), Length(min=5, max=12, message="Ilgis turi būti tarp %(min)s ir %(max)s simbolių")])
    email = EmailField("Elektroninis paštas", validators=[InputRequired("Prašome įvesti savo el. paštą."), Email("Prašome įvesti el. paštą naudodami el. pašto formatą."), Length(min=5, max=30, message="Ilgis turi būti tarp %(min)s ir %(max)s simbolių")])

    def validate_username(self, username):
        if db.is_username(username.data):
            raise ValidationError("Prašome pasirinkti kitokį slapyvardį.")

    def validate_email(self, email):
        if db.is_email(email.data):
            raise ValidationError("Prašome pasirinkti kitokį el. paštą.")
    register = SubmitField("Registruotis")


class LoginForm(FlaskForm):
    username = StringField("Slapyvardis", validators=[InputRequired("Prašome įvesti savo slapyvardį."), Length(min=5, max=20, message="Ilgis turi būti tarp %(min)s ir %(max)s simbolių")])
    password = PasswordField("Slaptažodis", validators=[InputRequired("Prašome įvesti savo slaptažodį."), Length(min=5, max=12, message="Ilgis turi būti tarp %(min)s ir %(max)s simbolių")])
    login = SubmitField("Prisijungti")


class RecipeBeforeForm(FlaskForm):
    step_count = IntegerField("Žingsnių skaičius", validators=[InputRequired("Prašome įrašyti žingsnių skaičių."), NumberRange(min=1, message="Mažiausias įmanomas skaičius yra %(min)s")])
    ingredient_count = IntegerField("Ingredientų skaičius", validators=[InputRequired("Prašome įrašyti Ingredientų skaičių."), NumberRange(min=1, message="Mažiausias įmanomas skaičius yra %(min)s")])
    create = SubmitField("Sukurti receptą")


class RecipeStepForm(Form):
    title = StringField("Pavadinimas", validators=[InputRequired("Prašome įrašyti recepto žingsnio pavadinimą."), Length(min=4, max=40, message="Ilgis turi būti tarp %(min)s ir %(max)s simbolių")])
    seo_title = StringField("SEO pavadinimas", validators=[InputRequired("Prašome įrašyti recepto žingsnio pavadinimą, kuris bus naudojamas nuorodose."), Length(min=4, max=40, message="Ilgis turi būti tarp %(min)s ir %(max)s simbolių")])
    step_description = TextAreaField("Aprašymas")
    order = HiddenField("Žingsnio eilė", validators=[Optional()])


class RecipeIngredientForm(Form):
    ingredient = SelectField("Ingredientas", validate_choice=False)
    ingredient_unit = StringField("unit", validators=[Optional()])
    quantity = DecimalField("Kiekis", validators=[Optional("Prašome įrašyti reikiamą ingrediento kiekį."), NumberRange(min=1, message="Mažiausias įmanomas skaičius yra %(min)s")])


class RecipeForm(FlaskForm):
    title = StringField("Pavadinimas", validators=[InputRequired("Prašome įrašyti recepto pavadinimą."), Length(min=5, max=40, message="Ilgis turi būti tarp %(min)s ir %(max)s simbolių")])
    seo_title = StringField("SEO pavadinimas", validators=[InputRequired("Prašome įrašyti recepto pavadinimą, kuris bus naudojamas nuorodose."), Length(min=5, max=40, message="Ilgis turi būti tarp %(min)s ir %(max)s simbolių")])
    description = TextAreaField("Aprašymas", validators=[InputRequired("Prašome įrašyti recepto aprašymą.")])
    description_exerpt = TextAreaField("Sutrumpintas aprašymas", validators=[InputRequired("Prašome įrašyti recepto sutrumpintą aprašymą.")])
    recipe_steps = FieldList(FormField(RecipeStepForm))
    recipe_ingredients = FieldList(FormField(RecipeIngredientForm))
    create = SubmitField("Sukurti receptą")


class RecipeCreatorForm(FlaskForm):
    recipe_creators = SelectField("Receptų kūrėjas", validate_choice=False)
    filter = SubmitField("Rūšiuoti receptų kūrėjus")


class IngredientForm(FlaskForm):
    title = StringField("Pavadinimas", validators=[InputRequired("Prašome įrašyti ingrediento pavadinimą."), Length(min=5, max=40, message="Ilgis turi būti tarp %(min)s ir %(max)s simbolių")])
    seo_title = StringField("SEO pavadinimas", validators=[InputRequired("Prašome įrašyti ingrediento pavadinimą, kuris bus naudojamas nuorodose."), Length(min=5, max=40, message="Ilgis turi būti tarp %(min)s ir %(max)s simbolių")])
    unit = StringField("Matavimo vienetai", validators=[InputRequired("Prašome įrašyti matavimo vienetus."), Length(min=1, max=15, message="Ilgis turi būti tarp %(min)s ir %(max)s simbolių")])
    create = SubmitField('Sukurti ingredientą')

    def __init__(self, old_seo_title=None, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)
        self.old_seo_title = old_seo_title

    def validate_seo_title(self, seo_title):
        if self.old_seo_title != seo_title.data and db.is_ingredient_single_seo_title(seo_title.data):
            raise ValidationError("Toks ingrediento SEO pavadinimas jau egzistuoja")


class IngredientSuggestionForm(FlaskForm):
    title = StringField("Pavadinimas", validators=[InputRequired("Prašome įrašyti ingrediento pavadinimą."), Length(min=5, max=40, message="Ilgis turi būti tarp %(min)s ir %(max)s simbolių")])
    seo_title = StringField("SEO pavadinimas", validators=[InputRequired("Prašome įrašyti ingrediento pavadinimą, kuris bus naudojamas nuorodose."), Length(min=5, max=40, message="Ilgis turi būti tarp %(min)s ir %(max)s simbolių")])
    unit = StringField("Matavimo vienetai", validators=[InputRequired("Prašome įrašyti matavimo vienetus."), Length(min=1, max=15, message="Ilgis turi būti tarp %(min)s ir %(max)s simbolių")])
    create = SubmitField('Pasiūlyti ingredientą')

    def validate_seo_title(self, seo_title):
        if db.is_ingredient_suggestion_single_seo_title(seo_title.data):
            raise ValidationError("Toks ingrediento SEO pavadinimas jau egzistuoja")
