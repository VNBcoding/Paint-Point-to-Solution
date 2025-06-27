# Filum.ai Solution Recommender Prototype

This prototype recommends Filum.ai features based on user-described business pain points. It uses semantic similarity via sentence embeddings to match user inputs with features from a knowledge base.

Demo Link: [Watch the demo video](https://drive.google.com/file/d/15-EtFai1WsFZB9o3gMQVwYKBhLBCyyHl/view?usp=sharing)
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
2. Navigate to the project directory:
   ```bash
   cd Pain-Point-to-Solution
3. Make sure `feature_knowledge_base.json` is placed in the same folder as `main.py`.  
4. Install dependencies:  
   ```bash
   pip install sentence-transformers
5. Run the app:
   ```bash
   python3 main.py
