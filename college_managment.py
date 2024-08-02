
class college ():
    def __init__(self,name,city,contact):
        self.name = name
        self.city = city
        self.contact = contact
        
    def open_college(self):
        print(f"{self.name} in {self.city} is now open for the semester.")
    def college_details(self):
        print("College Details:")
        print(f"Name: {self.name}")
        print(f"City: {self.city}")
        print(f"Contact: {self.contact}")

class department ():
    def __init__(self,dep_name, dep_id , hod_name , tot_staff ,tot_stud) :
        self.dep_name = dep_name
        self.dep_id = dep_id
        self.hod_name = hod_name
        self.tot_staff= tot_staff
        self.tot_stud = tot_stud
        self.events = []
    def department_details(self):
        print(f" department is {self.dep_name}")
        print(f" department is {self.dep_id}")
        print(f" department is {self.hod_name}")
        print(f" department is {self.tot_staff}")
        print(f" department is {self.tot_stud}")
        
    def add_event(self, event_name, event_date, event_description):
        event = {
            "name": event_name,
            "date": event_date,
            "description": event_description
        }
        self.events.append(event)
        print(f"Event '{event_name}' added to {self.dep_name} department.")

    def show_events(self):
        if not self.events:
            print(f"No events scheduled for {self.dep_name} department.")
            return
        
        print(f"Events for {self.dep_name} department:")
        for event in self.events:
            print(f"Name: {event['name']}, Date: {event['date']}, Description: {event['description']}")

class Student:
    def __init__(self, studentid, studentname, gender, year, classid):
        self.studentid = studentid
        self.studentname = studentname
        self.gender = gender
        self.year = year
        self.classid = classid
        self.fees_paid = 0  
        self.is_present = False  

    def student_details(self):
        print("Student Details:")
        print(f"Name: {self.studentname}")
        print(f"ID: {self.studentid}")
        print(f"Gender: {self.gender}")
        print(f"Year: {self.year}")
        print(f"Class ID: {self.classid}")
        print(f"Fees Paid: {'Yes' if self.fees_paid else 'No'}")
        print(f"Present: {'Yes' if self.is_present else 'No'}")

    def pay_fees(self, amount):
        self.fees_paid += amount
        print(f"Fees of {amount} paid by {self.studentname}. Total fees paid: {self.fees_paid}")

    def mark_present(self):
        self.is_present = True
        print(f"{self.studentname} is marked as present.")

    def mark_absent(self):
        self.is_present = False
        print(f"{self.studentname} is marked as absent.")
class room():
    def __init__(self, classid , section , depid):
        self.classid = classid
        self.section = section
        self.depid = depid
        self.isoccubied = False
        
    def room_details(self):
        print("room Details:")
        print(f"Name: {self.classid}")
        print(f"ID: {self.section}")
        print(f"Gender: {self.depid}")
    
    def occubied(self):
        self.isoccubied = True
        print(f"{self.depid} is availble.")
    def occubied(self):
        self.isoccubied = False
        print(f"{self.depid} is  not availble.")

class Hostel:
    def __init__(self, studentid, block_number, room_number):
        self.studentid = studentid
        self.block_number = block_number
        self.room_number = room_number
        self.checked_in = False  

    def hostel_details(self):
        print("Hostel Details:")
        print(f"Student ID: {self.studentid}")
        print(f"Block Number: {self.block_number}")
        print(f"Room Number: {self.room_number}")
        print(f"Checked In: {'Yes' if self.checked_in else 'No'}")

    def check_in(self):
        if not self.checked_in:
            self.checked_in = True
            print(f"Student ID {self.studentid} has checked into Block {self.block_number}, Room {self.room_number}.")
        else:
            print(f"Student ID {self.studentid} is already checked in.")

    def check_out(self):
        if self.checked_in:
            self.checked_in = False
            print(f"Student ID {self.studentid} has checked out of Block {self.block_number}, Room {self.room_number}.")
        else:
            print(f"Student ID {self.studentid} is already checked out.")


class GHostel(Hostel):
    def __init__(self, studentid, block_number, room_number):
        super().__init__(studentid, block_number, room_number)
        self.hostel_type = "Girls' Hostel"


class BHostel(Hostel):
    def __init__(self, studentid, block_number, room_number):
        super().__init__(studentid, block_number, room_number)
        self.hostel_type = "Boys' Hostel"
    
        