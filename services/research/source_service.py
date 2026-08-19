from urllib.parse import urlparse
from models.research.research import ResearchSource

GOVERNMENT_DOMAINS = (
    ".go.kr",
    ".gov",
)

ACADEMIC_DOMAINS = (
    ".ac.kr",
    ".edu"
)

WIKI_DOMAIN = (
    "wikipedia.org",
    "namu.wiki"
)

def get_domain(url: str) -> str:
    try:
        domain = urlparse(url).netloc.lower()
        if domain.startswith("www."):
            domain = domain[4:]
            
        return domain
    
    except ValueError:
        return ""
    

def classify_source(domain: str) -> tuple[str, int]:
    if domain.endswith(GOVERNMENT_DOMAINS):
        return "goverment", 1
    
    if domain.endswith(ACADEMIC_DOMAINS):
        return "academic", 2
    
    if any(
        wiki_domain in domain
        for wiki_domain in WIKI_DOMAIN
    ):
        return "wiki", 4
    
    return "other", 3


def create_research_source(url: str) -> ResearchSource:
    domain = get_domain(url)
    source_type, priority = classify_source(domain)
    
    return ResearchSource(
        url = url,
        domain = domain,
        source_type = source_type,
        priority = priority
    )
    
    
def sort_sources(sources: list[ResearchSource]) -> list[ResearchSource]:
    return sorted(
        sources,
        key = lambda source: (
            source.priority,
            source.domain,
            source.url
        )
    )