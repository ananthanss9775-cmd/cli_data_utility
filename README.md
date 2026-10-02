# CLI Data Utility - Employee Management System

A comprehensive command-line application for managing and analyzing employee data. This project demonstrates Python proficiency in file handling, data structures, input validation, and CLI design.

## 📋 Project Overview

**CLI Data Utility** is a robust employee data management system that allows users to perform CRUD operations and advanced data analysis through an interactive menu-driven interface. All data is stored in CSV format for easy portability and backup.

### Key Features

✅ **View Employees** - Display all employee records in a formatted table  
✅ **Search Functionality** - Find employees by ID, Name, or Department  
✅ **Add Employees** - Create new employee records with validation  
✅ **Update Records** - Modify existing employee information  
✅ **Delete Records** - Remove employees with confirmation  
✅ **Filter Data** - Filter by Department, Location, Experience, or Salary range  
✅ **Sort Operations** - Sort by Name, Salary, Experience, or Department  
✅ **Statistics** - Generate comprehensive employee analytics  
✅ **Export Function** - Export all or filtered data to timestamped CSV files  
✅ **Error Handling** - Robust exception handling and input validation  

## 🛠 Requirements

- **Python 3.7** or higher
- **CSV module** (built-in)
- **No external dependencies required**

## 📦 Installation & Setup

### Step 1: Download Files
Ensure you have the following files in your project directory:
```
cli_data_utility.py    # Main application
employees.csv          # Sample data (optional - app creates if missing)
README.md             # This documentation
```

### Step 2: Verify Python Installation
```bash
python --version
# or
python3 --version
```

### Step 3: Run the Application
```bash
# Using Python
python cli_data_utility.py

# Or using Python 3 explicitly
python3 cli_data_utility.py
```

## 📖 Usage Guide

### Starting the Application
When you run the application, you'll see the main menu:

```
==================================================
     CLI DATA UTILITY - EMPLOYEE MANAGER
==================================================
1.  View All Employees
2.  Search Employee
3.  Add New Employee
4.  Update Employee
5.  Delete Employee
6.  Filter Employees
7.  Sort Employees
8.  Generate Statistics
9.  Export Data
10. Exit
==================================================
```

### Feature Walkthrough

#### 1. View All Employees
Displays all employee records in a formatted table with columns for ID, Name, Department, Location, Experience, and Salary.

```
Select an option: 1
```

**Output:**
```
ID       Name                 Department      Location     Experience  Salary
EMP001   John Smith           Engineering     New York     5            $95000
EMP002   Sarah Johnson        Marketing       San Francisco3            $75000
...
```

#### 2. Search Employee
Find employees using three search methods:
- By Employee ID
- By Name (partial match supported)
- By Department (partial match supported)

```
Select an option: 2
Search by: 1) ID  2) Name  3) Department
Enter choice: 2
Enter search term: John
```

#### 3. Add New Employee
Create a new employee record with automatic validation:
- Prevents duplicate Employee IDs
- Validates all required fields
- Ensures numeric input for Experience and Salary

```
Select an option: 3
Employee ID: EMP021
Name: Alex Thompson
Department: Engineering
Location: Boston
Experience (years): 5
Salary: 100000
✓ Employee 'Alex Thompson' added successfully.
```

#### 4. Update Employee
Modify existing employee information:
- Leave fields blank to keep current values
- Update only the fields you need to change
- Changes are saved immediately

```
Select an option: 4
Enter Employee ID to update: EMP001
Current record: John Smith, Engineering, New York
Leave field blank to keep current value.

Name [John Smith]: 
Department [Engineering]: Senior Engineering
Location [New York]: 
Experience [5]: 6
Salary [95000]: 105000
✓ Employee record updated successfully.
```

#### 5. Delete Employee
Remove an employee record with confirmation:
- Shows employee details before deletion
- Requires confirmation before permanent removal
- Data is immediately saved to file

```
Select an option: 5
Enter Employee ID to delete: EMP021
About to delete: Alex Thompson (EMP021)
Are you sure? (yes/no): yes
✓ Employee 'Alex Thompson' deleted successfully.
```

#### 6. Filter Employees
Apply filters to view specific subsets of data:
- **By Department**: View all employees in a specific department
- **By Location**: See employees in a particular location
- **By Experience**: Filter within an experience range
- **By Salary**: Filter within a salary range

