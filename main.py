import json
from sentence_transformers import SentenceTransformer, util

# Load the knowledge base
with open("feature_knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)["features"]

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_relevance(user_input, feature):
    # Combine user input into a single context string
    user_text = " ".join([
        user_input["pain_point"],
        " ".join(user_input["channel"]),
        " ".join(user_input["industry"]),
        " ".join(user_input["company_size"]),
        " ".join(user_input["customer_segment"])
    ])

    # Combine feature details into a single contextt string 
    feature_text = " ".join([
        feature["name"],
        feature["description"],
        " ".join(feature["pain_points_addressed"]),
        " ".join(feature["keywords"]),
        " ".join(feature.get("channels_supported", [])),
        " ".join(feature.get("industries", [])),
        " ".join(feature.get("company_sizes", [])),
        " ".join(feature.get("customer_segments", []))
    ])

    # Compute cosine similarity between feature details and user input
    user_embedding = model.encode(user_text, convert_to_tensor=True)
    feature_embedding = model.encode(feature_text, convert_to_tensor=True)
    similarity = util.cos_sim(user_embedding, feature_embedding).item()
    return round(similarity, 3)

def find_relevant_features(user_input, top_n=3):
    scored = []
    for feature in knowledge_base:
        score = compute_relevance(user_input, feature)
        scored.append({
            "feature_name": feature["name"],
            "description": feature["description"],
            "relevance_score": score,
            "more_info_url": feature["more_info_url"]
        })

    # Sort by highest relevance score
    sorted_results = sorted(scored, key=lambda x: x["relevance_score"], reverse=True)
    return {
        "pain_point": user_input["pain_point"],
        "suggested_solutions": sorted_results[:top_n]
    }

def get_user_input():
    pain_point = input("Describe the business challenge (pain point): ")

    channel = input("Channels (comma-separated): ").split(",")
    channel = [ch.strip() for ch in channel if ch.strip()]

    industry = input("Industries (comma-separated): ").split(",")
    industry = [ind.strip() for ind in industry if ind.strip()]

    company_size = input("Company sizes (comma-separated - Small, Medium, Large): ").split(",")
    company_size = [size.strip() for size in company_size if size.strip()]

    customer_segment = input("Customer segments (comma-separated - B2C, B2B): ").split(",")
    customer_segment = [seg.strip() for seg in customer_segment if seg.strip()]

    return {
        "pain_point": pain_point,
        "channel": channel,
        "industry": industry,
        "company_size": company_size,
        "customer_segment": customer_segment
    }

if __name__ == "__main__":
    print("Welcome to the Filum.ai Solution Recommender!")
    while True:
        user_data = get_user_input()
        if not user_data["pain_point"]:
            print("Pain point description is required. Please try again.")
            continue

        results = find_relevant_features(user_data)

        print("\nSuggested Solutions:")
        for i, sol in enumerate(results["suggested_solutions"], start=1):
            print("\n")
            print(f"{i}. Feature: {sol['feature_name']}")
            print(f"   Description: {sol['description']}")
            print(f"   Relevance Score: {sol['relevance_score']}")
            print(f"   More info: {sol['more_info_url']}")

        checkout = input("\nDo you want to enter another pain point? (yes/no): ").strip().lower()
        if checkout not in ("yes", "y"):
            print("Goodbye!")
            break
