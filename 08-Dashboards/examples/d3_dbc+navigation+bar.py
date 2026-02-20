# -*- coding: utf-8 -*-
"""
Enhanced Navigation Bar Example

Demonstrates:
- Navigation links with callbacks
- Search bar functionality
- Dropdown menu
- Interactive button with counter
- Theme switching
- Responsive navbar that collapses on mobile
"""

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

# Navbar with multiple features
navbar = dbc.Navbar(
    dbc.Container([
        # Left side: Logo and brand
        dbc.Row([
            dbc.Col(html.Img(src=PLOTLY_LOGO, height="40px"), width="auto"),
            dbc.Col(dbc.NavbarBrand("Dashboard App", className="ms-2"), width="auto"),
        ], align="center", className="g-0"),

        # Mobile toggle button
        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),

        # Collapsible content
        dbc.Collapse(
            dbc.Row([
                # Navigation links
                dbc.Nav([
                    dbc.NavItem(dbc.NavLink("Home", id="nav-home", href="#", active=True)),
                    dbc.NavItem(dbc.NavLink("Dashboard", id="nav-dashboard", href="#")),
                    dbc.NavItem(dbc.NavLink("Reports", id="nav-reports", href="#")),

                    # Dropdown menu
                    dbc.DropdownMenu(
                        children=[
                            dbc.DropdownMenuItem("Settings", id="dropdown-settings"),
                            dbc.DropdownMenuItem("Profile", id="dropdown-profile"),
                            dbc.DropdownMenuItem(divider=True),
                            dbc.DropdownMenuItem("Logout", id="dropdown-logout"),
                        ],
                        nav=True,
                        in_navbar=True,
                        label="More",
                    ),
                ], navbar=True, className="me-auto"),

                # Right side: Search and button
                dbc.Col([
                    dbc.Input(
                        id="search-input",
                        type="search",
                        placeholder="Search...",
                        className="me-2",
                        style={"width": "200px"}
                    ),
                ], width="auto"),

                dbc.Col([
                    dbc.Button(
                        "Click Me!",
                        id="action-button",
                        color="primary",
                        className="me-2"
                    ),
                ], width="auto"),

            ], align="center", className="g-2 ms-auto flex-nowrap"),
            id="navbar-collapse",
            is_open=False,
            navbar=True,
        ),
    ], fluid=True),
    color="dark",
    dark=True,
    className="mb-4",
)

# Page content area
content = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Welcome to the Dashboard", id="page-title"),
            html.Hr(),
            html.Div(id="page-content", children=[
                html.P("Click on the navigation links above to see different content."),
                html.P("Try the search bar and the action button!"),
            ]),
        ]),
    ]),

    # Stats cards to show interactivity
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Button Clicks", className="card-title"),
                    html.H2(id="click-counter", children="0", className="text-primary"),
                ]),
            ], className="text-center"),
        ], width=4),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Active Page", className="card-title"),
                    html.H2(id="active-page", children="Home", className="text-success"),
                ]),
            ], className="text-center"),
        ], width=4),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Search Term", className="card-title"),
                    html.H2(id="search-display", children="-", className="text-info"),
                ]),
            ], className="text-center"),
        ], width=4),
    ], className="mt-4"),

    # Alert for dropdown actions
    html.Div(id="alert-container", className="mt-4"),
], fluid=True)

app.layout = html.Div([navbar, content])


# Callback for mobile navbar toggle
@app.callback(
    Output("navbar-collapse", "is_open"),
    Input("navbar-toggler", "n_clicks"),
    State("navbar-collapse", "is_open"),
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# Callback for navigation and page content
@app.callback(
    [Output("page-title", "children"),
     Output("page-content", "children"),
     Output("active-page", "children"),
     Output("nav-home", "active"),
     Output("nav-dashboard", "active"),
     Output("nav-reports", "active")],
    [Input("nav-home", "n_clicks"),
     Input("nav-dashboard", "n_clicks"),
     Input("nav-reports", "n_clicks")],
    prevent_initial_call=True
)
def update_page_content(home_clicks, dashboard_clicks, reports_clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = "nav-home"
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    # Set active states
    active_home = button_id == "nav-home"
    active_dashboard = button_id == "nav-dashboard"
    active_reports = button_id == "nav-reports"

    # Content for each page
    if button_id == "nav-home":
        title = "Welcome to the Dashboard"
        content = [
            html.P("This is the home page of your dashboard application."),
            html.P("Navigate using the links above to explore different sections."),
            html.Ul([
                html.Li("Interactive navigation bar with mobile support"),
                html.Li("Search functionality"),
                html.Li("Dropdown menus"),
                html.Li("Click counter demonstration"),
            ]),
        ]
        page_name = "Home"
    elif button_id == "nav-dashboard":
        title = "Dashboard View"
        content = [
            html.P("This is where your main dashboard visualizations would go."),
            dbc.Row([
                dbc.Col([dbc.Card(dbc.CardBody("Chart 1"), color="light")], width=6),
                dbc.Col([dbc.Card(dbc.CardBody("Chart 2"), color="light")], width=6),
            ], className="mt-3"),
            dbc.Row([
                dbc.Col([dbc.Card(dbc.CardBody("Chart 3"), color="light")], width=6),
                dbc.Col([dbc.Card(dbc.CardBody("Chart 4"), color="light")], width=6),
            ], className="mt-3"),
        ]
        page_name = "Dashboard"
    else:  # reports
        title = "Reports"
        content = [
            html.P("Generate and view reports here."),
            dbc.Table([
                html.Thead(html.Tr([html.Th("Report"), html.Th("Date"), html.Th("Status")])),
                html.Tbody([
                    html.Tr([html.Td("Monthly Report"), html.Td("2026-02-01"), html.Td("Complete")]),
                    html.Tr([html.Td("Quarterly Report"), html.Td("2026-01-01"), html.Td("Complete")]),
                    html.Tr([html.Td("Annual Report"), html.Td("2026-01-01"), html.Td("In Progress")]),
                ]),
            ], bordered=True, hover=True, className="mt-3"),
        ]
        page_name = "Reports"

    return title, content, page_name, active_home, active_dashboard, active_reports


# Callback for button clicks
@app.callback(
    Output("click-counter", "children"),
    Input("action-button", "n_clicks"),
    prevent_initial_call=True
)
def count_clicks(n_clicks):
    return str(n_clicks or 0)


# Callback for search
@app.callback(
    Output("search-display", "children"),
    Input("search-input", "value")
)
def update_search(value):
    return value if value else "-"


# Callback for dropdown menu actions
@app.callback(
    Output("alert-container", "children"),
    [Input("dropdown-settings", "n_clicks"),
     Input("dropdown-profile", "n_clicks"),
     Input("dropdown-logout", "n_clicks")],
    prevent_initial_call=True
)
def dropdown_action(settings, profile, logout):
    ctx = dash.callback_context
    if not ctx.triggered:
        return None

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    messages = {
        "dropdown-settings": ("Settings clicked!", "info"),
        "dropdown-profile": ("Profile clicked!", "success"),
        "dropdown-logout": ("Logout clicked!", "warning"),
    }

    msg, color = messages.get(button_id, ("Action clicked!", "info"))

    return dbc.Alert(msg, color=color, dismissable=True, duration=3000)


if __name__ == "__main__":
    app.run(debug=True)



