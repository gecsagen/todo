# Проект "Список дел"

***

## Описание:

Сайт "Список дел" повзоляет добавлять, изменять, удалять задачи. Реализована регистрация, вход и выход 
из системы. Дизайн создан с помочью чистого HTML + CSS без сторонних фреймворков.
<img height="400" src="https://i.ibb.co/wNZtqbK/Screenshot-1.png" width="1000"/>

* **Основные сущности (модели):**
  * Task(Задача)
    * user - пользователь сайта
    * title - название задачи
    * description - описание задачи
    * complete - статус задачи
    * create - дата создания
* **Обрабатывает следующие пути:**
    * '' - главная страница, отображает список добавленных сотрудников
    * 'login/' - страница входа в систему
    * 'logout/ - страница выхода из системы
    * 'register/' - страница регистрации в системе
    * 'task/<int:pk>/' - страница отображения детальной информации о задачи
    * 'create-task/' - страница создания новой задачи
    * 'update-task/<int:pk>/' - страница обновления задачи
    * 'delete-task/<int:pk>/' - страница удаления задачи

***

### Пакеты и файлы:

* **base** - директория соновоного Django приложения
    * **static** - директория для статики приложения
    * **templates** - директория с HTML шаблонами приложения.
    * **admin.py** - файл настройки админки
    * **apps.py** - файл конфигурации приложения
    * **forms.py** - формы проекта
    * **models.py** - модели проекат
    * **tests.py** - тессты проекта
    * **urls.py** - url проекта
    * **utils.py** - дополнительные классы и функции проекта
    * **view.pys** - представления
* **Avdeev** - директория конфигурации проекта
* **templates** - директория с HTML шаблонами проекта.
* **.gitignore** - файл игнорирования для GIT.
* **db.sqlite3** - файл базы данных проекта в формате SQLite3
* **manage.py** - файл управления Django проектом
* **requirements.txt** - файл содержит список внешних зависимостей проекта.