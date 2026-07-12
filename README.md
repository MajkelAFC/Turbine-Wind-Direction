# Wind Turbine Data Analytics Pipeline
# Turbine Wind Direction Analytics Pipeline

A production-ready data pipeline engineered in Python using **Domain-Driven Design (DDD)** principles and the **Medallion Architecture** (Bronze, Silver, and Gold layers). The system ingests, cleans, and processes high-frequency wind turbine data to compute the mathematically precise average wind direction using circular/vector analytics.

## 🚀 Architectural Overview

The project is structured according to **Domain-Driven Design (DDD)** to separate core business logic from technical infrastructure frameworks:

*   **Domain Layer (`src/domain/`)**: Pure business logic containing Domain Services (`WindAnalyticsService`) and Domain Models (`WindRecord`). It has zero external dependencies.
*   **Infrastructure Layer (`src/infrastructure/`)**: Technical implementations including database access layers (`PostgresWindTurbineRepository`) and ETL data loaders for each Medallion layer.

### 🥉🥈🥇 The Medallion Pipeline

1.  **Bronze Layer**: Ingests raw wind metrics straight from the input file and safely pipes them into the relational database raw table (`wind_data_bronze`).
2.  **Silver Layer**: Cleanses data by filtering out anomalies, noise, and system drops, persisting the refined metrics into `wind_data_silver`.
3.  **Gold Layer**: Fetches cleaned data, passes it through our domain circular vector math engine, and saves the final aggregate KPI along with a computation timestamp into `wind_data_gold`.

---

## 🧮 Mathematical Engine: Circular Mean

Standard arithmetic averaging fails for directional coordinates (e.g., the average of $350^\circ$ and $10^\circ$ should be $0^\circ$ or $360^\circ$, not $180^\circ$). 

To solve this, the **`WindAnalyticsService`** converts degrees into unit vectors on a Cartesian plane using sine and cosine, computes their component means, and maps the resulting vector back to a $0^\circ$ - $360^\circ$ angular space using the $atan2$ function:

$$x_{mean} = \frac{1}{n} \sum_{i=1}^{n} \cos(\theta_i)$$

$$y_{mean} = \frac{1}{n} \sum_{i=1}^{n} \sin(\theta_i)$$

$$\theta_{mean} = \text{atan2}(y_{mean}, x_{mean})$$

---

---

## 📈 Executive Summary & Engineering Insights

Based on the final analytical calculation from the **Gold Layer**, the precise circular mean wind direction for this specific geographic location is **$179.99^\circ$** (practically a perfect due South heading). 

To maximize the efficiency and energy yield of the wind farm infrastructure, engineers should apply the following data-driven optimizations:

### 1. Optimal Baseline Turbine Orientation (Yaw System Optimization)
*   **Target Heading**: **$179.99^\circ$** (South).
*   **Impact**: While modern wind turbines feature active yaw systems to automatically rotate the nacelle into the wind, setting the default baseline orientation to **$179.99^\circ$** minimizes the aggregate mechanical rotation required throughout the year. This directly reduces component wear on heavy łożyska (yaw bearings) and saves auxiliary energy consumption.

### 2. Wake Mitigation & Spatial Layout Design
*   **Array Layout Axis**: **$89.99^\circ \longleftrightarrow 269.99^\circ$** (East-West alignment).
*   **Impact**: Because the prevailing wind vector is strictly locked on a North-South axis ($179.99^\circ$), turbines must be positioned in rows stretching from East to West. This optimal spacing layout ensures that upstream turbines do not block or create aerodynamic turbulence (wake effect) for downstream units, maximizing the kinetic energy capture across the entire fleet.

## 🛠️ Project Structure

```text
wind_analytics/
├── src/
│   ├── domain/
│   │   ├── analytics.py       # Domain Service (Circular/Vector math logic)
│   │   ├── repository.py      # Abstract Domain Repository interfaces
│   │   └── wind_turbine.py    # Domain Entities and Value Objects
│   ├── infrastructure/
│   │   ├── csv_loader.py      # Ingests source CSV metrics
│   │   ├── database.py        # Database engine setup & raw connection management
│   │   ├── repository.py      # PostgreSQL Psycopg2 concrete repository implementation
│   │   ├── silver_loader.py   # Cleansing logic execution
│   │   └── gold_loader.py     # High-level analytical calculation supervisor
│   └── main.py                # Main orchestration entry point
├── .gitignore                 # Safe workspace filtering setup
└── README.md                  # System documentation

