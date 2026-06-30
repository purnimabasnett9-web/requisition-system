print("Requisition System")

# Global variable for unique requisition ID
requisition_counter = 10000


class Requisition:

    def __init__(self, date, staff_id, staff_name):
        global requisition_counter

        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name

        requisition_counter = requisition_counter + 1
        self.requisition_id = requisition_counter

        self.total = 0
        self.status = "Pending"
        self.approval_ref = "Not available"

    # Method to add requisition items
    def add_requisition(self):
        print("\nAdd requisition items:")

        while True:
            item_name = input("Enter item name: ")
            item_cost = float(input("Enter item cost: $"))

            self.total = self.total + item_cost

            choice = input("Do you want to add another item? yes/no: ")

            if choice != "yes":
                break

        return self.total

    # Method to approve requisition automatically
    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_ref = self.requisition_id
        else:
            self.status = "Pending"
            self.approval_ref = "Not available"

    # Method for manager response
    def respond_requisition(self):
        if self.status == "Pending":
            print("\nRequisition ID:", self.requisition_id)
            print("Staff Name:", self.staff_name)
            print("Total: $", self.total)

            response = input("Enter manager response Approved / Not approved / Pending: ")

            if response == "Approved":
                self.status = "Approved"
                self.approval_ref = self.requisition_id

            elif response == "Not approved":
                self.status = "Not approved"
                self.approval_ref = "Not available"

            elif response == "Pending":
                self.status = "Pending"
                self.approval_ref = "Not available"

    # Method to display requisition information
    def display_requisition(self):
        print("\nDate:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total: $", self.total)
        print("Status:", self.status)

        if self.status == "Approved":
            print("Approval Reference Number:", self.staff_id, self.approval_ref)
        else:
            print("Approval Reference Number:", self.approval_ref)


# Method to display all requisition statistics
def requisition_statistics(requisitions):
    total_submitted = len(requisitions)
    approved = 0
    pending = 0
    not_approved = 0

    for requisition in requisitions:
        if requisition.status == "Approved":
            approved = approved + 1
        elif requisition.status == "Pending":
            pending = pending + 1
        elif requisition.status == "Not approved":
            not_approved = not_approved + 1

    print("\nDisplaying the Requisition Statistics")
    print("The total number of requisitions submitted:", total_submitted)
    print("The total number of approved requisitions:", approved)
    print("The total number of pending requisitions:", pending)
    print("The total number of not approved requisitions:", not_approved)


requisitions = []

# Ask user how many requisitions they want to add
number_of_requisitions = int(input("How many requisitions do you want to add? "))

for i in range(number_of_requisitions):
    print("Requisition", i + 1)

    date = input("Date: ")
    staff_id = input("Staff ID: ")
    staff_name = input("Staff Name: ")

    # Create object
    requisition = Requisition(date, staff_id, staff_name)

    print("Requisition ID:", requisition.requisition_id)

    # Add items and approve automatically
    requisition.add_requisition()
    requisition.approve_requisition()

    requisitions.append(requisition)

    print("\nRequisition added successfully.")
    print("Total: $", requisition.total)
    print("Status:", requisition.status)

    if requisition.status == "Approved":
        print("Approval Reference Number:", requisition.staff_id, requisition.approval_ref)
    else:
        print("Approval Reference Number:", requisition.approval_ref)


print("\nManager Response Section")

# Manager responds to pending requisitions
for requisition in requisitions:
    requisition.respond_requisition()


print("\nPrinting Requisitions:")

# Display all requisitions
for requisition in requisitions:
    requisition.display_requisition()


# Display statistics
requisition_statistics(requisitions)