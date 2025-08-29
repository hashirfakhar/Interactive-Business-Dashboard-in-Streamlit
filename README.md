# Task 10 - Interactive Business Dashboard in Streamlit

## Objective
- Understand and analyze the **Global Superstore dataset**.
- Perform **data cleaning and preparation**.
- Conduct **exploratory data analysis (EDA)** with visualizations.
- Build a **Streamlit dashboard** for interactive insights.

---

## Dataset
- **File**: `Global Superstore.csv`
- **Columns include**:
  - `Order.Date`: Order placement date
  - `Region`: Region of sales
  - `Category`: Product category
  - `Sales`: Sales value
  - `Profit`: Profit value
  - …and other order-related details.

---

## 🛠Approach
1. **Data Cleaning**
   - Converted `Order.Date` column to proper datetime format.
   - Renamed columns for easier handling.

2. **EDA & Visualizations**
   - Sales by region
   - Sales trend over time
   - Profit by category

3. **Interactive Dashboard (Streamlit)**
   - Built a simple web app (`app.py`) to:
     - Display dataset preview
     - Visualize sales by region
     - Show time-series sales trends
     - Compare profits by category

---

## Results & Insights
- **Central Region (US)** showed the highest sales among all regions.
- Sales trends highlight **seasonal spikes**, especially around year-end.
- **Technology** category generated strong profit margins compared to others.
- The interactive dashboard allows quick exploration of different dimensions.
