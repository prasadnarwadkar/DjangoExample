from django import forms


class NameForm(forms.Form):
    avenger_id = forms.CharField(label="Avenger ID", min_length=36, max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly', 'size':40, 'id': 'avenger_id'}))
    avenger_name = forms.CharField(label="Avenger Name", max_length=100,widget=forms.TextInput(attrs={ 'id': 'avenger_name'}))
    disable_save = str
    hint_text = str
class NewNameForm(forms.Form):
    avenger_name = forms.CharField(label="Avenger Name", max_length=100,widget=forms.TextInput(attrs={ 'id': 'avenger_name'}))
    disable_save = str
class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=100,widget=forms.TextInput(attrs={ 'type':"text", 'id': 'username'}))
    password = forms.CharField(label="Password", max_length=100,widget=forms.TextInput(attrs={ 'type':"password", 'id': 'password'}))