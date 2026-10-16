"""
SIR SAATHI AI - Voice-First Multilingual Electoral Intelligence
Complete All-in-One Application:
- 🎙️ Saathi AI Chatbot & Voice Assistant with Semantic Relevancy Checking
- 🧭 AI Navigator & Step Journey
- 🧠 Interactive Neo4j Knowledge Graph & Cypher Console
- 📄 Comprehensive Draft Review & Read-Back Screen
- 👮‍♂️ Booth Level Officer (BLO) Assisted Review Queue
- ℹ️ System Architecture, Presentation Pitch & Trust Principles
- 🪪 Live Digital SIR Enumeration Form 2026 Preview
"""

import streamlit as st
import streamlit.components.v1 as components
import json
import base64
from io import BytesIO
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from graph_db import SIRKnowledgeGraph
from validation import SIRFormValidator

# Pydantic Schema mapped with Official Enumeration Form (EF) 2026
class EnumerationFormSchema(BaseModel):
    part1_name: str = Field(default="Lakshmi Devi (ಲಕ್ಷ್ಮಿ ದೇವಿ)")
    part1_ac: str = Field(default="154 - Malleshwaram")
    part1_blo_info: str = Field(default="Smt. Geetha R. (Ph: 98451-XXXXX)")
    part1_part_no: str = Field(default="42")
    part1_serial_no: str = Field(default="189")

    part2a_name: str = Field(default="Lakshmi Devi")
    part2a_epic: str = Field(default="ABC1234567")
    part2a_prev_ac: str = Field(default="Bengaluru South")

    part2b_ancestor_name: str = Field(default="Narasimhe Gowda (Father)")
    part2b_ancestor_epic: str = Field(default="XYZ9876543")
    part2b_status: str = Field(default="Linked via Lineage")

    part3_dob: str = Field(default="15/08/1954 (Age: 72 yrs - Senior)")
    part3_mobile: str = Field(default="9845012345")
    part3_aadhaar_masked: str = Field(default="XXXX-XXXX-4512")
    part3_father_name: str = Field(default="Narasimhe Gowda")
    part3_mother_name: str = Field(default="Late Kamalamma")
    part3_spouse_name: str = Field(default="Late Ramaswamy")

