# Contact Catalogue
A Python command-line worker contact management system with data persistence and input validation. Store and manage worker information including email, mobile and job role with automatic save and backup functionality.
# Features

Add Workers: Register new workers with full contact details
Edit Workers: Update any field individually with confirmation prompts
Remove Workers: Remove workers from the catalogue permanently
View All Workers: Display the full catalogue at a glance
Data Persistence: Save and load worker data via JSON file storage
Input Validation: Comprehensive error handling prevents crashes from invalid input
User-Friendly Interface: Menu-driven navigation with clear prompts and feedback
Automatic Backup System: Creates .backup files on every load and save
Graceful Error Handling: Handles missing files, corrupted JSON and permission errors
Manual Save on Exit: User prompted to save before closing

FunctionPurposeValidationadd_user()Creates new worker entry in catalogueName (letters only), Email, Mobile, Role (no empty fields)edit_user()Updates individual fields for existing workerName existence check, confirmation prompt per changeremove_user()Permanently removes worker from catalogueName existence check, confirmation promptview_all_users()Displays all workers with full contact detailsNone (no input)save_to_file()Persists data to JSON with automatic backupFile system error handling (PermissionError, OSError)load_from_file()Loads data from JSON on startupFileNotFoundError, JSONDecodeError, PermissionError handling
