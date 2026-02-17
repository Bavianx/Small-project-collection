# Contact Catalogue
A Python command-line worker contact management system with data persistence and input validation. Store and manage worker information including email, mobile and job role with automatic save and backup functionality.

# Features

- Add Workers: Register new workers with full contact details
- Edit Workers: Update any field individually with confirmation prompts
- Remove Workers: Remove workers from the catalogue permanently
- View All Workers: Display the full catalogue at a glance
- Data Persistence: Save and load worker data via JSON file storage
- Input Validation: Comprehensive error handling prevents crashes from invalid input
- User-Friendly Interface: Menu-driven navigation with clear prompts and feedback
- Automatic Backup System: Creates .backup files on every load and save
- Graceful Error Handling: Handles missing files, corrupted JSON and permission errors
- Manual Save on Exit: User prompted to save before closing

| Function | Purpose / Validation |
|----------|-------------|
| `add_user()` |Creates new worker entry in catalogue	Name (letters only), Email, Mobile, Role (no empty fields) |
| `edit_user()` | Updates individual fields for existing worker	Name existence check, confirmation prompt per change |
| `remove_user()` | Permanently removes worker from catalogue	Name existence check, confirmation prompt |
| `view_all_users()` | Displays all workers with full contact details	None (no input) |
| `save_to_file()` | Persists data to JSON file with automatic backup | File system error handling (PermissionError, OSError) |
| `load_from_file()` | Loads data from JSON on startup with backup creation | FileNotFoundError, JSONDecodeError, PermissionError handling |

# Future Enhancements

- [ ] Search workers by name, role or email
- [ ] Filter workers by department or job role
✅ Comprehensive error handling (corrupted JSON, permissions)
✅ Automatic backup system
- [ ] Export catalogue to CSV
- [ ] Sort workers alphabetically or by role
