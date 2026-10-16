// ============================================================================
// SIR SAATHI AI (ಧ್ವನಿ ಸಾರಥಿ) - NEO4J KNOWLEDGE GRAPH SEED SCRIPT
// Grounding the Special Intensive Revision (SIR) 2026 Enumeration Form (EF)
// Reference: Election Commission of India (ECI) / CEO Guidelines
// BLO House Visits: 30th June to 08th August 2026
// ============================================================================

// ----------------------------------------------------------------------------
// STEP 1: CONSTRAINTS & INDEXES (Execute first in Neo4j Browser / AuraDB)
// ----------------------------------------------------------------------------
CREATE CONSTRAINT form_id_unique IF NOT EXISTS FOR (f:SIRForm) REQUIRE f.id IS UNIQUE;
CREATE CONSTRAINT part_id_unique IF NOT EXISTS FOR (p:FormPart) REQUIRE p.id IS UNIQUE;
CREATE CONSTRAINT field_id_unique IF NOT EXISTS FOR (fld:FormField) REQUIRE fld.id IS UNIQUE;
CREATE CONSTRAINT rule_id_unique IF NOT EXISTS FOR (r:ValidationRule) REQUIRE r.id IS UNIQUE;
CREATE CONSTRAINT guidance_id_unique IF NOT EXISTS FOR (g:OfficialGuidance) REQUIRE g.id IS UNIQUE;
CREATE CONSTRAINT lang_exp_id_unique IF NOT EXISTS FOR (l:LanguageExplanation) REQUIRE l.id IS UNIQUE;

// ----------------------------------------------------------------------------
// STEP 2: CLEAR PREVIOUS SIR GRAPH DATA (Optional / Idempotent Reset)
// ----------------------------------------------------------------------------
MATCH (n:SIRSaathiEntity) DETACH DELETE n;

// ----------------------------------------------------------------------------
// STEP 3: CREATE ROOT FORM NODE
// ----------------------------------------------------------------------------
CREATE (form:SIRForm:SIRSaathiEntity {
    id: "SIR_EF_2026",
    name: "Special Intensive Revision (SIR) 2026 Enumeration Form (EF)",
    name_hi: "गणना प्रपत्र - विशेष गहन पुनरीक्षण 2026",
    authority: "Election Commission of India (ECI)",
    revision_year: 2026,
    blo_visit_window: "30th June to 08th August 2026",
    motto: "No eligible voter will be left out, no ineligible person will be included",
    helpline: "1800 22 1950 / 1950",
    portal_url: "https://voters.eci.gov.in"
});

// ----------------------------------------------------------------------------
// STEP 4: CREATE FORM PARTS (Matching Official Leaflet Structure)
// ----------------------------------------------------------------------------
CREATE (p1:FormPart:SIRSaathiEntity {
    id: "part_1",
    part_number: 1,
    title: "PART 1: Elector Identification & Photo",
    title_kn: "ಭಾಗ 1: ಮತದಾರರ ಗುರುತು ಮತ್ತು ಭಾವಚಿತ್ರ",
    title_hi: "भाग 1: निर्वाचक पहचान और फोटो",
    description: "Captures full legal name, current Assembly Constituency, Part No, Serial No, and passport photo.",
    is_mandatory: true
});

CREATE (p2a:FormPart:SIRSaathiEntity {
    id: "part_2a",
    part_number: 2,
    sub_part: "A",
    title: "PART 2A: Elector's Previous SIR Details",
    title_kn: "ಭಾಗ 2A: ಮತದಾರರ ಹಿಂದಿನ SIR ವಿವರಗಳು",
    title_hi: "भाग 2A: निर्वाचक का पिछला एसआईआर विवरण",
    description: "Previous SIR elector name, relative name, EPIC card number, AC name, district, state, and serial number.",
    is_mandatory: false
});

