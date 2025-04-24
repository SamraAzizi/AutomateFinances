# Simple Finance Dashboard

A user-friendly finance dashboard built with Streamlit, allowing you to upload CSV transaction files, categorize your expenses, and visualize your spending habits.

##  Features

-  Upload CSV files containing transactions
-  Automatically or manually categorize expenses
-  Add and edit categories dynamically
-  View total payments and categorized expenses
-  Interactive pie chart of spending breakdown
-  Persistent category saving using `categories.json`

##  CSV Format

Your uploaded CSV should follow this format:


Date,Details,Amount,Debit/Credit 01 Jan 2025,Grocery Store,150.00,Debit 02 Jan 2025,Salary,3000.00,Credit


- **Date format**: DD MMM YYYY (e.g., 01 Jan 2025)
- **Amount** can contain commas (e.g., 1,200.50)
- **Debit/Credit** must specify whether it's an expense or income

##  How Categorization Works

- Transactions are assigned to "Uncategorized" by default.
- You can manually assign categories in the table.
- When you apply changes, the app saves the Details as a keyword under that category.
- On the next upload, any matching transaction will be auto-categorized.

##  Tech Stack

- **Streamlit** – UI and dashboard
- **Pandas** – Data processing
- **Plotly** – Interactive pie chart
- **JSON** – Local storage for categories

##  Installation

```bash
# Clone the repo
git clone https://github.com/your-username/simple-finance-dashboard.git
cd simple-finance-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run main.py

```

## File Structure
```bash
simple-finance-dashboard/
├── main.py               # Main Streamlit app
├── categories.json       # Stores category keywords
├── README.md             # You're reading it!
└── requirements.txt      # Required Python packages

```

## TODO/Improvements
- Export updated categorized CSV
- Show monthly trends using line charts
- Authentication for multiple users
- Merge similar keywords automatically