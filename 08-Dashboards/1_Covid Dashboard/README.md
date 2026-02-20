# COVID-19 Live Tracker Dashboard

A real-time COVID-19 dashboard built with Dash and Plotly that visualizes global pandemic data.

## Overview

This dashboard provides an interactive visualization of COVID-19 statistics worldwide, featuring:
- Global statistics (confirmed cases, deaths, recoveries)
- Interactive world map with country-level data
- Searchable country-specific data table
- Real-time data from COVID-19 API

## Features

### 1. Global Statistics Cards
Three prominent cards displaying:
- **Confirmed Cases**: Total and new confirmed cases
- **Recovered Cases**: Total and new recoveries
- **Deaths**: Total and new deaths

Each card shows the current total with a "+N" indicator for new cases in the latest update.

### 2. Interactive World Map
- Choropleth map using orthographic projection (globe view)
- Color-coded by total confirmed cases (Plasma color scale)
- Hover tooltips showing:
  - Country name
  - Total confirmed cases
  - Total deaths
  - Total recovered

### 3. Country Data Table
- Filterable dropdown to select specific countries or view all
- Sortable columns
- Shows: Country, TotalConfirmed, TotalRecovered, TotalDeaths
- Styled with alternating row colors for readability
- Fixed header for scrolling large datasets

## Technical Implementation

### Data Source
- **API**: Novel COVID API / disease.sh (`https://disease.sh/v3/covid-19/`)
- Real-time data fetched on app initialization
- Global summary and country-level breakdown
- **Note**: Updated from the deprecated `api.covid19api.com` API

### Key Components

#### Layout Structure
```
├── Navbar
│   ├── COVID-19 logo
│   ├── App title
│   └── Support button
├── Global statistics row (3 cards)
├── Title: "Covid-19 Worldwide Impact"
└── Two-column row
    ├── World map (6 columns)
    └── Country dropdown + data table (6 columns)
```

#### Technology Stack
- **Dash**: Web application framework
- **Dash Bootstrap Components (dbc)**: FLATLY theme for styling
- **Plotly Express**: For choropleth map visualization
- **Pandas**: Data manipulation
- **Requests**: API calls

### Code Structure

#### Data Processing
1. Fetch global and country data from API
2. Extract global statistics (confirmed, deaths, recovered)
3. Map country codes (alpha-2 to ISO alpha-3) for map visualization
4. Create merged dataframe for mapping

#### Callback Function
```python
@app.callback(
    Output('world-table-output', 'children'),
    Input('country-dropdown', 'value')
)
def table_country(country):
    # Filters data based on dropdown selection
    # Returns formatted DataTable
```

**Input**: Country selection from dropdown
**Output**: Filtered/sorted data table

### Styling Features

#### Cards
- Color-coded: Primary (blue), Success (green), Danger (red)
- Centered text alignment
- Consistent padding and spacing
- Inverse colors for better contrast

#### Data Table
- Custom styling with:
  - Fixed header row
  - Alternating row colors (even/odd)
  - Centered text alignment
  - Ellipsis for text overflow
  - 4px white borders between cells
- Native sorting enabled
- Maximum height of 450px with scrolling

## Requirements

```bash
pip install dash
pip install dash-bootstrap-components
pip install plotly
pip install pandas
pip install requests
```

## Running the Application

```bash
python app.py
```

Then navigate to: `http://127.0.0.1:8050/`

## Key Insights from Code

### Strengths
1. **Real-time data**: Fetches live COVID-19 statistics
2. **Interactive visualizations**: Map and filterable table
3. **Responsive design**: Bootstrap grid system for mobile compatibility
4. **Professional styling**: Themed cards and well-formatted table
5. **User-friendly**: Dropdown for easy country selection

### Potential Improvements
1. **Deprecated components**: Uses older `dash_html_components` and `dash_core_components` (should use `dash.html` and `dash.dcc` in newer versions)
2. **Error handling**: No try-catch for API failures
3. **Data caching**: API called only once at startup (could add refresh button)
4. **Accessibility**: Could improve with ARIA labels
5. **Country code mapping**: Hardcoded mapping could be loaded from external file

### Notable Implementation Details

#### Country Code Mapping
The app includes a comprehensive mapping from alpha-2 (e.g., "US") to ISO alpha-3 (e.g., "USA") country codes, required for Plotly's choropleth maps.

#### Marquee Element
Uses HTML marquee (deprecated) for scrolling news: "USA, India and Brazil are top 3 countries..."

#### Card Data Function
The `data_for_cases()` function creates reusable card components with:
- Header
- Large number display (formatted with commas)
- Smaller "+N" indicator for new cases

## Use Cases

- **Educational**: Understanding pandemic spread patterns
- **Public Health**: Quick overview of global situation
- **Research**: Country-level comparison of COVID-19 impact
- **News/Media**: Visual representation for reports

## API Response Structure

### Global Endpoint (`/all`)
```python
response.json() = {
    'cases': int,
    'todayCases': int,
    'deaths': int,
    'todayDeaths': int,
    'recovered': int,
    'todayRecovered': int,
    'updated': timestamp,
    'active': int,
    'critical': int,
    ...
}
```

### Countries Endpoint (`/countries`)
```python
response.json() = [
    {
        'country': str,
        'countryInfo': {
            'iso2': str,
            'iso3': str,
            'lat': float,
            'long': float,
            'flag': str (url)
        },
        'cases': int,
        'todayCases': int,
        'deaths': int,
        'todayDeaths': int,
        'recovered': int,
        'todayRecovered': int,
        ...
    },
    ...
]
```

**API Documentation**: https://disease.sh/docs/

## Learning Outcomes

This example demonstrates:
1. API integration in Dash applications
2. Bootstrap theming and responsive layouts
3. Choropleth map creation with Plotly
4. DataTable component with custom styling
5. Callback functions for interactive filtering
6. Card-based dashboard layouts
7. Real-world data visualization patterns
