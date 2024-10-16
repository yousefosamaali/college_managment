# college_managment system oop

A Python-based project that models a college management system, including college details, departments, students, classrooms, and hostels. The system is designed using object-oriented programming principles to help manage different aspects of college operations efficiently.

# Project Structure
College-Management-System/
├── college_management.py
├── README.md

# Project Overview
The College Management System consists of several classes, each representing different components of a college setup:

College: Manages the college's basic information.
Department: Handles department details and events.
Student: Contains information about students, their attendance, and fee payment.
Room: Represents a classroom or lecture hall.
Hostel: Manages hostel details, with specific implementations for girls' and boys' hostels.
# Features
1. College
Attributes: Name, City, Contact
Methods:
open_college(): Displays a message that the college is open for the semester.
college_details(): Prints details of the college.
2. Department
Attributes: Department Name, Department ID, HOD Name, Total Staff, Total Students
Methods:
department_details(): Displays the department's information.
add_event(): Adds events to the department's schedule.
show_events(): Shows the list of scheduled events.
3. Student
Attributes: Student ID, Name, Gender, Year, Class ID
Methods:
student_details(): Prints the details of the student.
pay_fees(): Records the student's fee payment.
mark_present(): Marks the student as present.
mark_absent(): Marks the student as absent.
4. Room
Attributes: Class ID, Section, Department ID
Methods:
room_details(): Displays details of the room.
occubied(): Marks the room as available or occupied.
5. Hostel
Attributes: Student ID, Block Number, Room Number
Methods:
hostel_details(): Displays hostel information.
check_in(): Marks the student as checked in to the hostel.
check_out(): Marks the student as checked out of the hostel.
Inherited Classes:
Girls' Hostel (GHostel)
Boys' Hostel (BHostel)
These subclasses inherit the functionality of the Hostel class and specify the type of hostel.

# Requirements
Python 3.x
No external libraries are required
#Usage
1-Clone the repository: git clone https://github.com/yourusername/College-Management-System.git
2-Run the code: Run the college_management.py file in your Python environment:python college_management.py
#Examples of usage: Use the available methods to interact with the system and manage college data. Here's a quick example:
my_college = College("Helwan University", "Giza", "+20-123-456-789")
my_college.open_college()
my_college.college_details()

comp_sci_department = Department("Computer Science", 101, "Dr. Smith", 10, 200)
comp_sci_department.add_event("Coding Workshop", "2024-11-01", "A workshop on competitive programming.")
comp_sci_department.show_events()

Contribution
Contributions are welcome! If you have suggestions for improvements or find any bugs, please create an issue or submit a pull request.

License
This project is open-source and available under the MIT License.