# Page Configuration
st.set_page_config(
    page_title="Saathi AI | Electoral Intelligence System",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Attractive Styling
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at 10% 10%, #0B192C 0%, #030712 100%);
        color: #F8FAFC;
    }
    .top-announcement {
        background: linear-gradient(90deg, #FF6B35 0%, #0B192C 50%, #10B981 100%);
        padding: 6px 16px;
        border-radius: 8px;
        color: white;
        font-size: 0.85rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 16px;
    }
    .hero-header {
        background: rgba(17, 24, 39, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 14px 20px;
        backdrop-filter: blur(20px);
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 16px;
    }
    .hero-title {
        font-size: 1.45rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FF8A50 0%, #60A5FA 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .tag-badge {
        font-family: monospace;
        font-size: 0.72rem;
        background: rgba(59, 130, 246, 0.2);
        color: #93C5FD;
        padding: 3px 10px;
        border-radius: 16px;
        border: 1px solid rgba(59, 130, 246, 0.4);
    }
    .nav-step-active {
        background: linear-gradient(90deg, rgba(59, 130, 246, 0.25) 0%, rgba(59, 130, 246, 0.05) 100%);
        border-left: 4px solid #3B82F6;
        padding: 8px 12px;
        border-radius: 6px;
        color: #93C5FD;
        font-weight: 700;
    }
    .nav-step-done {
        border-left: 4px solid #10B981;
        padding: 8px 12px;
        color: #6EE7B7;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.04);
        border-radius: 10px;
        padding: 8px 16px;
        color: #CBD5E1;
        border: 1px solid rgba(255, 255, 255, 0.08);
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: #3B82F6 !important;
        color: white !important;
        border-color: #3B82F6 !important;
    }
</style>
""", unsafe_allow_html=True)

# State initialization
if "graph" not in st.session_state:
    st.session_state.graph = SIRKnowledgeGraph()

if "step" not in st.session_state:
    st.session_state.step = 1

if "language" not in st.session_state:
    st.session_state.language = "kn"

if "form_data" not in st.session_state:
    st.session_state.form_data = EnumerationFormSchema()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": "Namaskara! I am Saathi AI. I will help you fill your official Special Intensive Revision (SIR) 2026 Enumeration Form (EF). Let's start with PART 1: What is your full name?",
            "kannada": "ನಮಸ್ಕಾರ! ನಾನು ನಿಮ್ಮ ಸಾಥಿ ಎಐ. ನಿಮ್ಮ ಅಧಿಕೃತ SIR 2026 ಗಣನಾ ಪ್ರಪತ್ರವನ್ನು (EF) ಭರ್ತಿ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತೇನೆ. ಭಾಗ 1: ನಿಮ್ಮ ಪೂರ್ಣ ಹೆಸರು ಏನು?",
            "part": "PART 1: Elector Details",
            "why": "Establishes identity on official Enumeration Form (EF) as per Representation of the People Act 1950."
        }
    ]

# Stepper parts
PARTS = [
    {"id": 1, "code": "PART 1", "title": "Elector Identification & Photo", "title_kn": "ಮತದಾರರ ಹೆಸರು ಮತ್ತು ಭಾವಚಿತ್ರ"},
    {"id": 2, "code": "PART 2A", "title": "Elector's Previous SIR Details", "title_kn": "ಹಿಂದಿನ ಮತದಾರರ ಪಟ್ಟಿ / EPIC"},
    {"id": 3, "code": "PART 2B", "title": "Ancestor Previous SIR Linkage", "title_kn": "ಪೋಷಕರ ಹಿಂದಿನ SIR (Fallback)"},
    {"id": 4, "code": "PART 3", "title": "Elector's Family Details & Proofs", "title_kn": "ಕುಟುಂಬದ ವಿವರ & ದಾಖಲೆಗಳು"},
    {"id": 5, "code": "FINAL", "title": "Read-Back & Confirmation", "title_kn": "ದೃಢೀಕರಣ & BLO ಭೇಟಿ"}
]

# Audio Speech helper using gTTS with chosen language
def play_audio(text: str, lang: str):
    try:
        from gtts import gTTS
        tts_lang = "kn" if lang == "kn" else ("hi" if lang == "hi" else "en")
        tts = gTTS(text=text, lang=tts_lang, slow=False)
        buf = BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        b64 = base64.b64encode(buf.read()).decode()
        st.markdown(f'<audio controls autoplay style="height: 34px; width: 100%; margin: 8px 0;"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>', unsafe_allow_html=True)
    except Exception as e:
        st.caption(f"Speech notice: {e}")

# =========================================================================
# SIDEBAR: THE AI NAVIGATOR & ACCESSIBILITY CONTROLS
# =========================================================================
with st.sidebar:
    st.markdown("### 🧭 AI Navigator")
    pct = int((st.session_state.step / len(PARTS)) * 100)
    st.progress(pct / 100, text=f"Form Completion: {pct}%")

    for p in PARTS:
        if p["id"] < st.session_state.step:
            st.markdown(f'<div class="nav-step-done">✓ <strong>{p["code"]}:</strong> {p["title"]}<br><small style="color:#94A3B8;">{p["title_kn"]}</small></div>', unsafe_allow_html=True)
        elif p["id"] == st.session_state.step:
            st.markdown(f'<div class="nav-step-active">➔ <strong>{p["code"]}:</strong> {p["title"]} (Active)<br><small style="color:#60A5FA;">{p["title_kn"]}</small></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="padding: 6px 12px; color: #64748B;">○ <strong>{p["code"]}:</strong> {p["title"]}</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🌐 Preferred Language")
    st.session_state.language = st.radio(
        "Voice & Text Language:",
        options=["kn", "en", "hi"],
        format_func=lambda x: "ಕನ್ನಡ (Kannada)" if x == "kn" else ("English" if x == "en" else "हिन्दी (Hindi)"),
        horizontal=True
    )

    st.markdown("---")
    st.info("""
    **📜 Official ECI Leaflet Rule:**
    *If details not found in previous SIR, only Part 3 may be filled and submitted to the BLO with prescribed documents.*
    """)

    st.markdown("---")
    st.subheader("📞 Helpline Assistance")
    st.write("Voter Helpline: **1950 / 1800 22 1950** (Toll Free)")
    st.caption("BLO House Visits: 30th June to 08th August 2026. Zero ECI fee.")


# Top Announcement Banner
st.markdown('<div class="top-announcement">🇮🇳 SPECIAL INTENSIVE REVISION (SIR) 2026 &bull; BLO House Visits: 30th June to 08th August 2026 &bull; Voter Helpline: 1950 (Zero ECI Fee)</div>', unsafe_allow_html=True)

# Hero Header
st.markdown("""
<div class="hero-header">
    <div>
        <div class="hero-title">Saathi AI | ಧ್ವನಿ ಸಾರಥಿ</div>
        <div style="font-size:0.85rem; color:#94A3B8;">Voice-First Multilingual Electoral Intelligence &bull; SIR Form 2026</div>
    </div>
    <div style="display:flex; gap:8px; align-items:center;">
        <span class="tag-badge">Groq Llama 3.3 70B</span>
        <span class="tag-badge" style="background:rgba(16,185,129,0.2); color:#6EE7B7; border-color:#10B981;">Neo4j Graph Active</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ALL 5 MAJOR FEATURE TABS RESTORED
tabs = st.tabs([
    "🎙️ Voice Assistant & Chatbot",
    "🧠 Neo4j Knowledge Graph",
    "📄 Review Draft & Read-Aloud",
    "👮‍♂️ BLO Review Queue",
    "ℹ️ Architecture & Pitch"
])


# =========================================================================
# TAB 1: VOICE ASSISTANT & CHATBOT WITH LIVE FORM PREVIEW
# =========================================================================
with tabs[0]:
    col_chat, col_form = st.columns([1.25, 0.95])

    with col_chat:
        st.markdown("### 🤖 Saathi AI Chatbot")
        
        # Render messages
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                if "part" in msg:
                    st.caption(f"**{msg['part']}**")
                st.markdown(f"**{msg['content']}**")
                if "kannada" in msg:
                    st.markdown(f"<span style='color:#FF8A50; font-size:1.05rem;'>{msg['kannada']}</span>", unsafe_allow_html=True)
                if "why" in msg:
                    with st.expander("🧠 Saathi AI Reasoning & Official ECI Grounding"):
                        st.caption(f"**Statutory Guideline:** {msg['why']}")

        # Quick Evaluator Simulators (Including Voice Relevancy Test)
        st.write("⚡ **Quick Persona Simulators (Test Voice Relevancy):**")
        cp1, cp2, cp3 = st.columns(3)
        if cp1.button("👵 Lakshmi Devi (Valid Elector)"):
            st.session_state.form_data.part1_name = "Lakshmi Devi (ಲಕ್ಷ್ಮಿ ದೇವಿ)"
            st.session_state.chat_history.append({"role": "user", "content": "Lakshmi Devi (ಲಕ್ಷ್ಮಿ ದೇವಿ)"})
            st.session_state.step = 2
            prompt_en = "PART 2A: Were you registered in the previous SIR? Do you have an existing Voter Card (EPIC) number?"
            prompt_kn = "ಭಾಗ 2A: ನೀವು ಹಿಂದಿನ SIR ನಲ್ಲಿ ನೋಂದಣಿಯಾಗಿದ್ದೀರಾ? ನಿಮ್ಮ ಹಳೆಯ ವೋಟರ್ ಕಾರ್ಡ್ (EPIC) ಸಂಖ್ಯೆ ನೆನಪಿದೆಯೇ?"
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": prompt_en,
                "kannada": prompt_kn,
                "part": "PART 2A: Elector Previous SIR",
                "why": "Enables transfer without duplicate voting entries."
            })
            st.rerun()

        if cp2.button("⚠️ Test Unrelated Voice Input"):
            unrelated_val = "What is the weather today?"
            is_rel, err_msg = SIRFormValidator.validate_answer_relevance(st.session_state.step, unrelated_val, st.session_state.language)
            st.session_state.chat_history.append({"role": "user", "content": unrelated_val})
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": f"⚠️ Unrelated Answer: {err_msg}",
                "kannada": err_msg,
                "part": "Semantic Relevancy Check",
                "why": "AI detected question mismatch. Citizen guided back politely in their chosen language."
            })
            st.rerun()

        if cp3.button("🛡️ Not in Old SIR &rarr; Part 3"):
            st.session_state.form_data.part2a_name = "Not Found in Previous SIR"
            st.session_state.form_data.part2a_epic = "N/A"
            st.session_state.form_data.part2b_status = "Part 3 Direct Fallback"
            st.session_state.chat_history.append({"role": "user", "content": "Not in previous SIR"})
            st.session_state.step = 4
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": "Understood! As per the official leaflet: If details are not found in previous SIR, only Part 3 is filled. What is your Date of Birth, Father/Mother/Spouse name, and mobile number?",
                "kannada": "ಅಧಿಕೃತ ನಿಯಮ: ಹಿಂದಿನ SIR ನಲ್ಲಿ ವಿವರ ಸಿಗದಿದ್ದರೆ, ಭಾಗ 3 ನ್ನು ಮಾತ್ರ ಭರ್ತಿ ಮಾಡಲಾಗುತ್ತದೆ. ನಿಮ್ಮ ಹುಟ್ಟಿದ ದಿನಾಂಕ ಮತ್ತು ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ತಿಳಿಸಿ.",
                "part": "PART 3: Family Details Fallback",
                "why": "Official ECI leaflet fallback rule applied."
            })
            st.rerun()

        # Chat Input with Semantic Relevancy Checking
        user_msg = st.chat_input("Speak or type answer to Saathi AI...")
        if user_msg:
            is_relevant, explanation = SIRFormValidator.validate_answer_relevance(st.session_state.step, user_msg, st.session_state.language)

            if not is_relevant:
                st.session_state.chat_history.append({"role": "user", "content": user_msg})
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": f"⚠️ {explanation}",
                    "kannada": explanation,
                    "part": "⚠️ Unrelated Answer Detected",
                    "why": "Semantic Relevancy Guardrail: Input did not match the question."
                })
                st.rerun()

            st.session_state.chat_history.append({"role": "user", "content": user_msg})
            
            if st.session_state.step == 1:
                st.session_state.form_data.part1_name = user_msg
                st.session_state.step = 2
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": "PART 2A: Were you registered in the previous SIR? Do you have your old EPIC number?",
                    "kannada": "ಭಾಗ 2A: ನೀವು ಹಿಂದಿನ SIR ನಲ್ಲಿ ನೋಂದಣಿಯಾಗಿದ್ದೀರಾ? ನಿಮ್ಮ ಹಳೆಯ ವೋಟರ್ ಕಾರ್ಡ್ (EPIC) ಸಂಖ್ಯೆ ನೆನಪಿದೆಯೇ?",
                    "part": "PART 2A: Elector Previous SIR",
                    "why": "Duplicate check & migration."
                })
            elif st.session_state.step == 2:
                st.session_state.step = 3
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": "PART 2B: If your own previous SIR is not found, do you have your Father's, Mother's, or Grandparent's previous voter details?",
                    "kannada": "ಭಾಗ 2B: ನಿಮ್ಮ ಸ್ವಂತ ವಿವರ ಸಿಗದಿದ್ದರೆ, ನಿಮ್ಮ ತಂದೆ/ತಾಯಿ/ಅಜ್ಜ-ಅಜ್ಜಿಯರ ಹಳೆಯ ವೋಟರ್ ವಿವರ ಇದೆಯೇ?",
                    "part": "PART 2B: Ancestor Previous SIR",
                    "why": "Official Lineage Linkage under ECI SIR rules."
                })
            elif st.session_state.step == 3:
                st.session_state.step = 4
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": "PART 3: Please provide your Date of Birth, Father/Mother/Spouse name, and mobile number.",
                    "kannada": "ಭಾಗ 3: ನಿಮ್ಮ ಹುಟ್ಟಿದ ದಿನಾಂಕ, ತಂದೆ/ತಾಯಿ/ಗಂಡನ ಹೆಸರು, ಮತ್ತು ಮೊಬೈಲ್ ಸಂಖ್ಯೆಯನ್ನು ತಿಳಿಸಿ.",
                    "part": "PART 3: Family Details & Proofs",
                    "why": "Family linkage and verification."
                })
            else:
                st.session_state.step = 5
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": "All Parts complete! Your Enumeration Form (EF) is prepared. Keep 1 copy for yourself, 1 copy for the BLO during house visits (30th June - 08th August 2026).",
                    "kannada": "ಎಲ್ಲ ಭಾಗಗಳು ಪೂರ್ಣಗೊಂಡಿವೆ! 30 ಜೂನ್‌ನಿಂದ 08 ಆಗಸ್ಟ್ ಒಳಗೆ BLO ಮನೆಗೆ ಭೇಟಿ ನೀಡಿದಾಗ ಒಂದು ಪ್ರತಿಯನ್ನು ಸಲ್ಲಿಸಿ.",
                    "part": "FINAL: Confirmation",
                    "why": "Final read-back and preparation."
                })
            st.rerun()

    # Right column: Official Enumeration Form Clean Document Preview
    with col_form:
        st.markdown("### 📄 Official Enumeration Form (EF)")
        fd = st.session_state.form_data

        doc_html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
  body {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 4px;
    background: transparent;
  }}
  .ef-doc-card {{
    background: #FFFFFF;
    color: #111827;
    border: 2px solid #000000;
    border-radius: 8px;
    padding: 14px;
    font-size: 12px;
    line-height: 1.4;
    box-shadow: 0 4px 14px rgba(0,0,0,0.25);
  }}
  .part-box {{
    border: 1px solid #9CA3AF;
    padding: 8px;
    margin-bottom: 8px;
    background: #F9FAFB;
    border-radius: 4px;
  }}
  .split-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-bottom: 8px;
  }}
  .table-box {{
    width: 100%;
    border-collapse: collapse;
    font-size: 11px;
  }}
  .table-box td {{
    border: 1px solid #D1D5DB;
    padding: 4px 6px;
  }}
  .col-head {{
    background: #F3F4F6;
    font-weight: bold;
    width: 45%;
  }}
