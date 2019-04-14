# Chefsbook-spa
## Opis aplikacji
Aplikacja służąca usprawnieniu obsługi zamówień w restauracjach. Umożliwia kelnerom zbieranie zamówień, przekazywanie ich do kuchni i wyświetlanie notyfikacji o przygotowanych daniach. Aplikacja umożliwii również łatwy dostęp do informacji o wartościach odżywczych każdego z oferowanych dań. Przekazane do kuchni zamówienia wyświetlane są w kolejce oczekujących zamówień i widoczne dla szefa kuchni i kucharzy.

## Funkcjonalności
Uwierzytelnianie kont pracowników;

Przyjmowanie zamówień klientów;

Wyświetlanie informacji o wartościach odżywczych dań;

Wyświetlenie kolejki zamówień.

## Uruchomienie aplikacji

### Backend
virtualenv env

source env/bin/activate  # On Windows use `env\Scripts\activate`

pip install django

pip install djangorestframework

python manage.py migrate

python manage.py createsuperuser --email admin@example.com --username admin

python manage.py runserver