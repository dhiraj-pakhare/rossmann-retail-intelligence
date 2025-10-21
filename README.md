Rossmann Retail Intelligence Project
====================================

A full-stack business intelligence solution that analyzes Rossmann store performance across sales, promotions, and efficiency. This project combines Python, MySQL, and Tableau to deliver actionable insights and recruiter-grade polish.

------------------------------------------------------------
📊 Dashboard
------------------------------------------------------------

View the interactive Tableau dashboard:
https://public.tableau.com/views/YourDashboardName/Sheet1

Features:
- Total revenue and average sales per customer
- Store efficiency scoring
- Top stores by revenue
- Monthly sales trends
- Promo vs non-promo revenue comparison
- Interactive filters: promotion, day of week, store type, assortment

------------------------------------------------------------
🛠️ Tech Stack
------------------------------------------------------------

- Python: Data cleaning, transformation, and MySQL insertion
- MySQL: Structured storage of cleaned sales data
- Tableau: Dashboard visualization and storytelling
- (Optional) Streamlit: For future AI/ML integration
- (Optional) scikit-learn / XGBoost: For forecasting and promo scoring

------------------------------------------------------------
📂 Project Structure
------------------------------------------------------------

rossmann-retail-intelligence/
├── README.txt
├── requirements.txt
├── data/
│   ├── raw/
│   │   ├── train.csv
│   │   ├── store.csv
│   │   ├── test.csv
│   │   ├── sample_submission.csv
│   │   └── rossmann_sales.csv
├── mysql/
│   ├── schema.sql
│   └── insert_queries.sql
├── python/
│   └── data_pipeline.py
├── dashboard/
│   ├── dashboard_info.md
│   └── dashboard_screenshot.png

------------------------------------------------------------
⚙️ How It Works
------------------------------------------------------------

1. Data Cleaning (python/data_pipeline.py)
   - Merges train.csv and store.csv
   - Converts dates, maps holiday codes, filters out closed stores and zero sales
   - Drops nulls and prepares data for insertion

2. MySQL Integration
   - Connects to local MySQL database 'rossmann'
   - Inserts cleaned rows into 'sales' table
   - Tracks success/failure counts and commits in batches

3. Tableau Dashboard
   - Connects to MySQL or uses exported rossmann_sales.csv
   - Visualizes key metrics and trends
   - Publishes to Tableau Public for sharing

------------------------------------------------------------
🤖 AI/ML (Coming Soon)
------------------------------------------------------------

Planned enhancements:
- Sales forecasting using XGBoost
- Promo effectiveness scoring
- Anomaly detection for sales drops/spikes
- Streamlit frontend for interactive AI insights

------------------------------------------------------------
📦 Installation
------------------------------------------------------------

Install required Python packages:
pip install -r requirements.txt

------------------------------------------------------------
✅ Status
------------------------------------------------------------

- ✔️ Data pipeline complete
- ✔️ MySQL integration working
- ✔️ Tableau dashboard published
- 🔜 AI/ML features in progress

------------------------------------------------------------
📬 Contact
------------------------------------------------------------

Built by Dhiraj  
Connect on LinkedIn or explore more on GitHub: https://github.com/yourusername