CREATE (p2b:FormPart:SIRSaathiEntity {
    id: "part_2b",
    part_number: 2,
    sub_part: "B",
    title: "PART 2B: Ancestral Lineage Previous SIR Details",
    title_kn: "ಭಾಗ 2B: ಪೋಷಕರು/ಅಜ್ಜ-ಅಜ್ಜಿಯರ ಹಿಂದಿನ SIR ವಿವರಗಳು",
    title_hi: "भाग 2B: पूर्वज (माता/पिता/दादा-दादी) का पिछला एसआईआर विवरण",
    description: "Lineage linkage if elector's own previous SIR record is unavailable or shifted.",
    is_mandatory: false
});

CREATE (p3:FormPart:SIRSaathiEntity {
    id: "part_3",
    part_number: 3,
    title: "PART 3: Elector's Family Details & Prescribed Proofs",
    title_kn: "ಭಾಗ 3: ಮತದಾರರ ಕುಟುಂಬದ ವಿವರಗಳು ಮತ್ತು ದಾಖಲೆಗಳು",
    title_hi: "भाग 3: परिवार विवरण और निर्धारित दस्तावेज",
    description: "Date of birth, Aadhaar (voluntary), mobile contact, Father/Mother/Spouse details, and prescribed ID documents.",
    is_mandatory: true
});

// ----------------------------------------------------------------------------
// STEP 5: CREATE FORM FIELDS
// ----------------------------------------------------------------------------
CREATE (f1:FormField:SIRSaathiEntity {
    id: "part1_name",
    name: "Elector Full Name",
    name_kn: "ಮತದಾರರ ಪೂರ್ಣ ಹೆಸರು",
    name_hi: "निर्वाचक का पूरा नाम",
    field_type: "text",
    step_order: 1,
    required: true
});

CREATE (f2:FormField:SIRSaathiEntity {
    id: "part1_ac",
    name: "Assembly Constituency & Booth",
    name_kn: "ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಮತ್ತು ಬೂತ್",
    name_hi: "विधानसभा क्षेत्र और बूथ",
    field_type: "text",
    step_order: 2,
    required: true
});

CREATE (f3:FormField:SIRSaathiEntity {
    id: "part2a_prev_sir",
    name: "Previous SIR EPIC & Roll Details",
    name_kn: "ಹಿಂದಿನ SIR ವೋಟರ್ ಕಾರ್ಡ್ (EPIC)",
    name_hi: "पिछला वोटर कार्ड और रोल विवरण",
    field_type: "epic_number",
    step_order: 3,
    required: false
});

CREATE (f4:FormField:SIRSaathiEntity {
    id: "part2b_ancestor_sir",
    name: "Father/Mother/Grandparent Previous SIR Linkage",
    name_kn: "ಪೋಷಕರ ಹಿಂದಿನ SIR ವಿವರ",
    name_hi: "माता/पिता/पूर्वज का पिछला एसआईआर विवरण",
    field_type: "ancestor_linkage",
    step_order: 4,
    required: false
});

CREATE (f5:FormField:SIRSaathiEntity {
    id: "part3_dob",
    name: "Date of Birth & Age",
    name_kn: "ಹುಟ್ಟಿದ ದಿನಾಂಕ ಮತ್ತು ವಯಸ್ಸು",
    name_hi: "जन्म तिथि और आयु",
    field_type: "date",
    step_order: 5,
    required: true
});

CREATE (f6:FormField:SIRSaathiEntity {
    id: "part3_family",
    name: "Father/Mother/Spouse Names & EPICs",
    name_kn: "ಕುಟುಂಬದ ಸದಸ್ಯರ ವಿವರ ಮತ್ತು ವೋಟರ್ ಐಡಿ",
    name_hi: "परिवार के सदस्यों का नाम और वोटर आईडी",
    field_type: "family_tree",
    step_order: 6,
    required: true
});

CREATE (f7:FormField:SIRSaathiEntity {
    id: "part3_contact",
    name: "Mobile Contact & Masked Aadhaar",
    name_kn: "ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಮತ್ತು ಆಧಾರ್",
    name_hi: "मोबाइल नंबर और आधार",
    field_type: "contact",
    step_order: 7,
    required: true
});

