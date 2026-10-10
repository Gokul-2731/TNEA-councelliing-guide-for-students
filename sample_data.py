from database import (
    create_tables,
    add_college,
    add_branch,
    add_cutoff
)


# ==================================================
# CREATE DATABASE
# ==================================================

create_tables()


# ==================================================
# FICTIONAL COLLEGES
# ==================================================

colleges = [

    {
        "code": "NCET001",
        "name": "Naidu College of Engineering and Technology",
        "location": "Chennai",
        "type": "Private",
        "placement": 4.5
    },

    {
        "code": "SIT002",
        "name": "Silver Oak Institute of Technology",
        "location": "Chengalpattu",
        "type": "Private",
        "placement": 4.2
    },

    {
        "code": "GVT003",
        "name": "Green Valley Government Engineering College",
        "location": "Kanchipuram",
        "type": "Government",
        "placement": 4.0
    },

    {
        "code": "RCE004",
        "name": "Royal Crest College of Engineering",
        "location": "Coimbatore",
        "type": "Private",
        "placement": 4.3
    },

    {
        "code": "VIT005",
        "name": "Velan Institute of Technology",
        "location": "Tiruvallur",
        "type": "Private",
        "placement": 3.9
    },

    {
        "code": "AEC006",
        "name": "Alpha Engineering College",
        "location": "Trichy",
        "type": "Government Aided",
        "placement": 4.1
    }
]


# ==================================================
# BRANCHES + CUTOFFS
# ==================================================

branch_data = {

    "NCET001": [
        ("CS", "CSE", 95000, 2025, 185.50),
        ("IT", "IT", 90000, 2025, 180.25),
        ("EC", "ECE", 85000, 2025, 175.50),
        ("AD", "AI & DS", 95000, 2025, 182.00)
    ],

    "SIT002": [
        ("CS", "CSE", 90000, 2025, 178.50),
        ("EC", "ECE", 85000, 2025, 172.25),
        ("EE", "EEE", 80000, 2025, 165.50)
    ],

    "GVT003": [
        ("CS", "CSE", 50000, 2025, 190.00),
        ("EC", "ECE", 45000, 2025, 182.50),
        ("ME", "Mechanical", 40000, 2025, 155.00),
        ("CE", "Civil", 40000, 2025, 150.00)
    ],

    "RCE004": [
        ("CS", "CSE", 100000, 2025, 183.75),
        ("IT", "IT", 95000, 2025, 178.00),
        ("EC", "ECE", 90000, 2025, 170.50)
    ],

    "VIT005": [
        ("CS", "CSE", 85000, 2025, 170.00),
        ("AD", "AI & DS", 90000, 2025, 168.50),
        ("AL", "AI & ML", 90000, 2025, 165.75)
    ],

    "AEC006": [
        ("CS", "CSE", 70000, 2025, 176.50),
        ("EC", "ECE", 65000, 2025, 168.00),
        ("EE", "EEE", 60000, 2025, 160.50)
    ]
}


# ==================================================
# INSERT DATA
# ==================================================

for college in colleges:

    college_id = add_college(
        college["code"],
        college["name"],
        college["location"],
        college["type"],
        college["placement"]
    )

    # If college already exists, find its ID
    if not college_id:

        from database import connect_db

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT id FROM colleges WHERE college_code = ?",
            (college["code"],)
        )

        college_id = cursor.fetchone()[0]

        connection.close()

    for branch in branch_data[college["code"]]:

        branch_code = branch[0]
        department = branch[1]
        fees = branch[2]
        year = branch[3]
        cutoff = branch[4]

        branch_id = add_branch(
            college_id,
            branch_code,
            department,
            fees
        )

        add_cutoff(
            branch_id,
            year,
            cutoff
        )


print()
print("====================================")
print(" SAMPLE DATA IMPORTED SUCCESSFULLY")
print("====================================")
print()
print("Colleges : 6")
print("Branches : 20")
print("Cutoffs  : 20")
print()
print("All colleges are fictional demo data.")