## Brew'vin

## List of Content
- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)

### Tugas 2
- ##### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    1. Saya membuat direktori baru bernama brewvin sebagai direktori utama, kemudian membuat virtual environment di dalamnya.
    2. Saya membuat requirements.txt yang diperlukan untuk menjalankan app django. Isi dari requirements.txt adalah sebagai berikut:
        ```
        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3
        ```
    3. Saya install semua dependencies yang diperlukan dari requirements.txt dengan command:
    ```pip install -r requirements.txt```
    4. Setelah semua dependencies selesai diinstall, buat proyek Django bernama brewvin dengan command:
    ```django-admin startproject shopping_list .```
    5. Untuk mempermudah proses deployment, maka semua host diizinkan untuk mengakses app untuk sementara waktu.
    ```ALLOWED_HOSTS = ["*"]``` pada `settings.py`
    6. Menambahkan file .gitignore dengan isi:
        ```
        # Django
        *.log
        *.pot
        *.pyc
        __pycache__
        db.sqlite3
        media

        # Backup files
        *.bak 

        # If you are using PyCharm
        # User-specific stuff
        .idea/**/workspace.xml
        .idea/**/tasks.xml
        .idea/**/usage.statistics.xml
        .idea/**/dictionaries
        .idea/**/shelf

        # AWS User-specific
        .idea/**/aws.xml

        # Generated files
        .idea/**/contentModel.xml

        # Sensitive or high-churn files
        .idea/**/dataSources/
        .idea/**/dataSources.ids
        .idea/**/dataSources.local.xml
        .idea/**/sqlDataSources.xml
        .idea/**/dynamic.xml
        .idea/**/uiDesigner.xml
        .idea/**/dbnavigator.xml

        # Gradle
        .idea/**/gradle.xml
        .idea/**/libraries

        # File-based project format
        *.iws

        # IntelliJ
        out/

        # JIRA plugin
        atlassian-ide-plugin.xml

        # Python
        *.py[cod] 
        *$py.class 

        # Distribution / packaging 
        .Python build/ 
        develop-eggs/ 
        dist/ 
        downloads/ 
        eggs/ 
        .eggs/ 
        lib/ 
        lib64/ 
        parts/ 
        sdist/ 
        var/ 
        wheels/ 
        *.egg-info/ 
        .installed.cfg 
        *.egg 
        *.manifest 
        *.spec 

        # Installer logs 
        pip-log.txt 
        pip-delete-this-directory.txt 

        # Unit test / coverage reports 
        htmlcov/ 
        .tox/ 
        .coverage 
        .coverage.* 
        .cache 
        .pytest_cache/ 
        nosetests.xml 
        coverage.xml 
        *.cover 
        .hypothesis/ 

        # Jupyter Notebook 
        .ipynb_checkpoints 

        # pyenv 
        .python-version 

        # celery 
        celerybeat-schedule.* 

        # SageMath parsed files 
        *.sage.py 

        # Environments 
        .env 
        .venv 
        env/ 
        venv/ 
        ENV/ 
        env.bak/ 
        venv.bak/ 

        # mkdocs documentation 
        /site 

        # mypy 
        .mypy_cache/ 

        # Sublime Text
        *.tmlanguage.cache 
        *.tmPreferences.cache 
        *.stTheme.cache 
        *.sublime-workspace 
        *.sublime-project 

        # sftp configuration file 
        sftp-config.json 

        # Package control specific files Package 
        Control.last-run 
        Control.ca-list 
        Control.ca-bundle 
        Control.system-ca-bundle 
        GitHub.sublime-settings 

        # Visual Studio Code
        .vscode/* 
        !.vscode/settings.json 
        !.vscode/tasks.json 
        !.vscode/launch.json 
        !.vscode/extensions.json 
        .history
        ```
    7. Aktifkan virtual environment untuk memulai proses development.
    8. Buat aplikasi baru bernama `main` dengan command:
    ```python manage.py startapp main```
    9. Tambahkan app `main` sebagai installed apps di `settings.py` dalam direktori proyek `brewvin`.
    10. Membuat model bernama `Item` yang merupakan model untuk biji kopi dengan attributes `name: CharField, amount: IntegerField, description: TextField, taste: TextField`.
    11. Buat migrasi model yang baru dibuat dengan command:
    ```python manage.py makemigrations```
    12. Jalankan proses migrasi
    ```python manage.py migrate```
    13. Buat view sementara yang berisi:
        ```
        from django.shortcuts import render

        def show_main(request):
            context = {
                'app_name': 'Brew\'vin',
                'name': 'Arvin',
                'class': 'PBP D',
            }

            return render(request, "main.html", context)
        ```
    14. Kemudian, buat template yang bernama `main.html` dengan isi:
        ```
        <h1>{{ app_name }} </h1>

        <h5>Name: </h5>
        <p>{{ name }}</p>
        <h5>Class: </h5>
        <p>{{ class }}</p>
        ```
    15. Tambahkan routing `show_main` dalam berkas `urls.py` pada aplikasi `main`.
        ```
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
        ```
    16. Include semua urls pada aplikasi main ke direktori proyek dalam berkas `urls.py`.
        ```
        urlpatterns = [
            path('main/', include('main.urls')),
        ]
        ```
    17. Pastikan proyek Django berhasil berjalan dengan baik.
        ```python manage.py runserver```
    18. Bikin repository baru bernama `brewvin` pada akun GitHub saya.
    19. Tambahin remote origin pada device, kemudian lakukan `add, commit, push` pada branch baru bernama `main`.
    20. Lakukan deployment pada Adaptable.io dengan template deployment yaitu `Python App Template` dan tipe basis data yaitu `PostgreSQL`.
    21. Atur start command menjadi `python manage.py migrate && gunicorn shopping_list.wsgi`.
    22. Nyalakan `HTTP Listener on Port`.
    23. Tunggu proses deployment selesai.

