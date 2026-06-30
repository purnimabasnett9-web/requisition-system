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
