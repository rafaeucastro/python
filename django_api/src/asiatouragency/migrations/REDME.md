Migrations are changes made in the database.
It saves a history of what I have done, allowing me to roolback to a previous version of the database.

This folder is used to save the generated migrations, just run the following code:
`python manage.py makemigrations`

But it only applies the migration (changes take effect in the database) when I execute:
`python manage.py migrate`