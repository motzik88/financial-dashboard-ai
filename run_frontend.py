#!/usr/bin/env python3
"""
Run script for Financial Dashboard Frontend
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    """Main entry point"""
    print("🚀 Starting Financial Dashboard Frontend...")
    print("📊 AI-Powered Investment Analysis Platform")
    print("=" * 50)
    
    # Get the project root directory
    project_root = Path(__file__).parent
    frontend_dir = project_root / "frontend"
    
    if not frontend_dir.exists():
        print("❌ Error: Frontend directory not found!")
        sys.exit(1)
    
    # Change to frontend directory
    os.chdir(frontend_dir)
    
    print("📁 Working directory:", os.getcwd())
    print("📦 Checking dependencies...")
    
    # Check if we're in a virtual environment
    if not hasattr(sys, 'real_prefix') and sys.base_prefix == sys.prefix:
        print("⚠️  Not in virtual environment. Using system Python...")
        python_cmd = "python3"
    else:
        print("✅ Using virtual environment")
        python_cmd = sys.executable
    
    print("\n🌐 Starting Streamlit server...")
    print("📱 Open your browser to: http://localhost:8501")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Start Streamlit
    try:
        subprocess.run([
            python_cmd, "-m", "streamlit", "run", "app.py",
            "--server.headless", "true",
            "--server.port", "8501",
            "--theme.base", "light"
        ], check=True)
    except KeyboardInterrupt:
        print("\n👋 Financial Dashboard stopped.")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error starting Streamlit: {e}")
        print("💡 Try running manually:")
        print(f"   cd frontend && {python_cmd} -m streamlit run app.py")

if __name__ == "__main__":
    main()
