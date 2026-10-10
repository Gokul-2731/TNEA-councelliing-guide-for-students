# 🎓 TNEA Student Guide — Pro Edition

A desktop college counselling navigator for Tamil Nadu Engineering Admissions (TNEA), featuring a direct CustomTkinter interface for exploring college options and counselling tools.

---

## ✨ Highlights & New Features

1. **Direct Desktop App** (`python app.py` or `python main.py`):
   - Opens a native CustomTkinter window; it does not start Flask or open a localhost page.
   - Includes college recommendations, college and cutoff explorers, and a counselling guide.

2. **Core Analytics & Scoring**:
   - Shared **100-Point Recommendation Engine** (`recommendation.py`):
     - **Cutoff Margin (50 pts)**
     - **Budget Affordability (15 pts)**
     - **Placement Track Record (15 pts)**
     - **District Location Match (10 pts)**
     - **Management Type (10 pts)**
   - Categorization into **Safe**, **Moderate**, and **Ambitious** tiers.
   - Shared SQLite Database (`database/tnea.db`).

---

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Desktop Application
```bash
python app.py
```
This opens the program in a desktop window. `python main.py` launches the same application.

---

## 📁 Project Structure

```
TNEA_Student_Guide_Pro/
├── app.py                     # Direct desktop application launcher
├── main.py                    # Optimized CustomTkinter desktop launcher
├── database.py                # SQLite schema & queries (database/tnea.db)
├── recommendation.py          # 100-Point multi-factor matching engine
├── requirements.txt           # Desktop dependency (customtkinter)
├── static/
│   ├── css/style.css          # Modern dark-glass design system
│   ├── js/main.js             # Cutoff calculator and live filters
│   └── images/                # Static web assets
├── templates/                 # Jinja2 web templates
│   ├── base.html              # Shell with quote ticker & navbar
│   ├── index.html             # Homepage with hero and calculator
│   ├── find_colleges.html     # Preference form
│   ├── results.html           # Recommendations & choice strategy sidebar
│   ├── colleges.html          # Searchable college directory
│   ├── cutoffs.html           # Historical cutoff explorer
│   ├── guide.html             # 7-Step TNEA roadmap
│   └── about.html             # Scoring methodology & disclosures
└── gui/                       # Lag-free CustomTkinter desktop package
    ├── theme.py               # Design tokens & color palette
    ├── widgets.py             # Optimized zero-lag components
   ├── home.py                # Desktop home and navigation
    ├── student_form.py        # Desktop form view
    ├── results.py             # Desktop results dashboard
    ├── colleges.html          # Desktop college explorer
    ├── cutoff.py              # Desktop cutoff viewer
    ├── guide.py               # Desktop counselling roadmap
    └── about.py               # Desktop methodology view
```
