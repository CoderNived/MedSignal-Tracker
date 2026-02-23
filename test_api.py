import requests

base_url = "https://clinicaltrials.gov/api/v2"

params = {
    "query.term": "paracetamol",
    "pageSize": 25,
    "sort": "ResultsFirstPostDate"
}

response = requests.get(f"{base_url}/studies", params=params)

if response.status_code != 200:
    print("API Error:", response.status_code)
    exit()

studies = response.json().get("studies", [])

aggregated = {}

for study in studies:

    if not study.get("hasResults"):
        continue

    adverse_module = (
        study.get("resultsSection", {})
             .get("adverseEventsModule", {})
    )

    serious_events = adverse_module.get("seriousEvents", [])

    for event in serious_events:

        stats = event.get("stats", [])
        if not stats:
            continue

        num_affected = stats[0].get("numAffected", 0)
        num_at_risk = stats[0].get("numAtRisk", 0)

        if num_at_risk == 0:
            continue

        probability = num_affected / num_at_risk
        name = event.get("term", "Unknown")

        aggregated.setdefault(name, []).append(probability)

# Final aggregation
results = [
    {
        "side_effect_name": name,
        "average_probability": sum(probs) / len(probs)
    }
    for name, probs in aggregated.items()
]

# Filter meaningful signals
filtered = [r for r in results if r["average_probability"] > 0.01]

print(filtered)