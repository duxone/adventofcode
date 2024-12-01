from pathlib import Path
import json
from datetime import datetime
import hashlib
from typing import Optional, Dict

class AdventCache:
    """Handles caching of problems, inputs, and solutions. Serves to reduce load on AoC server"""
    
    def __init__(self):
        self.cache_dir = Path(".aoc_cache")
        self.cache_structure = {
            'problems': self.cache_dir / 'problems',
            'inputs': self.cache_dir / 'inputs',
            'session': self.cache_dir / 'session',
            'solutions': self.cache_dir / 'solutions'
        }
        self._initialize_cache_structure()

    def _initialize_cache_structure(self) -> None:
        """Create cache directory structure."""
        for directory in self.cache_structure.values():
            directory.mkdir(parents=True, exist_ok=True)

    def _cache_key(self, day: int, part: Optional[int] = None) -> str:
        """Generate a cache key for a specific day and part."""
        return f"day_{day}" + (f"_part_{part}" if part else "")

    def _get_cache_path(self, category: str, day: int, part: Optional[int] = None) -> Path:
        """Get the full path for a cache file."""
        return self.cache_structure[category] / f"{self._cache_key(day, part)}.json"

    def save(self, category: str, day: int, content: str, part: Optional[int] = None) -> None:
        """Save content to cache with metadata."""
        cache_data = {
            'content': content,
            'timestamp': datetime.now().isoformat(),
            'day': day,
            'part': part,
            'checksum': hashlib.md5(content.encode()).hexdigest()
        }
        
        cache_path = self._get_cache_path(category, day, part)
        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump(cache_data, f, indent=2)

    def load(self, category: str, day: int, part: Optional[int] = None) -> Optional[str]:
        """Load content from cache if it exists and is valid."""
        cache_path = self._get_cache_path(category, day, part)
        
        if cache_path.exists():
            with open(cache_path, 'r', encoding='utf-8') as f:
                cache_data = json.load(f)
                
                # Verify content integrity
                current_checksum = hashlib.md5(cache_data['content'].encode()).hexdigest()
                if current_checksum == cache_data['checksum']:
                    return cache_data['content']
        return None

    def clear(self, category: Optional[str] = None, day: Optional[int] = None) -> None:
        """Clear cache entries."""
        if category and day:
            cache_path = self._get_cache_path(category, day)
            if cache_path.exists():
                cache_path.unlink()
        elif category:
            for file in self.cache_structure[category].glob('*.json'):
                file.unlink()
        else:
            for directory in self.cache_structure.values():
                for file in directory.glob('*.json'):
                    file.unlink()