- ##### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    ![Technical Diagrams](https://github.com/ArvinCS/brewvin/assets/36118285/8b27da7a-bd78-4212-a7c4-86cdd746b7da)

- ##### Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

    Virtual environment digunakan untuk memisahkan environment antar proyek sehingga dependencies yang sama namun beda versi tidak akan saling bertabrakan. Sehingga, kita tetap bisa membuat aplikasi web Django tanpa virtual environment, namun dengan resiko adanya konflik antar dependencies di device development.

- ##### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

    - MVC (Model-View-Controller)
        Sebuah *architectural pattern* yang membagi sebuah aplikasi menjadi tiga komponen utama, yaitu `model, view, controller`. Setiap komponen memiliki peranan masing-masing yang berbeda. Model memegang peran sebagai tempat bagaimana data model diatur. View memegang peran sebagai bagaimana tampilan yang akan diberikan kepada pengguna. Controller memegang peran sebagai mengatur alur masuk dan keluarnya *business logic* dan *requests*, manipulasi data dari model kemudian ditampilan ke view.
    
    - MVT (Model-View-Template)
        Sebuah *architectural pattern* yang membagi sebuah aplikasi menjadi tiga komponen utama, yaitu `model, view, template`. Setiap komponen memiliki peranan masing-masing yang berbeda. Model memegang peran sebagai tempat bagaimana data model diatur. View memegang peran sebagai bagaimana *business logic* yang akan dijalankan dan bagaimana data yang diberikan akan ditampilkan kepada pengguna. Template memegang peran sebagai tampilan yang akan muncul kepada pengguna.

    - MVVM (Model-View-ViewModel)
        Sebuah *architectural pattern* yang membagi sebuah aplikasi menjadi tiga komponen utama, yaitu `model, view, viewmodel`. Setiap komponen memiliki peranan masing-masing yang berbeda. Model memegang peran sebagai tempat bagaimana data model diatur. View memegang peran sebagai bagaimana data yang diberikan akan ditampilkan kepada pengguna dengan meminimalisir *business logic* yang ada. ViewModel memegang peran sebagai perantara antara View dan Model, misalnya memproses *business logic* atau manipulasi data.
    
    Perbedaan ketiga *architectural pattern* tersebut tidak terlalu signifikan, karena setiap *architectural pattern* mempunyai kelebihan dan kelemahannya masing-masing. Jadi, *architectural pattern* yang sebaiknya digunakan bergantung pada kasus aplikasi apa yang akan dibuat. Contohnya, aplikasi mobile *Flutter* lebih baik menggunakan MVVM karena behaviour dari Flutter yang lebih cocok.  

