# Contact Management System

A Python command-line contact management application built 
with full OOP architecture demonstrating core software 
engineering principles.

## Features
- Add contacts with name, email and mobile number
- View a specific contact by name (O(1) lookup)
- View all contacts in the catalogue
- Remove contacts with confirmation prompt
- Input validation and error handling throughout
- Graceful exit with confirmation

## Project Structure
| Class | Purpose |
|-------|---------|
| `Contact` | Stores individual contact data — name, email, mobile |
| `ContactBook` | Manages all contacts in a dictionary of objects |

## Data Structure
Contacts stored as a **dictionary of objects** — contact name 
as key, Contact object as value. Provides O(1) lookup for 
instant retrieval by name.

## Tech Stack
- Python 3
- OOP (Classes, encapsulation, dot notation)
- JSON persistence (coming)

## Planned Features
- JSON save and load with backup handling
- CSV export via Pandas
- Search contacts by email or mobile
- Edit existing contact details
