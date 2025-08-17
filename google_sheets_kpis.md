### KPI Formulas for Google Sheets

- **Total Income:**  
  `=SUMIF(E:E, "Income", D:D)`

- **Total Expense:**  
  `=SUMIF(E:E, "Expense", D:D)`

- **Net Savings:**  
  `=SUMIF(E:E, "Income", D:D) - SUMIF(E:E, "Expense", D:D)`

- **Savings Ratio (%):**  
  `=((SUMIF(E:E, "Income", D:D) - SUMIF(E:E, "Expense", D:D)) / SUMIF(E:E, "Income", D:D)) * 100`
