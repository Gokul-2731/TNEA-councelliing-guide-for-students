from database import create_tables, add_college, add_branch, add_cutoff


def main():

    create_tables()

    print("\n===== ADD NEW COLLEGE =====\n")

    college_code = input("College Code: ")
    college_name = input("College Name: ")
    location = input("Location: ")
    college_type = input("College Type: ")

    placement = float(
        input("Placement Rating (0-5): ")
    )

    college_id = add_college(
        college_code,
        college_name,
        location,
        college_type,
        placement
    )

    print("\nCollege added successfully!")
    print("College ID:", college_id)

    while True:

        print("\n----- ADD BRANCH -----")

        branch_code = input("Branch Code: ")
        department = input("Department: ")
        fees = int(input("Annual Fees: "))

        branch_id = add_branch(
            college_id,
            branch_code,
            department,
            fees
        )

        print("Branch added successfully!")
        print("Branch ID:", branch_id)

        add_more = input(
            "\nAdd another branch? (y/n): "
        ).lower()

        if add_more != "y":
            break

    while True:

        print("\n----- ADD CUTOFF -----")

        branch_id = int(
            input("Branch ID: ")
        )

        year = int(
            input("Cutoff Year: ")
        )

        cutoff = float(
            input("Cutoff: ")
        )

        add_cutoff(
            branch_id,
            year,
            cutoff
        )

        print("Cutoff added successfully!")

        add_more = input(
            "\nAdd another cutoff? (y/n): "
        ).lower()

        if add_more != "y":
            break

    print("\n================================")
    print("College data added successfully!")
    print("================================")


if __name__ == "__main__":
    main()