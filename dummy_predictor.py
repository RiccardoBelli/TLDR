from enum import Enum


class Category(Enum):
    BIG_TECH = "BIG TECH & STARTUPS"
    SCIENCE_FUTURISTIC_TECH = "SCIENCE & FUTURISTIC TECHNOLOGY"
    PROGRAMMING_DESIGN_DATA_SCIENCE = "PROGRAMMING, DESIGN & DATA SCIENCE"

    def __repr__(self):
        return f"{self.value}"


class DummyPredictor:
    def __init__(self):
        self.keywords_big_tech = [
            "Google", "Apple", "Twitter", "Microsoft", "Amazon", "Facebook", "Meta", "Elon Musk", "iPhone",
            "Tesla", "SpaceX", "Netflix", "Uber", "Lyft", "Airbnb", "startup", "funding", "acquisition", "IPO",
            "Series A", "Palo Alto", "Cybertruck", "ChatGPT", "Bing", "AI", "search engine", "Pro Max", "Ultra",
            "Sundar Pichai", "Edge", "browser", "GPT-4", "conversational", "Bard", "rival", "CEO", "BIG", "TECH"
        ]

        self.keywords_science_futuristic = [
            "physics", "astrophysics", "nuclear", "fusion", "plasma", "quantum", "energy", "nanotechnology",
            "biotechnology", "genetics", "crispr", "synthetic", "biology", "medical", "device", "climate",
            "environment", "astronomy", "space", "exploration", "satellite", "mars", "lunar", "moon", "telescope",
            "hubble", "rover", "dark", "matter", "artificial", "intelligence", "neural", "network", "deep", "learning",
            "machine", "superconductor", "battery", "solar", "wind", "power", "transmission", "wireless", "infrared",
            "laser", "optical", "semiconductor", "material", "3d", "printing", "graphene", "carbon", "nanotube",
            "material", 
        ]

        self.keywords_programming_design = [
            "TypeScript", "Rust", "SQLite", "distributed", "relational", "database",
            "CSS", "HTML", "utility", "framework", "React", "web application", "DevOps",
            "API", "SDK", "chat", "activity feeds", "Python", "command-line", "JSON",
            "parsing", "software", "developer", "programming", "data science", "machine learning",
            "GitHub", "repo", "web development", "design"
        ]

    def predict(self, sentence):
        scores = [
            (Category.BIG_TECH, self._get_score(sentence, self.keywords_big_tech)),
            (Category.SCIENCE_FUTURISTIC_TECH, self._get_score(sentence, self.keywords_science_futuristic)),
            (Category.PROGRAMMING_DESIGN_DATA_SCIENCE, self._get_score(sentence, self.keywords_programming_design))
        ]

        return scores

    @staticmethod
    def _get_score(sentence, keywords):
        count = sum([1 for keyword in keywords if keyword.lower() in sentence.lower()])
        return count / len(keywords)
