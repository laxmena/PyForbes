# Lists Configurations
WEALTH_LIST = {
    "billionaires": {"verbose": "World richest", "category": "person"},
    "forbes-400": {"verbose": "American richest 400", "category": "person"},
    "hong-kong-billionaires": {
        "verbose": "Hong Kong richest 50",
        "category": "person",
    },
    "australia-billionaires": {
        "verbose": "Australia richest 50",
        "category": "person",
    },
    "china-billionaires": {
        "verbose": "China richest 400",
        "category": "person",
    },
    "taiwan-billionaires": {
        "verbose": "Taiwan richest 50",
        "category": "person",
    },
    "india-billionaires": {
        "verbose": "India richest 100",
        "category": "person",
    },
    "japan-billionaires": {"verbose": "Japan richest 50", "category": "person"},
    "africa-billionaires": {
        "verbose": "Africa richest 50",
        "category": "person",
    },
    "korea-billionaires": {"verbose": "Korea richest 50", "category": "person"},
    "malaysia-billionaires": {
        "verbose": "Malaysia richest 50",
        "category": "person",
    },
    "philippines-billionaires": {
        "verbose": "Philippines richest 50",
        "category": "person",
    },
    "singapore-billionaires": {
        "verbose": "Singapore richest 50",
        "category": "person",
    },
    "indonesia-billionaires": {
        "verbose": "Indonesia richest 50",
        "category": "person",
    },
    "thailand-billionaires": {
        "verbose": "Thailand richest 50",
        "category": "person",
    },
    "self-made-women": {
        "verbose": "American richest self-made women",
        "category": "person",
    },
    "richest-in-tech": {"verbose": "Tech richest", "category": "person"},
    "hedge-fund-managers": {
        "verbose": "Hedge Fund highest-earning",
        "category": "person",
    },
    "rtb": {"verbose": "Real-time world billionaires", "category": "person"},
    "rtrl": {"verbose": "Real-time American richest 400", "category": "person"},
    "top-wealth-advisors": {
        "verbose": "Top Wealth Advisors",
        "category": "person",
    },
}

POWER_LIST = {
    "powerful-people": {
        "verbose": "World's powerful people",
        "category": "person",
    },
    "power-women": {"verbose": "World's powerful women", "category": "person"},
}

# 30 under 30
THIRTY_UNDER_30 = {
    "30under30-hollywood-entertainment": {
        "verbose": "HOLLYWOOD & ENTERTAINMENT",
        "category": "person",
    },
    "30under30-big-money-startups": {
        "verbose": "Big Money",
        "category": "person",
    },
    "30under30-social-media": {
        "verbose": "SOCIAL MEDIA",
        "category": "person",
    },
    "30under30-media": {
        "verbose": "MEDIA",
        "category": "person",
    },
    "30under30-education": {
        "verbose": "EDUCATION",
        "category": "person",
    },
    "30under30-finance": {
        "verbose": "FINANCE",
        "category": "person",
    },
    "30under30-youngest": {
        "verbose": "Youngest",
        "category": "person",
    },
    "30under30-sports": {
        "verbose": "SPORTS",
        "category": "person",
    },
    "30under30-venture-capital": {
        "verbose": "VENTURE CAPITAL",
        "category": "person",
    },
    "30under30-energy": {
        "verbose": "ENERGY",
        "category": "person",
    },
    "30under30-art-style": {
        "verbose": "ART & STYLE",
        "category": "person",
    },
    "30under30-enterprise-technology": {
        "verbose": "ENTERPRISE TECHNOLOGY",
        "category": "person",
    },
    "30under30-music": {
        "verbose": "MUSIC",
        "category": "person",
    },
    "30under30-immigrants": {
        "verbose": "Immigrants",
        "category": "person",
    },
    "30under30-healthcare": {
        "verbose": "HEALTHCARE",
        "category": "person",
    },
    "30under30-manufacturing-industry": {
        "verbose": "MANUFACTURING & INDUSTRY",
        "category": "person",
    },
    "30under30-science": {
        "verbose": "SCIENCE",
        "category": "person",
    },
    "30under30-games": {
        "verbose": "GAMES",
        "category": "person",
    },
    "30under30-retail-ecommerce": {
        "verbose": "RETAIL & ECOMMERCE",
        "category": "person",
    },
    "30under30-food-drink": {
        "verbose": "FOOD & DRINK",
        "category": "person",
    },
    "30under30-social-impact": {
        "verbose": "SOCIAL IMPACT",
        "category": "person",
    },
    "30under30-consumer-technology": {
        "verbose": "CONSUMER TECHNOLOGY",
        "category": "person",
    },
    "30under30-marketing-advertising": {
        "verbose": "MARKETING & ADVERTISING",
        "category": "person",
    },
}

ORG_LISTS = {
    "global2000": {"category": "org", "verbose": "Global2000"},
    "sports-agencies": {"category": "org", "verbose": "Sports Agencies"},
    "fintech": {"category": "org", "verbose": "Fintech"},
    "best-management-consulting-firms": {
        "category": "org",
        "verbose": "Best Management-Consulting firms",
    },
    "top-charities": {"category": "org", "verbose": "Top Charities"},
    "canada-best-employers": {
        "category": "org",
        "verbose": "Canada Best Employers",
    },
    "best-employers": {"category": "org", "verbose": "Best Employers"},
    "best-midsize-employers": {
        "category": "org",
        "verbose": "Best Midsize Employers",
    },
    "best-employers-for-women": {
        "category": "org",
        "verbose": "Best Midsize Employers for Women",
    },
    "best-employers-for-new-grads": {
        "category": "org",
        "verbose": "Best Midsize Employers for New-Grads",
    },
    "top-regarded-companies": {
        "category": "org",
        "verbose": "Top regarded companies",
    },
    "world-best-employers": {
        "category": "org",
        "verbose": "World's best Employers",
    },
    "powerful-brands": {"category": "org", "verbose": "Powerful Brands"},
    "best-insurance-firms": {
        "category": "org",
        "verbose": "Best Insurance Firms",
    },
    "worlds-best-banks": {"category": "org", "verbose": "World's Best Banks"},
    "best-corporate-law-firms": {
        "category": "org",
        "verbose": "Best Corporate Law Firms",
    },
}

PERSON_LISTS = {**WEALTH_LIST, **THIRTY_UNDER_30, **POWER_LIST}
ALL_LISTS = {**PERSON_LISTS, **ORG_LISTS}
