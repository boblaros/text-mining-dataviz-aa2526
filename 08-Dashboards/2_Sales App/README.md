# Retail Sales Dashboard

A comprehensive retail analytics dashboard built with Dash and Plotly for analyzing sales performance across stores and departments.

## Overview

This dashboard provides interactive analysis of retail sales data with period-over-period comparison capabilities, featuring:
- Comparative analysis between two time periods
- Store-level performance metrics
- Department-level sales analysis
- Weekly sales trends visualization
- Holiday vs. regular sales tracking

## Features

### 1. Period Selection
Interactive dropdown menus to select:
- **Current Period**: Month to analyze
- **Reference Period**: Month to compare against

### 2. Key Performance Indicators (KPIs)
Three cards displaying:
- **Total Sales**: Current period sales with difference indicator
- **Holiday Sales**: Sales during holiday periods with difference
- **Total Stores**: Number of active stores with difference

Each card shows:
- Current value
- Positive (+$X.XM) or negative (-$X.XM) difference vs. reference period
- Color-coded styling (#090059 for values)

### 3. Weekly Sales Comparison
Line chart showing week-by-week sales trends:
- Two lines comparing current period (red) vs. reference period (blue)
- Week numbers on x-axis
- Sales values on y-axis (formatted as $XM)

### 4. Top Stores Analysis
Side-by-side horizontal bar charts showing:
- Top 10 stores by sales for current period
- Top 10 stores by sales for reference period
- Sales values displayed on bars
- Color-coded: Red for current, Blue for reference

### 5. Department Sales Difference
Horizontal bar chart displaying:
- Top 10 departments
- Sales difference between periods (Current - Reference)
- Positive differences indicate growth, negative indicate decline

## Dataset

### Source
- CSV file: `retail_sales.csv` (14.6 MB)
- Can be loaded from GitHub: [retail_sales.csv](https://raw.githubusercontent.com/nluninja/text-mining-dataviz/refs/heads/main/6.%20Dashboards/2_Sales%20App/retail_sales.csv)

### Schema
```
Columns:
- Store: Store identifier (integer)
- Dept: Department identifier (integer)
- Date: Transaction date (YYYY-MM-DD)
- Weekly_Sales: Sales amount for the week (float)
- IsHoliday: Boolean (1 = holiday week, 0 = regular week)
- Month: Month name (derived)
- month: Month number (derived)
```

## Technical Implementation

### Data Processing Pipeline

#### 1. Monthly Aggregation
```python
monthly_sales_df = pd_2.groupby(['month','Month']).agg({
    'Weekly_Sales':'sum'
}).reset_index()
```

#### 2. Holiday Sales Calculation
```python
holiday_sales = pd_2[pd_2['IsHoliday'] == 1].groupby(['month'])[
    'Weekly_Sales'
].sum().reset_index()
```

#### 3. Weekly Breakdown
```python
weekly_sale = pd_2.groupby(['month','Month','Date']).agg({
    'Weekly_Sales':'sum'
}).reset_index()
# Add week number within each month
weekly_sale['week_no'] = weekly_sale.groupby(['Month'])[
    'Date'
].rank(method='min')
```

#### 4. Store-Level Aggregation
```python
store_df = pd_2.groupby(['month','Month','Store']).agg({
    'Weekly_Sales':'sum'
}).reset_index()
# Format store names: "Store 1", "Store 2", etc.
```

#### 5. Department-Level Aggregation
```python
dept_df = pd_2.groupby(['month','Month','Dept']).agg({
    'Weekly_Sales':'sum'
}).reset_index()
# Format department names: "Dept 1", "Dept 2", etc.
```

### Layout Structure

```
├── Navbar (Plotly logo + title)
├── Row 1: KPI Cards
│   ├── Month Selection Card (4 cols)
│   ├── Total Sales Card (auto)
│   ├── Holiday Sales Card (auto)
│   └── Total Stores Card (auto)
├── Row 2: Visualizations
│   ├── Weekly Sales Comparison (full width)
│   ├── Top Stores Comparison (2 charts side-by-side)
│   └── Department Sales Difference (full width)
```

### Callback Architecture

Single comprehensive callback managing all dashboard updates:

```python
@app.callback(
    [Output('card_num1', 'children'),  # Total Sales
     Output('card_num2', 'children'),  # Holiday Sales
     Output('card_num3', 'children'),  # Total Stores
     Output('card_num4', 'children'),  # Weekly chart
     Output('card_num5', 'children'),  # Store charts
     Output('card_num6', 'children')], # Dept chart
    [Input('dropdown_base', 'value'),   # Current period
     Input('dropdown_comp', 'value')]   # Reference period
)
def update_cards(base, comparison):
    # Calculates all metrics and returns updated components
```

**Inputs**:
- `dropdown_base`: Selected current month
- `dropdown_comp`: Selected reference month

**Outputs**: 6 card components with updated data and visualizations

### Visualization Details

#### Line Chart (Weekly Sales)
```python
go.Figure([
    go.Scatter(x=week_no, y=sales, line=dict(color='firebrick', width=4)),
    go.Scatter(x=week_no, y=sales, line=dict(color='#090059', width=4))
])
```

#### Horizontal Bar Charts (Stores)
```python
go.Figure([
    go.Bar(x=sales, y=stores, orientation='h',
           text=sales, textposition='outside',
           marker_color='indianred')
])
```

#### Department Difference Chart
```python
merged_df['diff'] = (merged_df['Weekly_Sales_base'] -
                     merged_df['Weekly_Sales_comp'])
go.Figure([
    go.Bar(x=diff, y=dept, orientation='h',
           marker_color='#4863A0')
])
```

## Requirements

```bash
pip install dash
pip install dash-bootstrap-components
pip install plotly
pip install pandas
pip install numpy
```

## Running the Application

```bash
python app.py
```

For development with auto-reload:
```bash
# Uncomment line 407 in app.py:
# app.run_server(debug=True)
```

Then navigate to: `http://127.0.0.1:8050/`

## Key Insights from Code

### Strengths
1. **Comprehensive metrics**: Multiple views (stores, departments, weekly trends)
2. **Comparative analysis**: Period-over-period comparison built-in
3. **Professional styling**: Clean, business-focused design
4. **Top performers**: Focus on top 10 stores/departments
5. **Responsive**: Bootstrap grid for different screen sizes
6. **Rich visualizations**: Multiple chart types for different insights

### Design Patterns
1. **Single callback pattern**: One callback updates all 6 outputs simultaneously
2. **Calculated differences**: Real-time delta calculations with +/- indicators
3. **Conditional formatting**: Different colors/styles based on positive/negative values
4. **Data preprocessing**: All aggregations done upfront for performance

### Potential Improvements
1. **Deprecated components**: Uses older import style (`dash_html_components`)
2. **Large callback**: Could be split into smaller, focused callbacks
3. **Data loading**: CSV loaded on startup (could add caching/lazy loading)
4. **Error handling**: No validation for missing data
5. **Date range**: Currently month-based, could expand to custom date ranges
6. **Export functionality**: Could add CSV/Excel export of filtered data

## Business Use Cases

### Retail Management
- Identify top-performing stores
- Compare seasonal trends
- Track holiday performance impact
- Monitor department contribution

### Strategic Planning
- Resource allocation based on store performance
- Inventory planning for top departments
- Staffing decisions for holiday periods
- Identify underperforming locations

### Financial Analysis
- Period-over-period revenue comparison
- Sales trend analysis
- Holiday sales impact quantification
- Department profitability insights

## Data Insights Available

1. **Temporal Patterns**: Weekly fluctuations within months
2. **Store Performance**: Sales distribution across locations
3. **Department Analysis**: Product category performance
4. **Holiday Impact**: Sales lift during holiday weeks
5. **Comparative Metrics**: Month-over-month changes

## Styling Customization

### Color Scheme
- Primary brand: `#090059` (dark blue)
- Current period: `firebrick` (red)
- Reference period: `#4863A0` (blue)
- Background: `#f7f7f7` (light gray)

### Card Heights
- KPI cards: 150px
- Visualization cards: 350px

### Chart Configuration
- White plot backgrounds
- Currency formatting: `$XM`
- Margins: `l=40, r=5, t=60, b=40`

## Learning Outcomes

This example demonstrates:
1. Complex data aggregation and preprocessing
2. Multi-level groupby operations in pandas
3. Period-over-period comparison patterns
4. Multiple synchronized visualizations
5. Horizontal bar chart best practices
6. Business dashboard layout design
7. KPI card implementation
8. Conditional rendering based on calculations
9. Professional styling with Bootstrap themes
10. Single callback managing multiple outputs

## Screenshot
A PNG reference is included: `sales_dashboard_app.png` showing the complete dashboard layout.
