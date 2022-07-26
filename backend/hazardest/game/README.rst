game
=====

Polls is a Django app to conduct web-based polls. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "game" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'game',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('api/', include('game.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/api/ to participate in the poll.