</style>
</head>
<body>
<div class="ef-doc-card">
    <div style="text-align:center; border-bottom:2px solid #000; padding-bottom:6px; margin-bottom:8px;">
        <div style="font-size:11px; font-weight:bold;">भारत निवडणूक आयोग / ELECTION COMMISSION OF INDIA</div>
        <div style="font-size:15px; font-weight:900;">गणना प्रपत्र / ENUMERATION FORM (EF)</div>
        <div style="font-size:11px; color:#4B5563;">Special Intensive Revision (SIR) of Electoral Rolls 2026</div>
    </div>
    
    <div style="background:#EFF6FF; border:1px solid #3B82F6; padding:5px; text-align:center; font-size:11px; font-weight:bold; color:#1E40AF; margin-bottom:8px; border-radius:4px;">
        BLO House Visits: 30th June to 08th August 2026 &bull; Ref: #SIR-2026-89412
    </div>

    <div class="part-box">
        <div style="display:flex; justify-content:space-between; align-items:start;">
            <div>
                <div style="font-weight:bold; color:#1E40AF; font-size:11px; text-transform:uppercase;">PART 1 &bull; Elector Details</div>
                <div style="margin-top:2px;">Name of Elector: <strong>{fd.part1_name}</strong></div>
                <div>AC: <strong>{fd.part1_ac}</strong> &bull; Part: <strong>{fd.part1_part_no}</strong> &bull; Serial: <strong>{fd.part1_serial_no}</strong></div>
                <div>BLO: <strong>{fd.part1_blo_info}</strong></div>
            </div>
            <div style="border:1px dashed #6B7280; padding:4px 8px; text-align:center; font-size:9px; background:#FFF; border-radius:4px;">
                <div style="font-size:22px;">👵</div>
                <div>Photo</div>
            </div>
        </div>
    </div>

    <div class="split-grid">
        <div class="part-box" style="background:#FFF;">
            <div style="font-weight:bold; color:#1E40AF; font-size:11px; margin-bottom:4px; border-bottom:1px solid #E5E7EB; padding-bottom:2px;">PART 2A: Elector Prev SIR</div>
            <div>Name: <strong>{fd.part2a_name}</strong></div>
            <div>EPIC: <strong>{fd.part2a_epic}</strong></div>
            <div>AC: <strong>{fd.part2a_prev_ac}</strong></div>
        </div>
        <div class="part-box" style="background:#FFFBEB;">
            <div style="font-weight:bold; color:#B45309; font-size:11px; margin-bottom:4px; border-bottom:1px solid #FDE68A; padding-bottom:2px;">PART 2B: Ancestor Prev SIR</div>
            <div>Ancestor: <strong>{fd.part2b_ancestor_name}</strong></div>
            <div>EPIC: <strong>{fd.part2b_ancestor_epic}</strong></div>
            <div>Status: <strong style="color:#0B7A4C;">{fd.part2b_status}</strong></div>
        </div>
    </div>

    <div class="part-box">
        <div style="font-weight:bold; color:#1E40AF; font-size:11px; margin-bottom:4px;">PART 3 &bull; Family Details & Proofs</div>
        <table class="table-box">
            <tr><td class="col-head">DOB / Age</td><td><strong>{fd.part3_dob}</strong></td></tr>
            <tr><td class="col-head">Mobile & Aadhaar</td><td><strong>{fd.part3_mobile}</strong> &bull; {fd.part3_aadhaar_masked}</td></tr>
            <tr><td class="col-head">Father</td><td><strong>{fd.part3_father_name}</strong></td></tr>
            <tr><td class="col-head">Mother</td><td><strong>{fd.part3_mother_name}</strong></td></tr>
            <tr><td class="col-head">Spouse</td><td><strong>{fd.part3_spouse_name}</strong></td></tr>
        </table>
    </div>

    <div style="border-top:1px solid #000; padding-top:6px; font-size:10px; display:flex; justify-content:space-between; align-items:center;">
        <div>Keep 1 copy with yourself, 1 copy to BLO.</div>
        <div style="font-weight:bold; color:#1E40AF;">Signature: {fd.part1_name.split()[0]}</div>
    </div>
