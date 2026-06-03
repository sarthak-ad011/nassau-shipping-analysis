import streamlit as st

st.title('📄 Research Paper')
st.caption('Factory-to-Customer Shipping Route Efficiency — Nassau Candy Distributor')

st.markdown("---")

st.header('1. Introduction')
st.markdown("""
**Background:** Nassau Candy Distributor operates as a national distributor across 5 factories,
shipping to customers in 50+ US states.

**Problem:** Despite rich order/shipment data, logistics decisions are made without route-level
efficiency intelligence. There is no systematic way to identify which routes are fast, which are
slow, and where geographic bottlenecks exist.

**Objectives:**
- Identify consistently efficient routes
- Detect routes with frequent delays
- Map geographic bottlenecks
- Compare ship mode performance
""")

st.header('2. Data & Methodology')
st.markdown("""
**Dataset:** 10,194 shipment records, 18 fields covering orders, shipping, and financials.

**Methodology:**
1. **Data cleaning** — Validated dates, removed invalid lead times
2. **Feature engineering** — Lead time calculation, route IDs, factory mapping, profit margin
3. **KPI computation** — 7 route-level metrics (avg lead time, median, std dev, volume, delay %, efficiency score, sales)
4. **Geographic analysis** — State-level aggregation with bottleneck flagging using volume and lead-time thresholds
""")

st.header('3. Exploratory Findings')
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    - **Lead time distribution:** Median 1,274 days, right-skewed
    - **Volume by region:** Atlantic and Interior dominate order volume
    """)
with col2:
    st.markdown("""
    - **Time trend:** No significant seasonal pattern detected
    - **Factory reach:** Sugar Shack has the longest geographic reach
    """)

st.header('4. KPI Results')
st.markdown("""
**Top 10 Most Efficient Routes** — lowest average lead time with ≥10 orders:

| Route | Avg LT | Volume | Efficiency Score |
|-------|--------|--------|-----------------|
| Wicked Choccy's → Nevada | 1,182 d | 53 | 100.0 |
| Secret Factory → Texas | 1,227 d | 503 | 91.4 |
| Lot's O' Nuts → Virginia | 1,229 d | 147 | 90.7 |

**Bottom 10 Least Efficient Routes** — highest average lead time:

| Route | Avg LT | Volume | Delay % |
|-------|--------|--------|---------|
| Wicked Choccy's → New Mexico | 1,489 d | 47 | High |
| Lot's O' Nuts → Iowa | 1,479 d | 49 | High |
| Secret Factory → Washington | 1,472 d | 136 | High |
""")

st.header('5. Geographic Bottlenecks')
st.markdown("""
**Critical bottleneck states** (high volume + high lead time):
- **Tennessee** — Avg LT: 1,391 days, Volume: 183 orders
- **Washington** — Avg LT: 1,361 days, Volume: 506 orders

**Pacific region** is underserved:
- Sugar Shack → California averages 1,638 days
- Only 3 Pacific orders out of Sugar Shack's 33 total

**Top 5 high-volume + slow states:** Washington, Tennessee, Indiana, Maryland, Connecticut
""")

st.header('6. Ship Mode Tradeoffs')
st.markdown("""
| Ship Mode | Avg Lead Time | Share of Orders | Observation |
|-----------|--------------|-----------------|-------------|
| Same Day | 1,333 days | 5.4% | No speed advantage |
| First Class | ~1,330 days | ~15% | Marginal difference |
| Second Class | ~1,310 days | ~20% | Comparable to Standard |
| Standard Class | 1,314 days | 60.0% | Dominant and competitive |

**Key finding:** Ship mode labels do not correspond to meaningful differences in actual delivery speed.
This suggests the field may represent customer selection or pricing tier rather than carrier service level.
""")

st.header('7. Recommendations')
st.markdown("""
1. **Distribution hub** — Open Pacific hub to reduce Sugar Shack's reach (est. 30-40% lead time reduction for CA/OR/WA)
2. **Ship-mode policy** — Upgrade orders >$X to faster mode for bottleneck states (TN, WA)
3. **Carrier audit** — Investigate states with >2× avg lead time across all factories
4. **Capacity planning** — Pre-position inventory in Q4 for top 10 high-volume states
""")

st.header('8. Conclusion')
st.markdown("""
This analysis transforms raw order and shipment data into **route-level operational intelligence**,
giving Nassau Candy Distributor data-driven leverage to improve logistics performance,
reduce delays, and enhance nationwide delivery reliability.

The live Streamlit dashboard with 7 modules and interactive filters enables continuous monitoring
and decision-making across the organization.
""")

with st.expander('📎 Appendix'):
    st.markdown("""
    - **Dataset schema:** 28 fields after feature engineering
    - **Factory coordinates:** 5 factories mapped with lat/long
    - **KPI database:** 200+ routes with 7 metrics each
    - **Visualization library:** 8 interactive Plotly charts + 4 EDA static plots
    """)
