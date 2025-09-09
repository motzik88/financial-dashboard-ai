# 📊 Financial Dashboard - AI-Powered Investment Analysis

An interactive financial analysis platform with AI-powered chat assistant, real-time market data, and advanced charting capabilities.

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Internet connection (for data fetching)

### Installation & Run

**Option 1: One-Command Setup**
```bash
# Make sure you're in the project root directory
cd /path/to/elad-test

# Run the frontend (installs dependencies automatically)
./run_frontend.py
```

**Option 2: Manual Setup**
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Access the Dashboard
Once running, open your browser to: **http://localhost:8501**

## 🎯 Features

### 🔍 Company Search & Analysis
- **Smart Search**: Search by ticker symbol (AAPL) or company name (Apple)
- **Autocomplete**: Intelligent suggestions as you type
- **Popular Stocks**: Quick access to major companies

### 📊 Interactive Charts & Visualizations
- **Real-time Data**: Live stock prices and market data
- **Multiple Views**: Valuation, Trading, Sentiment analysis
- **Interactive Charts**: Zoom, pan, hover for detailed information
- **Peer Comparison**: Compare with industry competitors

### 🤖 AI-Powered Chat Assistant
- **Intelligent Responses**: Contextual financial analysis
- **Company-Specific Questions**: Ask about any aspect of the company
- **Quick Questions**: Pre-built question templates
- **Conversation Memory**: Maintains context throughout the chat

### 💰 Financial Metrics
- **Key Ratios**: P/E, P/B, EV/EBITDA
- **Performance**: Price changes, volume analysis
- **Market Data**: Real-time quotes and market status
- **Analyst Coverage**: Ratings and price targets

## 🏗️ Architecture

```
financial-dashboard/
├── frontend/                 # Streamlit Frontend
│   ├── app.py               # Main application
│   ├── src/
│   │   ├── components/      # UI Components
│   │   │   ├── search_widget.py
│   │   │   ├── chart_display.py
│   │   │   ├── chat_interface.py
│   │   │   └── dashboard_layout.py
│   │   ├── services/        # Business Logic
│   │   │   ├── api_client.py
│   │   │   └── session_manager.py
│   │   └── pages/          # Page Components
│   └── requirements.txt     # Python dependencies
├── backend/                 # FastAPI Backend (Future)
├── docs/                   # Documentation
└── specs/                  # Feature Specifications
```

## 🎮 How to Use

### 1. Company Search
- Use the search box in the sidebar
- Type a ticker symbol (e.g., "AAPL") or company name
- Select from autocomplete suggestions
- Or click popular stock buttons

### 2. Explore Charts
- View **Overview** metrics at the top
- Switch between **Valuation**, **Trading**, and **Sentiment** tabs
- Use interactive chart features (zoom, hover)
- Compare with peer companies

### 3. AI Chat Assistant
- Ask questions about the selected company
- Try quick question buttons for inspiration
- Get contextual analysis and insights
- Export conversation if needed

### 4. Customize Settings
- Adjust chart preferences (theme, period, indicators)
- Configure AI assistant behavior
- Manage user preferences and notifications

## 📊 Sample Companies Available

The dashboard includes mock data for these popular companies:
- **AAPL** - Apple Inc.
- **GOOGL** - Alphabet Inc.
- **MSFT** - Microsoft Corporation
- **TSLA** - Tesla, Inc.
- **NVDA** - NVIDIA Corporation
- And 15+ more major companies

## 🔧 Development

### Adding New Features
1. Create components in `frontend/src/components/`
2. Add business logic to `frontend/src/services/`
3. Update main app in `frontend/app.py`
4. Follow the established patterns

### Code Quality
- Black for code formatting
- Flake8 for linting
- pytest for testing
- Pre-commit hooks for quality checks

## 🚧 Current Status

- ✅ **Frontend**: Complete with all major features
- ✅ **Mock Data**: Comprehensive financial data simulation
- ✅ **Interactive UI**: Full Streamlit dashboard
- ✅ **AI Chat**: Contextual conversation interface
- ✅ **Chart Library**: Plotly-based visualizations
- 🚧 **Backend**: API structure planned (FastAPI + LangChain)
- 🚧 **Real Data**: Integration with financial APIs pending
- 🚧 **Persistence**: Database integration planned

## 📈 Roadmap

### Phase 1: Frontend MVP ✅
- Interactive dashboard with mock data
- AI chat interface with smart responses
- Comprehensive chart library
- Session management

### Phase 2: Backend Integration (Next)
- FastAPI backend with real data sources
- LangChain integration for advanced AI
- Azure OpenAI deployment
- Real-time data streaming

### Phase 3: Production Features
- User authentication and profiles
- Advanced analytics and reporting
- Portfolio tracking
- Mobile-responsive design

## 🤝 Contributing

This dashboard was built using a structured development approach:
- Feature specifications in `specs/`
- Implementation plans and tasks
- TDD principles with contract tests
- Clean architecture with service layers

## 📄 License

Built as part of the Financial Dashboard project.

---

**🎯 Ready to analyze your investments? Start the dashboard and explore!**