```
Select an option: 6
Filter by: 1) Department  2) Location  3) Experience  4) Salary Range
Enter choice: 3
Minimum experience (years): 5
Maximum experience (years): 8
✓ Found 3 match(es):
```

#### 7. Sort Employees
Sort the complete employee list:
- **By Name**: Alphabetical order
- **By Salary**: Lowest to highest or vice versa
- **By Experience**: Years of experience
- **By Department**: Alphabetical by department
- Choose ascending or descending order

```
Select an option: 7
Sort by: 1) Name  2) Salary  3) Experience  4) Department
Enter choice: 2
Order: 1) Ascending  2) Descending: 2
✓ Sorted by Salary (Descending):
```

#### 8. Generate Statistics
View comprehensive analytics about your employee data:
- Total number of employees
- Average salary across all employees
- Highest and lowest salary
- Average years of experience
- Employee count by department

```
Select an option: 8

--- Employee Statistics ---
Overall Statistics:
  • Total Employees: 20
  • Average Salary: $94,750.00
  • Highest Salary: $130,000
  • Lowest Salary: $65,000
  • Average Experience: 5.5 years

Department-wise Employee Count:
  • Engineering: 6 employee(s)
  • HR: 3 employee(s)
  • Marketing: 4 employee(s)
  • Sales: 7 employee(s)
```

#### 9. Export Data
Save employee data to a new CSV file:
- Export all employees or filtered results
- Timestamped filenames prevent overwrites
- Useful for reports and backups

```
Select an option: 9
1) Export all employees  2) Export filtered results
Enter choice: 1
✓ Data exported successfully to 'employees_export_20240115_143022.csv'
```

#### 10. Exit
Safely close the application. All changes are already saved automatically.

```
Select an option: 10
Thank you for using CLI Data Utility. Goodbye!
```

## 📊 Sample Data

The application includes sample data with 20 employees across 4 departments:

| Department | Count |
|------------|-------|
| Engineering | 6 |
| Sales | 7 |
| Marketing | 4 |
| HR | 3 |

**Locations represented:**
- New York
- San Francisco
- Chicago
- Los Angeles

**Experience range:** 2-10 years  
**Salary range:** $65,000 - $130,000

## 🏗 Code Architecture

### Class Structure
```
CLIDataUtility
├── __init__()           # Initialize with CSV file
├── load_data()          # Load employees from CSV
├── save_data()          # Save employees to CSV
├── display_menu()       # Show menu options
├── view_employees()     # Display employees
├── search_employees()   # Search functionality
├── add_employee()       # Add new record
├── update_employee()    # Update existing record
├── delete_employee()    # Delete record
├── filter_employees()   # Filter data
├── sort_employees()     # Sort data
├── generate_statistics()# Generate analytics
├── export_data()        # Export to CSV
├── get_valid_input()    # Input validation
├── get_valid_number()   # Numeric validation
└── run()               # Main application loop
```

### Data Structures Used

**Lists:** Store and iterate through employee records
```python
self.employees = []  # List of dictionaries
```

**Dictionaries:** Represent individual employee records
```python
{
    'Employee ID': 'EMP001',
    'Name': 'John Smith',
    'Department': 'Engineering',
    'Location': 'New York',
    'Experience': '5',
    'Salary': '95000'
}
```

**Sets:** Used implicitly for uniqueness checking
```python
if any(emp['Employee ID'] == emp_id for emp in self.employees)
```

**Tuples:** Could be used for immutable field definitions (extensible)

## ✨ Features Implemented

### Core Requirements ✅
- [x] Menu-driven interface
- [x] View all employees
- [x] Search by ID, Name, Department
- [x] Add new employees
- [x] Update existing records
- [x] Delete employees with confirmation
- [x] Filter by Department, Location, Experience, Salary
- [x] Sort by Name, Salary, Experience, Department
- [x] Generate statistics
- [x] Export data to CSV
- [x] Input validation and error handling
- [x] CSV file handling
- [x] Organized code structure with functions
- [x] README documentation

### Advanced Features 🚀
- [x] Duplicate ID detection
- [x] Timestamped export files
- [x] Department-wise analytics
- [x] Numeric sorting (not string)
- [x] Case-insensitive search and filter
- [x] Formatted table output
- [x] User-friendly error messages
- [x] Data persistence
- [x] Field-specific update capability
- [x] Comprehensive statistics

