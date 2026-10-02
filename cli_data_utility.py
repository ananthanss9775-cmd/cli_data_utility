
import csv
import os
import sys
from pathlib import Path
from datetime import datetime


class CLIDataUtility:
    """Main application class for managing employee data."""
    
    def __init__(self, csv_file="employees.csv"):
        """Initialize the application with a CSV file."""
        self.csv_file = csv_file
        self.employees = []
        self.load_data()
    
    def load_data(self):
        """Load employee data from CSV file."""
        if not os.path.exists(self.csv_file):
            print(f"⚠️  File '{self.csv_file}' not found. Starting with empty database.")
            self.employees = []
            return
        
        try:
            with open(self.csv_file, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.employees = list(reader)
            print(f"✓ Loaded {len(self.employees)} employee records.")
        except Exception as e:
            print(f"❌ Error loading file: {e}")
            self.employees = []
    
    def save_data(self):
        """Save employee data to CSV file."""
        if not self.employees:
            print("⚠️  No data to save.")
            return False
        
        try:
            fieldnames = ['Employee ID', 'Name', 'Department', 'Location', 'Experience', 'Salary']
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.employees)
            print(f"✓ Data saved successfully to '{self.csv_file}'")
            return True
        except Exception as e:
            print(f"❌ Error saving file: {e}")
            return False
    
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "="*50)
        print("     CLI DATA UTILITY - EMPLOYEE MANAGER")
        print("="*50)
        print("1.  View All Employees")
        print("2.  Search Employee")
        print("3.  Add New Employee")
        print("4.  Update Employee")
        print("5.  Delete Employee")
        print("6.  Filter Employees")
        print("7.  Sort Employees")
        print("8.  Generate Statistics")
        print("9.  Export Data")
        print("10. Exit")
        print("="*50)
    
    def view_employees(self, employees=None):
        """Display employees in a formatted table."""
        data = employees if employees else self.employees
        
        if not data:
            print("❌ No employees to display.")
            return
        
        print("\n" + "-"*100)
        print(f"{'ID':<8} {'Name':<20} {'Department':<15} {'Location':<12} {'Experience':<12} {'Salary':<12}")
        print("-"*100)
        
        for emp in data:
            try:
                print(f"{emp['Employee ID']:<8} {emp['Name']:<20} {emp['Department']:<15} "
                      f"{emp['Location']:<12} {emp['Experience']:<12} ${emp['Salary']:<11}")
            except KeyError:
                print("❌ Data format error in employee record.")
        
        print("-"*100)
        print(f"Total: {len(data)} employee(s)\n")
    
    def search_employees(self):
        """Search for employees by ID, Name, or Department."""
        print("\n--- Search Employee ---")
        print("Search by: 1) ID  2) Name  3) Department")
        
        choice = self.get_valid_input("Enter choice (1-3): ", ['1', '2', '3'])
        search_term = input("Enter search term: ").strip()
        
        if not search_term:
            print("❌ Search term cannot be empty.")
            return
        
        results = []
        search_fields = {
            '1': 'Employee ID',
            '2': 'Name',
            '3': 'Department'
        }
        
        field = search_fields[choice]
        
        for emp in self.employees:
            if search_term.lower() in emp[field].lower():
                results.append(emp)
        
        if results:
            print(f"\n✓ Found {len(results)} match(es):")
            self.view_employees(results)
        else:
            print(f"❌ No employees found matching '{search_term}'.")
    
    def add_employee(self):
        """Add a new employee record."""
        print("\n--- Add New Employee ---")
        
        try:
            emp_id = input("Employee ID: ").strip()
            if not emp_id:
                print("❌ Employee ID cannot be empty.")
                return
            
            # Check for duplicate ID
            if any(emp['Employee ID'] == emp_id for emp in self.employees):
                print(f"❌ Employee ID '{emp_id}' already exists.")
                return
            
            name = input("Name: ").strip()
            if not name:
                print("❌ Name cannot be empty.")
                return
            
            department = input("Department: ").strip()
            if not department:
                print("❌ Department cannot be empty.")
                return
            
            location = input("Location: ").strip()
            if not location:
                print("❌ Location cannot be empty.")
                return
            
            experience = self.get_valid_number("Experience (years): ")
            salary = self.get_valid_number("Salary: ")
            
            new_emp = {
                'Employee ID': emp_id,
                'Name': name,
                'Department': department,
                'Location': location,
                'Experience': experience,
                'Salary': salary
            }
            
            self.employees.append(new_emp)
            self.save_data()
            print(f"✓ Employee '{name}' added successfully.")
        
        except Exception as e:
            print(f"❌ Error adding employee: {e}")
    
    def update_employee(self):
        """Update an existing employee's details."""
        print("\n--- Update Employee ---")
        
        emp_id = input("Enter Employee ID to update: ").strip()
        employee = None
        
        for emp in self.employees:
            if emp['Employee ID'] == emp_id:
                employee = emp
                break
        
        if not employee:
            print(f"❌ Employee with ID '{emp_id}' not found.")
            return
        
        print(f"Current record: {employee['Name']}, {employee['Department']}, {employee['Location']}")
        print("Leave field blank to keep current value.\n")
        
        try:
            name = input(f"Name ({employee['Name']}): ").strip()
            if name:
                employee['Name'] = name
            
            department = input(f"Department ({employee['Department']}): ").strip()
            if department:
                employee['Department'] = department
            
            location = input(f"Location ({employee['Location']}): ").strip()
            if location:
                employee['Location'] = location
            
            experience = input(f"Experience ({employee['Experience']}): ").strip()
            if experience:
                try:
                    employee['Experience'] = str(int(experience))
                except ValueError:
                    print("⚠️  Invalid experience value, keeping current.")
            
            salary = input(f"Salary ({employee['Salary']}): ").strip()
            if salary:
                try:
                    employee['Salary'] = str(int(salary))
                except ValueError:
                    print("⚠️  Invalid salary value, keeping current.")
            
            self.save_data()
            print(f"✓ Employee record updated successfully.")
        
        except Exception as e:
            print(f"❌ Error updating employee: {e}")
    
    def delete_employee(self):
        """Delete an employee record after confirmation."""
        print("\n--- Delete Employee ---")
        
        emp_id = input("Enter Employee ID to delete: ").strip()
        employee = None
        emp_index = None
        
        for i, emp in enumerate(self.employees):
            if emp['Employee ID'] == emp_id:
                employee = emp
                emp_index = i
                break
        
        if not employee:
            print(f"❌ Employee with ID '{emp_id}' not found.")
            return
        
        print(f"About to delete: {employee['Name']} ({employee['Employee ID']})")
        confirm = input("Are you sure? (yes/no): ").strip().lower()
        
        if confirm in ['yes', 'y']:
            self.employees.pop(emp_index)
            self.save_data()
            print(f"✓ Employee '{employee['Name']}' deleted successfully.")
        else:
            print("❌ Deletion cancelled.")
    
    def filter_employees(self):
        """Filter employees by Department, Location, Experience, or Salary range."""
        print("\n--- Filter Employees ---")
        print("Filter by: 1) Department  2) Location  3) Experience  4) Salary Range")
        
        choice = self.get_valid_input("Enter choice (1-4): ", ['1', '2', '3', '4'])
        results = []
        
        try:
            if choice == '1':
                department = input("Enter department: ").strip()
                results = [emp for emp in self.employees 
                          if emp['Department'].lower() == department.lower()]
            
            elif choice == '2':
                location = input("Enter location: ").strip()
                results = [emp for emp in self.employees 
                          if emp['Location'].lower() == location.lower()]
            
            elif choice == '3':
                min_exp = int(input("Minimum experience (years): "))
                max_exp = int(input("Maximum experience (years): "))
                results = [emp for emp in self.employees 
                          if min_exp <= int(emp['Experience']) <= max_exp]
            
            elif choice == '4':
                min_sal = int(input("Minimum salary: "))
                max_sal = int(input("Maximum salary: "))
                results = [emp for emp in self.employees 
                          if min_sal <= int(emp['Salary']) <= max_sal]
            
            if results:
                print(f"\n✓ Found {len(results)} match(es):")
                self.view_employees(results)
            else:
                print("❌ No employees match the filter criteria.")
        
        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"❌ Error filtering: {e}")
    
    def sort_employees(self):
        """Sort employee records by Name, Salary, Experience, or Department."""
        print("\n--- Sort Employees ---")
        print("Sort by: 1) Name  2) Salary  3) Experience  4) Department")
        
        choice = self.get_valid_input("Enter choice (1-4): ", ['1', '2', '3', '4'])
        order = self.get_valid_input("Order: 1) Ascending  2) Descending: ", ['1', '2'])
        
        sort_keys = {
            '1': 'Name',
            '2': 'Salary',
            '3': 'Experience',
            '4': 'Department'
        }
        
        try:
            key = sort_keys[choice]
            reverse = (order == '2')
            
            # For numeric fields, convert to int for proper sorting
            if key in ['Salary', 'Experience']:
                sorted_employees = sorted(self.employees, 
                                         key=lambda x: int(x[key]), 
                                         reverse=reverse)
            else:
                sorted_employees = sorted(self.employees, 
                                         key=lambda x: x[key].lower(), 
                                         reverse=reverse)
            
            print(f"\n✓ Sorted by {key} ({['Ascending', 'Descending'][reverse]}):")
            self.view_employees(sorted_employees)
        
        except Exception as e:
            print(f"❌ Error sorting: {e}")
    
    def generate_statistics(self):
        """Display total employees, average salary, salary range, and department stats."""
        print("\n--- Employee Statistics ---")
        
        if not self.employees:
            print("❌ No data available.")
            return
        
        total = len(self.employees)
        
        try:
            salaries = [int(emp['Salary']) for emp in self.employees]
            experiences = [int(emp['Experience']) for emp in self.employees]
            
            avg_salary = sum(salaries) / len(salaries)
            avg_experience = sum(experiences) / len(experiences)
            
            print(f"\nOverall Statistics:")
            print(f"  • Total Employees: {total}")
            print(f"  • Average Salary: ${avg_salary:,.2f}")
            print(f"  • Highest Salary: ${max(salaries):,}")
            print(f"  • Lowest Salary: ${min(salaries):,}")
            print(f"  • Average Experience: {avg_experience:.1f} years")
            
            # Department-wise analysis
            depts = {}
            for emp in self.employees:
                dept = emp['Department']
                depts[dept] = depts.get(dept, 0) + 1
            
            print(f"\nDepartment-wise Employee Count:")
            for dept, count in sorted(depts.items()):
                print(f"  • {dept}: {count} employee(s)")
        
        except ValueError:
            print("❌ Error: Data format issue in salary or experience fields.")
        except Exception as e:
            print(f"❌ Error generating statistics: {e}")
    
    def export_data(self):
        """Export employee data or filtered results to a new CSV file."""
        print("\n--- Export Data ---")
        print("1) Export all employees  2) Export filtered results")
        
        choice = self.get_valid_input("Enter choice (1-2): ", ['1', '2'])
        
        data_to_export = self.employees
        
        if choice == '2':
            print("\nApply filter:")
            print("Filter by: 1) Department  2) Location  3) Salary Range")
            filter_choice = self.get_valid_input("Enter choice (1-3): ", ['1', '2', '3'])
            
            try:
                if filter_choice == '1':
                    department = input("Enter department: ").strip()
                    data_to_export = [emp for emp in self.employees 
                                     if emp['Department'].lower() == department.lower()]
                
                elif filter_choice == '2':
                    location = input("Enter location: ").strip()
                    data_to_export = [emp for emp in self.employees 
                                     if emp['Location'].lower() == location.lower()]
                
                elif filter_choice == '3':
                    min_sal = int(input("Minimum salary: "))
                    max_sal = int(input("Maximum salary: "))
                    data_to_export = [emp for emp in self.employees 
                                     if min_sal <= int(emp['Salary']) <= max_sal]
            
            except ValueError:
                print("❌ Invalid input.")
                return
        
        if not data_to_export:
            print("❌ No data to export.")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        export_file = f"employees_export_{timestamp}.csv"
        
        try:
            fieldnames = ['Employee ID', 'Name', 'Department', 'Location', 'Experience', 'Salary']
            with open(export_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data_to_export)
            print(f"✓ Data exported successfully to '{export_file}'")
        except Exception as e:
            print(f"❌ Error exporting data: {e}")
    
    def get_valid_input(self, prompt, valid_options):
        """Get validated input from user."""
        while True:
            choice = input(prompt).strip()
            if choice in valid_options:
                return choice
            print(f"❌ Invalid choice. Please enter one of: {', '.join(valid_options)}")
    
    def get_valid_number(self, prompt):
        """Get a valid number from user."""
        while True:
            try:
                value = input(prompt).strip()
                return str(int(value))
            except ValueError:
                print("❌ Please enter a valid number.")
    
    def run(self):
        """Main application loop."""
        print("\n" + "="*50)
        print("  Welcome to CLI Data Utility!")
        print("="*50)
        
        while True:
            self.display_menu()
            choice = self.get_valid_input("Select an option (1-10): ", 
                                         ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
            
            if choice == '1':
                self.view_employees()
            elif choice == '2':
                self.search_employees()
            elif choice == '3':
                self.add_employee()
            elif choice == '4':
                self.update_employee()
            elif choice == '5':
                self.delete_employee()
            elif choice == '6':
                self.filter_employees()
            elif choice == '7':
                self.sort_employees()
            elif choice == '8':
                self.generate_statistics()
            elif choice == '9':
                self.export_data()
            elif choice == '10':
                print("\nThank you for using CLI Data Utility. Goodbye!")
                sys.exit(0)


if __name__ == "__main__":
    app = CLIDataUtility("employees.csv")
    app.run()
