# 💬 Sentiment‑Aware Multilingual Support Chatbot

Customer support chatbot that understands sentiment and responds in the user’s language using a retrieval‑based system.

---

## 🚀 Features

- **Sentiment‑aware responses**  
  The chatbot detects whether the user is positive, negative, or neutral, and adapts the tone of the reply accordingly.

- **Multilingual support**  
  The bot supports:
  - English (en)
  - Hindi (hi)
  - Spanish (es)
  - French (fr)

  It:
  - detects the user’s language,
  - translates the input to English for search,
  - retrieves the best answer,
  - and translates the reply back to the user’s language.

- **Advanced language processing (Task 6)**  
  The chatbot now includes several **advanced language‑aware features**:

  - **Multilingual query expansion**  
    The user’s message is enriched with language‑aware hints (e.g., `in Hindi customer support query`) before being passed to the retrieval engine, improving multilingual understanding.

  - **Language‑specific response templates**  
    Replies are generated using different templates for each language, so the style and tone match the user’s language, instead of just translating raw English.

  - **Robust translation fallbacks**  
    If translation fails, the bot gracefully falls back to showing the original English reply, preventing silent crashes or truncated messages.

- **Debug / matches panel**  
  You can inspect:
  - detected language,
  - sentiment label and intensity,
  - the retrieved “top match”,
  - and the bot’s raw English reply.

---

## 📦 How It Works

1. **User input**  
   The user types a message (e.g., `मेरा ऑर्डर अभी तक नहीं आया` or `Mon colis n'est pas encore arrivé`).

2. **Language detection**  
   The bot uses `langdetect` to detect the language code (`en`, `hi`, `es`, `fr`) and shows it in the UI.

3. **Translation to English**  
   The input is translated to English (via `deep_translator`) so the retrieval system can work in a single language.

4. **Sentiment + retrieval**  
   - Sentiment is computed.  
   - The retrieval engine searches an FAISS‑indexed knowledge base for the best matching instruction‑response pair.

5. **Response generation**  
   The bot:
   - uses language‑aware templates to phrase the reply,
   - and then translates it back to the user’s language.

6. **Display**  
   The UI shows:
   - the user message,  
   - the bot’s reply,  
   - and a caption: `Detected language: ...`.

---

## 🧪 Example Questions (for screenshots)

You can test it with:

- English  
  - `My order hasn't arrived yet`  
  - `Where is my order?`  
  - `I'm very happy with your service`  
  - `I'm angry about the delay`

- French  
  - `Bonjour`  
  - `Mon colis n'est pas encore arrivé`  
  - `Où est ma commande ?`  
  - `Je suis très mécontent`

- Spanish  
  - `Hola`  
  - `Mi pedido no ha llegado`  
  - `¿Dónde está mi pedido?`  
  - `Estoy muy decepcionado`

- Hindi  
  - `हैलो`  
  - `मेरा ऑर्डर अभी तक नहीं आया`  
  - `मेरा पैकेज अभी तक कहाँ है?`  
  - `मैं बहुत नाराज़ हूँ`

You can use these as **assets / screenshots** in your GitHub repo.

---

## 🛠️ Installation

1. Clone this repo  
   ```bash
   git clone https://github.com/Rishika-AQRS/task6-support-chatbot.git
   cd task6-support-chatbot
   ```

2. Create a virtual environment (recommended)  
   ```bash
   python -m venv venv
   venv\Scripts\activate  # on Windows
   source venv/bin/activate  # on Linux/macOS
   ```

3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app  
   ```bash
   streamlit run app.py
   ```

---

## 📚 Notes

- The bot **does not retrain the model**; it relies on a pre‑built FAISS index stored in the `artifacts/` folder.  
- For **Task 6**, the focus is on **multilingual understanding and generation**, not on changing the core retrieval index.

---

## 📸 Assets

You can find example screenshots for:
- English queries,
- French queries,
- Spanish queries,
- Hindi queries,
in the `assets/` folder.


## 📦 Data & Index

- The chatbot uses a **local FAISS index** stored in the `artifacts/` folder.
- This folder is **not included in the repo** because it is large and environment‑specific.
- To run the app:
  1. Make sure you already have your `artifacts/` folder from your local environment.
  2. Copy it into the project root before running:
     ```bash
     streamlit run app.py
     ```