# Executive Summary
## Factory-to-Customer Shipping Route Efficiency — Nassau Candy Distributor

### The Problem
Nassau Candy ships from 5 factories to customers in 50+ states with no route-level performance visibility.
Logistics decisions are reactive, not data-driven.

### What We Did
Analyzed 10,194 shipments to compute 7 KPIs per route, mapped geographic bottlenecks, and built a live dashboard.

### Top 3 Findings

**1. Sugar Shack → California averages 1,638 days vs. 1,182 days for the best route (Wicked Choccy's → Nevada) — a 39% slower delivery, highlighting the need for a Pacific-region hub.**

**2. Same Day class is used in only 5.4% of orders but shows no meaningful lead-time advantage over Standard Class (1,333 vs. 1,314 days), suggesting the ship mode field may not reflect actual shipping speed.**

**3. 2 critical bottleneck states (Tennessee, Washington) account for 6.8% of volume and 6.8% of all delays, with Washington alone handling 506 orders at an average lead time of 1,361 days.**

### Recommendations (ranked by impact)
1. **Open Pacific distribution hub** — Est. reduces lead time for Sugar Shack's Pacific shipments (currently 1,638 days for CA)
2. **Ship-mode policy for bottleneck states** — Upgrade orders to Tennessee and Washington to faster carriers
3. **Carrier audit on 5 worst-performing routes** — Wicked Choccy's → New Mexico (1,489 days), Lot's O' Nuts → Iowa (1,479 days), Secret Factory → Washington (1,472 days)
4. **Q4 inventory pre-positioning** in top 10 high-volume states

### Tools Built
- Live Streamlit dashboard with 4 modules + filters
- Reproducible analysis pipeline
- Route-level KPI database (200+ routes)
