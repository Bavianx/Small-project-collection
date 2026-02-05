# Grade Booking System

A Python command-line grade management system with data persistence and comprehensive input validation. Track student performance across multiple subjects with automatic average calculations and pass/fail reporting.

## Features

- **Student Management**: Add new students with their first grade entry
- **Grade Tracking**: Record multiple subject grades per student
- **Individual Records**: View detailed student information with calculated averages
- **Class Overview**: Display all students and their performance at a glance
- **Performance Reports**: Automatically categorize students as passing (≥65%) or failing (<65%)
- **Data Persistence**: Save and load grade data via JSON file storage
- **Input Validation**: Comprehensive error handling prevents crashes from invalid input
- **User-Friendly Interface**: Menu-driven navigation with clear prompts and feedback
- JSON file storage for permanent data retention
- Automatic load on startup
- Manual save on exit
- Graceful handling of missing files (first run)

| Function | Purpose | Validation |
|----------|---------|------------|
| `add_student()` | Creates new student with initial grade | Name (letters only), Subject (valid list), Grade (0-100) |
| `add_grade()` | Adds subjects to existing students | Name, Subject, Grade validation |
| `view_student()` | Displays individual performance with average | Name validation |
| `show_all_students()` | Lists all students with calculated averages | None (no input) |
| `view_all_passing()` | Groups by pass/fail (65% threshold) | None (no input) |
| `save_to_file()` | Persists data to JSON file | File system error handling |
| `load_from_file()` | Loads data from JSON on startup | FileNotFoundError handling |


## Future Enhancements
- [ ] Delete students or subjects
- [ ] Letter grade assignments (A, B, C, D, F)
- [ ] Graphical data visualization
- ✅ Comprehensive error handling (corrupted JSON, permissions, disk full)
- ✅ Automatic backup system
