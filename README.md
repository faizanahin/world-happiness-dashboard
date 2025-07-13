# 🌍 World Happiness Dashboard

A Streamlit web application for visualizing and exploring world happiness data, focusing on key indicators such as life satisfaction, GDP per capita, social support, and healthy life expectancy. This dashboard allows users to filter by region and country, view detailed statistics, and interact with insightful visualizations.

---

## Table of Contents
- [How to Run the Project](#how-to-run-the-project)
  - [Run Locally](#run-locally)
  - [Run in Google Colab](#run-in-google-colab)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Dependencies](#dependencies)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

---

## How to Run the Project

### Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/world-happiness-dashboard.git
   cd world-happiness-dashboard
   ```
2. **(Optional) Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
5. **Open your browser:**
   - Go to the local URL provided by Streamlit (usually http://localhost:8501)
6. **Explore the dashboard:**
   - Use the sidebar to filter by region and country, and interact with the visualizations.

### Run in Google Colab

1. **Open the `Happiness_Streamlit_Colab.ipynb` notebook in Google Colab.**
   - You can upload the notebook to your Google Drive and open it with Colab, or use the GitHub import feature in Colab.
2. **Follow the instructions in the notebook.**
   - The notebook contains code cells to generate the `app.py` file and instructions for running Streamlit in Colab.
3. **Run the notebook cells.**
   - The notebook will create the `app.py` file and may provide a link to launch the Streamlit app using a service like `ngrok` or `streamlit` magic commands (see notebook output for details).
4. **Interact with the dashboard.**
   - Once the Streamlit app is running, follow the provided link to access the dashboard in your browser.



## Features
- **Interactive Filtering:** Filter data by region and country using the sidebar.
- **Country Details:** View detailed statistics for the selected country.
- **Bar Chart:** Visualize key indicators (Life Ladder, GDP per capita, Social Support) for the selected country.
- **Bubble Chart:** Explore the relationship between GDP per capita and happiness, with bubble size representing healthy life expectancy.
- **Modern UI:** Clean, user-friendly interface powered by Streamlit and Plotly.

---

## Dataset

The dashboard uses a simulated subset of world happiness data with the following columns:

| Column                          | Description                                 |
|----------------------------------|---------------------------------------------|
| Country name                     | Name of the country                         |
| year                             | Year of the data                            |
| Life Ladder                      | Happiness score (subjective well-being)     |
| Log GDP per capita               | Logarithm of GDP per capita                 |
| Social support                   | Perceived social support (0-1 scale)        |
| Healthy life expectancy at birth | Life expectancy in years                    |
| Region                           | Geographical region                         |

**Sample Data:**
```
Country name,year,Life Ladder,Log GDP per capita,Social support,Healthy life expectancy at birth,Region
Finland,2021,7.8,10.7,0.96,72.0,Western Europe
Denmark,2021,7.6,10.6,0.95,71.8,Western Europe
... (see cleaned_happiness_data.csv)
```

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/world-happiness-dashboard.git
   cd world-happiness-dashboard
   ```
2. **(Optional) Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
2. **Open your browser:**
   - Go to the local URL provided by Streamlit (usually http://localhost:8501)
3. **Interact with the dashboard:**
   - Use the sidebar to filter by region and country
   - Explore the visualizations and data tables

---

## File Structure

```
world-happiness-dashboard/
├── app.py                      # Main Streamlit app
├── cleaned_happiness_data.csv  # Sample dataset
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── Happiness_Streamlit_Colab.ipynb # Jupyter/Colab notebook version
```

- **app.py:** Main dashboard code (uses a hardcoded sample dataset; you can modify it to load from CSV).
- **cleaned_happiness_data.csv:** Example data file (not used by default in app.py, but can be adapted).
- **requirements.txt:** List of required Python packages.
- **Happiness_Streamlit_Colab.ipynb:** Notebook for prototyping and exporting the app code.

---

## Dependencies

- streamlit
- pandas
- plotly
- matplotlib
- seaborn

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## Customization

- To use your own data, modify the data loading section in `app.py`:
  ```python
  # Replace the hardcoded data dictionary with:
  df = pd.read_csv('cleaned_happiness_data.csv')
  ```
- Ensure your CSV has the same columns as described above.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Push to your fork and submit a pull request

---

## License

This project is open source. See [LICENSE](LICENSE) for details (add a LICENSE file if needed).