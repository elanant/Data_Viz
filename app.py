import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Constants
CSV_FILE = "top50.csv"
CHART_TITLE = "Top 50 ARTISTS OF 2024"

# Load CSV file
@st.cache_data
def load_data():
    df = pd.read_csv(CSV_FILE)
    # Ensure proper data types
    df['SERIAL.NO'] = df['SERIAL.NO'].astype(str)
    return df

df = load_data()

# Set page config
st.set_page_config(
    page_title="Top 50 Artists Dashboard",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #155a8a;
    }
    .dataframe-container {
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<div class="main-header">🎵 Top 50 Artists Dashboard</div>', unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a section:", [
    "Data Overview",
    "DataFrame Attributes",
    "Records Management",
    "Columns Management",
    "Data Visualization"
])

# Data Overview Section
if page == "Data Overview":
    st.markdown('<div class="section-header">📊 Data Overview</div>', unsafe_allow_html=True)

    # Display basic info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Records", len(df))
    with col2:
        st.metric("Total Columns", len(df.columns))
    with col3:
        st.metric("Data Shape", f"{df.shape[0]} x {df.shape[1]}")

    # Display the entire DataFrame
    st.subheader("Complete Dataset")
    st.dataframe(df, width='stretch')

    # Data summary
    st.subheader("Data Summary")
    st.write(df.describe())

# DataFrame Attributes Section
elif page == "DataFrame Attributes":
    st.markdown('<div class="section-header">🔍 DataFrame Attributes</div>', unsafe_allow_html=True)

    attributes = st.selectbox("Select an attribute to display:", [
        "Transpose",
        "Column Names",
        "Index",
        "Shape",
        "Dimension",
        "Data Types",
        "Size",
        "Values",
        "Null Values",
        "Row Count",
        "Column Count",
        "Is Empty",
        "Axes",
        "Maximum Values",
        "Minimum Values",
        "Sum of Values"
    ])

    if attributes == "Transpose":
        st.write("DataFrame Transpose:")
        st.dataframe(df.T, width='stretch')
    elif attributes == "Column Names":
        st.write("Column Names:")
        st.write(list(df.columns))
    elif attributes == "Index":
        st.write("Index:")
        st.write(df.index.tolist())
    elif attributes == "Shape":
        st.write(f"Shape: {df.shape}")
    elif attributes == "Dimension":
        st.write(f"Dimension: {df.ndim}")
    elif attributes == "Data Types":
        st.write("Data Types:")
        st.write(df.dtypes)
    elif attributes == "Size":
        st.write(f"Size: {df.size}")
    elif attributes == "Values":
        st.write("Values:")
        st.dataframe(df.values, width='stretch')
    elif attributes == "Null Values":
        st.write("Null Values:")
        st.dataframe(df.isnull(), width='stretch')
    elif attributes == "Row Count":
        st.write("Row Count:")
        st.write(df.count())
    elif attributes == "Column Count":
        st.write("Column Count:")
        st.write(df.count(axis=1))
    elif attributes == "Is Empty":
        st.write(f"Is DataFrame Empty: {df.empty}")
    elif attributes == "Axes":
        st.write("Axes:")
        st.write(df.axes)
    elif attributes == "Maximum Values":
        st.write("Maximum Values:")
        st.write(df.max())
    elif attributes == "Minimum Values":
        st.write("Minimum Values:")
        st.write(df.min())
    elif attributes == "Sum of Values":
        st.write("Sum of Values:")
        st.write(df.sum())

