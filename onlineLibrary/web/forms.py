from django import forms

from onlineLibrary.web.models import Profile, Book


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class BaseBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class EditBookForm(BaseBookForm):
    pass


class EditProfileForm(BaseProfileForm):
    pass


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_fields_to_disabled()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def set_fields_to_disabled(self):
        for _, field in self.fields.items():
            field.disabled = True
