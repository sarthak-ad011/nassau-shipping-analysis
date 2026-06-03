import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

st.set_page_config(
    page_title='Nassau Candy — Shipping Analytics',
    page_icon='🍬',
    layout='wide',
    initial_sidebar_state='expanded'
)

# ---------- Data loading (cached) ----------
@st.cache_data
def load_data():
    base = os.path.join(os.path.dirname(__file__), '..', 'data', 'Processed')
    df = pd.read_csv(os.path.join(base, 'cleaned_data.csv'))
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    route_kpis = pd.read_csv(os.path.join(base, 'route_state_kpis.csv'))
    state_perf = pd.read_csv(os.path.join(base, 'state_performance.csv'))
    return df, route_kpis, state_perf

df, route_kpis, state_perf = load_data()

# ---------- Sidebar Filters ----------
st.sidebar.header('🎯 Filters')

# Date range
min_date, max_date = df['Order Date'].min(), df['Order Date'].max()
date_range = st.sidebar.date_input(
    'Date range',
    value=(min_date.date(), max_date.date()),
    min_value=min_date.date(),
    max_value=max_date.date()
)

# Region
all_regions = sorted(df['Region'].unique())
selected_regions = st.sidebar.multiselect('Region', all_regions, default=all_regions)

# Ship Mode
all_modes = sorted(df['Ship Mode'].unique())
selected_modes = st.sidebar.multiselect('Ship Mode', all_modes, default=all_modes)
# Lead-time threshold for delay
delay_threshold = st.sidebar.slider('Delay threshold (days)', 1, 30, 7)

# Apply filters
def filter_df(df):
    mask = (
        (df['Order Date'] >= pd.Timestamp(date_range[0])) &
        (df['Order Date'] <= pd.Timestamp(date_range[1])) &
        (df['Region'].isin(selected_regions)) &
        (df['Ship Mode'].isin(selected_modes))
    )
    return df[mask]

filtered = filter_df(df)

# ---------- Make filtered data available across pages ----------
st.session_state['filtered_df'] = filtered
st.session_state['delay_threshold'] = delay_threshold
st.session_state['route_kpis'] = route_kpis
st.session_state['state_perf'] = state_perf

# ---------- Hide default Streamlit footer branding ----------
st.markdown("""
<style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    /* Capitalize sidebar navigation labels (e.g. "streamlit app" → "Streamlit App") */
    [data-testid="stSidebarNav"] span {text-transform: capitalize;}
</style>
""", unsafe_allow_html=True)

# ---------- Home Page ----------
st.title('🍬 Nassau Candy Distributor — Shipping Analytics')
st.markdown('Factory-to-customer shipping route efficiency dashboard — Powered by **Streamlit**')

# ---- Row 1: Primary KPIs ----
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    st.metric('Total Orders', f"{len(filtered):,}")
with col2:
    st.metric('Avg Lead Time', f"{filtered['Shipping Lead Time'].mean():.1f} days")
with col3:
    delay_rate = (filtered['Shipping Lead Time'] > delay_threshold).mean() * 100
    st.metric('Delay Rate', f"{delay_rate:.1f}%")
with col4:
    st.metric('Total Sales', f"${filtered['Sales'].sum():,.0f}")
with col5:
    st.metric('Units Shipped', f"{filtered['Units'].sum():,}")
with col6:
    st.metric('Gross Profit', f"${filtered['Gross Profit'].sum():,.0f}")

st.divider()

# ---- Row 2: Quick charts ----
col_left, col_right = st.columns(2)

with col_left:
    st.subheader('Monthly Lead Time Trend')
    monthly = (
        filtered.groupby(pd.Grouper(key='Order Date', freq='ME'))['Shipping Lead Time']
        .mean().reset_index()
    )
    fig_trend = px.area(
        monthly, x='Order Date', y='Shipping Lead Time',
        labels={'Shipping Lead Time': 'Avg Lead Time (days)'}
    )
    fig_trend.update_layout(height=300, margin=dict(l=0, r=0, t=10, b=0))
    fig_trend.update_traces(line_color='#1f77b4', fillcolor='rgba(31,119,180,0.15)')
    st.plotly_chart(fig_trend, use_container_width=True)

