# Dashboards with Plotly Dash

This folder contains Dash examples and applications demonstrating interactive data visualization and web application development with Python.

## Folder Structure

```
08-Dashboards/
├── examples/               # Simple examples for learning Dash basics
│   ├── d1-d7              # Layout and component examples
│   ├── d8-d12             # Callback examples
│   └── README.md          # Detailed guide for examples
├── 1_Covid Dashboard/     # COVID-19 live tracker application
│   ├── app.py
│   └── README.md
├── 2_Sales App/           # Retail sales analytics dashboard
│   ├── app.py
│   ├── retail_sales.csv
│   └── README.md
├── 3_NLP QA app/          # Question-answering NLP application
│   ├── NLP_app.py
│   └── README.md
└── README.md              # This file
```

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Environment Setup

#### Option 1: Virtual Environment (Recommended)

**Linux/Mac:**
```bash
# Navigate to project directory
cd /path/to/text-mining-dataviz-aa2526

# Create virtual environment
python3 -m venv venv_dashboards

# Activate virtual environment
source venv_dashboards/bin/activate

# Upgrade pip
pip install --upgrade pip
```

**Windows:**
```bash
# Navigate to project directory
cd C:\path\to\text-mining-dataviz-aa2526

# Create virtual environment
python -m venv venv_dashboards

# Activate virtual environment
venv_dashboards\Scripts\activate

# Upgrade pip
pip install --upgrade pip
```

#### Option 2: Conda Environment

```bash
# Create conda environment
conda create -n dash_env python=3.9

# Activate environment
conda activate dash_env

# Upgrade pip
pip install --upgrade pip
```

### Install Dependencies

#### For All Examples and Applications
```bash
pip install dash==2.14.0
pip install dash-bootstrap-components==1.5.0
pip install plotly==5.17.0
pip install pandas==2.1.0
pip install numpy==1.24.3
```

#### Additional for COVID Dashboard
```bash
pip install requests==2.31.0
```

#### Additional for NLP QA App
```bash
pip install transformers==4.35.0
pip install torch==2.1.0  # For CPU
# OR for GPU support (if available):
# pip install torch==2.1.0+cu118 -f https://download.pytorch.org/whl/torch_stable.html
```

#### Complete Installation (All Dependencies)
```bash
pip install dash==2.14.0 \
            dash-bootstrap-components==1.5.0 \
            plotly==5.17.0 \
            pandas==2.1.0 \
            numpy==1.24.3 \
            requests==2.31.0 \
            transformers==4.35.0 \
            torch==2.1.0
```

### Using Requirements File

Create a `requirements.txt` file:
```txt
dash==2.14.0
dash-bootstrap-components==1.5.0
plotly==5.17.0
pandas==2.1.0
numpy==1.24.3
requests==2.31.0
transformers==4.35.0
torch==2.1.0
```

Install all at once:
```bash
pip install -r requirements.txt
```

## Applications Overview

### 1. Examples Folder
**Purpose**: Learning Dash fundamentals

**Content**: 12 progressive examples covering:
- Layout design (HTML and Bootstrap)
- UI components (dropdowns, buttons, cards)
- Callbacks (basic, state-based, chained)

**Learning Path**: Start here if new to Dash

**Documentation**: [examples/README.md](examples/README.md)

**Run any example**:
```bash
cd 08-Dashboards/examples
python d1_layout+html.py
# Navigate to http://127.0.0.1:8050/
```

### 2. COVID-19 Dashboard
**Purpose**: Real-time pandemic data visualization

**Features**:
- Global statistics (confirmed, deaths, recoveries)
- Interactive world map
- Country-specific filtering
- Live API data

**Tech Stack**: Dash, Plotly, Pandas, Requests

**Documentation**: [1_Covid Dashboard/README.md](1_Covid%20Dashboard/README.md)

**Run**:
```bash
cd "08-Dashboards/1_Covid Dashboard"
python app.py
# Navigate to http://127.0.0.1:8050/
```

**Dependencies**:
```bash
pip install dash dash-bootstrap-components plotly pandas requests
```

### 3. Retail Sales Dashboard
**Purpose**: Business analytics and period comparison

**Features**:
- Period-over-period sales comparison
- Store performance analysis
- Department sales breakdown
- Weekly trends visualization
- Holiday sales tracking

**Tech Stack**: Dash, Plotly, Pandas, NumPy

**Dataset**: 14.6 MB retail sales CSV

**Documentation**: [2_Sales App/README.md](2_Sales%20App/README.md)

**Run**:
```bash
cd "08-Dashboards/2_Sales App"
python app.py
# Navigate to http://127.0.0.1:8050/
```

**Dependencies**:
```bash
pip install dash dash-bootstrap-components plotly pandas numpy
```

### 4. NLP Question Answering App
**Purpose**: Interactive question-answering with AI

**Features**:
- Text context input
- Natural language questions
- Real-time answer extraction
- Transformer model integration

**Tech Stack**: Dash, Transformers, PyTorch

**Model**: DistilBERT fine-tuned on SQuAD

**Documentation**: [3_NLP QA app/README.md](3_NLP%20QA%20app/README.md)

**Run**:
```bash
cd "08-Dashboards/3_NLP QA app"
python NLP_app.py
# Navigate to http://127.0.0.1:8050/
# First run will download ~250MB model
```

