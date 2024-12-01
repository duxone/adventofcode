import os
from datetime import datetime, timedelta
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv

class AdventSession:
    """Handles session management and authentication for adventofcode.com."""
    
    def __init__(self, session_cookie: Optional[str] = None):
        self.session_cookie = self._initialize_session(session_cookie)
        self.headers = {
            'Cookie': f'session={self.session_cookie}',
            'User-Agent': 'github.com/duxone'
        }

    def _initialize_session(self, session_cookie: Optional[str]) -> str:
        """Initialize session from various sources."""
        # Try to load from .env file
        env_path = Path('.') / '.env'
        if env_path.exists():
            load_dotenv(env_path)

        # Try different sources in order
        cookie = session_cookie or os.getenv('AOC_SESSION')
        
        if not cookie:
            raise ValueError(
                "No session cookie provided. You can:\n"
                "1. Pass it directly to AdventOfCode()\n"
                "2. Set the AOC_SESSION environment variable in your .zshrc/.bashrc:\n"
                "   export AOC_SESSION='your_session_cookie_here'\n"
                "3. Create a .env file with:\n"
                "   AOC_SESSION=your_session_cookie_here"
            )
        
        return cookie

    def validate(self) -> bool:
        """Validate the current session cookie."""
        # Implementation for session validation
        # You might want to make a test request to the AoC API
        return True

    def days_until_expiry(self) -> int:
        """Calculate days until session expiry."""
        # AoC sessions typically expire after ~30 days
        # You might want to store the creation date and calculate based on that
        return 30