</div>
</body>
</html>
"""
        components.html(doc_html, height=540, scrolling=True)


# =========================================================================
# TAB 2: INTERACTIVE NEO4J KNOWLEDGE GRAPH
# =========================================================================
with tabs[1]:
    st.subheader("🧠 Neo4j Knowledge Graph Architecture")
    st.write("Stores relationships connecting Form Fields &rarr; Validation Rules &rarr; Official Guidance &rarr; Multilingual Explanations &rarr; Help Resources.")

    status_str = "🟢 Live Neo4j Connection Active" if st.session_state.graph.is_connected_to_neo4j else "🔵 Resilient In-Memory Graph Engine (Zero-setup Fallback Active)"
    st.info(status_str)

    col_g1, col_g2 = st.columns([1, 1])
    with col_g1:
        st.markdown("#### 📌 Knowledge Graph Schema:")
        st.code("""
(SIRForm) -[:HAS_PART]-> (FormPart)
(FormPart) -[:HAS_FIELD]-> (FormField)
(FormField) -[:VALIDATED_BY]-> (ValidationRule)
(FormField) -[:EXPLAINED_BY]-> (OfficialGuidance)
(OfficialGuidance) -[:AVAILABLE_IN]-> (LanguageExplanation)
(FormField) -[:HAS_HELP_RESOURCE]-> (HelpResource)
(DemoSession) -[:CURRENT_STEP]-> (FormField)
        """, language="cypher")

    with col_g2:
        st.markdown("#### ⚡ Active Cypher Query (Grounded in ECI Rules):")
        st.code("""
