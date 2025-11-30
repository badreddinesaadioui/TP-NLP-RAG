# TP - NLP RAG Project

## Team Members
- Ghita Nahli
- Abderrahmane Salehi
- Badreddine Saadioui
- Oussama Hajji

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/badreddinesaadioui/TP-NLP-RAG.git
   cd TP-NLP-RAG
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **API Key Setup:**
   - For Streamlit: Create `.streamlit/secrets.toml` and add:
     ```toml
     OPENAI_API_KEY = "your_key_here"
     ```
   - For CLI: Create a `.env` file in the root directory and add:
     ```env
     OPENAI_API_KEY=your_key_here
     ```

## Usage

### Run Streamlit App (Chatbot)
```bash
streamlit run app.py
```

### Run CLI Tool
- **Index Documents:**
  ```bash
  python cli.py --index
  ```
- **Ask a Question:**
  ```bash
  python cli.py --query "Your question here"
  ```
