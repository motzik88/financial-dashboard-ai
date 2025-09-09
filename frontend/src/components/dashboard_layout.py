"""
Dashboard Layout Component for Financial Dashboard
Provides consistent layout and navigation
"""

import streamlit as st
from datetime import datetime
import random

class DashboardLayout:
    """Dashboard layout and navigation component"""
    
    def render_header(self):
        """Render the dashboard header"""
        
        # Main header with logo and title
        col1, col2, col3 = st.columns([2, 6, 2])
        
        with col1:
            st.markdown("### 📊 **Financial Dashboard**")
        
        with col2:
            st.markdown("""
            <div style='text-align: center;'>
                <h1 style='color: #1f77b4; margin: 0;'>AI-Powered Investment Analysis</h1>
                <p style='color: #666; margin: 5px 0; font-size: 14px;'>
                    Real-time market data, interactive charts, and AI insights
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            # Market status indicator
            market_status = self._get_market_status()
            if market_status == "open":
                st.success("🟢 Market Open")
            elif market_status == "closed":
                st.warning("🔴 Market Closed")
            else:
                st.info("🟡 Pre-Market")
            
            # Current time
            current_time = datetime.now().strftime("%H:%M:%S")
            st.caption(f"Last updated: {current_time}")
    
    def _get_market_status(self) -> str:
        """Get current market status"""
        now = datetime.now()
        current_time = now.time()
        
        # US Market hours (simplified)
        market_open = datetime.strptime("09:30", "%H:%M").time()
        market_close = datetime.strptime("16:00", "%H:%M").time()
        
        # Check if it's a weekday
        if now.weekday() >= 5:  # Saturday = 5, Sunday = 6
            return "closed"
        
        if market_open <= current_time <= market_close:
            return "open"
        elif current_time < market_open:
            return "pre-market"
        else:
            return "after-hours"
    
    def render_footer(self):
        """Render dashboard footer"""
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.caption("© 2024 Financial Dashboard")
        
        with col2:
            st.caption("Data provided by multiple sources")
        
        with col3:
            st.caption("Version 1.0.0")
    
    def render_sidebar_navigation(self):
        """Render sidebar navigation (called from main app)"""
        st.sidebar.markdown("### 🧭 Navigation")
        
        # Main navigation items
        nav_items = {
            "🏠 Dashboard": "dashboard",
            "🔍 Company Search": "search", 
            "📊 Charts": "charts",
            "💬 AI Assistant": "chat",
            "📈 Analysis": "analysis",
            "⚙️ Settings": "settings"
        }
        
        for icon_text, page_key in nav_items.items():
            if st.sidebar.button(icon_text, key=f"nav_{page_key}"):
                st.session_state.current_page = page_key
                st.rerun()
        
        # Quick stats in sidebar
        st.sidebar.markdown("---")
        st.sidebar.markdown("### 📊 Quick Stats")
        
        # Mock market data
        market_data = {
            "S&P 500": {"value": "4,567.23", "change": "+0.85%"},
            "Dow Jones": {"value": "35,678.90", "change": "+0.72%"},
            "NASDAQ": {"value": "14,234.56", "change": "+1.23%"},
            "VIX": {"value": "18.45", "change": "-2.1%"}
        }
        
        for index, data in market_data.items():
            change_color = "green" if "+" in data["change"] else "red"
            st.sidebar.metric(
                label=index,
                value=data["value"],
                delta=data["change"]
            )
    
    def render_market_overview(self):
        """Render market overview section"""
        st.markdown("### 🌍 Market Overview")
        
        # Major indices
        col1, col2, col3, col4 = st.columns(4)
        
        indices = [
            ("S&P 500", "4,567.23", "+0.85%"),
            ("Dow Jones", "35,678.90", "+0.72%"),
            ("NASDAQ", "14,234.56", "+1.23%"),
            ("Russell 2000", "2,123.45", "-0.34%")
        ]
        
        for i, (name, value, change) in enumerate(indices):
            with [col1, col2, col3, col4][i]:
                delta_color = "normal" if "+" in change else "inverse"
                st.metric(name, value, change, delta_color=delta_color)
        
        # Market sectors
        st.markdown("### 📊 Sector Performance")
        
        sectors = {
            "Technology": {"change": "+1.8%", "color": "green"},
            "Healthcare": {"change": "+0.9%", "color": "green"},
            "Financials": {"change": "+0.3%", "color": "green"},
            "Energy": {"change": "-0.7%", "color": "red"},
            "Consumer": {"change": "+0.5%", "color": "green"},
            "Industrials": {"change": "-0.2%", "color": "red"}
        }
        
        cols = st.columns(3)
        sector_items = list(sectors.items())
        
        for i in range(0, len(sector_items), 2):
            for j in range(2):
                if i + j < len(sector_items):
                    sector_name, data = sector_items[i + j]
                    with cols[j]:
                        if data["color"] == "green":
                            st.success(f"📈 {sector_name}: {data['change']}")
                        else:
                            st.error(f"📉 {sector_name}: {data['change']}")
    
    def render_welcome_message(self):
        """Render welcome message for new users"""
        st.markdown("""
        # 🎯 Welcome to Financial Dashboard
        
        ## Your AI-Powered Investment Analysis Platform
        
        **🚀 Key Features:**
        - **Real-time Market Data**: Live stock prices and market indices
        - **Interactive Charts**: Advanced visualizations for technical analysis
        - **AI Assistant**: Get instant insights and answers to your questions
        - **Comparative Analysis**: Compare companies and track performance
        - **Sentiment Analysis**: Understand market sentiment and news impact
        
        **📈 Getting Started:**
        1. Search for any company using the sidebar
        2. Explore different chart views and analysis tools
        3. Ask the AI assistant for investment insights
        4. Compare with peer companies and industry benchmarks
        
        ---
        """)
        
        # Quick demo buttons
        st.markdown("### 🎮 Quick Demo")
        st.markdown("Try these popular stocks:")
        
        demo_stocks = ["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA"]
        cols = st.columns(5)
        
        for i, stock in enumerate(demo_stocks):
            with cols[i]:
                if st.button(f"📊 {stock}", key=f"demo_{stock}"):
                    st.session_state.current_ticker = stock
                    st.success(f"Selected {stock} for analysis!")
                    st.rerun()