# Records Management Section
elif page == "Records Management":
    st.markdown('<div class="section-header">📝 Records Management</div>', unsafe_allow_html=True)

    # Display records
    st.subheader("Display Records")
    display_option = st.selectbox("Select display option:", [
        "Top 5 Records",
        "Bottom 5 Records",
        "Custom Number from Top",
        "Custom Number from Bottom"
    ])

    if display_option == "Top 5 Records":
        st.dataframe(df.head(), width='stretch')
    elif display_option == "Bottom 5 Records":
        st.dataframe(df.tail(), width='stretch')
    elif display_option == "Custom Number from Top":
        n = st.number_input("Number of records from top:", min_value=1, max_value=len(df), value=5)
        st.dataframe(df.head(n), width='stretch')
    elif display_option == "Custom Number from Bottom":
        n = st.number_input("Number of records from bottom:", min_value=1, max_value=len(df), value=5)
        st.dataframe(df.tail(n), width='stretch')

    # Insert new record
    st.subheader("Insert New Record")
    with st.form("insert_record"):
        col1, col2 = st.columns(2)
        with col1:
            no = st.text_input("No.")
            track_name = st.text_input("Track Name")
            artist_name = st.text_input("Artist Name")
        with col2:
            genre = st.text_input("Genre")
            bpm = st.number_input("BPM", min_value=0)
            valence = st.number_input("Valence", min_value=0, max_value=100)
            acousticness = st.number_input("Acousticness", min_value=0, max_value=100)
            liveness = st.number_input("Liveness", min_value=0, max_value=100)
            popularity = st.number_input("Popularity", min_value=0, max_value=100)

        submitted = st.form_submit_button("Insert Record")
        if submitted:
            new_record = {
                df.columns[0]: no,
                df.columns[1]: track_name,
                df.columns[2]: artist_name,
                df.columns[3]: genre,
                df.columns[4]: bpm,
                df.columns[5]: valence,
                df.columns[6]: acousticness,
                df.columns[7]: liveness,
                df.columns[8]: popularity
            }
            df.loc[len(df)] = new_record
            st.success("Record inserted successfully!")
            st.rerun()

# Columns Management Section
elif page == "Columns Management":
    st.markdown('<div class="section-header">📋 Columns Management</div>', unsafe_allow_html=True)

    st.subheader("Current Columns")
    st.write(list(df.columns))

    # Insert new column
    st.subheader("Insert New Column")
    with st.form("insert_column"):
        col_name = st.text_input("Column Name")
        default_value = st.text_input("Default Value (leave empty for NaN)")
        submitted = st.form_submit_button("Insert Column")

        if submitted:
            if col_name in df.columns:
                st.error("Column already exists!")
            else:
                if default_value == "":
                    df[col_name] = np.nan
                else:
                    df[col_name] = default_value
                st.success(f"Column '{col_name}' inserted successfully!")
                st.rerun()

# Data Visualization Section
elif page == "Data Visualization":
    st.markdown('<div class="section-header">📈 Data Visualization</div>', unsafe_allow_html=True)

    chart_type = st.selectbox("Select Chart Type:", [
        "Line Chart",
        "Vertical Bar Chart",
        "Horizontal Bar Chart",
        "Histogram",
        "Scatter Plot"
    ])

    # Number of records selector
    if chart_type in ["Line Chart", "Vertical Bar Chart", "Horizontal Bar Chart"]:
        n_records = st.slider("Number of records from bottom:", 5, len(df), 10)
        df_subset = df.tail(n_records)
    else:
        n_records = st.slider("Number of records from top:", 5, len(df), 10)
        df_subset = df.head(n_records)

    # Column selector for charts
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    if chart_type == "Scatter Plot":
        x_col = st.selectbox("X-axis column:", numeric_columns, index=0 if len(numeric_columns) > 0 else None)
        y_col = st.selectbox("Y-axis column:", numeric_columns, index=1 if len(numeric_columns) > 1 else 0)
    else:
        y_col = st.selectbox("Y-axis column:", numeric_columns)

    if st.button("Generate Chart"):
        if chart_type == "Line Chart":
            fig = px.line(df_subset, y=y_col, title=f"{CHART_TITLE} - Line Chart")
        elif chart_type == "Vertical Bar Chart":
            fig = px.bar(df_subset, y=y_col, title=f"{CHART_TITLE} - Vertical Bar Chart")
        elif chart_type == "Horizontal Bar Chart":
            fig = px.bar(df_subset, x=y_col, orientation='h', title=f"{CHART_TITLE} - Horizontal Bar Chart")
        elif chart_type == "Histogram":
            fig = px.histogram(df_subset, x=y_col, title=f"{CHART_TITLE} - Histogram")
        elif chart_type == "Scatter Plot":
            fig = px.scatter(df_subset, x=x_col, y=y_col, title=f"{CHART_TITLE} - Scatter Plot")

        fig.update_layout(
            xaxis_title="Index" if chart_type != "Scatter Plot" else x_col,
            yaxis_title=y_col if chart_type != "Scatter Plot" else y_col,
            template="plotly_white"
        )
        st.plotly_chart(fig, width='stretch')

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Plotly")