### Tugas 3

- ##### 1. Apa perbedaan antara form POST dan form GET dalam Django?
    Form POST pada umumnya (berdasarkan convention HTTP) digunakan untuk melakukan update atau menambahkan data ke suatu database. Jika berhasil, maka data tersebut akan masuk ke database. Sebaliknya, response akan menampilkan status codenya yang menandakan bermasalah.
    
    Form GET pada umumnya (berdasarkan convention HTTP) digunakan untuk mengambil data dari suatu database yang dijadikan dalam bentuk response dengan status code 200.
- ##### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    XML (Extensible Markup Language) merupakan salah satu format data delivery yang membentuk struktur seperti tree dengan relasi root - branch - leaves. XML menggunakan tag untuk mendeskripsikan data dan memperdalam relasi tersebut.

    JSON (JavaScript Object Notation) merupakan salah satu format data delivery yang membentuk struktur seperti dictionary terdiri dari key dan value. Sehingga, value tersebut dapat merupakan sebuah nilai data primitif, array, atau bahkan dictionary lainnya.

    HTML (Hypertext Markup Language) lebih digunakan untuk menampilkan sebuah halaman pada website berisi data-data yang ada. Sehingga, jarang digunakan untuk pengiriman data.

- ##### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    JSON lebih sering digunakan dalam pertukaran data karena strukturnya yang lebih intuitif, sederhana dan ringan. Sehingga, dengan kemudahannya tersebut, data JSON juga lebih mudah untuk diparsing dibandingkan format data lainnya dan ukurannya yang lebih kecil. 

- ##### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Membuat kerangka base.html yang berisi:
    ```
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta
                name="viewport"
                content="width=device-width, initial-scale=1.0"
            />
            {% block meta %}
            {% endblock meta %}
        </head>

        <body>
            {% block content %}
            {% endblock content %}
        </body>
    </html>
    ```
    - Membuat input form untuk model Item:
    ```
    from django.forms import ModelForm
    from main.models import Item

    class ItemForm(ModelForm):
        class Meta:
            model = Item
            fields = ["name", "amount", "description", "taste"]
    ```
    - Membuat fungsi baru `create_item`, `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id` pada `views.py`:
    ```
    def create_item(request):
        form = ItemForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_item.html", context)

    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    - Membuat `create_item.html`:
    ```
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Item</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Item"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```
    - Menambahkan routing untuk `create_item`, `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id` pada `urls.py`:
    ```
    app_name = "main"
    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create_item/', create_item, name='create_item'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ]
    ```

- ##### 5. Screenshot Postman (pastikan anda memiliki akses internet untuk melihat screenshot)
- 1) HTML
    ![postman-html](https://github.com/ArvinCS/brewvin/assets/36118285/69bb7a1c-b9cd-48e4-8e61-1fd68d6e23ef)
- 2) XML
    ![postman-xml](https://github.com/ArvinCS/brewvin/assets/36118285/1b9a024f-bb03-42f4-815d-9b7285c1bc94)
- 3) JSON
    ![postman-json](https://github.com/ArvinCS/brewvin/assets/36118285/4b4348ed-5ae3-45d7-ada8-a6e129b4ff47)
- 4) XML by ID
    ![postman-xml-id](https://github.com/ArvinCS/brewvin/assets/36118285/de5ac1f7-aaba-404b-aace-3b9accf06d1f)
- 5) JSON by ID
    ![postman-json-id](https://github.com/ArvinCS/brewvin/assets/36118285/1bb7a97f-ba2b-4673-bb12-07148dc62cda)

### Tugas 4

- ##### 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

- ##### 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

- ##### 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

- ##### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

- ##### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.