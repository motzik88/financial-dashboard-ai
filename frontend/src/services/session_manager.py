"""
Session Manager Service for Financial Dashboard
Manages user session state and preferences
"""

import streamlit as st
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
import json
import time

class SessionManager:
    """Manages user session state and preferences"""
    
    def __init__(self):
        """Initialize session manager"""
        self._initialize_session_state()
    
    def _initialize_session_state(self):
        """Initialize default session state values"""
        defaults = {
            'current_ticker': None,
            'search_history': [],
            'chart_preferences': {
                'default_period': '1Y',
                'theme': 'light',
                'show_volume': True,
                'technical_indicators': ['SMA_20', 'SMA_50']
            },
            'ai_preferences': {
                'response_style': 'balanced',
                'detail_level': 'medium',
                'include_sources': True
            },
            'user_settings': {
                'notifications': True,
                'auto_refresh': True,
                'refresh_interval': 300  # 5 minutes
            },
            'session_start': datetime.now().isoformat(),
            'last_activity': datetime.now().isoformat()
        }
        
        for key, default_value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = default_value
    
    def update_last_activity(self):
        """Update last activity timestamp"""
        st.session_state.last_activity = datetime.now().isoformat()
    
    def add_to_search_history(self, ticker: str):
        """Add ticker to search history"""
        if ticker not in st.session_state.search_history:
            st.session_state.search_history.insert(0, ticker)
            # Keep only last 10 searches
            st.session_state.search_history = st.session_state.search_history[:10]
    
    def get_search_history(self) -> List[str]:
        """Get recent search history"""
        return st.session_state.search_history
    
    def set_current_ticker(self, ticker: str):
        """Set current selected ticker"""
        st.session_state.current_ticker = ticker
        self.add_to_search_history(ticker)
        self.update_last_activity()
    
    def get_current_ticker(self) -> Optional[str]:
        """Get currently selected ticker"""
        return st.session_state.current_ticker
    
    def get_chart_preferences(self) -> Dict[str, Any]:
        """Get chart display preferences"""
        return st.session_state.chart_preferences
    
    def update_chart_preferences(self, preferences: Dict[str, Any]):
        """Update chart preferences"""
        st.session_state.chart_preferences.update(preferences)
        self.update_last_activity()
    
    def get_ai_preferences(self) -> Dict[str, Any]:
        """Get AI assistant preferences"""
        return st.session_state.ai_preferences
    
    def update_ai_preferences(self, preferences: Dict[str, Any]):
        """Update AI assistant preferences"""
        st.session_state.ai_preferences.update(preferences)
        self.update_last_activity()
    
    def get_user_settings(self) -> Dict[str, Any]:
        """Get user settings"""
        return st.session_state.user_settings
    
    def update_user_settings(self, settings: Dict[str, Any]):
        """Update user settings"""
        st.session_state.user_settings.update(settings)
        self.update_last_activity()
    
    def clear_session(self):
        """Clear all session data"""
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        self._initialize_session_state()
    
    def get_session_info(self) -> Dict[str, Any]:
        """Get session information"""
        session_start = datetime.fromisoformat(st.session_state.session_start)
        last_activity = datetime.fromisoformat(st.session_state.last_activity)
        
        return {
            'session_duration': str(datetime.now() - session_start),
            'last_activity': str(last_activity),
            'current_ticker': st.session_state.current_ticker,
            'search_history_count': len(st.session_state.search_history),
            'chart_theme': st.session_state.chart_preferences['theme']
        }
    
    def render_settings(self):
        """Render settings interface"""
        st.markdown("### ⚙️ Dashboard Settings")
        
        # Chart Settings
        with st.expander("📊 Chart Preferences", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                theme = st.selectbox(
                    "Chart Theme",
                    ["light", "dark", "auto"],
                    index=["light", "dark", "auto"].index(st.session_state.chart_preferences['theme'])
                )
                
                period = st.selectbox(
                    "Default Period",
                    ["1D", "1W", "1M", "3M", "1Y", "5Y"],
                    index=["1D", "1W", "1M", "3M", "1Y", "5Y"].index(st.session_state.chart_preferences['default_period'])
                )
            
            with col2:
                show_volume = st.checkbox(
                    "Show Volume",
                    value=st.session_state.chart_preferences['show_volume']
                )
                
                indicators = st.multiselect(
                    "Technical Indicators",
                    ["SMA_20", "SMA_50", "SMA_200", "RSI", "MACD"],
                    default=st.session_state.chart_preferences['technical_indicators']
                )
            
            if st.button("Save Chart Settings"):
                self.update_chart_preferences({
                    'theme': theme,
                    'default_period': period,
                    'show_volume': show_volume,
                    'technical_indicators': indicators
                })
                st.success("Chart settings saved!")
        
        # AI Assistant Settings
        with st.expander("🤖 AI Assistant Preferences", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                response_style = st.selectbox(
                    "Response Style",
                    ["concise", "balanced", "detailed"],
                    index=["concise", "balanced", "detailed"].index(st.session_state.ai_preferences['response_style'])
                )
                
                detail_level = st.selectbox(
                    "Detail Level",
                    ["brief", "medium", "comprehensive"],
                    index=["brief", "medium", "comprehensive"].index(st.session_state.ai_preferences['detail_level'])
                )
            
            with col2:
                include_sources = st.checkbox(
                    "Include Data Sources",
                    value=st.session_state.ai_preferences['include_sources']
                )
            
            if st.button("Save AI Settings"):
                self.update_ai_preferences({
                    'response_style': response_style,
                    'detail_level': detail_level,
                    'include_sources': include_sources
                })
                st.success("AI settings saved!")
        
        # User Settings
        with st.expander("👤 User Preferences", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                notifications = st.checkbox(
                    "Enable Notifications",
                    value=st.session_state.user_settings['notifications']
                )
                
                auto_refresh = st.checkbox(
                    "Auto-refresh Data",
                    value=st.session_state.user_settings['auto_refresh']
                )
            
            with col2:
                refresh_interval = st.slider(
                    "Refresh Interval (minutes)",
                    min_value=1,
                    max_value=60,
                    value=st.session_state.user_settings['refresh_interval'] // 60,
                    step=5
                ) * 60  # Convert to seconds
            
            if st.button("Save User Settings"):
                self.update_user_settings({
                    'notifications': notifications,
                    'auto_refresh': auto_refresh,
                    'refresh_interval': refresh_interval
                })
                st.success("User settings saved!")
        
        # Session Management
        with st.expander("�� Session Management", expanded=False):
            st.markdown("### Session Information")
            session_info = self.get_session_info()
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Session Duration:** {session_info['session_duration']}")
                st.write(f"**Current Ticker:** {session_info['current_ticker'] or 'None'}")
            
            with col2:
                st.write(f"**Search History:** {session_info['search_history_count']} items")
                st.write(f"**Chart Theme:** {session_info['chart_theme']}")
            
            st.markdown("### Actions")
            if st.button("🗑️ Clear Search History"):
                st.session_state.search_history = []
                st.success("Search history cleared!")
            
            if st.button("🔄 Reset All Settings"):
                if st.checkbox("⚠️ Confirm reset all settings to defaults"):
                    self.clear_session()
                    st.success("All settings reset!")
                    st.rerun()
    
    def export_session_data(self) -> str:
        """Export session data as JSON string"""
        export_data = {
            'session_info': self.get_session_info(),
            'chart_preferences': self.get_chart_preferences(),
            'ai_preferences': self.get_ai_preferences(),
            'user_settings': self.get_user_settings(),
            'search_history': self.get_search_history(),
            'export_timestamp': datetime.now().isoformat()
        }
        return json.dumps(export_data, indent=2)