**Dependencies**:
```bash
pip install dash dash-bootstrap-components transformers torch
```

## Running Applications

### Standard Run
```bash
python app.py
```

### Development Mode (with auto-reload)
```bash
# Add to end of app.py:
if __name__ == "__main__":
    app.run_server(debug=True)
```

### Custom Port
```bash
# Add to end of app.py:
if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
```

### External Access (for deployment)
```bash
# Add to end of app.py:
if __name__ == "__main__":
    app.run_server(debug=False, host='0.0.0.0', port=8050)
```

## Troubleshooting

### Common Issues

#### 1. Port Already in Use
```bash
# Error: Address already in use
# Solution: Use different port
app.run_server(port=8051)
```

#### 2. Module Not Found
```bash
# Error: ModuleNotFoundError: No module named 'dash'
# Solution: Ensure virtual environment is activated and dependencies installed
source venv_dashboards/bin/activate  # Linux/Mac
pip install dash
```

#### 3. Deprecated Import Warnings
```python
# Old style (may show warnings):
import dash_html_components as html
import dash_core_components as dcc

# New style (recommended):
from dash import html, dcc
```

#### 4. Transformer Model Download Fails
```bash
# Error: Connection timeout or SSL error
# Solution: Manual download
export HF_ENDPOINT=https://hf-mirror.com  # Use mirror if needed
```

#### 5. Memory Issues with NLP App
```bash
# Error: CUDA out of memory or RAM full
# Solution: Use CPU-only inference
import torch
torch.set_num_threads(1)  # Limit threads if needed
```

## Performance Tips

### 1. Data Loading
- Preprocess data once at startup
- Use caching for expensive operations
- Consider lazy loading for large datasets

### 2. Callbacks
- Prevent unnecessary updates with `prevent_initial_call=True`
- Use `State` instead of `Input` when appropriate
- Minimize callback complexity

### 3. Visualizations
- Limit data points in plots (sampling if needed)
- Use `uirevision` to prevent unnecessary re-renders
- Optimize figure updates

## Deployment Options

### Local Development
- Use `debug=True` for development
- Access at `http://127.0.0.1:8050/`

### Production Deployment

#### Option 1: Heroku
```bash
# Create Procfile:
web: gunicorn app:server

# Install gunicorn:
pip install gunicorn

# Deploy:
heroku create your-app-name
git push heroku main
```

#### Option 2: Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

#### Option 3: Cloud Platforms
- AWS Elastic Beanstalk
- Google Cloud Run
- Azure App Service

## Learning Resources

### Official Documentation
- **Dash**: https://dash.plotly.com/
- **Plotly**: https://plotly.com/python/
- **Dash Bootstrap**: https://dash-bootstrap-components.opensource.faculty.ai/

### Tutorials
1. Start with [examples/README.md](examples/README.md)
2. Review individual app documentation
3. Experiment with modifications
4. Build your own dashboard

### Key Concepts to Master
1. **Layout**: Organizing components hierarchically
2. **Callbacks**: Making apps interactive
3. **State vs Input**: When to trigger vs. when to read
4. **Bootstrap Grid**: Responsive design with rows and columns
5. **Plotly Graphs**: Various chart types and customization

## Comparison of Applications

| Feature | Examples | COVID Dashboard | Sales Dashboard | NLP QA App |
|---------|----------|-----------------|-----------------|------------|
| **Complexity** | Basic | Medium | High | Medium |
| **Data Source** | Built-in | API | CSV | User Input |
| **Size** | ~1-2 KB | ~10 KB | ~14 KB | ~3 KB |
| **Dependencies** | 3 | 5 | 6 | 4 |
| **Learning Focus** | Fundamentals | API integration | Business analytics | ML integration |
| **Callbacks** | 0-1 | 1 | 1 (complex) | 1 |
| **Visualizations** | 2-3 | 2 (map + table) | 5 (charts) | 0 (text only) |
| **Best For** | Learning | Real-time data | KPI tracking | NLP demos |

## Project Structure Best Practices

### Organizing Your Dash App

```
my_dashboard/
├── app.py                 # Main application file
├── requirements.txt       # Dependencies
├── README.md             # Documentation
├── assets/               # CSS, images, fonts
│   └── style.css
├── data/                 # Data files
│   └── dataset.csv
├── components/           # Reusable components
│   ├── navbar.py
│   └── cards.py
└── callbacks/            # Callback functions
    └── data_callbacks.py
```

## Contributing

To add your own dashboard:
1. Create a new folder: `4_Your_Dashboard_Name/`
2. Include `app.py` and `README.md`
3. Document dependencies and setup
4. Update this main README

## License

See main project LICENSE file.

## Support

For issues or questions:
1. Check individual README files in subfolders
2. Review troubleshooting section above
3. Consult official Dash documentation
4. Check Python package versions compatibility

## Version Compatibility

Tested with:
- Python: 3.8, 3.9, 3.10, 3.11
- Dash: 2.14.0
- Plotly: 5.17.0
- Pandas: 2.1.0

## Next Steps

1. **Beginners**: Start with `examples/` folder
2. **Intermediate**: Modify existing applications
3. **Advanced**: Build custom dashboard combining concepts
4. **Production**: Deploy to cloud platform

Happy Dashboard Building! 🚀📊
