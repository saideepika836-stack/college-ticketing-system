# ============================================
#       COLLEGE TICKETING SYSTEM
# ============================================

tickets = []
ticket_id = 1001


def create_ticket():
    global ticket_id

    print("\n========== CREATE TICKET ==========")

    student_name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    
    print("\nSelect Problem Category:")
    print("1. IT Problem")
    print("2. Projector Problem")
    print("3. Maintenance Problem")
    print("4. Other")

    choice = input("Enter your choice: ")

    categories = {
        "1": "IT Problem",
        "2": "Projector Problem",
        "3": "Maintenance Problem",
        "4": "Other"
    }

    category = categories.get(choice, "Other")

    problem = input("Enter problem description: ")

    ticket = {
        "id": ticket_id,
        "student_name": student_name,
        "roll_number": roll_number,
        "category": category,
        "problem": problem,
        "status": "Open"
    }

    tickets.append(ticket)

    print("\nTicket created successfully!")
    print("Your Ticket ID is:", ticket_id)

    ticket_id += 1


def view_tickets():
    print("\n========== ALL TICKETS ==========")

    if not tickets:
        print("No tickets available.")
        return

    for ticket in tickets:
        print("\n------------------------------")
        print("Ticket ID      :", ticket["id"])
        print("Student Name   :", ticket["student_name"])
        print("Roll Number    :", ticket["roll_number"])
        print("Category       :", ticket["category"])
        print("Problem        :", ticket["problem"])
        print("Status         :", ticket["status"])


def update_ticket():
    print("\n========== UPDATE TICKET ==========")

    if not tickets:
        print("No tickets available.")
        return

    try:
        search_id = int(input("Enter Ticket ID: "))
    except ValueError:
        print("Invalid Ticket ID.")
        return

    for ticket in tickets:
        if ticket["id"] == search_id:

            print("\nCurrent Status:", ticket["status"])
            print("\nSelect New Status:")
            print("1. Open")
            print("2. In Progress")
            print("3. Completed")

            choice = input("Enter your choice: ")

            status = {
                "1": "Open",
                "2": "In Progress",
                "3": "Completed"
            }

            if choice in status:
                ticket["status"] = status[choice]
                print("\nTicket status updated successfully!")
            else:
                print("\nInvalid choice.")

            return

    print("\nTicket not found.")


def search_ticket():
    print("\n========== SEARCH TICKET ==========")

    if not tickets:
        print("No tickets available.")
        return

    try:
        search_id = int(input("Enter Ticket ID: "))
    except ValueError:
        print("Invalid Ticket ID.")
        return

    for ticket in tickets:
        if ticket["id"] == search_id:
            print("\nTicket Found!")
            print("------------------------------")
            print("Ticket ID      :", ticket["id"])
            print("Student Name   :", ticket["student_name"])
            print("Roll Number    :", ticket["roll_number"])
            print("Category       :", ticket["category"])
            print("Problem        :", ticket["problem"])
            print("Status         :", ticket["status"])
            return

    print("\nTicket not found.")


def show_statistics():
    print("\n========== TICKET STATISTICS ==========")

    total = len(tickets)
    open_count = 0
    progress_count = 0
    completed_count = 0

    for ticket in tickets:
        if ticket["status"] == "Open":
            open_count += 1
        elif ticket["status"] == "In Progress":
            progress_count += 1
        elif ticket["status"] == "Completed":
            completed_count += 1

    print("Total Tickets       :", total)
    print("Open Tickets        :", open_count)
    print("In Progress         :", progress_count)
    print("Completed Tickets   :", completed_count)


# ============================================
#              MAIN MENU
# ============================================

while True:

    print("\n========================================")
    print("       COLLEGE TICKETING SYSTEM")
    print("========================================")

    print("1. Create Ticket")
    print("2. View All Tickets")
    print("3. Update Ticket Status")
    print("4. Search Ticket")
    print("5. Ticket Statistics")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        create_ticket()

    elif choice == "2":
        view_tickets()

    elif choice == "3":
        update_ticket()

    elif choice == "4":
        search_ticket()

    elif choice == "5":
        show_statistics()

    elif choice == "6":
        print("\nThank you for using College Ticketing System!")
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")