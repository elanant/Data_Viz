# Top 50 Artists Dashboard

A modern, interactive web dashboard for analyzing the Top 50 Artists dataset from 2024. Built with Streamlit and Plotly for a better user experience compared to the original CLI application.

## Features

### 🎵 Data Overview
- Complete dataset display with interactive dataframes
- Summary statistics and metrics
- Data exploration capabilities

### 🔍 DataFrame Attributes
- Transpose, column names, index information
- Shape, dimensions, data types
- Size, values, null values analysis
- Row/column counts, axes information
- Maximum, minimum, and sum calculations

### 📝 Records Management
- Display top/bottom N records
- Add new records with form validation
- Custom record range selection

### 📋 Columns Management
- View existing columns
- Add new columns with default values

### 📈 Data Visualization
- Interactive line charts
- Vertical and horizontal bar charts
- Histograms
- Scatter plots with customizable axes

## Technology Stack

- **Frontend**: Streamlit
- **Visualization**: Plotly
- **Data Processing**: Pandas, NumPy
- **Containerization**: Docker, Docker Compose

## Installation & Running

### Option 1: Docker (Recommended)

1. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

2. **Or build and run manually:**
   ```bash
   docker build -t top50-dashboard .
   docker run -p 8501:8501 top50-dashboard
   ```

3. Access the application at `http://localhost:8501`

### Option 2: Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Project Structure

```
.
├── app.py                 # Main Streamlit application
├── top50.csv             # Dataset file
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker container configuration
├── docker-compose.yml   # Docker Compose configuration
├── .dockerignore        # Docker ignore file
└── README.md           # This file
```

## Docker Configuration

The application is containerized using Docker for easy deployment:

- **Base Image**: Python 3.11 slim
- **Port**: 8501
- **Health Check**: Built-in Streamlit health endpoint
- **Volume Mount**: CSV file can be mounted for live updates

## Data Format

The application expects a CSV file with the following columns:
- SERIAL.NO (string)
- TRACK NAME (string)
- ARTIST NAME (string)
- GENRE (string)
- BPM (integer)
- VALENCE (integer)
- ACOUSTICNESS (integer)
- LIVENESS (integer)
- POPULARITY (integer)

## Development

To modify the application:

1. Edit `app.py` for UI/UX changes
2. Update `requirements.txt` for new dependencies
3. Modify `Dockerfile` for container changes
4. Rebuild with `docker-compose up --build`

## Migration from CLI

This web application replaces the original CLI-based tool (`program001.py`) with:
- Better user interface and navigation
- Interactive visualizations
- Form-based data entry
- Real-time updates
- Cross-platform compatibility via Docker

## License

This project is open source and available under the MIT License.