"""
Definition of urls for DjangoWeb.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [

    path('', views.home, name='home'),

    path('contact/', views.contact, name='contact'),

    path('about/', views.about, name='about'),

    #組み込みの Django ビューを使用します。
    path('login/',
         LoginView.as_view
         (
            # template_name は、ログイン ページ用のテンプレート (この場合は templates/app/login.html) を特定します。
            # extra_context プロパティは、テンプレートに指定された既定のコンテキスト データに追加されます。 
            # authentication_form は、テンプレートに form オブジェクトとして示される、ログインに使用するフォーム クラスを定義します。
            # 既定値は AuthenticationForm (django.contrib.auth.views より) です。
            # Visual Studio プロジェクト テンプレートでは代わりに、アプリの forms.py ファイルに定義された次のフォームを使用します。

             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),

    #組み込みの Django ビューを使用します。
    #path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    path('logout/', 
         LogoutView.as_view
        (
            template_name='app/loggedoff.html',
            # 'next_page': '/',
        ),
        name='logout'),


    path('admin/', admin.site.urls),

]
