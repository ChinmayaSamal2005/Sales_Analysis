# app.py (Fully Upgraded Version)
from flask import Flask, render_template, request, send_file
import pandas as pd
import os
import io
import plotly.express as px
import plotly.io as pio
from sklearn.linear_model import LinearRegression
import numpy as np
from datetime import datetime

app = Flask(__name__,template_folder='template')
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    bar_chart_html = None
    trend_chart_html = None
    table_data = None
    predictions = None
    top_products = None

    if request.method == 'POST':
        file = request.files['file']
        if file:
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            df = pd.read_excel(filepath)

            df['Revenue'] = df['Quantity Sold'] * df['Unit Price']
            summary = df.groupby('Product Name').agg({'Quantity Sold': 'sum', 'Revenue': 'sum'}).reset_index()
            table_data = summary.to_dict(orient='records')

            # Plotly Bar Chart
            fig = px.bar(
                summary,
                x="Product Name",
                y="Revenue",
                title="💰 Total Revenue by Product",
                color="Revenue",
                color_continuous_scale='Agsunset',
                text_auto=True
            )
            fig.update_traces(marker_line_color='black', marker_line_width=1.5)
            fig.update_layout(transition_duration=500, plot_bgcolor='#111', paper_bgcolor='#111', font_color='white')
            bar_chart_html = pio.to_html(fig, full_html=False)

            # Top 3 Products
            top_products = summary.sort_values(by='Revenue', ascending=False).head(3).to_dict(orient='records')

            # Monthly Trend Chart
            if 'Date' in df.columns:
                df['Date'] = pd.to_datetime(df['Date'])
                monthly_trend = df.groupby([pd.Grouper(key='Date', freq='M'), 'Product Name'])['Quantity Sold'].sum().reset_index()
                trend_fig = px.line(monthly_trend, x='Date', y='Quantity Sold', color='Product Name', title='📈 Monthly Sales Trend')
                trend_fig.update_layout(plot_bgcolor='#111', paper_bgcolor='#111', font_color='white')
                trend_chart_html = pio.to_html(trend_fig, full_html=False)

                # Forecast
                monthly_data = df.groupby(['Date', 'Product Name'])['Quantity Sold'].sum().reset_index()
                predictions = []
                for product in monthly_data['Product Name'].unique():
                    product_data = monthly_data[monthly_data['Product Name'] == product].copy()
                    product_data = product_data.sort_values('Date')
                    product_data['Month'] = range(1, len(product_data) + 1)
                    X = product_data[['Month']]
                    y = product_data['Quantity Sold']
                    model = LinearRegression()
                    model.fit(X, y)
                    next_month = [[len(product_data) + 1]]
                    predicted_sales = model.predict(next_month)[0]
                    predictions.append({
                        "Product": product,
                        "Predicted Quantity Next Month": round(predicted_sales, 2)
                    })

    return render_template("index.html", table=table_data, predictions=predictions, trend_chart=trend_chart_html, top_products=top_products, bar_chart=bar_chart_html)

@app.route('/download-summary')
def download_summary():
    file = os.path.join(app.config['UPLOAD_FOLDER'], os.listdir(app.config['UPLOAD_FOLDER'])[0])
    df = pd.read_excel(file)
    df['Revenue'] = df['Quantity Sold'] * df['Unit Price']
    summary = df.groupby('Product Name').agg({'Quantity Sold': 'sum', 'Revenue': 'sum'}).reset_index()
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        summary.to_excel(writer, index=False, sheet_name='Summary')
    output.seek(0)
    return send_file(output, as_attachment=True, download_name='sales_summary.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == '__main__':
    app.run(debug=True)