"""
Financial Dashboard - Main Streamlit Application
AI-powered financial analysis dashboard with chat assistant
"""

import streamlit as st
import sys
import os
from pathlib import Path

# Add the frontend src directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Import our custom components
from components.search_widget import SearchWidget
from components.chart_display import ChartDisplay
from components.chat_interface import ChatInterface
from components.dashboard_layout import DashboardLayout
from services.api_client import APIClient
from services.session_manager import SessionManager

# Configure the page
st.set_page_config(
    page_title="Financial Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize services
api_client = APIClient()
session_manager = SessionManager()

def main():
    """Main application entry point"""
    
    # Initialize session state
    if 'current_ticker' not in st.session_state:
        st.session_state.current_ticker = None
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Create dashboard layout
    layout = DashboardLayout()
    layout.render_header()
    
    # Sidebar with search and navigation
    with st.sidebar:
        st.header("🔍 Company Search")
        
        # Search widget
        search_widget = SearchWidget()
        selected_ticker = search_widget.render()
        
        if selected_ticker:
            st.session_state.current_ticker = selected_ticker
            st.success(f"Selected: {selected_ticker}")
        
        # Navigation
        st.header("📊 Dashboard Views")
        view_options = ["Overview", "Valuation", "Trading", "Sentiment", "Analysis"]
        selected_view = st.radio("Select View:", view_options, index=0)
        
        # Current selection display
        if st.session_state.current_ticker:
            st.info(f"📈 **{st.session_state.current_ticker}**")
    
    # Main content area
    if st.session_state.current_ticker:
        # Create tabs for different views
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Charts", "�� AI Assistant", "📋 Details", "⚙️ Settings"])
        
        with tab1:
            st.header(f"�� {st.session_state.current_ticker} Analysis")
            
            # Chart display component
            chart_display = ChartDisplay(st.session_state.current_ticker)
            chart_display.render_overview()
            
            # Individual charts
            col1, col2 = st.columns(2)
            with col1:
                chart_display.render_valuation_chart()
            with col2:
                chart_display.render_trading_chart()
            
            # Sentiment chart
            chart_display.render_sentiment_chart()
        
        with tab2:
            st.header("�� AI Financial Assistant")
            
            # Chat interface component
            chat_interface = ChatInterface(st.session_state.current_ticker)
            chat_interface.render()
        
        with tab3:
            st.header("📋 Company Details")
            chart_display.render_company_details()
        
        with tab4:
            st.header("⚙️ Settings")
            session_manager.render_settings()
    
    else:
        # Welcome screen
        st.title("🎯 Welcome to Financial Dashboard")
        st.markdown("""
        ### Elad Hagever
        
        **Features:**
        - 🔍 Search companies by ticker or name
        - 📊 Interactive financial charts and analysis
        - 🤖 AI chat assistant for investment insights
        - 📈 Real-time market data and sentiment analysis
        - 💡 Comparative analysis with peer companies
        
        **Getting Started:**
        1. Use the search box in the sidebar to find a company
        2. Explore different chart views and analysis
        3. Ask questions to the AI assistant for insights
        4. Compare with peer companies and industry benchmarks
        """)
        
        # Quick examples
        st.subheader("🚀 Quick Start Examples")
        example_tickers = ["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA"]
        
        cols = st.columns(5)
        for i, ticker in enumerate(example_tickers):
            with cols[i]:
                if st.button(f"📈 {ticker}", key=f"example_{ticker}"):
                    st.session_state.current_ticker = ticker
                    st.rerun()

if __name__ == "__main__":
    main()
