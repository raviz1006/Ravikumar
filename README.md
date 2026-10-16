# 🇮🇳 Saathi AI (ಧ್ವನಿ ಸಾರಥಿ)
### *Voice-First Electoral Intelligence & Form Assistance for Every Citizen*
**Special Intensive Revision (SIR) 2026 &bull; Enumeration Form (EF) Assistant**

[![Llama 3.3 70B](https://img.shields.io/badge/LLM-Llama%203.3%2070B%20(Groq)-7C3AED?style=for-the-badge&logo=meta)](https://groq.com/)
[![Neo4j](https://img.shields.io/badge/Knowledge%20Graph-Neo4j%20Cypher-008CC1?style=for-the-badge&logo=neo4j)](https://neo4j.com/)
[![Voice](https://img.shields.io/badge/Voice-Web%20Speech%20%2B%20gTTS-10B981?style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
[![Pydantic](https://img.shields.io/badge/Validation-Pydantic%20v2-E11D48?style=for-the-badge&logo=pydantic)](https://pydantic.dev/)

---

## 🌟 Key New Features Implemented

### 1. 🛡️ Intelligent Semantic Relevancy Checking
When taking voice or text input, Saathi AI checks whether the citizen's response relates directly to the asked question:
* **Name Question (PART 1):** If the citizen says numbers (e.g. "72"), weather talk ("What's the temperature?"), or random queries, the AI politely flags:
  > *"ಕ್ಷಮಿಸಿ, ಇದು ಮತದಾರರ ಹೆಸರಿನಂತೆ ಕಾಣುತ್ತಿಲ್ಲ. ದಯವಿಟ್ಟು ನಿಮ್ಮ ಗುರುತಿನ ಚೀಟಿಯಲ್ಲಿರುವಂತೆ ನಿಮ್ಮ ಪೂರ್ಣ ಹೆಸರನ್ನು ತಿಳಿಸಿ."*  
  *(Spoken aloud in the citizen's selected language).*
* **Age Question (PART 3):** If no number or date is detected, the AI reminds the citizen to provide their age or birth year.
* **Previous SIR Question (PART 2A/2B):** Detects affirmative/negative intent and guides the citizen safely without guessing.

### 2. 🎙️ Robust Voice Input & Live Visual Feedback
* **Live Interim Transcription:** Displays spoken words in real time inside the input box as the citizen speaks.
* **Active Mic Wave Visualizer:** Audio orb turns pulsing red with a green/red live status dot so the user knows exactly when the microphone is recording.
* **Noise Filter:** Prevents blank inputs or accidental mic clicks from skipping questions.

### 3. 🌐 Strict Native Language Audio Output
* If **Kannada (ಕನ್ನಡ)** is selected: Every question, explanation, relevancy alert, and final read-back is synthesized strictly in **Kannada (`kn-IN`)**.
* If **English** is selected: Spoken in natural Indian English (`en-IN`).
* If **Hindi (हिन्दी)** is selected: Spoken in Hindi (`hi-IN`).

### 4. 📄 1-to-1 Mapping to Official SIR 2026 Enumeration Form (EF)
Directly reflects the official ECI / State CEO Enumeration Form flyer:
* **PART 1:** Elector Identification & Photo, AC No. 154 - Malleshwaram, BLO contact.
* **PART 2A:** Elector's Previous SIR Details (Name, EPIC, Previous AC).
* **PART 2B:** Ancestral Lineage (Father/Mother/Grandparent previous roll).
* **PART 3:** Family Details (DOB, Mobile, Aadhaar, Parent/Spouse names).
* **Official Fallback Rule:** *"If details not found in previous SIR, only Part 3 may be filled and submitted to the BLO with prescribed documents."*
* **Schedule & Zero Fee:** BLO House Visits from **30th June to 08th August 2026** &bull; Helpline **1950** &bull; ECI charges zero fee.

---

## 🚀 How to Launch the Prototype

### Option 1: Standalone Web Prototype (Recommended)
Double-click [`run_prototype.bat`](file:///C:/Users/Ravikumar%20V/.gemini/antigravity/scratch/sir-saathi-ai/run_prototype.bat) or open [`index.html`](file:///C:/Users/Ravikumar%20V/.gemini/antigravity/scratch/sir-saathi-ai/index.html) in your browser.
* Use the **"⚠️ Test Unrelated Voice"** chip to see the AI detect an irrelevant answer and politely correct the user in their chosen language.
* Click **"📢 Read Aloud"** to hear the completed draft in Kannada, English, or Hindi.

### Option 2: Python + Streamlit Chat Interface
```powershell
cd "C:\Users\Ravikumar V\.gemini\antigravity\scratch\sir-saathi-ai"
.\run_app.bat
```
Visit `http://localhost:8501`.
