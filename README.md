# Django course management project

A Django project with 7 models and a REST API (Django REST Framework).

## Tech stack

- Python 3
- Django
- Django REST Framework
- Pillow
- Database: SQLite

## Project structure

- `course_mgt_project/`: project settings and root URLs
- `course_app/`: Django app
- Tests: `course_app/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `Person` | `course_app` | name, familyName, email, birthdate |
| `Tutor` | `course_app` | photo, grade |
| `Course` | `course_app` | name, startDate, nbLectures, duration, coefficient, courseAvatar, tutor |
| `Student` | `course_app` | cin, courses |
| `Profile` | `course_app` | linkedIn, github, photo, student |
| `Location` | `course_app` | locationNumber, streetName, city, zipCode, courses |
| `Enrollment` | `course_app` | student, course, registrationDate, result |

## URL routes

Declared in `urls.py`:

- `/tutors/ (router)`
- `/students/ (router)`
- `/courses/ (router)`
- `/blog/`
- `/course-app/`

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