// ----------------------------------------------------------------------------
// STEP 6: CREATE VALIDATION & SAFETY RULES
// ----------------------------------------------------------------------------
CREATE (r1:ValidationRule:SIRSaathiEntity {
    id: "rule_sir_fallback",
    name: "Official Fallback Rule (ECI Leaflet Clause 4)",
    rule_type: "BRANCHING_FALLBACK",
    severity: "CRITICAL",
    rule_text: "If details are not found in previous SIR (Part 2A or 2B), only Part 3 may be filled and submitted to the BLO with prescribed documents.",
    rule_text_kn: "ಹಿಂದಿನ SIR ನಲ್ಲಿ ವಿವರಗಳು ಸಿಗದಿದ್ದರೆ, ಭಾಗ 3 ನ್ನು ಮಾತ್ರ ಭರ್ತಿ ಮಾಡಿ ಬಿಎಲ್ಒಗೆ ನಿಗದಿತ ದಾಖಲೆಗಳೊಂದಿಗೆ ಸಲ್ಲಿಸಬಹುದು."
});

CREATE (r2:ValidationRule:SIRSaathiEntity {
    id: "rule_never_guess_ancestor",
    name: "Never Guess Ancestor Roll Safeguard",
    rule_type: "ACCURACY_GUARD",
    severity: "HIGH",
    rule_text: "The AI assistant must NEVER invent, assume, or fabricate previous roll serial numbers or ancestor EPICs. If unknown, mark as 'Direct Part 3 Fallback'.",
    rule_text_kn: "ಪೋಷಕರ ಹಳೆಯ ವಿವರ ತಿಳಿದಿಲ್ಲದಿದ್ದರೆ ಊಹಿಸದೆ ನೇರವಾಗಿ ಭಾಗ 3 ಕ್ಕೆ ತೆರಳಬೇಕು."
});

CREATE (r3:ValidationRule:SIRSaathiEntity {
    id: "rule_no_payment",
    name: "ECI Zero-Fee Public Service Guarantee",
    rule_type: "FRAUD_PROTECTION",
    severity: "MANDATORY",
    rule_text: "No online payment is ever required. ECI and BLO doorstep enumeration services are 100% free of charge.",
    rule_text_kn: "ಚುನಾವಣಾ ಆಯೋಗ ಯಾವುದೇ ಶುಲ್ಕ ವಿಧಿಸುವುದಿಲ್ಲ; ಯಾವುದೇ ಆನ್‌ಲೈನ್ ಪಾವತಿ ಮಾಡಬಾರದು."
});

CREATE (r4:ValidationRule:SIRSaathiEntity {
    id: "rule_senior_priority",
    name: "Senior Citizen Doorstep Priority Flag",
    rule_type: "ASSISTIVE_PRIORITY",
    severity: "INFO",
    rule_text: "Electors aged 70+ are automatically flagged in the BLO verification queue for prioritized doorstep visits.",
    rule_text_kn: "70 ವರ್ಷ ಮೇಲ್ಪಟ್ಟ ಹಿರಿಯ ನಾಗರಿಕರಿಗೆ ಮನೆ ಬಾಗಿಲಿಗೆ ಬಿಎಲ್ಒ ಆದ್ಯತೆಯ ಭೇಟಿ ನೀಡಲಾಗುತ್ತದೆ."
});

// ----------------------------------------------------------------------------
// STEP 7: CREATE OFFICIAL GUIDANCE & LEGAL BASIS NODES
// ----------------------------------------------------------------------------
CREATE (g1:OfficialGuidance:SIRSaathiEntity {
    id: "guidance_part1",
    topic: "Identity & Photo Guidelines",
    legal_basis: "Representation of the People Act 1950 (Section 23) & Registration of Electors Rules 1960",
    official_text: "Affix one clear recent passport size color photo. The elector identity must match official records.",
    source: "ECI SIR 2026 Manual Chapter 2"
});

CREATE (g2:OfficialGuidance:SIRSaathiEntity {
    id: "guidance_part2a",
    topic: "Deduplication via Previous SIR Roll",
    legal_basis: "ECI SIR Manual Chapter 4 (De-duplication & Roll Continuity)",
    official_text: "EPIC from previous SIR enables automated linking across polling stations and prevents duplicate voting records.",
    source: "ECI Guidelines for Special Intensive Revision 2026"
});

CREATE (g3:OfficialGuidance:SIRSaathiEntity {
    id: "guidance_part2b",
    topic: "Ancestral Lineage Verification",
    legal_basis: "Registration of Electors Rules 1960 Rule 13 (Lineage Linkage)",
    official_text: "When a citizen's own previous roll cannot be traced due to age or relocation, linking parental/grandparent records establishes electoral continuity.",
    source: "CEO Reference Manual 2026"
});

CREATE (g4:OfficialGuidance:SIRSaathiEntity {
    id: "guidance_part3_fallback",
    topic: "Prescribed Supporting Documents",
    legal_basis: "ECI Prescribed Identity Documents List 2026",
    official_text: "Eligible prescribed documents include: Aadhaar card, PAN card, Indian Passport, Driving License, Pension Document with photo, or Bank Passbook with photo.",
    source: "ECI Public Notice 2026"
});

// ----------------------------------------------------------------------------
// STEP 8: CREATE MULTILINGUAL EXPLANATIONS (Kannada, Hindi, English)
// ----------------------------------------------------------------------------
CREATE (l1_kn:LanguageExplanation:SIRSaathiEntity {
    id: "exp_part1_kn",
    lang: "kn",
    language_name: "Kannada",
    plain_speech: "ನಿಮ್ಮ ಪೂರ್ಣ ಹೆಸರನ್ನು ಅಧಿಕೃತ ದಾಖಲೆಗಳಲ್ಲಿ ಇರುವಂತೆಯೇ ತಿಳಿಸಿ. ನಿಮ್ಮ ಭಾವಚಿತ್ರವನ್ನು ಬಿಎಲ್ಒ ಪರಿಶೀಲಿಸುತ್ತಾರೆ."
});

CREATE (l2_kn:LanguageExplanation:SIRSaathiEntity {
    id: "exp_part2a_kn",
    lang: "kn",
    language_name: "Kannada",
    plain_speech: "ನಿಮ್ಮ ಹಳೆಯ ವೋಟರ್ ಕಾರ್ಡ್ (EPIC) ಸಂಖ್ಯೆ ಇದ್ದರೆ ತಿಳಿಸಿ. ಇದರಿಂದ ನಿಮ್ಮ ಹಿಂದಿನ ದಾಖಲೆ ಸುಲಭವಾಗಿ ವರ್ಗಾವಣೆಯಾಗುತ್ತದೆ."
});

CREATE (l2b_kn:LanguageExplanation:SIRSaathiEntity {
    id: "exp_part2b_kn",
    lang: "kn",
    language_name: "Kannada",
    plain_speech: "ನಿಮ್ಮ ಸ್ವಂತ ಹಳೆಯ ವಿವರ ಸಿಗದಿದ್ದರೆ, ನಿಮ್ಮ ತಂದೆ, ತಾಯಿ ಅಥವಾ ಅಜ್ಜ-ಅಜ್ಜಿಯರ ಹಳೆಯ ವೋಟರ್ ವಿವರಗಳನ್ನು ಜೋಡಿಸಬಹುದು."
});

CREATE (l3_kn:LanguageExplanation:SIRSaathiEntity {
    id: "exp_part3_kn",
    lang: "kn",
    language_name: "Kannada",
    plain_speech: "ಹಿಂದಿನ ವಿವರಗಳು ಇಲ್ಲದಿದ್ದರೂ ಚಿಂತಿಸಬೇಡಿ! ಭಾಗ 3 ರ ವಿವರಗಳನ್ನು ಭರ್ತಿ ಮಾಡಿ, ಬಿಎಲ್ಒ ಬಂದಾಗ ನಿಮ್ಮ ಆಧಾರ್ ಅಥವಾ ಗುರುತಿನ ಚೀಟಿಯ ಪ್ರತಿ ನೀಡಿದರೆ ಸಾಕು."
});

CREATE (l1_hi:LanguageExplanation:SIRSaathiEntity {
    id: "exp_part1_hi",
    lang: "hi",
    language_name: "Hindi",
    plain_speech: "कृपया अपना पूरा नाम आधिकारिक पहचान पत्र के अनुसार बताएं। बीएलओ आपके घर आकर फोटो सत्यापित करेंगे।"
});

CREATE (l3_hi:LanguageExplanation:SIRSaathiEntity {
    id: "exp_part3_hi",
    lang: "hi",
    language_name: "Hindi",
    plain_speech: "यदि पिछला रिकॉर्ड नहीं मिलता है, तो केवल भाग 3 भरें और बीएलओ को अपना आधार या निर्धारित दस्तावेज दिखाएं।"
});

// ----------------------------------------------------------------------------
// STEP 9: ESTABLISH GRAPH RELATIONSHIPS (Connecting Nodes into Knowledge Graph)
// ----------------------------------------------------------------------------

// Form Part Hierarchy
MATCH (form:SIRForm {id: "SIR_EF_2026"})
MATCH (p1:FormPart {id: "part_1"}), (p2a:FormPart {id: "part_2a"}), (p2b:FormPart {id: "part_2b"}), (p3:FormPart {id: "part_3"})
MERGE (form)-[:HAS_PART]->(p1)
MERGE (form)-[:HAS_PART]->(p2a)
MERGE (form)-[:HAS_PART]->(p2b)
MERGE (form)-[:HAS_PART]->(p3)
MERGE (p1)-[:NEXT_PART]->(p2a)
MERGE (p2a)-[:NEXT_PART]->(p2b)
MERGE (p2b)-[:NEXT_PART]->(p3);

// Dynamic Branching & Official Fallback Path
MATCH (p2a:FormPart {id: "part_2a"}), (p2b:FormPart {id: "part_2b"}), (p3:FormPart {id: "part_3"})
MERGE (p2a)-[:IF_NOT_FOUND]->(p2b)
MERGE (p2b)-[:FALLBACK_ROUTE {rule: "Official Leaflet Fallback Clause 4"}]->(p3);

// Form Fields linking to Form Parts
MATCH (p1:FormPart {id: "part_1"}), (f1:FormField {id: "part1_name"}), (f2:FormField {id: "part1_ac"})
MERGE (p1)-[:HAS_FIELD]->(f1)
MERGE (p1)-[:HAS_FIELD]->(f2);

MATCH (p2a:FormPart {id: "part_2a"}), (f3:FormField {id: "part2a_prev_sir"})
MERGE (p2a)-[:HAS_FIELD]->(f3);

MATCH (p2b:FormPart {id: "part_2b"}), (f4:FormField {id: "part2b_ancestor_sir"})
MERGE (p2b)-[:HAS_FIELD]->(f4);

MATCH (p3:FormPart {id: "part_3"}), (f5:FormField {id: "part3_dob"}), (f6:FormField {id: "part3_family"}), (f7:FormField {id: "part3_contact"})
MERGE (p3)-[:HAS_FIELD]->(f5)
MERGE (p3)-[:HAS_FIELD]->(f6)
MERGE (p3)-[:HAS_FIELD]->(f7);

// Validation Rules linking to Fields and Parts
MATCH (f3:FormField {id: "part2a_prev_sir"}), (r1:ValidationRule {id: "rule_sir_fallback"})
MERGE (f3)-[:GOVERNED_BY]->(r1);

MATCH (f4:FormField {id: "part2b_ancestor_sir"}), (r2:ValidationRule {id: "rule_never_guess_ancestor"})
MERGE (f4)-[:VALIDATED_BY]->(r2);

