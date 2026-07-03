# 🛒 AI Shopping Assistant

<p align="center">
  <img src="assets/banner.png" alt="AI Shopping Assistant Banner" width="100%">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Groq](https://img.shields.io/badge/LLM-Groq-purple)
![LangChain](https://img.shields.io/badge/Framework-LangChain-green)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![Docker](https://img.shields.io/badge/Container-Docker-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

</p>

<p align="center">
<b>AI-powered shopping assistant that compares products, analyzes customer reviews, and delivers personalized recommendations using Groq, LangChain, and Streamlit.</b>
</p>

---

## ✨ Features

* 🔍 Search products from a product API
* ⚖️ AI-powered product comparison
* 📝 Customer review summarization
* ✅ Automatic Pros & Cons extraction
* 📊 Sentiment analysis
* 🤖 Personalized AI recommendations
* 🧠 End-to-end shopping pipeline
* 🎨 Professional Streamlit UI
* 🐳 Docker support

---

# 🎬 Demo

<p align="center">
<img src="assets/demo.gif" width="90%">
</p>

---

# 📸 Screenshots

| Home                 | Product Comparison         |
| -------------------- | -------------------------- |
| ![](assets/home.png) | ![](assets/comparison.png) |

| Review Analysis        | Recommendation                 |
| ---------------------- | ------------------------------ |
| ![](assets/review.png) | ![](assets/recommendation.png) |

---

# 🏗 Architecture

```text
                           User

                             │

                             ▼

                     Streamlit UI

                             │

                             ▼

                shopping_pipeline.py

        ┌──────────────┼──────────────┐
        ▼              ▼              ▼

 Product Search   Review Analysis   Comparison

        └──────────────┼──────────────┘
                       ▼

            Recommendation Engine

                       ▼

                 Groq LLM (LangChain)
```

---

# ⚡ Workflow

```text
Search Product
        │
        ▼
Fetch Products
        │
        ▼
Analyze Reviews
        │
        ▼
Compare Products
        │
        ▼
Generate Recommendation
        │
        ▼
Display Best Product
```

---

# 🧠 Tech Stack

| Category         | Technology         |
| ---------------- | ------------------ |
| Language         | Python 3.11        |
| LLM              | Groq               |
| Framework        | LangChain          |
| Frontend         | Streamlit          |
| Containerization | Docker             |
| Prompting        | Prompt Engineering |
| Data Format      | JSON               |

---

# 📂 Project Structure

```text
ai-shopping-assistant/

│── app.py
│── config.py
│── llm.py
│── chains.py
│── prompts.py
│── requirements.txt
│── Dockerfile
│── .dockerignore
│── .env.example
│── README.md
│── LICENSE
│
├── assets/
│   ├── banner.png
│   ├── demo.gif
│   ├── home.png
│   ├── comparison.png
│   ├── review.png
│   └── recommendation.png
│
├── services/
│   ├── product_search.py
│   ├── product_compare.py
│   ├── review_summarizer.py
│   ├── recommendation.py
│   └── shopping_pipeline.py
│
├── ui/
│   ├── sidebar.py
│   ├── product_card.py
│   ├── comparison_tab.py
│   ├── review_tab.py
│   ├── recommendation_tab.py
│   └── assistant_mode.py
│
└── data/
    └── reviews.json
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/akashbharangar/ai-shopping-assistant.git

cd ai-shopping-assistant
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file using `.env.example`.

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
```

---

## 5. Run the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# 🐳 Docker

Build the Docker image:

```bash
docker build -t ai-shopping-assistant .
```

Run the container:

```bash
docker run -p 8501:8501 --env-file .env ai-shopping-assistant
```

---

# 📌 Example Use Case

Suppose a user wants to buy a gaming laptop.

The assistant:

* Searches available products
* Analyzes customer reviews
* Summarizes strengths and weaknesses
* Compares multiple products
* Generates a personalized recommendation

All powered by an LLM.

---

# 💡 Skills Demonstrated

* Generative AI
* Large Language Models (LLMs)
* LangChain
* Groq API
* Prompt Engineering
* AI Workflow Orchestration
* Product Recommendation Systems
* Review Analysis
* Structured JSON Outputs
* Streamlit Application Development
* Docker
* Python Project Architecture

---

# 🔮 Future Scope

* Real e-commerce API integration
* Multi-vendor product search
* Authentication
* Wishlist support
* Purchase history
* Multi-language support

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

See the **LICENSE** file for details.

---

# 👨‍💻 Author

### Akash Bharangar

**AI Engineer | GenAI Engineer**

* GitHub: https://github.com/akashbharangar
* LinkedIn: https://www.linkedin.com/in/akash-bharangar-757440186/

---

<p align="center">
⭐ If you found this project helpful, consider starring the repository!
</p>
