# Dash Examples

This folder contains simple examples demonstrating various Dash concepts and components.

## Layout Examples

### Basic Layout
- **d1_layout+html.py** - Layout using HTML components with GapMinder dataset (India vs US comparison)
  - Shows bar chart for GDP per capita
  - Shows line chart for life expectancy
  - Uses `dash_html_components` for layout

- **d2_layout+dbc.py** - Layout using Dash Bootstrap Components (DBC) with themes
  - Same visualizations as d1 but with Bootstrap grid system
  - Demonstrates responsive design (xs, sm, md, lg, xl)
  - Uses DARKLY theme from dash-bootstrap-components

## Component Examples

### Navigation & Structure
- **d3_dbc+navigation+bar.py** - Dash Bootstrap navigation bar component
- **d4_dbc+card.py** - Dash Bootstrap card component

### Core Components
- **d5_Dash+html+component+code.py** - HTML components reference
- **d6_dash+core+components+code.py** - Core components (dropdowns, sliders, etc.)
- **d7_dash+table+code.py** - DataTable component

## Callback Examples

### Basic Callbacks
- **d8_basic+callback.py** - Simple callback example with dropdown
  - Input: Dropdown selection (value)
  - Output: Text display
  - Demonstrates basic Input/Output decorator

- **d9_html+button+callback.py** - Callback triggered by HTML button

### Advanced Callbacks
- **d10_multiple+inputs+and+outputs.py** - Multiple inputs and outputs in callbacks
  - Demonstrates handling multiple input components
  - Shows how to return multiple outputs

- **d11_callback+with+State.py** - Callbacks with State
  - Uses `State` to access values without triggering callback
  - Useful for forms where you want to submit on button click

- **d12_chained+callback.py** - Chained callbacks
  - Output of one callback becomes input to another
  - Demonstrates callback dependencies

## Running the Examples

Each example is a standalone Dash application. To run any example:

```bash
python <example_name>.py
```

Then open your browser to `http://127.0.0.1:8050/`

## Requirements

```bash
pip install dash plotly dash-bootstrap-components
```

## Learning Path

Recommended order to study these examples:

1. **Layout basics**: d1 → d2 (understand HTML vs Bootstrap layouts)
2. **Components**: d3 → d4 → d5 → d6 → d7 (learn about UI components)
3. **Interactivity**: d8 → d9 → d10 → d11 → d12 (master callbacks)
