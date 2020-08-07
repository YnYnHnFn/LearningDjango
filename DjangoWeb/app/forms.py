"""
Definition of forms.

このフォーム クラスは AuthenticationForm (django.contrib.auth.views)
から派生し、明示的にユーザー名とパスワードのフィールドをオーバーライド
して、プレースホルダ― テキストを追加します。 
Visual Studio テンプレートには、パスワード強度の検証を追加するなど、
必要に応じてフォームをカスタマイズすることを予想して、この明示的な
コードが含まれています。

"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):

    """Authentication form which uses boostrap CSS."""

    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))

    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
