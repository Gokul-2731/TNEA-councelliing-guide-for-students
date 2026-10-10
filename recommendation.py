from database import connect_db


# ==========================================================
# GET COLLEGE DATA
# ==========================================================

def get_colleges():

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            c.id,
            c.college_code,
            c.name,
            c.location,
            c.type,
            c.placement,

            b.id,
            b.branch_code,
            b.department,
            b.fees,

            co.year,
            co.cutoff

        FROM colleges c

        JOIN branches b
            ON c.id = b.college_id

        LEFT JOIN cutoffs co
            ON b.id = co.branch_id

        ORDER BY c.name, b.department, co.year DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    colleges = []

    for row in rows:

        colleges.append({
            "college_id": row[0],
            "college_code": row[1],
            "name": row[2],
            "location": row[3],
            "type": row[4],
            "placement": row[5],

            "branch_id": row[6],
            "branch_code": row[7],
            "department": row[8],
            "fees": row[9],

            "year": row[10],
            "cutoff": row[11]
        })

    return colleges


# ==========================================================
# CUTOFF CATEGORY
# ==========================================================

def get_category(student_cutoff, college_cutoff):

    if college_cutoff is None:
        return "Unknown"

    difference = student_cutoff - college_cutoff

    if difference >= 10:
        return "Safe"

    elif difference >= 5:
        return "Safe"

    elif difference >= 0:
        return "Moderate"

    elif difference >= -5:
        return "Ambitious"

    else:
        return "Highly Ambitious"


# ==========================================================
# CUTOFF SCORE
# Maximum = 50
# ==========================================================

def calculate_cutoff_score(
    student_cutoff,
    college_cutoff
):

    if college_cutoff is None:
        return 0

    difference = student_cutoff - college_cutoff

    if difference >= 10:
        return 50

    elif difference >= 5:
        return 45

    elif difference >= 0:
        return 40

    elif difference >= -5:
        return 25

    elif difference >= -10:
        return 10

    else:
        return 0


# ==========================================================
# FEES SCORE
# Maximum = 15
# ==========================================================

def calculate_fee_score(
    college_fees,
    student_budget
):

    if student_budget == "No Limit":
        return 15

    if college_fees <= student_budget:
        return 15

    elif college_fees <= student_budget + 10000:
        return 8

    else:
        return 0


# ==========================================================
# LOCATION SCORE
# Maximum = 10
# ==========================================================

def calculate_location_score(
    college_location,
    student_location
):

    if student_location == "Any Location":
        return 10

    if college_location == student_location:
        return 10

    return 0


# ==========================================================
# COLLEGE TYPE SCORE
# Maximum = 10
# ==========================================================

def calculate_type_score(
    college_type,
    student_type
):

    if student_type == "Any Type":
        return 10

    if college_type == student_type:
        return 10

    return 0


# ==========================================================
# PLACEMENT SCORE
# Maximum = 15
# ==========================================================

def calculate_placement_score(
    placement
):

    if placement is None:
        return 0

    # Placement rating is between 1 and 5
    score = (placement / 5) * 15

    return round(score)


# ==========================================================
# TOTAL MATCH SCORE
# Maximum = 100
#
# Cutoff    = 50
# Fees      = 15
# Location  = 10
# Type      = 10
# Placement = 15
# ==========================================================

def calculate_score(
    student_cutoff,
    college,
    fees,
    location,
    college_type
):

    cutoff_score = calculate_cutoff_score(
        student_cutoff,
        college["cutoff"]
    )

    fee_score = calculate_fee_score(
        college["fees"],
        fees
    )

    location_score = calculate_location_score(
        college["location"],
        location
    )

    type_score = calculate_type_score(
        college["type"],
        college_type
    )

    placement_score = calculate_placement_score(
        college["placement"]
    )

    total_score = (
        cutoff_score
        + fee_score
        + location_score
        + type_score
        + placement_score
    )

    return min(total_score, 100)


