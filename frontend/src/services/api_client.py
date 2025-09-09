"""
API Client Service for Financial Dashboard
Handles communication with backend services
"""

import requests
import streamlit as st
from typing import Dict, Any, Optional, List
from datetime import datetime
import json
import time

class APIClient:
    """Client for communicating with backend API services"""
    
    def __init__(self, base_url: str = "http://localhost:8000/api"):
        """Initialize API client"""
        self.base_url = base_url
        self.session = requests.Session()
        self.session.timeout = 30  # 30 second timeout
        
    def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """
        Make HTTP request to API
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint
            **kwargs: Additional request parameters
            
        Returns:
            API response data
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            
            # Try to parse JSON response
            if response.content:
                return response.json()
            else:
                return {"success": True}
                
        except requests.exceptions.RequestException as e:
            # For demo purposes, return mock data instead of failing
            st.warning(f"API request failed ({method} {endpoint}): {str(e)}")
            return self._get_mock_response(endpoint)
        except json.JSONDecodeError:
            st.warning(f"Invalid JSON response from {endpoint}")
            return {"error": "Invalid response format"}
    
    def _get_mock_response(self, endpoint: str) -> Dict[str, Any]:
        """Get mock response for demo purposes"""
        if "companies/search" in endpoint:
            return {
                "results": [
                    {"ticker": "AAPL", "name": "Apple Inc.", "sector": "Technology"},
                    {"ticker": "GOOGL", "name": "Alphabet Inc.", "sector": "Technology"},
                    {"ticker": "MSFT", "name": "Microsoft Corporation", "sector": "Technology"}
                ]
            }
        elif "companies/" in endpoint and "/data" in endpoint:
            ticker = endpoint.split("/")[1]
            return {
                "ticker": ticker,
                "price": 175.50,
                "volume": 45000000,
                "market_cap": 2800000000000,
                "pe_ratio": 28.5,
                "pb_ratio": 8.2,
                "timestamp": datetime.now().isoformat()
            }
        elif "chat/query" in endpoint:
            return {
                "response": "This is a mock AI response. Backend integration coming soon!",
                "confidence": 0.85,
                "timestamp": datetime.now().isoformat()
            }
        else:
            return {"message": "Mock response", "status": "success"}
    
    def search_companies(self, query: str) -> List[Dict[str, Any]]:
        """
        Search for companies by ticker or name
        
        Args:
            query: Search query
            
        Returns:
            List of matching companies
        """
        response = self._make_request("GET", f"companies/search?q={query}")
        return response.get("results", [])
    
    def get_company_data(self, ticker: str) -> Dict[str, Any]:
        """
        Get comprehensive financial data for a company
        
        Args:
            ticker: Company ticker symbol
            
        Returns:
            Company financial data
        """
        response = self._make_request("GET", f"companies/{ticker}/data")
        return response
    
    def get_comparables(self, ticker: str) -> List[Dict[str, Any]]:
        """
        Get comparable companies for peer analysis
        
        Args:
            ticker: Company ticker symbol
            
        Returns:
            List of comparable companies
        """
        response = self._make_request("GET", f"companies/{ticker}/comparables")
        return response.get("comparables", [])
    
    def chat_query(self, query: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Send query to AI assistant
        
        Args:
            query: User question
            context: Optional context data
            
        Returns:
            AI assistant response
        """
        payload = {
            "query": query,
            "context": context or {},
            "timestamp": datetime.now().isoformat()
        }
        
        response = self._make_request("POST", "chat/query", json=payload)
        return response
    
    def get_chart_data(self, ticker: str, chart_type: str = "valuation") -> Dict[str, Any]:
        """
        Get chart data for visualization
        
        Args:
            ticker: Company ticker
            chart_type: Type of chart data
            
        Returns:
            Chart data for plotting
        """
        response = self._make_request("GET", f"charts/{ticker}/{chart_type}")
        return response
    
    def get_market_overview(self) -> Dict[str, Any]:
        """
        Get overall market overview data
        
        Returns:
            Market indices and sector data
        """
        response = self._make_request("GET", "market/overview")
        return response
    
    def export_data(self, ticker: str, data_type: str = "all") -> Dict[str, Any]:
        """
        Export company data
        
        Args:
            ticker: Company ticker
            data_type: Type of data to export
            
        Returns:
            Export result
        """
        response = self._make_request("GET", f"companies/{ticker}/export?type={data_type}")
        return response
    
    def get_health_status(self) -> Dict[str, Any]:
        """
        Get API health status
        
        Returns:
            Health check result
        """
        try:
            response = self._make_request("GET", "health")
            return response
        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
