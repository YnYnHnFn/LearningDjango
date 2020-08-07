from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render   # Added for this step


# Create your views here.

##def index(request):
##    return HttpResponse("Hello, Django!")
##↓↓
#def index(request):
#    now = datetime.now()
#    html_content = "<html><head><title>Hello, Django</title></head><body>"
#    html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
#    html_content += "</body></html>"
#    return HttpResponse(html_content)
#↓↓

#　見てわかるように、render の最初の引数は要求オブジェクトであり、
#　その後ろにはアプリの templates フォルダー内の一時ファイルへの相対パスが続きます。 
#　必要に応じて、ビューに対応する名前を付けたテンプレートがサポートされます。
#　render の 3 つ目の引数は、テンプレートが参照する変数のディクショナリです。 
#　テンプレートの変数が {{ object.property }} を参照できる場合、ディクショナリに
#　オブジェクトを含めることができます。


def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )


def about(request):
    return render(
        request,
        "HelloDjangoApp/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )
