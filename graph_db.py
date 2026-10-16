"""
SIR SAATHI AI - Knowledge Graph Engine
Grounding the Special Intensive Revision (SIR) 2026 Enumeration Form (EF)
Ref: Election Commission of India (ECI) / CEO Reference Guidelines
BLO House Visits: 30th June to 08th August 2026
"""

import json
import logging
from typing import Dict, List, Optional, Any

logger = logging.getLogger("SIR_Saathi_Graph")

# Seed knowledge graph representing verified ECI Special Intensive Revision (SIR) 2026 Enumeration Form
KNOWLEDGE_GRAPH_DATA = {
    "nodes": {
        "forms": [
            {
                "id": "SIR_EF_2026",
                "name": "Enumeration Form (EF) / गणना प्रपत्र - SIR 2026",
                "authority": "Election Commission of India (ECI)",
                "blo_visit_window": "30th June to 08th August 2026",
                "motto": "No eligible voter will be left out, no ineligible person will be included",
                "helpline": "1800 22 1950 / 1950"
            }
        ],
        "parts": [
            {
                "id": "part_1",
                "label": "PART 1: Elector Identification & Photo",
                "label_kn": "ಭಾಗ 1: ಮತದಾರರ ಗುರುತು ಮತ್ತು ಭಾವಚಿತ್ರ",
                "description": "Basic details, photo box, BLO details and Assembly Constituency"
            },
            {
                "id": "part_2a",
                "label": "PART 2A: Elector's Previous SIR Details",
                "label_kn": "ಭಾಗ 2A: ಮತದಾರರ ಹಿಂದಿನ SIR ವಿವರಗಳು",
                "description": "Previous SIR name, relative, EPIC, AC, district, state, polling station, serial/part"
            },
            {
                "id": "part_2b",
                "label": "PART 2B: Ancestral Lineage (Father/Mother/Grandparent) Previous SIR Details",
                "label_kn": "ಭಾಗ 2B: ಪೋಷಕರು/ಅಜ್ಜ-ಅಜ್ಜಿಯರ ಹಿಂದಿನ SIR ವಿವರಗಳು",
                "description": "Used if elector's own previous SIR record is not found"
            },
            {
                "id": "part_3",
                "label": "PART 3: Elector's Family Details & Proofs",
                "label_kn": "ಭಾಗ 3: ಮತದಾರರ ಕುಟುಂಬದ ವಿವರಗಳು ಮತ್ತು ದಾಖಲೆಗಳು",
                "description": "Date of Birth, Aadhaar (optional), Mobile, Father/Mother/Spouse details"
            }
        ],
        "fields": [
            {
                "id": "part1_elector_name",
                "part": "part_1",
                "label": "Elector Full Name",
                "label_kn": "ಮತದಾರರ ಪೂರ್ಣ ಹೆಸರು",
                "required": True,
                "step_order": 1
            },
            {
                "id": "part2a_prev_sir",
                "part": "part_2a",
                "label": "Previous SIR Roll / EPIC Details",
                "label_kn": "ಹಿಂದಿನ SIR ಮತದಾರರ ಗುರುತಿನ ಚೀಟಿ (EPIC)",
                "required": False,
                "step_order": 2
            },
            {
                "id": "part2b_ancestor_sir",
                "part": "part_2b",
                "label": "Father/Mother/Grandparent Previous SIR Linkage",
                "label_kn": "ತಂದೆ/ತಾಯಿ/ಅಜ್ಜ-ಅಜ್ಜಿಯರ ಹಿಂದಿನ SIR ವಿವರ",
                "required": False,
                "step_order": 3
            },
            {
                "id": "part3_dob_age",
                "part": "part_3",
                "label": "Date of Birth / Age (DD/MM/YYYY)",
                "label_kn": "ಹುಟ್ಟಿದ ದಿನಾಂಕ / ವಯಸ್ಸು",
                "required": True,
                "step_order": 4
            },
            {
                "id": "part3_family_epic",
                "part": "part_3",
                "label": "Father/Mother/Spouse Names & EPICs",
                "label_kn": "ತಂದೆ/ತಾಯಿ/ಗಂಡನ ಹೆಸರು & ವೋಟರ್ ಐಡಿ",
                "required": True,
                "step_order": 5
            },
            {
                "id": "part3_mobile_aadhaar",
                "part": "part_3",
                "label": "Mobile Contact & Aadhaar (Optional)",
                "label_kn": "ಮೊಬೈಲ್ ಸಂಖ್ಯೆ & ಆಧಾರ್ ಸಂಖ್ಯೆ",
                "required": True,
                "step_order": 6
            }
        ],
        "validation_rules": [
            {
                "id": "rule_sir_fallback",
                "target_part": "part_3",
                "rule_type": "OFFICIAL_FALLBACK_RULE",
                "rule_text": "If details are not found in previous SIR (Part 2A/2B), only Part 3 may be filled and submitted to BLO with prescribed documents.",
                "rule_text_kn": "ಹಿಂದಿನ SIR ನಲ್ಲಿ ವಿವರಗಳು ಸಿಗದಿದ್ದರೆ, ಭಾಗ 3 ನ್ನು ಮಾತ್ರ ಭರ್ತಿ ಮಾಡಿ ಬಿಎಲ್ಒಗೆ ಸಲ್ಲಿಸಬಹುದು."
            },
            {
                "id": "rule_never_guess_ancestor",
                "target_part": "part_2b",
                "rule_type": "NEVER_GUESS_SAFEGUARD",
                "rule_text": "Never guess ancestor roll records. Mark as 'Not Found / Direct Part 3 Path'.",
                "rule_text_kn": "ಪೋಷಕರ ಹಳೆಯ ವಿವರ ತಿಳಿದಿಲ್ಲದಿದ್ದರೆ ಊಹಿಸದೆ ನೇರವಾಗಿ ಭಾಗ 3 ಕ್ಕೆ ತೆರಳಬೇಕು."
            },
            {
                "id": "rule_no_payment",
                "target_part": "all",
                "rule_type": "ECI_ZERO_FEE",
                "rule_text": "No online payments to be made because ECI does not charge any fee for its services.",
                "rule_text_kn": "ಚುನಾವಣಾ ಆಯೋಗ ಯಾವುದೇ ಶುಲ್ಕ ವಿಧಿಸುವುದಿಲ್ಲ; ಯಾವುದೇ ಹಣ ಪಾವತಿ ಮಾಡಬಾರದು."
            }
        ],
        "official_guidance": [
            {
                "id": "guidance_ef_overview",
                "legal_basis": "ECI SIR Manual 2026 & CEO Maharashtra Enumeration Instructions",
                "official_text": "Submit one copy of the enumeration form, filled as above, to the BLO during house visits (30th June to 08th August 2026), and keep one copy with yourself.",
                "source_url": "https://voters.eci.gov.in/sir",
                "last_verified": "2026"
            }
        ]
    }
}


class SIRKnowledgeGraph:
    """Knowledge graph interface connecting official SIR 2026 Form Parts, Rules, and Explanations."""

    def __init__(self, uri: Optional[str] = None, user: Optional[str] = None, password: Optional[str] = None):
        self.uri = uri
        self.user = user
        self.password = password
        self.driver = None
        self.is_connected_to_neo4j = False

        if uri and user and password:
            try:
                from neo4j import GraphDatabase
                self.driver = GraphDatabase.driver(uri, auth=(user, password))
                with self.driver.session() as session:
                    session.run("RETURN 1")
                self.is_connected_to_neo4j = True
                logger.info("Connected to live Neo4j database.")
            except Exception as e:
                logger.warning(f"Neo4j connection failed ({e}). Using in-memory graph.")
                self.is_connected_to_neo4j = False

    def get_parts(self) -> List[Dict[str, Any]]:
        return KNOWLEDGE_GRAPH_DATA["nodes"]["parts"]

    def get_fields(self) -> List[Dict[str, Any]]:
        return sorted(KNOWLEDGE_GRAPH_DATA["nodes"]["fields"], key=lambda x: x["step_order"])

    def get_guidance(self, field_id: str, lang: str = "en") -> Dict[str, Any]:
        """Contextual retrieval for SIR 2026 Enumeration Form field."""
        return {
            "field_id": field_id,
            "form": KNOWLEDGE_GRAPH_DATA["nodes"]["forms"][0],
            "rules": KNOWLEDGE_GRAPH_DATA["nodes"]["validation_rules"],
            "cypher_query": f"MATCH (p:FormPart)-[:HAS_FIELD]->(f:FormField {{id: '{field_id}'}})-[:VALIDATED_BY]->(r:ValidationRule) RETURN p, f, r;"
        }