with col_right:
    st.subheader('Orders by Ship Mode')
    mode_counts = filtered['Ship Mode'].value_counts().reset_index()
    mode_counts.columns = ['Ship Mode', 'Count']
    fig_mode = px.pie(
        mode_counts, names='Ship Mode', values='Count',
        hole=0.4, color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig_mode.update_layout(height=300, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig_mode, use_container_width=True)

st.divider()

# ---- Row 3: Region & Factory breakdown ----
col_a, col_b = st.columns(2)

with col_a:
    st.subheader('Orders by Region')
    region_data = filtered.groupby('Region').agg(
        Orders=('Order ID', 'count'),
        Avg_LT=('Shipping Lead Time', 'mean'),
        Sales=('Sales', 'sum')
    ).reset_index().round(2)
    fig_region = px.bar(
        region_data, x='Region', y='Orders', color='Avg_LT',
        color_continuous_scale='RdYlGn_r',
        labels={'Avg_LT': 'Avg LT (days)'}
    )
    fig_region.update_layout(height=300, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig_region, use_container_width=True)

with col_b:
    st.subheader('Factory Performance')
    factory_data = filtered.groupby('Factory').agg(
        Orders=('Order ID', 'count'),
        Avg_LT=('Shipping Lead Time', 'mean'),
        Sales=('Sales', 'sum')
    ).reset_index().round(2).sort_values('Avg_LT')
    fig_factory = px.bar(
        factory_data, x='Factory', y='Orders', color='Avg_LT',
        color_continuous_scale='RdYlGn_r',
        labels={'Avg_LT': 'Avg LT (days)'},
        text='Avg_LT'
    )
    fig_factory.update_traces(texttemplate='%{text:.0f}d', textposition='outside')
    fig_factory.update_layout(height=300, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig_factory, use_container_width=True)

st.divider()

# ---- Row 4: Top & Bottom routes quick view ----
st.subheader('Quick Route Snapshot')
col_top, col_bot = st.columns(2)

from kpi_calculator import compute_route_kpis
route_kpis_filt = compute_route_kpis(filtered, 'Route_State', delay_threshold)
qualified = route_kpis_filt[route_kpis_filt['Route_Volume'] >= 10]

with col_top:
    st.markdown('**Top 5 Fastest Routes**')
    top5 = qualified.nsmallest(5, 'Avg_Lead_Time')[['Route_State', 'Avg_Lead_Time', 'Route_Volume', 'Route_Efficiency_Score']]
    st.dataframe(top5, use_container_width=True, hide_index=True)

with col_bot:
    st.markdown('**Bottom 5 Slowest Routes**')
    bot5 = qualified.nlargest(5, 'Avg_Lead_Time')[['Route_State', 'Avg_Lead_Time', 'Route_Volume', 'Delay_Frequency_%']]
    st.dataframe(bot5, use_container_width=True, hide_index=True)

st.divider()

# ---- Navigation ----
st.markdown("""
### 📍 Navigation
Use the left sidebar to navigate between pages:
- **Executive Summary** — Key findings, recommendations, and insights
- **Route Overview** — Top/bottom routes, leaderboards, factory performance
- **Geographic Map** — US heatmap, route network, bottleneck detection
- **Ship Mode Comparison** — Performance across shipping classes
- **Route Drill-Down** — Detailed state-level analysis with product breakdown
- **EDA Visualizations** — Exploratory data analysis charts
- **Research Paper** — Full research paper and methodology
""")

# ---- Recent orders ----
st.subheader('📋 Recent Orders (Filtered)')
st.dataframe(
    filtered.sort_values('Order Date', ascending=False).head(20)[
        ['Order Date', 'Order ID', 'Region', 'State/Province', 'Ship Mode',
         'Factory', 'Product Name', 'Shipping Lead Time', 'Sales']
    ],
    use_container_width=True
)
