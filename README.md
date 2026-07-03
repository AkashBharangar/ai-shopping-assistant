# 🛒 AI Shopping Assistant

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Groq](https://img.shields.io/badge/LLM-Groq-purple)
![LangChain](https://img.shields.io/badge/Framework-LangChain-green)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![Docker](https://img.shields.io/badge/Container-Docker-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

An AI-powered shopping assistant that helps users make informed purchasing decisions by comparing products, analyzing customer reviews, and generating personalized recommendations using Large Language Models (LLMs).

---

# ✨ Features

* 🔍 Search products from an external product API
* ⚖️ Compare multiple products using AI
* 📝 AI-powered customer review analysis
* ✅ Extract Pros & Cons from reviews
* 🤖 Personalized product recommendations
* 🧠 End-to-end shopping pipeline
* 🎨 Professional Streamlit interface
* 🐳 Dockerized for easy deployment

---

# 📸 Demo

> Add screenshots or a short demo GIF here.

Example:

```
assets/demo.gif
```

or

```
assets/homepage.png
```

---

# 🏗️ Architecture

```
                    User

                      │

                      ▼

               Streamlit UI

                      │

                      ▼

           shopping_pipeline.py

        ┌────────────┼────────────┐
        ▼            ▼            ▼

 Product Search  Review AI  Product Compare

        └────────────┼────────────┘
                     ▼

        Recommendation Engine

                     ▼

                Groq LLM
```

---

# 🧠 Tech Stack

| Category         | Technology         |
| ---------------- | ------------------ |
| Language         | Python             |
| LLM              | Groq               |
| Framework        | LangChain          |
| Frontend         | Streamlit          |
| Containerization | Docker             |
| Prompting        | Prompt Engineering |
| Data             | JSON               |

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
│── README.md
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
├── data/
│   └── reviews.json
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/ai-shopping-assistant.git

cd ai-shopping-assistant
```

---

## 2. Create Virtual Environment

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

## 4. Create `.env`

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
```

---

## 5. Run the Application

```bash
streamlit run app.py
```

---

# 🐳 Run with Docker

Build the image

```bash
docker build -t ai-shopping-assistant .
```

Run the container

```bash
docker run -p 8501:8501 --env-file .env ai-shopping-assistant
```

Open

```
http://localhost:8501
```

---

# ⚙️ How It Works

### Step 1 — Product Search

The application searches for products based on the user's query.

↓

### Step 2 — Review Analysis

Customer reviews are summarized using an LLM to extract:

* Summary
* Pros
* Cons
* Overall sentiment

↓

### Step 3 — Product Comparison

The selected products are compared using AI, highlighting strengths and weaknesses.

↓

### Step 4 — Recommendation

The assistant recommends the most suitable product based on the user's preferences and the analyzed product data.

---

# 📖 Example Workflow

```
Search Product

↓

Compare Products

↓

Analyze Reviews

↓

AI Recommendation

↓

Best Product
```

---

# 📌 Skills Demonstrated

* Large Language Models (LLMs)
* LangChain
* Prompt Engineering
* AI Pipelines
* Structured JSON Outputs
* Service-Oriented Architecture
* Streamlit
* Docker
* Environment Variable Management
* Python Project Organization

---

# 🔮 Future Improvements

* Real e-commerce API integration
* Live pricing data
* Authentication
* Wishlist support
* Shopping history
* Multi-language support

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Akash Bharangar**

AI Engineer | GenAI Engineer

* GitHub: https://github.com/akashbharangar
* LinkedIn: https://www.linkedin.com/in/akash-bharangar-757440186/

If you found this project useful, consider giving it a ⭐.
