# Django Book Catalogue

A Django web application built as an introduction to the 
Django framework demonstrating models, database integration 
and the Django admin interface.

## Features
- Add books via Django admin panel
- Store book data in SQLite database
- Book model with ISBN, title, author and availability status
- Django ORM for database operations — no raw SQL required

## Tech Stack
- Python 3
- Django 5.1
- SQLite (development database)
- Django Admin interface

## Project Structure
| File | Purpose |
|------|---------|
| `models.py` | Book model — defines database schema |
| `views.py` | Application logic and request handling |
| `admin.py` | Registers models for Django admin panel |
| `settings.py` | Project configuration and installed apps |

## Learning Context
Demonstrates transition from procedural Python and OOP to full web framework architecture.

## Planned Features
- Book list view in browser
- Search functionality
- Remove Functionality (if added)
- Checkout and return system
- User authentication

