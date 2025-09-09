# Data Model: Financial Dashboard

**Version**: 1.0.0  
**Context**: AI-powered financial dashboard entities and relationships

## Core Entities

### Company
**Purpose**: Represents a publicly traded company with basic identification and classification

```python
@dataclass
class Company:
    ticker: str                    # Primary key, e.g., "AAPL"
    name: str                     # Full company name
    sector: str                   # GICS sector classification
    industry: str                 # GICS industry classification
    market_cap: float            # Current market capitalization
    currency: str                # Trading currency, e.g., "USD"
    exchange: str                # Stock exchange, e.g., "NASDAQ"
    created_at: datetime
    updated_at: datetime
```

**Validation Rules**:
- ticker: 1-5 uppercase alphanumeric characters
- name: Non-empty string, max 200 characters
- market_cap: Positive float
- currency: ISO 4217 currency code

### FinancialData
**Purpose**: Real-time and historical financial metrics for a company

```python
@dataclass
class FinancialData:
    ticker: str                   # Foreign key to Company
    timestamp: datetime           # Data point timestamp
    price: float                 # Current stock price
    volume: int                  # Trading volume
    market_cap: float           # Market capitalization
    
    # Valuation Ratios
    pe_ratio: float             # Price-to-Earnings ratio
    pb_ratio: float             # Price-to-Book ratio
    ev_ebitda: float           # Enterprise Value / EBITDA
    
    # Performance Metrics
    price_change_1d: float      # 1-day price change %
    price_change_1w: float      # 1-week price change %
    price_change_1m: float      # 1-month price change %
    price_change_1y: float      # 1-year price change %
    
    # Technical Indicators
    moving_avg_50d: float       # 50-day moving average
    moving_avg_200d: float      # 200-day moving average
    rsi_14d: float             # 14-day RSI
    
    data_source: str           # "yfinance" | "alpha_vantage"
    created_at: datetime
```

### ComparableCompanies
**Purpose**: Peer companies for relative valuation analysis

```python
@dataclass
class ComparableCompanies:
    ticker: str                  # Primary company ticker
    peer_ticker: str            # Comparable company ticker
    similarity_score: float     # 0.0-1.0 similarity metric
    comparison_basis: str       # "sector" | "industry" | "market_cap"
    created_at: datetime
```

**Relationships**:
- Many-to-many relationship between companies
- Self-referencing for peer analysis

### AnalystCoverage
**Purpose**: Professional analyst ratings and price targets

```python
@dataclass
class AnalystCoverage:
    ticker: str                  # Foreign key to Company
    analyst_firm: str           # Research firm name
    analyst_name: str           # Individual analyst
    rating: str                 # "BUY" | "HOLD" | "SELL"
    price_target: float        # Target price
    current_price: float       # Price when rating issued
    report_date: datetime      # Rating publication date
    report_summary: str        # Brief summary (max 500 chars)
    confidence_score: float    # Internal rating confidence
    created_at: datetime
```

### SentimentData
**Purpose**: Public sentiment from news and social media

```python
@dataclass
class SentimentData:
    ticker: str                  # Foreign key to Company
    source_type: str            # "news" | "social" | "analyst"
    sentiment_score: float      # -1.0 (negative) to 1.0 (positive)
    confidence: float           # 0.0-1.0 confidence in sentiment
    article_title: str          # News headline or post summary
    source_url: str             # Original content URL
    publish_date: datetime      # Content publication date
    keywords: List[str]         # Extracted keywords
    created_at: datetime
```

### UserSession
**Purpose**: Track user interactions and maintain session state

```python
@dataclass
class UserSession:
    session_id: str             # Primary key, UUID
    user_ip: str               # Anonymized user identifier
    search_history: List[str]   # Recently searched tickers
    chat_history: List[Dict]    # Conversation with AI assistant
    preferences: Dict           # Chart settings, display options
    last_active: datetime      # Last interaction timestamp
    created_at: datetime
```

**Session State Schema**:
```python
chat_history = [
    {
        "timestamp": "2025-09-09T15:30:00Z",
        "type": "user" | "assistant",
        "content": "message text",
        "context": {"ticker": "AAPL", "chart_type": "valuation"}
    }
]

preferences = {
    "default_chart_period": "1Y",
    "favorite_tickers": ["AAPL", "MSFT"],
    "theme": "dark" | "light"
}
```

### ChartConfiguration
**Purpose**: User-customizable chart settings and saved views

```python
@dataclass
class ChartConfiguration:
    config_id: str              # Primary key, UUID
    session_id: str             # Foreign key to UserSession
    chart_type: str             # "valuation" | "trading" | "sentiment"
    ticker: str                 # Target company
    time_period: str            # "1D" | "1W" | "1M" | "3M" | "1Y" | "5Y"
    selected_metrics: List[str] # Displayed metrics
    comparison_tickers: List[str] # Peer companies to include
    layout_settings: Dict       # Plotly layout configuration
    created_at: datetime
    updated_at: datetime
```

## Entity Relationships

### Primary Relationships
```
Company (1) ←→ (N) FinancialData
Company (N) ←→ (N) ComparableCompanies  
Company (1) ←→ (N) AnalystCoverage
Company (1) ←→ (N) SentimentData
UserSession (1) ←→ (N) ChartConfiguration
```

### Data Flow Dependencies
```
1. Company → FinancialData (price, ratios)
2. Company → ComparableCompanies (peer analysis)
3. FinancialData + ComparableCompanies → Chart Data
4. UserSession + ChartConfiguration → Personalized Dashboard
5. All Entities → AI Context for Chat Assistant
```

## Caching Strategy

### Cache TTL (Time-To-Live)
- **FinancialData**: 5 minutes during market hours, 1 hour after close
- **AnalystCoverage**: 24 hours (updated daily)
- **SentimentData**: 15 minutes (news updates frequently)
- **ComparableCompanies**: 7 days (peer relationships stable)
- **UserSession**: Session-based (expires on close)

### Cache Keys
```python
# Redis cache key patterns
financial_data_key = f"financial:{ticker}:{date}"
sentiment_key = f"sentiment:{ticker}:{hour}"
analyst_key = f"analysts:{ticker}:{date}"
comparables_key = f"peers:{ticker}"
```

## Data Validation

### Input Validation
- All ticker symbols: uppercase, alphanumeric, 1-5 characters
- Financial ratios: positive floats, NaN handling for N/A values
- Timestamps: UTC timezone, ISO 8601 format
- URLs: valid HTTP/HTTPS format
- Sentiment scores: bounded between -1.0 and 1.0

### Data Quality Checks
- Price data consistency (no impossible jumps)
- Volume validation (reasonable trading ranges)
- Analyst rating standardization
- Sentiment score normalization across sources 