# Library Catalogue System
A Python command-line library management system with book tracking, check-out/return functionality, and data persistence. Manage library inventory with availability status tracking and comprehensive search capabilities.

# Features

- Add Books: Register new books with ISBN, title, and author

- View All Books: Display complete catalogue with availability status

- Search Books: Find books by ISBN, title, or author

- Check Out Books: Mark books as unavailable when borrowed

- Return Books: Mark books as available when returned

- Availability Tracking: Real-time status updates (Available/Checked Out)

- Data Persistence: Save and load library data via JSON file storage

- Input Validation: Prevents invalid operations (can't check out unavailable books)

- User-Friendly Interface: Menu-driven navigation with confirmation prompts

- Automatic Backup System: Creates .backup files on every load and save

- Graceful Error Handling: Handles missing files, corrupted JSON and permission errors

| Function | Purpose / Validation |
|----------|-------------|
| `add_book()` |Creates new book entry in catalogue. ISBN uniqueness check, all fields required (no empty fields) |
| `view_all_books()` | Displays all books with availability statusNone (no input) |
| `search_book()` | Finds books by title, author, or ISBN. Returns matches or "No books found" |
| `check_out_book()` | Marks book as unavailable (borrowed). ISBN existence check, availability check, confirmation prompt|
| `return_book()` | Marks book as available (returned)ISBN existence check, checked-out status verification, confirmation prompt|
| `save_to_file()` | Persists data to JSON file with automatic backup | File system error handling (PermissionError, OSError) |
| `load_from_file()` | Loads data from JSON on startup with backup creation | FileNotFoundError, JSONDecodeError, PermissionError handling |


Future Enhancements

- [ ] Track borrower information (who checked out each book)
- [ ] Due date tracking with overdue notifications
- [ ] Multiple copies per title with individual tracking
- [ ] Genre/category classification
- ✅ Comprehensive error handling (corrupted JSON, permissions)
- ✅ Automatic backup system
- [ ] Export catalogue to CSV or PDF report
- [ ] Book reservation system
