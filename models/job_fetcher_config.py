from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class JobScraperConfig:
    site_names: List[str] = field(default_factory=lambda: ["linkedin"])
    search_term: str = "software engineer"
    location: Optional[str] = "Ankara"
    results_wanted: int = 1
    hours_old: int = 24
    linkedin_fetch_description: bool = False