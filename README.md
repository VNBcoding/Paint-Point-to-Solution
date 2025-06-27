# Filum.ai Solution Recommender Prototype

This prototype recommends Filum.ai features based on user-described business pain points. It uses semantic similarity via sentence embeddings to match user inputs with features from a knowledge base.

---

## Features

- Accepts multiple channels and industries as input arrays.
- Matches pain point, channels, industries, company size, and industries.
- Ranks and returns top relevant Filum.ai features.
- Interactive command-line interface.

---

## Setup & Run Instructions

### Prerequisites

- Python 3.7 or later
- Internet connection (to download the model on first run)

### Installation

1. Clone or download this repository.
2. Make sure `feature_knowledge_base.json` is placed in the same folder as `main.py`.
3. Install dependencies:
    pip install sentence-transformers
4. Run the app
    python3 main.py