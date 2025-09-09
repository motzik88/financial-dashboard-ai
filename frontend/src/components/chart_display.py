"""
Chart Display Component for Financial Dashboard
Provides interactive financial charts and visualizations
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import random

class ChartDisplay:
    """Interactive financial chart display component"""
    
    def __init__(self, ticker: str):
        """Initialize chart display for a specific ticker"""
        self.ticker = ticker
        self.company_data = self._get_mock_company_data()
        
    def _get_mock_company_data(self) -> dict:
        """Get mock company data for demonstration"""
        companies = {
            "AAPL": {
                "name": "Apple Inc.",
                "sector": "Technology",
                "industry": "Consumer Electronics",
                "market_cap": 2800000000000,
                "pe_ratio": 28.5,
                "pb_ratio": 8.2,
                "price": 175.50,
                "volume": 45000000
            },
            "GOOGL": {
                "name": "Alphabet Inc.",
                "sector": "Technology", 
                "industry": "Internet Content & Information",
                "market_cap": 1600000000000,
                "pe_ratio": 25.8,
                "pb_ratio": 4.1,
                "price": 135.20,
                "volume": 28000000
            },
            "MSFT": {
                "name": "Microsoft Corporation",
                "sector": "Technology",
                "industry": "Software—Infrastructure", 
                "market_cap": 2500000000000,
                "pe_ratio": 32.1,
                "pb_ratio": 12.5,
                "price": 335.80,
                "volume": 32000000
            },
            "TSLA": {
                "name": "Tesla, Inc.",
                "sector": "Consumer Cyclical",
                "industry": "Auto Manufacturers",
                "market_cap": 650000000000,
                "pe_ratio": 45.2,
                "pb_ratio": 8.9,
                "price": 248.30,
                "volume": 89000000
            },
            "NVDA": {
                "name": "NVIDIA Corporation",
                "sector": "Technology",
                "industry": "Semiconductors",
                "market_cap": 1200000000000,
                "pe_ratio": 65.4,
                "pb_ratio": 22.1,
                "price": 485.20,
                "volume": 42000000
            }
        }
        return companies.get(self.ticker, companies["AAPL"])
    
    def _generate_price_history(self, days: int = 365) -> pd.DataFrame:
        """Generate mock price history data"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        dates = pd.date_range(start=start_date, end=end_date, freq='D')
        base_price = self.company_data["price"]
        
        # Generate realistic price movements
        np.random.seed(42)  # For reproducible results
        daily_returns = np.random.normal(0.0005, 0.02, len(dates))
        prices = base_price * np.exp(np.cumsum(daily_returns))
        
        return pd.DataFrame({
            'Date': dates,
            'Price': prices,
            'Volume': np.random.randint(20000000, 100000000, len(dates))
        })
    
    def render_overview(self):
        """Render company overview metrics"""
        data = self.company_data
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="📈 Stock Price",
                value=f"${data['price']:.2f}",
                delta=f"{random.uniform(-2, 3):.1f}%"
            )
        
        with col2:
            st.metric(
                label="💰 Market Cap",
                value=f"${data['market_cap']/1000000000:.1f}B"
            )
        
        with col3:
            st.metric(
                label="📊 P/E Ratio",
                value=f"{data['pe_ratio']:.1f}",
                delta="vs Industry"
            )
        
        with col4:
            st.metric(
                label="📦 Volume",
                value=f"{data['volume']/1000000:.1f}M"
            )
    
    def render_valuation_chart(self):
        """Render valuation multiples chart"""
        # Mock peer company data
        peers = ["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA"]
        pe_ratios = [28.5, 25.8, 32.1, 45.2, 65.4]
        pb_ratios = [8.2, 4.1, 12.5, 8.9, 22.1]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='P/E Ratio',
            x=peers,
            y=pe_ratios,
            marker_color='lightblue'
        ))
        
        fig.add_trace(go.Bar(
            name='P/B Ratio', 
            x=peers,
            y=pb_ratios,
            marker_color='lightgreen'
        ))
        
        fig.update_layout(
            title="Valuation Multiples Comparison",
            xaxis_title="Company",
            yaxis_title="Ratio",
            barmode='group'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def render_trading_chart(self):
        """Render price and volume trading chart"""
        df = self._generate_price_history(90)
        
        fig = go.Figure()
        
        # Candlestick chart (simplified as line for demo)
        fig.add_trace(go.Scatter(
            x=df['Date'],
            y=df['Price'],
            mode='lines',
            name='Price',
            line=dict(color='blue', width=2)
        ))
        
        # Volume bars
        fig.add_trace(go.Bar(
            x=df['Date'],
            y=df['Volume']/1000000,  # Convert to millions
            name='Volume (M)',
            marker_color='rgba(255, 165, 0, 0.5)',
            yaxis='y2'
        ))
        
        fig.update_layout(
            title=f"{self.ticker} Price & Volume (90 Days)",
            xaxis_title="Date",
            yaxis_title="Price ($)",
            yaxis2=dict(
                title="Volume (Millions)",
                overlaying="y",
                side="right"
            ),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def render_sentiment_chart(self):
        """Render sentiment analysis chart"""
        # Mock sentiment data
        dates = pd.date_range(start=datetime.now()-timedelta(days=30), periods=30, freq='D')
        sentiment_scores = np.random.normal(0.6, 0.15, 30)
        sentiment_scores = np.clip(sentiment_scores, -1, 1)  # Bound between -1 and 1
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=dates,
            y=sentiment_scores,
            mode='lines+markers',
            name='Sentiment Score',
            line=dict(color='green', width=2),
            marker=dict(size=6)
        ))
        
        # Add neutral line
        fig.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="Neutral")
        
        fig.update_layout(
            title="Market Sentiment Analysis (30 Days)",
            xaxis_title="Date",
            yaxis_title="Sentiment Score",
            yaxis_range=[-1, 1],
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Sentiment summary
        avg_sentiment = np.mean(sentiment_scores)
        sentiment_label = "Positive" if avg_sentiment > 0.1 else "Negative" if avg_sentiment < -0.1 else "Neutral"
        
        st.info(f"**Overall Sentiment:** {sentiment_label} (Average: {avg_sentiment:.2f})")
    
    def render_company_details(self):
        """Render detailed company information"""
        data = self.company_data
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🏢 Company Information")
            st.write(f"**Name:** {data['name']}")
            st.write(f"**Ticker:** {self.ticker}")
            st.write(f"**Sector:** {data['sector']}")
            st.write(f"**Industry:** {data['industry']}")
        
        with col2:
            st.subheader("📊 Financial Metrics")
            st.write(f"**Market Cap:** ${data['market_cap']/1000000000:.1f}B")
            st.write(f"**Stock Price:** ${data['price']:.2f}")
            st.write(f"**P/E Ratio:** {data['pe_ratio']:.1f}")
            st.write(f"**P/B Ratio:** {data['pb_ratio']:.1f}")
        
        # Additional details
        st.subheader("📈 Key Statistics")
        stats_col1, stats_col2, stats_col3 = st.columns(3)
        
        with stats_col1:
            st.metric("52W High", "$200.00", "▲ 14.3%")
        with stats_col2:
            st.metric("52W Low", "$120.00", "▼ 46.3%") 
        with stats_col3:
            st.metric("Beta", "1.23", "vs Market")
        
        # Analyst recommendations (mock)
        st.subheader("👥 Analyst Coverage")
        analyst_data = {
            "Firm": ["Morgan Stanley", "Goldman Sachs", "JPMorgan", "Barclays"],
            "Rating": ["Buy", "Buy", "Hold", "Buy"],
            "Price Target": ["$195", "$188", "$172", "$190"],
            "Date": ["2024-01-15", "2024-01-12", "2024-01-10", "2024-01-08"]
        }
        
        st.table(pd.DataFrame(analyst_data))