# ==========================================================
# GENERATE REASONS
# ==========================================================

def generate_reasons(
    student_cutoff,
    college,
    fees,
    location,
    college_type
):

    reasons = []

    college_cutoff = college["cutoff"]

    # ------------------------------------------------------
    # CUTOFF
    # ------------------------------------------------------

    if college_cutoff is not None:

        difference = student_cutoff - college_cutoff

        if difference >= 10:

            reasons.append(
                "Your cutoff is significantly above "
                "the previous cutoff."
            )

        elif difference >= 5:

            reasons.append(
                "Your cutoff is comfortably above "
                "the previous cutoff."
            )

        elif difference >= 0:

            reasons.append(
                "Your cutoff meets or exceeds "
                "the previous cutoff."
            )

        elif difference >= -5:

            reasons.append(
                "Your cutoff is slightly below "
                "the previous cutoff."
            )

        else:

            reasons.append(
                "Your cutoff is below the previous "
                "cutoff, making this ambitious."
            )

    # ------------------------------------------------------
    # FEES
    # ------------------------------------------------------

    if fees == "No Limit":

        reasons.append(
            "Your budget has no upper limit."
        )

    elif college["fees"] <= fees:

        reasons.append(
            "Annual fees are within your selected budget."
        )

    elif college["fees"] <= fees + 10000:

        reasons.append(
            "Annual fees are slightly above your budget."
        )

    else:

        reasons.append(
            "Annual fees are above your selected budget."
        )

    # ------------------------------------------------------
    # LOCATION
    # ------------------------------------------------------

    if location == "Any Location":

        reasons.append(
            "You selected any location."
        )

    elif college["location"] == location:

        reasons.append(
            "The college location matches your preference."
        )

    # ------------------------------------------------------
    # COLLEGE TYPE
    # ------------------------------------------------------

    if college_type == "Any Type":

        reasons.append(
            "You selected any college type."
        )

    elif college["type"] == college_type:

        reasons.append(
            "The college type matches your preference."
        )

    # ------------------------------------------------------
    # PLACEMENT
    # ------------------------------------------------------

    placement = college["placement"]

    if placement is not None:

        if placement >= 4.5:

            reasons.append(
                "The college has a strong placement rating."
            )

        elif placement >= 4.0:

            reasons.append(
                "The college has a good placement rating."
            )

        else:

            reasons.append(
                "The college has a moderate placement rating."
            )

    return reasons


# ==========================================================
# FIND RECOMMENDED COLLEGES
# ==========================================================

def find_colleges(
    student_cutoff,
    department,
    fees,
    location,
    college_type
):

    results = []

    colleges = get_colleges()

    for college in colleges:

        # --------------------------------------------------
        # DEPARTMENT FILTER
        # --------------------------------------------------

        if college["department"] != department:
            continue

        # --------------------------------------------------
        # CALCULATE SCORE
        # --------------------------------------------------

        score = calculate_score(
            student_cutoff,
            college,
            fees,
            location,
            college_type
        )

        # --------------------------------------------------
        # CATEGORY
        # --------------------------------------------------

        category = get_category(
            student_cutoff,
            college["cutoff"]
        )

        # --------------------------------------------------
        # CUTOFF DIFFERENCE
        # --------------------------------------------------

        if college["cutoff"] is not None:

            difference = round(
                student_cutoff - college["cutoff"],
                2
            )

        else:

            difference = None

        # --------------------------------------------------
        # REASONS
        # --------------------------------------------------

        reasons = generate_reasons(
            student_cutoff,
            college,
            fees,
            location,
            college_type
        )

        # --------------------------------------------------
        # RESULT
        # --------------------------------------------------

        results.append({

            "college": college,

            "score": score,

            "category": category,

            "difference": difference,

            "reasons": reasons
        })

    # ======================================================
    # SORT BY BEST MATCH
    # ======================================================

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results