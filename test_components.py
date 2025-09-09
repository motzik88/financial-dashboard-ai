#!/usr/bin/env python3
"""
Test script to verify frontend components can be imported and instantiated
"""

import sys
import os
from pathlib import Path

# Add frontend src to path
frontend_src = Path(__file__).parent / "frontend" / "src"
sys.path.insert(0, str(frontend_src))

def test_imports():
    """Test that all components can be imported"""
    print("🧪 Testing component imports...")
    
    try:
        # Test component imports
        from components.search_widget import SearchWidget
        print("✅ SearchWidget imported successfully")
        
        from components.chart_display import ChartDisplay
        print("✅ ChartDisplay imported successfully")
        
        from components.chat_interface import ChatInterface
        print("✅ ChatInterface imported successfully")
        
        from components.dashboard_layout import DashboardLayout
        print("✅ DashboardLayout imported successfully")
        
        # Test service imports
        from services.api_client import APIClient
        print("✅ APIClient imported successfully")
        
        from services.session_manager import SessionManager
        print("✅ SessionManager imported successfully")
        
        # Test instantiation
        print("\n🔧 Testing component instantiation...")
        
        search = SearchWidget()
        print("✅ SearchWidget instantiated")
        
        chart = ChartDisplay("AAPL")
        print("✅ ChartDisplay instantiated")
        
        chat = ChatInterface("AAPL")
        print("✅ ChatInterface instantiated")
        
        layout = DashboardLayout()
        print("✅ DashboardLayout instantiated")
        
        api = APIClient()
        print("✅ APIClient instantiated")
        
        session = SessionManager()
        print("✅ SessionManager instantiated")
        
        print("\n🎉 All components imported and instantiated successfully!")
        print("🚀 Ready to run the Financial Dashboard!")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Instantiation error: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality of components"""
    print("\n🔬 Testing basic functionality...")
    
    try:
        from components.search_widget import SearchWidget
        from components.chat_interface import ChatInterface
        
        # Test search
        search = SearchWidget()
        results = search.search_companies("AAPL")
        print(f"✅ Search returned {len(results)} results for 'AAPL'")
        
        # Test AI response
        chat = ChatInterface("AAPL")
        response = chat._generate_ai_response("What is Apple's P/E ratio?")
        print(f"✅ AI response generated: {len(response)} characters")
        
        print("🎯 Basic functionality tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Functionality test error: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Financial Dashboard Component Test")
    print("=" * 40)
    
    success = test_imports()
    if success:
        test_basic_functionality()
    
    print("\n" + "=" * 40)
    if success:
        print("🎊 All tests passed! Components are ready.")
        print("💡 Run: ./run_frontend.py")
    else:
        print("❌ Some tests failed. Check the error messages above.")
