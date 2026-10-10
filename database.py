import sqlite3


DATABASE = "database/tnea.db"


def connect_db():
    return sqlite3.connect(DATABASE)


# ==================================================
# CREATE TABLES
# ==================================================

def create_tables():

    connection = connect_db()
    cursor = connection.cursor()

    # --------------------------------------------------
    # COLLEGES
    # --------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS colleges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            college_code TEXT UNIQUE,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            type TEXT NOT NULL,
            placement REAL
        )
    """)

    # --------------------------------------------------
    # BRANCHES
    # --------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS branches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            college_id INTEGER NOT NULL,
            branch_code TEXT NOT NULL,
            department TEXT NOT NULL,
            fees INTEGER NOT NULL,

            FOREIGN KEY (college_id)
                REFERENCES colleges(id)
        )
    """)

    # --------------------------------------------------
    # CUTOFFS
    # --------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cutoffs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            branch_id INTEGER NOT NULL,
            year INTEGER NOT NULL,
            cutoff REAL NOT NULL,

            FOREIGN KEY (branch_id)
                REFERENCES branches(id)
        )
    """)

    connection.commit()
    connection.close()


# ==================================================
# ADD COLLEGE
# ==================================================

def add_college(
    college_code,
    name,
    location,
    college_type,
    placement
):

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO colleges
        (college_code, name, location, type, placement)
        VALUES (?, ?, ?, ?, ?)
    """, (
        college_code,
        name,
        location,
        college_type,
        placement
    ))

    connection.commit()

    college_id = cursor.lastrowid

    connection.close()

    return college_id


# ==================================================
# ADD BRANCH
# ==================================================

def add_branch(
    college_id,
    branch_code,
    department,
    fees
):

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO branches
        (college_id, branch_code, department, fees)
        VALUES (?, ?, ?, ?)
    """, (
        college_id,
        branch_code,
        department,
        fees
    ))

    connection.commit()

    branch_id = cursor.lastrowid

    connection.close()

    return branch_id


# ==================================================
# ADD CUTOFF
# ==================================================

def add_cutoff(
    branch_id,
    year,
    cutoff
):

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO cutoffs
        (branch_id, year, cutoff)
        VALUES (?, ?, ?)
    """, (
        branch_id,
        year,
        cutoff
    ))

    connection.commit()
    connection.close()


# ==================================================
# GET ALL COLLEGES
# ==================================================

def get_all_colleges():

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM colleges
        ORDER BY name
    """)

    colleges = cursor.fetchall()

    connection.close()

    return colleges


# ==================================================
# GET ALL BRANCHES
# ==================================================

def get_all_branches():

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM branches
        ORDER BY department
    """)

    branches = cursor.fetchall()

    connection.close()

    return branches


# ==================================================
# GET ALL CUTOFFS
# ==================================================

def get_all_cutoffs():

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM cutoffs
        ORDER BY year DESC
    """)

    cutoffs = cursor.fetchall()

    connection.close()

    return cutoffs


# ==================================================
# DELETE COLLEGE
# ==================================================

def delete_college(college_id):

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM colleges WHERE id = ?",
        (college_id,)
    )

    connection.commit()
    connection.close()


# ==================================================
# TEST DATABASE
# ==================================================

if __name__ == "__main__":

    create_tables()

    print("Database created successfully.")

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        ORDER BY name
    """)

    tables = cursor.fetchall()

    print("\nTables:")

    for table in tables:
        print("-", table[0])

    connection.close()
if __name__ == "__main__":

    create_tables()

    college_id = add_college(
        "TEST001",
        "Test Engineering College",
        "Chennai",
        "Private",
        4
    )

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id
        FROM colleges
        WHERE college_code = ?
    """, ("TEST001",))

    result = cursor.fetchone()

    connection.close()

    college_id = result[0]

    branch_id = add_branch(
        college_id,
        "CS",
        "CSE",
        85000
    )

    add_cutoff(
        branch_id,
        2025,
        180.00
    )

    print("Test data added successfully.")