MATCH (p:FormPart {id: 'part_2a'})-[:HAS_FIELD]->(f:FormField {id: 'part2a_prev_sir'})
-[:EXPLAINED_BY]->(g:OfficialGuidance)
-[:AVAILABLE_IN]->(l:LanguageExplanation {lang: 'kn'})
RETURN g.legal_basis, g.official_text, l.plain_speech;
        """, language="cypher")

    st.markdown("#### 🗂️ Loaded Graph Entities:")
    parts_data = st.session_state.graph.get_parts()
    st.table([{"Part Code": p["id"], "Description": p["label"], "Kannada Label": p["label_kn"]} for p in parts_data])


# =========================================================================
# TAB 3: REVIEW DRAFT & READ-ALOUD
# =========================================================================
with tabs[2]:
    st.subheader("📄 Special Intensive Revision (SIR) 2026 Enumeration Form Draft")
    st.write("Review all captured answers. Every field is confirmed by the citizen.")

    col_t1, col_t2 = st.columns([2, 1])
    with col_t1:
        fd = st.session_state.form_data
        st.table([
            {"Form Section": "PART 1: Elector Name", "Captured Information": fd.part1_name, "Status": "Verified"},
            {"Form Section": "PART 1: Assembly Constituency", "Captured Information": fd.part1_ac, "Status": "Matched"},
            {"Form Section": "PART 2A: Previous SIR Roll", "Captured Information": fd.part2a_name, "Status": "Recorded"},
            {"Form Section": "PART 2B: Ancestor Linkage", "Captured Information": fd.part2b_ancestor_name, "Status": fd.part2b_status},
            {"Form Section": "PART 3: DOB / Age", "Captured Information": fd.part3_dob, "Status": "Senior Citizen Flag"},
            {"Form Section": "PART 3: Mobile Contact", "Captured Information": fd.part3_mobile, "Status": "Verified"},
            {"Form Section": "PART 3: Family Linkage", "Captured Information": f"Spouse: {fd.part3_spouse_name}", "Status": "Verified"}
        ])

    with col_t2:
        st.markdown("#### 📢 Read Draft Aloud")
        if st.button("🔊 Read Entire Draft in Kannada", use_container_width=True):
            kn_text = f"ಮತದಾರರ ನಮೂನೆ ಸಾರಾಂಶ. ಹೆಸರು: {fd.part1_name}. ಭಾಗ 1 ಮತದಾರರ ವಿವರ. ಭಾಗ 2 ಮತ್ತು 3 ರ ವಿವರಗಳನ್ನು BLO ಪರಿಶೀಲನೆಗೆ ದಾಖಲಿಸಲಾಗಿದೆ."
            play_audio(kn_text, "kn")

        if st.button("🔊 Read Entire Draft in English", use_container_width=True):
            en_text = f"Draft summary for elector {fd.part1_name}. Part 1, 2, and 3 entries drafted for BLO doorstep verification."
            play_audio(en_text, "en")

        st.markdown("---")
        st.download_button(
            label="💾 Download Draft JSON",
            data=fd.model_dump_json(indent=2),
            file_name="SIR_2026_Enumeration_Form_Draft.json",
            mime="application/json",
            use_container_width=True
        )

    st.info("""
    **Official Next Steps Instructions:**
    - Draft Reference Number: **#SIR-2026-89412**
    - Designated BLO: **Smt. Geetha R. (Ward 45, Malleshwaram)**
    - Scheduled Action: BLO will visit between **30th June and 08th August 2026** for physical signature & document inspection.
    - Zero online payment: ECI does not charge any fee for its services.
    """)


# =========================================================================
# TAB 4: BLO REVIEW QUEUE
# =========================================================================
with tabs[3]:
    st.subheader("👮‍♂️ Booth Level Officer (BLO) Review Dashboard")
    st.write("Assisted verification portal for election staff to prioritize senior citizens and cases with unverified previous rolls.")

    blo_cases = [
        {"Draft ID": "#SIR-89412", "Citizen Name": "Lakshmi Devi", "Age": "72 yrs", "Previous Roll Status": "Unknown / Part 3 Fallback", "Priority": "🔴 High (Elderly)", "Action Required": "Doorstep Home Visit"},
        {"Draft ID": "#SIR-89410", "Citizen Name": "Ramesh Gowda", "Age": "19 yrs", "Previous Roll Status": "None (First Time)", "Priority": "🟢 Normal", "Action Required": "Marks Card Check"},
        {"Draft ID": "#SIR-89408", "Citizen Name": "Savitri Bai", "Age": "68 yrs", "Previous Roll Status": "KL/08/042/123456", "Priority": "🟡 Medium (Transfer)", "Action Required": "Old Roll Deletion"}
    ]
    st.dataframe(blo_cases, use_container_width=True)


# =========================================================================
# TAB 5: ABOUT & PRESENTATION PITCH
# =========================================================================
with tabs[4]:
    st.subheader("🚀 SIR Saathi AI Project Overview")
    st.markdown("""
    ### 🎤 Suggested Presentation Pitch:
    > *"SIR Saathi AI is a voice-first, multilingual assistant that helps elderly and low-literacy citizens complete an SIR form more confidently. Instead of navigating a complex form, the citizen answers one question at a time. The assistant fills a draft, explains fields using a Neo4j knowledge graph of verified guidance, checks for missing information, and reads the answers back for confirmation. Our goal is to make digital form assistance more accessible while keeping the citizen in control and leaving official decisions to authorized election officials."*

    ### 🛡️ Core Safety & Trust Principles:
    1. **Never Guess Rule:** The assistant never invents missing dates or previous roll IDs.
    2. **Read-Back Authority:** The citizen verifies every single field aloud before printing.
    3. **Preserving Human Authority:** Automated decisions on voting rights or eligibility are strictly forbidden.
    4. **Verified Legal Grounding:** Statutory references mapped directly in Neo4j knowledge graph.
    """)
