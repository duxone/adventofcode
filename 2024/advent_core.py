from advent_session import AdventSession
from advent_cache import AdventCache
import requests
from bs4 import BeautifulSoup
from typing import Optional

class AdventOfCode:
    """Main interface for Advent of Code interactions."""
    
    def __init__(self, session_cookie: Optional[str] = None, year: int = 2023):
        self.year = year
        self.base_url = f"https://adventofcode.com/{year}"
        self.session = AdventSession(session_cookie)
        self.cache = AdventCache()

    def get_problem(self, day: int) -> str:
        """Get problem description for a specific day."""
        # Try cache first
        cached_content = self.cache.load('problems', day)
        if cached_content:
            return cached_content

        # Fetch from website if not cached
        url = f"{self.base_url}/day/{day}"
        response = requests.get(url, headers=self.session.headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find('article', class_='day-desc')
        
        if article:
            content = article.get_text().strip()
            self.cache.save('problems', day, content)
            return content
        
        raise ValueError(f"Problem description not found for day {day}")

    def get_input(self, day: int) -> str:
        """Get input data for a specific day."""
        # Try cache first
        cached_content = self.cache.load('inputs', day)
        if cached_content:
            return cached_content

        # Fetch from website if not cached
        url = f"{self.base_url}/day/{day}/input"
        response = requests.get(url, headers=self.session.headers)
        response.raise_for_status()
        
        content = response.text.strip()
        self.cache.save('inputs', day, content)
        return content

    def save_solution(self, day: int, part: int, solution: str) -> None:
        """Save a solution for a specific day and part."""
        self.cache.save('solutions', day, solution, part)

    def get_solution(self, day: int, part: int) -> Optional[str]:
        """Get a previously saved solution."""
        return self.cache.load('solutions', day, part)

    def validate_session(self) -> bool:
        """Validate the current session."""
        return self.session.validate()

    def check_session_expiry(self) -> int:
        """Check days until session expiry."""
        return self.session.days_until_expiry()