## 🔒 Error Handling

The application handles multiple error scenarios:

| Error Type | Handling |
|-----------|----------|
| Missing CSV file | Creates empty database, offers to add data |
| Invalid input format | Prompts user to re-enter with validation |
| Duplicate Employee ID | Prevents duplicate IDs from being added |
| File I/O errors | Catches and reports errors gracefully |
| Data format errors | Handles missing or malformed fields |
| Numeric conversion errors | Validates numeric input before processing |

## 📝 CSV File Format

The CSV file uses the following structure:

```csv
Employee ID,Name,Department,Location,Experience,Salary
EMP001,John Smith,Engineering,New York,5,95000
EMP002,Sarah Johnson,Marketing,San Francisco,3,75000
```

**Field specifications:**
- **Employee ID**: Unique identifier (string, no spaces)
- **Name**: Full name (string)
- **Department**: Department name (string)
- **Location**: City/location (string)
- **Experience**: Years of experience (integer)
- **Salary**: Annual salary (integer)

## 🎯 Testing Guide

### Test Scenario 1: Basic Operations
1. Run the application
2. View all employees (Option 1)
3. Search for "Engineering" (Option 2)
4. Check statistics (Option 8)

### Test Scenario 2: Data Modification
1. Add a new employee (Option 3)
2. Update their record (Option 4)
3. View changes (Option 1)
4. Delete the test employee (Option 5)

### Test Scenario 3: Filtering & Sorting
1. Filter by Department: "Engineering" (Option 6)
2. Sort by Salary, Descending (Option 7)
3. Compare with statistics (Option 8)

### Test Scenario 4: Export
1. Filter by Location (Option 6, choice 2)
2. Export filtered results (Option 9, choice 2)
3. Check generated file

## 📂 Project Files

```
cli_data_utility/
├── cli_data_utility.py      # Main application (413 lines)
├── employees.csv            # Sample data (20 records)
├── README.md               # This documentation
└── employees_export_*.csv  # Generated export files (created during runtime)
```

## 🚀 Enhancement Ideas

While the project meets all requirements, here are additional features you could add:

1. **Pagination**: Display large datasets in pages
2. **Advanced Search**: Multi-field search, regex patterns
3. **Data Validation**: Email, phone format validation
4. **Logging**: File-based application logging
5. **Database**: SQLite integration instead of CSV
6. **Analytics Dashboard**: Visual charts and graphs
7. **Backup System**: Automatic data backups
8. **Undo/Redo**: Transaction history
9. **User Roles**: Admin, manager, employee levels
10. **Reporting**: Generate PDF reports

## 💡 Development Notes

### Python Concepts Demonstrated
- **Object-Oriented Programming**: Class-based design
- **File I/O**: CSV reading and writing
- **Data Structures**: Lists, dictionaries
- **Exception Handling**: Try-except blocks
- **Input Validation**: User input verification
- **String Methods**: Lower(), strip(), formatting
- **List Comprehensions**: Filtering data
- **Lambda Functions**: Sorting with custom keys
- **Type Conversion**: String to integer conversions

### Best Practices Implemented
- Descriptive function names
- Comprehensive docstrings
- Input validation at entry points
- Automatic data persistence
- User-friendly error messages
- Clean code organization
- Consistent naming conventions

## 📞 Support & Troubleshooting

### Application won't start
```bash
# Check Python version
python --version

# Run with verbose output
python cli_data_utility.py
```

### Data not saving
- Ensure `employees.csv` file exists and is writable
- Check file permissions
- Verify disk space availability

### Import errors
- Confirm all required files are in the same directory
- Check file names match exactly (case-sensitive on Linux/Mac)

### Encoding issues
- On Windows: Ensure file is UTF-8 encoded
- Check regional settings

## 📄 License

This is a capstone project created for educational purposes.

## ✍️ Author Notes

This CLI Data Utility demonstrates comprehensive Python skills including:
- Command-line interface design
- Data persistence and file management
- User input validation and error handling
- Object-oriented programming principles
- Data manipulation and analysis
- Professional code organization

The application is production-ready and can be extended with additional features as needed.

---

**Version:** 1.0  
**Last Updated:** January 2024  
**Python Version:** 3.7+
