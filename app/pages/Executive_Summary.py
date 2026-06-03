import streamlit as st
import os

st.title('📊 Executive Summary & Key Insights')

# ---------- Executive Summary ----------
st.header('Executive Summary')
st.markdown("""
**Factory-to-Customer Shipping Route Efficiency — Nassau Candy Distributor**
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.info("**10,194** shipments analyzed")
with col2:
    st.info("**200+** routes profiled")
with col3:
    st.info("**7** KPIs per route")

st.markdown("---")

st.subheader('The Problem')
st.markdown("""
Nassau Candy ships from **5 factories** to customers in **50+ states** with no route-level
performance visibility. Logistics decisions are reactive, not data-driven.
""")

st.subheader('Top 3 Findings')

st.error("""
**1. Sugar Shack → California** averages 1,638 days vs. 1,182 days for the best route
(Wicked Choccy's → Nevada) — a **39% slower delivery**, highlighting the need for a Pacific-region hub.
""")

st.warning("""
**2. Same Day class** is used in only 5.4% of orders but shows **no meaningful lead-time advantage**
over Standard Class (1,333 vs. 1,314 days), suggesting the ship mode field may not reflect actual
shipping speed.
""")

st.warning("""
**3. 2 critical bottleneck states** (Tennessee, Washington) account for 6.8% of volume and
6.8% of all delays, with Washington alone handling 506 orders at an average lead time of 1,361 days.
""")

st.markdown("---")

st.subheader('Recommendations (ranked by impact)')
st.markdown("""
| # | Recommendation | Detail |
|---|---|---|
| 1 | **Open Pacific distribution hub** | Reduces lead time for Sugar Shack's Pacific shipments (currently 1,638 days for CA) |
| 2 | **Ship-mode policy for bottleneck states** | Upgrade orders to Tennessee and Washington to faster carriers |
| 3 | **Carrier audit on 5 worst routes** | Wicked Choccy's → NM (1,489d), Lot's O' Nuts → IA (1,479d), Secret Factory → WA (1,472d) |
| 4 | **Q4 inventory pre-positioning** | Pre-position in top 10 high-volume states |
""")

st.markdown("---")

# ---------- Key Insights ----------
st.header('Key Insights')

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    '📦 Lead Time Patterns', '🛣️ Route Performance',
    '🗺️ Geographic Bottlenecks', '🚚 Ship Mode Tradeoffs',
    '💡 Recommendations'
])

with tab1:
    st.markdown("""
    - **Median lead time:** 1,274 days across 10,194 shipments
    - Same Day class averages **1,333 days**; Standard Class averages **1,314 days**
    - Lead times vary across regions: Atlantic = 1,323, Gulf = 1,311, Interior = 1,323, Pacific = 1,322
    """)

with tab2:
    st.markdown("**Most Efficient Routes:**")
    st.markdown("""
    | Rank | Route | Avg Lead Time |
    |------|-------|---------------|
    | 1 | Wicked Choccy's → Nevada | 1,182 days |
    | 2 | Secret Factory → Texas | 1,227 days |
    | 3 | Lot's O' Nuts → Virginia | 1,229 days |
    """)
    st.markdown("**Worst-Performing Routes:**")
    st.markdown("""
    | Rank | Route | Avg Lead Time |
    |------|-------|---------------|
    | 1 | Wicked Choccy's → New Mexico | 1,489 days |
    | 2 | Lot's O' Nuts → Iowa | 1,479 days |
    | 3 | Secret Factory → Washington | 1,472 days |
    """)
    st.markdown("""
    - Sugar Shack (Minnesota) has the longest reach into Pacific region with only 3 Pacific orders out of 33 total
    """)

with tab3:
    st.markdown("""
    **Critical bottleneck states:**
    - **Tennessee**: Avg LT 1,391 days, Volume 183
    - **Washington**: Avg LT 1,361 days, Volume 506

    **High-volume + slow states (top 5):** Washington, Tennessee, Indiana, Maryland, Connecticut
    """)

with tab4:
    st.markdown("""
    | Ship Mode | Avg Lead Time | Order Share |
    |-----------|--------------|-------------|
    | Same Day | 1,333 days | 5.4% (547) |
    | First Class | ~higher than Standard | ~15% |
    | Standard Class | 1,314 days | 60.0% (6,120) |

    Same Day and First Class show slightly **higher** lead times than Standard, suggesting ship mode
    has **minimal impact** on actual delivery speed in this dataset.
    """)

with tab5:
    st.markdown("""
    1. **Open Pacific-region distribution hub** — Reduce Sugar Shack → CA/OR/WA times (Sugar Shack → CA averages 1,638 days)
    2. **Audit Standard Class** for routes to New Mexico, Iowa, and Washington showing >10% above average lead time
    3. **Investigate Tennessee and Washington** — Why do they underperform despite high volume? (carrier issues? geographic distance?)
    4. **Pilot ship-mode upgrades** for high-margin / high-value orders to bottleneck states
    """)
