# 💼 Business Sales Analyzer

An advanced Flask-based web application that empowers business owners to **upload Excel sales data**, visualize their performance, forecast future sales, and download actionable reports — all in one stylish, interactive dashboard.

---

## 🚀 Features

- 📤 **Upload Sales Excel File** (`.xlsx`)
- 📊 **Interactive Bar Chart** showing total revenue per product (Plotly)
- 📈 **Monthly Sales Trend** line graph
- 🔮 **Forecast Next Month’s Sales** using Linear Regression
- 🏆 **Top 3 Best-Selling Products**
- ⬇️ **Downloadable Summary Report** as Excel
- 🎨 **Modern UI** with animations, gradients, and glassmorphism styling

---

## 🧠 Technologies Used

| Category         | Tool/Library              |
|------------------|---------------------------|
| Backend          | Flask                     |
| Data Processing  | Pandas, NumPy             |
| Visualization    | Plotly, HTML, CSS         |
| Machine Learning | scikit-learn (Regression) |
| Excel Handling   | openpyxl, xlsxwriter      |
| Styling          | Custom CSS with animation |

---

## 📈 Algorithm Used: Linear Regression

### 🔍 Why Linear Regression?
- Simple and interpretable
- Great for modeling trends in time series data

### 🧠 How it Works
1. Monthly sales grouped per product
2. Time index (Month 1, 2, …)
3. Model trained on `(month, quantity)`
4. Predicts quantity for next month

💼 Why This App Helps Businessmen
	•	✅ Quickly identify best-performing products
	•	📊 Visualize trends and seasonality
	•	🔮 Forecast future demand
	•	🧾 Download Excel reports
	•	🤖 No Excel or analytics skills needed!

 🛠️ Future Enhancements
	•	📝 Export as PDF reports
	•	🔐 Add user login system
	•	☁️ Deploy on Render or PythonAnywhere
	•	📦 Database support (PostgreSQL/SQLite)

 
Chinmaya Samal
🎓 B.Tech CSE @ SRM University
📫 GitHub

📄 License

Licensed under the MIT License — free to use and modify for any purpose.


⭐ Found this helpful? Give a ⭐ on GitHub and share with fellow developers and business owners!
