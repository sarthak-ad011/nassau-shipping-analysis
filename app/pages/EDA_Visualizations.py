import streamlit as st
import os

st.title('📈 Exploratory Data Analysis')

reports_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'reports')

st.markdown("""
These visualizations were generated during the exploratory data analysis phase to understand
the underlying patterns in Nassau Candy's shipping data.
""")

# ---- Correlation Analysis ----
st.header('Correlation Matrix')
corr_path = os.path.join(reports_dir, 'eda_correlation.png')
if os.path.exists(corr_path):
    st.image(corr_path, use_container_width=True)
    st.caption('Correlation between numeric variables — identifies relationships between sales, units, profit, and lead time.')
else:
    st.warning('eda_correlation.png not found in reports/')

st.divider()

# ---- Lead Time Distribution ----
st.header('Lead Time Distribution')
lt_path = os.path.join(reports_dir, 'eda_lead_time.png')
if os.path.exists(lt_path):
    st.image(lt_path, use_container_width=True)
    st.caption('Distribution of shipping lead times across all orders.')
else:
    st.warning('eda_lead_time.png not found in reports/')

st.divider()

# ---- Time Series ----
st.header('Time Series Analysis')
ts_path = os.path.join(reports_dir, 'eda_timeseries.png')
if os.path.exists(ts_path):
    st.image(ts_path, use_container_width=True)
    st.caption('Order volume and lead time trends over time.')
else:
    st.warning('eda_timeseries.png not found in reports/')

st.divider()

# ---- Volume Analysis ----
st.header('Volume Analysis')
vol_path = os.path.join(reports_dir, 'eda_volume.png')
if os.path.exists(vol_path):
    st.image(vol_path, use_container_width=True)
    st.caption('Order volume breakdown by key dimensions.')
else:
    st.warning('eda_volume.png not found in reports/')