MATCH (form:SIRForm {id: "SIR_EF_2026"}), (r3:ValidationRule {id: "rule_no_payment"})
MERGE (form)-[:ENFORCES]->(r3);

MATCH (f5:FormField {id: "part3_dob"}), (r4:ValidationRule {id: "rule_senior_priority"})
MERGE (f5)-[:TRIGGERS_FLAG]->(r4);

// Official Legal Guidance linking to Fields
MATCH (f1:FormField {id: "part1_name"}), (g1:OfficialGuidance {id: "guidance_part1"})
MERGE (f1)-[:EXPLAINED_BY]->(g1);

MATCH (f3:FormField {id: "part2a_prev_sir"}), (g2:OfficialGuidance {id: "guidance_part2a"})
MERGE (f3)-[:EXPLAINED_BY]->(g2);

MATCH (f4:FormField {id: "part2b_ancestor_sir"}), (g3:OfficialGuidance {id: "guidance_part2b"})
MERGE (f4)-[:EXPLAINED_BY]->(g3);

MATCH (p3:FormPart {id: "part_3"}), (g4:OfficialGuidance {id: "guidance_part3_fallback"})
MERGE (p3)-[:BACKED_BY_LEGAL_CLAUSE]->(g4);

// Multilingual Explanations linking to Guidance
MATCH (g1:OfficialGuidance {id: "guidance_part1"}), (l1_kn:LanguageExplanation {id: "exp_part1_kn"}), (l1_hi:LanguageExplanation {id: "exp_part1_hi"})
MERGE (g1)-[:AVAILABLE_IN]->(l1_kn)
MERGE (g1)-[:AVAILABLE_IN]->(l1_hi);

MATCH (g2:OfficialGuidance {id: "guidance_part2a"}), (l2_kn:LanguageExplanation {id: "exp_part2a_kn"})
MERGE (g2)-[:AVAILABLE_IN]->(l2_kn);

MATCH (g3:OfficialGuidance {id: "guidance_part2b"}), (l2b_kn:LanguageExplanation {id: "exp_part2b_kn"})
MERGE (g3)-[:AVAILABLE_IN]->(l2b_kn);

MATCH (g4:OfficialGuidance {id: "guidance_part3_fallback"}), (l3_kn:LanguageExplanation {id: "exp_part3_kn"}), (l3_hi:LanguageExplanation {id: "exp_part3_hi"})
MERGE (g4)-[:AVAILABLE_IN]->(l3_kn)
MERGE (g4)-[:AVAILABLE_IN]->(l3_hi);


// ============================================================================
// STEP 10: VERIFICATION & DEMO CYPHER QUERIES (Run these to show judges)
// ============================================================================

// Query 1: Show the complete form hierarchy with parts, fields, and rules
// MATCH path = (f:SIRForm)-[:HAS_PART]->(p:FormPart)-[:HAS_FIELD]->(fld:FormField)
// RETURN path LIMIT 25;

// Query 2: Retrieve the exact statutory explanation and Kannada voice prompt for Part 2A
// MATCH (p:FormPart {id: 'part_2a'})-[:HAS_FIELD]->(f:FormField {id: 'part2a_prev_sir'})
//       -[:EXPLAINED_BY]->(g:OfficialGuidance)
//       -[:AVAILABLE_IN]->(l:LanguageExplanation {lang: 'kn'})
// RETURN p.title AS Part, f.name AS Field, g.legal_basis AS Law, l.plain_speech AS KannadaVoice;

// Query 3: Demonstrate the Fallback Route (When previous records are not found)
// MATCH (p2a:FormPart {id: 'part_2a'})-[:IF_NOT_FOUND]->(p2b:FormPart)-[:FALLBACK_ROUTE]->(p3:FormPart)
// MATCH (p3)-[:BACKED_BY_LEGAL_CLAUSE]->(g:OfficialGuidance)-[:AVAILABLE_IN]->(l:LanguageExplanation {lang: 'kn'})
// RETURN p3.title AS FallbackDestination, g.official_text AS LegalInstruction, l.plain_speech AS CitizenGuidance;
