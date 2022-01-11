from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField, widgets
from wtforms.validators import DataRequired

data = [('batonas', 'Batonas'), ('suris', 'Sūris'), ('sviestas', 'Sviestas'), ('daktariska_desra', 'Daktariška dešra'), ('kopustai', 'Kopūstai')]


class FilterRecipesForm(FlaskForm):
    select_ingredients = SelectMultipleField('Pasirinkite ingredientus:', choices=data, option_widget=widgets.CheckboxInput(), widget=widgets.ListWidget(prefix_label=False) )
    search = SubmitField('Ieškoti')
