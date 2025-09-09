"""
Chat Interface Component for Financial Dashboard
AI-powered chat assistant for financial analysis
"""

import streamlit as st
from datetime import datetime
from typing import List, Dict, Any
import random

class ChatInterface:
    """AI chat interface for financial analysis conversations"""
    
    def __init__(self, ticker: str):
        """Initialize chat interface for a specific company"""
        self.ticker = ticker
        self.company_name = self._get_company_name()
        
    def _get_company_name(self) -> str:
        """Get company name for the ticker"""
        companies = {
            "AAPL": "Apple Inc.",
            "GOOGL": "Alphabet Inc.",
            "MSFT": "Microsoft Corporation",
            "TSLA": "Tesla, Inc.",
            "NVDA": "NVIDIA Corporation"
        }
        return companies.get(self.ticker, self.ticker)
    
    def _generate_ai_response(self, user_query: str) -> str:
        """Generate mock AI response based on user query"""
        query_lower = user_query.lower()
        
        responses = {
            "pe ratio": [
                f"{self.company_name}'s current P/E ratio is 28.5, which is slightly above the industry average of 25.2. This suggests the market is willing to pay a premium for {self.company_name}'s growth prospects.",
                f"The P/E ratio for {self.ticker} stands at 28.5, compared to the sector average of 25.2. This indicates investors are optimistic about future earnings growth."
            ],
            "valuation": [
                f"{self.company_name} is currently valued at $2.8T in market capitalization. Based on current earnings, this represents a P/E ratio of 28.5x. The company trades at a premium to its historical averages due to strong growth in services and emerging markets.",
                f"At a market cap of $2.8T, {self.ticker} represents approximately 6.2% of the S&P 500. The valuation appears reasonable given the company's dominant market position and consistent revenue growth."
            ],
            "competitors": [
                f"{self.company_name}'s main competitors include Samsung, Huawei, and Xiaomi in consumer electronics. However, {self.company_name} maintains a significant premium positioning due to its ecosystem integration and brand loyalty.",
                f"In terms of market share, {self.company_name} leads the premium smartphone segment with approximately 55% share, well ahead of Samsung's 20% and other competitors."
            ],
            "growth": [
                f"{self.company_name} has demonstrated consistent revenue growth of 8-10% annually. The services segment, including Apple Music and iCloud, has been a key growth driver, contributing over 20% of total revenue.",
                f"Analysts project {self.ticker} revenue growth of 6-8% for the next fiscal year, driven by new product launches and expansion in emerging markets."
            ],
            "risks": [
                f"Key risks for {self.company_name} include supply chain dependencies, regulatory scrutiny in major markets, and competitive pressures in the services segment. However, the company's strong balance sheet provides resilience.",
                f"Market risks include potential economic slowdown affecting premium product sales and currency fluctuations impacting international revenue, which comprises about 60% of total sales."
            ]
        }
        
        # Default response
        default_responses = [
            f"Based on the latest financial data, {self.company_name} shows strong fundamentals with consistent profitability and market leadership in its segments. The company's balance sheet remains robust with significant cash reserves.",
            f"{self.ticker} demonstrates solid financial health with improving margins and market share gains. The company's strategic investments in AI and services should drive future growth.",
            f"From a financial perspective, {self.company_name} maintains a competitive advantage through brand strength, ecosystem integration, and consistent innovation. The current valuation appears reasonable relative to growth prospects."
        ]
        
        # Find matching response
        for keyword, response_list in responses.items():
            if keyword in query_lower:
                return random.choice(response_list)
        
        return random.choice(default_responses)
    
    def render(self):
        """Render the chat interface"""
        
        # Chat container
        st.markdown("### 💬 AI Financial Assistant")
        st.markdown(f"Ask me anything about **{self.company_name}** ({self.ticker})")
        
        # Initialize chat history if not exists
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        
        # Display chat history
        chat_container = st.container()
        
        with chat_container:
            for message in st.session_state.chat_history:
                if message['role'] == 'user':
                    st.markdown(f"**👤 You:** {message['content']}")
                else:
                    st.markdown(f"**🤖 Assistant:** {message['content']}")
                st.markdown("---")
        
        # Chat input
        with st.form(key='chat_form', clear_on_submit=True):
            user_input = st.text_input(
                "Ask a question about the company:",
                placeholder=f"e.g., What is {self.ticker}'s valuation? How does it compare to competitors?",
                key="chat_input"
            )
            
            col1, col2 = st.columns([1, 4])
            with col1:
                submit_button = st.form_submit_button("Send 🚀")
            
            if submit_button and user_input:
                # Add user message to history
                st.session_state.chat_history.append({
                    'role': 'user',
                    'content': user_input,
                    'timestamp': datetime.now()
                })
                
                # Generate AI response
                ai_response = self._generate_ai_response(user_input)
                
                # Add AI response to history
                st.session_state.chat_history.append({
                    'role': 'assistant', 
                    'content': ai_response,
                    'timestamp': datetime.now()
                })
                
                # Rerun to update chat display
                st.rerun()
        
        # Quick question buttons
        st.markdown("### 💡 Quick Questions")
        
        quick_questions = [
            f"What is {self.ticker}'s current valuation?",
            f"How does {self.company_name} compare to competitors?",
            f"What are the growth prospects for {self.ticker}?",
            f"What are the main risks for {self.company_name}?",
            f"What is the P/E ratio analysis?"
        ]
        
        cols = st.columns(2)
        for i, question in enumerate(quick_questions):
            with cols[i % 2]:
                if st.button(
                    question, 
                    key=f"quick_{i}",
                    use_container_width=True,
                    help="Click to ask this question"
                ):
                    # Simulate asking the question
                    st.session_state.chat_history.append({
                        'role': 'user',
                        'content': question,
                        'timestamp': datetime.now()
                    })
                    
                    ai_response = self._generate_ai_response(question)
                    
                    st.session_state.chat_history.append({
                        'role': 'assistant',
                        'content': ai_response,
                        'timestamp': datetime.now()
                    })
                    
                    st.rerun()
        
        # Chat controls
        st.markdown("### ⚙️ Chat Controls")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🗑️ Clear Chat", help="Clear conversation history"):
                st.session_state.chat_history = []
                st.rerun()
        
        with col2:
            if st.button("📄 Export Chat", help="Download conversation"):
                # Mock export functionality
                st.info("Chat export feature coming soon!")
        
        with col3:
            if st.button("💡 Analysis Mode", help="Switch to detailed analysis mode"):
                st.info("Detailed analysis mode activated!")
        
        # Chat statistics
        if st.session_state.chat_history:
            total_messages = len(st.session_state.chat_history)
            user_messages = len([m for m in st.session_state.chat_history if m['role'] == 'user'])
            ai_messages = len([m for m in st.session_state.chat_history if m['role'] == 'assistant'])
            
            st.markdown(f"**📊 Chat Stats:** {total_messages} messages ({user_messages} yours, {ai_messages} AI)")
