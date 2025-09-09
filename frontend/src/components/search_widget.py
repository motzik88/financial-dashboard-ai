"""
Search Widget Component for Financial Dashboard
Provides company search functionality with autocomplete
"""

import streamlit as st
from typing import Optional, List, Dict
import random

class SearchWidget:
    """Company search widget with autocomplete functionality"""
    
    def __init__(self):
        """Initialize the search widget"""
        self.mock_companies = {
            "AAPL": "Apple Inc.",
            "GOOGL": "Alphabet Inc.",
            "MSFT": "Microsoft Corporation", 
            "TSLA": "Tesla, Inc.",
            "NVDA": "NVIDIA Corporation",
            "AMZN": "Amazon.com, Inc.",
            "META": "Meta Platforms, Inc.",
            "NFLX": "Netflix, Inc.",
            "CRM": "Salesforce, Inc.",
            "INTC": "Intel Corporation",
            "AMD": "Advanced Micro Devices, Inc.",
            "UBER": "Uber Technologies, Inc.",
            "SPOT": "Spotify Technology S.A.",
            "PYPL": "PayPal Holdings, Inc.",
            "ZOOM": "Zoom Video Communications, Inc.",
            "SHOP": "Shopify Inc.",
            "SQ": "Block, Inc.",
            "COIN": "Coinbase Global, Inc.",
            "ROKU": "Roku, Inc.",
            "PINS": "Pinterest, Inc."
        }
    
    def search_companies(self, query: str) -> List[Dict[str, str]]:
        """
        Search companies by ticker or name
        
        Args:
            query: Search query (ticker or company name)
            
        Returns:
            List of matching companies with ticker and name
        """
        if not query:
            return []
        
        query = query.upper()
        results = []
        
        # Search by ticker
        for ticker, name in self.mock_companies.items():
            if query in ticker:
                results.append({"ticker": ticker, "name": name})
        
        # Search by name
        for ticker, name in self.mock_companies.items():
            if query in name.upper() and not any(r["ticker"] == ticker for r in results):
                results.append({"ticker": ticker, "name": name})
        
        return results[:10]  # Limit to 10 results
    
    def render(self) -> Optional[str]:
        """
        Render the search widget
        
        Returns:
            Selected ticker symbol or None
        """
        st.markdown("### Search Companies")
        
        # Search input
        search_query = st.text_input(
            "Enter ticker symbol or company name:",
            placeholder="e.g., AAPL, Apple, Tesla...",
            key="company_search"
        )
        
        selected_ticker = None
        
        if search_query:
            results = self.search_companies(search_query)
            
            if results:
                st.markdown("**Search Results:**")
                
                # Display results as clickable buttons
                for result in results:
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        if st.button(
                            f"📈 {result['ticker']}", 
                            key=f"select_{result['ticker']}",
                            help=f"Select {result['name']}"
                        ):
                            selected_ticker = result['ticker']
                    with col2:
                        st.write(f"**{result['name']}**")
                        st.write("---")
            else:
                st.warning("No companies found matching your search.")
        
        # Quick access to popular companies
        st.markdown("### Popular Companies")
        popular_tickers = ["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA"]
        
        cols = st.columns(5)
        for i, ticker in enumerate(popular_tickers):
            with cols[i]:
                if st.button(
                    f"{ticker}", 
                    key=f"popular_{ticker}",
                    help=f"Quick select {self.mock_companies[ticker]}"
                ):
                    selected_ticker = ticker
        
        return selected_ticker
