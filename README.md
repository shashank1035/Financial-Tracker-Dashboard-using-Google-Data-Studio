# Financial Tracker Dashboard using Google Data Studio

## 📌 Overview
The **Financial Tracker Dashboard** is an interactive solution built using **Google Data Studio** and **Google Sheets** to track income, expenses, and savings. It provides real-time insights, category-wise analysis, and KPIs for better financial planning.

---

## ✅ Features
- Track **monthly income vs. expenses**
- Visualize **category-wise spending patterns**
- Calculate **Net Savings** and **Savings Ratio (%)**
- Interactive filters for **Month** and **Payment Method**
- Automated updates via **Google Sheets**

---

## 📂 Project Structure
```
Financial-Tracker-Dashboard/
│
├── data/                      # Contains actual financial data
│   └── transactions.csv
│
├── scripts/                   # Python script to upload data to Google Sheets
│   └── upload_to_sheets.py
│
├── docs/                      # Screenshots and visual documentation
│   └── dashboard_screenshot.png
│
├── formulas/                  # Google Sheets KPI formulas
│   └── google_sheets_kpis.md
│
└── README.md                  # Project details
```

---

## 🛠 Tech Stack
- **Google Data Studio** – Dashboard and Visualization
- **Google Sheets** – Data Source
- **Python (Optional)** – Data cleaning and uploading via Sheets API
- **Google Apps Script (Optional)** – Automation

---

## 🚀 Steps to Set Up
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Financial-Tracker-Dashboard.git
   cd Financial-Tracker-Dashboard
   ```
2. Open the `data/transactions.csv` file and upload it to **Google Sheets**.
3. Connect **Google Sheets** to **Google Data Studio**.
4. Create calculated fields for:
   - **Total Income**
   - **Total Expenses**
   - **Net Savings**
   - **Savings Ratio (%)**
5. Design the dashboard with **scorecards, charts, and filters**.
6. (Optional) Use `scripts/upload_to_sheets.py` to automate updates.

---

## 📊 KPI Formulas (Google Sheets)
- **Total Income:**  
  `=SUMIF(E:E, "Income", D:D)`

- **Total Expense:**  
  `=SUMIF(E:E, "Expense", D:D)`

- **Net Savings:**  
  `=SUMIF(E:E, "Income", D:D) - SUMIF(E:E, "Expense", D:D)`

- **Savings Ratio (%):**  
  `=((SUMIF(E:E, "Income", D:D) - SUMIF(E:E, "Expense", D:D)) / SUMIF(E:E, "Income", D:D)) * 100`

---

## 📸 Dashboard Preview
![Dashboard Screenshot](docs/dashboard_screenshot.png)

---

## 🔗 Live Dashboard
*(Add your Google Data Studio link here after publishing)*

---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
This project is open-source under the [MIT License](LICENSE).
