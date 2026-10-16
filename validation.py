"""
SIR SAATHI AI - Form Validation and Semantic Relevancy Engine
Checks whether voice input directly relates to the asked question.
If unrelated, flags it and generates a polite vernacular clarification message.
"""

import re
from datetime import datetime, date
from typing import Dict, Any, List, Tuple, Optional

class SIRFormValidator:
    """Validates SIR form fields and checks conversational answer relevancy."""

    @staticmethod
    def validate_answer_relevance(step_id: int, answer: str, lang: str = "kn") -> Tuple[bool, str]:
        """
        Validates if the user's spoken answer relates to the specific question asked.
        Returns (is_relevant: bool, explanation_or_error_message: str)
        """
        t = (answer or "").strip().lower()

        # Step 1: Elector Full Name
        if step_id == 1:
            if re.match(r'^\d+$', t):
                err = {
                    "kn": "ಇದು ಕೇವಲ ಸಂಖ್ಯೆಯಾಗಿದೆ. ದಯವಿಟ್ಟು ನಿಮ್ಮ ಪೂರ್ಣ ಹೆಸರನ್ನು ತಿಳಿಸಿ (ಉದಾಹರಣೆಗೆ: ಲಕ್ಷ್ಮಿ ದೇವಿ).",
                    "en": "You provided numbers. Please speak your full name as used in official records (e.g. Lakshmi Devi).",
                    "hi": "यह केवल संख्या है। कृपया पहचान पत्र के अनुसार अपना पूरा नाम बताएं।"
                }
                return False, err.get(lang, err["en"])

            unrelated_phrases = ["weather", "time", "pizza", "hello", "song", "food", "ಹವಾಮಾನ", "ಸಮಯ", "ಏನು"]
            if any(w in t for w in unrelated_phrases) and len(t.split()) < 3:
                err = {
                    "kn": "ಕ್ಷಮಿಸಿ, ಇದು ಮತದಾರರ ಹೆಸರಿನಂತೆ ಕಾಣುತ್ತಿಲ್ಲ. ದಯವಿಟ್ಟು ನಿಮ್ಮ ಗುರುತಿನ ಚೀಟಿಯಲ್ಲಿರುವ ಹೆಸರನ್ನು ಹೇಳಿ.",
                    "en": "That does not sound like an elector's name. Please provide your full name as in your ID proof.",
                    "hi": "यह मतदाता का नाम नहीं लगता है। कृपया पहचान पत्र के अनुसार अपना पूरा नाम बताएं।"
                }
                return False, err.get(lang, err["en"])

            if len(t) < 2:
                err = {
                    "kn": "ಹೆಸರು ತುಂಬಾ ಚಿಕ್ಕದಾಗಿದೆ. ದಯವಿಟ್ಟು ಸ್ಪಷ್ಟವಾಗಿ ಪೂರ್ಣ ಹೆಸರನ್ನು ಹೇಳಿ.",
                    "en": "The name is too short. Please speak your full name clearly.",
                    "hi": "नाम बहुत छोटा है। कृपया अपना पूरा नाम बताएं।"
                }
                return False, err.get(lang, err["en"])

        # Step 2: Previous SIR / EPIC (Part 2A)
        elif step_id == 2:
            unrelated = ["weather", "time", "pizza", "biryani", "who are you"]
            if any(w in t for w in unrelated):
                err = {
                    "kn": "ಇದು ಸಂಬಂಧವಿಲ್ಲದ ಉತ್ತರವಾಗಿದೆ. ದಯವಿಟ್ಟು ನೀವು ಹಿಂದಿನ ಮತದಾರರ ಪಟ್ಟಿಯಲ್ಲಿದ್ದೀರಾ ಎಂದು 'ಹೌದು' ಅಥವಾ 'ಇಲ್ಲ' ಎಂದು ತಿಳಿಸಿ.",
                    "en": "That is an unrelated response. Please clarify if you were in the previous SIR by saying 'Yes' with your card or 'No'.",
                    "hi": "यह असंबंधित उत्तर है। कृपया बताएं कि क्या आपके पास पुराना वोटर कार्ड है या नहीं।"
                }
                return False, err.get(lang, err["en"])

        # Step 3: Ancestor Previous SIR (Part 2B)
        elif step_id == 3:
            unrelated = ["weather", "pizza", "movie", "cinema"]
            if any(w in t for w in unrelated):
                err = {
                    "kn": "ದಯವಿಟ್ಟು ನಿಮ್ಮ ತಂದೆ/ತಾಯಿ/ಅಜ್ಜ-ಅಜ್ಜಿಯರ ಹಳೆಯ ವಿವರ ಇದೆಯೇ ಎಂದು ತಿಳಿಸಿ ಅಥವಾ 'ಲಭ್ಯವಿಲ್ಲ' ಎಂದು ಹೇಳಿ.",
                    "en": "Please tell if you have your Father, Mother, or Grandparent's previous voter details, or say 'Not available'.",
                    "hi": "कृपया बताएं कि क्या पूर्वजों का पुराना विवरण है या 'उपलब्ध नहीं' कहें।"
                }
                return False, err.get(lang, err["en"])

        # Step 4: Family Details & DOB (Part 3)
        elif step_id == 4:
            has_digits = bool(re.search(r'\d', t))
            has_age_words = any(w in t for w in ["year", "age", "ವರ್ಷ", "ವಯಸ್ಸು", "ಹುಟ್ಟಿದ", "date", "august", "साल", "आयु"])
            if not has_digits and not has_age_words:
                err = {
                    "kn": "ಈ ಉತ್ತರದಲ್ಲಿ ವಯಸ್ಸು ಅಥವಾ ದಿನಾಂಕ ಕಂಡುಬಂದಿಲ್ಲ. ದಯವಿಟ್ಟು ನಿಮ್ಮ ವಯಸ್ಸು ಅಥವಾ ಹುಟ್ಟಿದ ದಿನಾಂಕ ತಿಳಿಸಿ (ಉದಾಹರಣೆಗೆ: 72 ವರ್ಷ).",
                    "en": "We did not detect an age or date. Please speak your age or date of birth (for example: 72 years).",
                    "hi": "इसमें आयु या जन्म तिथि नहीं मिली। कृपया अपनी आयु बताएं (उदा. 72 वर्ष)।"
                }
                return False, err.get(lang, err["en"])

        return True, "Valid"

    @staticmethod
    def calculate_age(dob_str: str) -> Tuple[Optional[int], Optional[str]]:
        if not dob_str or not dob_str.strip():
            return None, "Date of birth / age is required."
        if dob_str.strip().isdigit():
            return int(dob_str.strip()), None
        for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"):
            try:
                dt = datetime.strptime(dob_str.strip(), fmt).date()
                today = date.today()
                return today.year - dt.year - ((today.month, today.day) < (dt.month, dt.day)), None
            except ValueError:
                pass
        return None, "Please provide date of birth in DD/MM/YYYY or enter age in years."
