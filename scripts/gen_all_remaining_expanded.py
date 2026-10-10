import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated: {path}")

def gen_remaining():
    # ==========================================
    # 03. Police & Uniformed Expanded
    # ==========================================
    write_file("03_Assam_Police_SLPRB/APRO_Communication_Radio/SYLLABUS.md", """# APRO Sub-Inspector & Constable (Communication / Radio) - Syllabus

**Organization:** Assam Police Radio Organisation (APRO)  
**Conducting Body:** SLPRB Assam

---

## 1. Technical Physics & Electronics (10+2 / Diploma Standard)
* **Mechanics & Waves:** Simple harmonic motion, wave equations, sound waves, Doppler effect.
* **Electromagnetism:** Coulomb's Law, Gauss's Law, capacitors, Biot-Savart Law, Ampere's Law, Faraday's laws of electromagnetic induction, AC circuits, resonance.
* **Electromagnetic Waves & Propagation:** EM wave spectrum, ground wave, sky wave, space wave propagation, ionospheric layers, antennas (dipole, Yagi-Uda basics).
* **Semiconductor Physics & Digital Electronics:** P-N junction diode, Zener diode, BJT characteristics, logic gates (AND, OR, NOT, NAND, NOR, XOR), Boolean algebra, flip-flops, modulation (AM, FM, PM), demodulation, digital communication basics (PCM, ASK, FSK).

---

## 2. General Knowledge, Mathematics & English
* Mathematics (Algebra, Coordinate Geometry, Trigonometry, Matrices, Differential Calculus basics).
* General Knowledge of Assam and India, reasoning, and English grammar.
""")

    write_file("03_Assam_Police_SLPRB/APRO_Communication_Radio/EXAM_PATTERN.md", """# APRO Communication - Exam Pattern

* **Stage 1 (Written Exam):** 100 Marks (50 Marks Technical Physics/Maths + 50 Marks GK/English/Reasoning).
* **Stage 2 (PST & PET):** Physical fitness and running test.
* **Stage 3 (Practical / Trade Test):** For specialized craft/radio operator posts.
""")

    write_file("03_Assam_Police_SLPRB/Prisons_Jailer_Jail_Warder/SYLLABUS.md", """# Assam Prisons Department (Jailer, Assistant Jailer, Jail Warder) - Syllabus

**Department:** Directorate of Prisons, Govt. of Assam

---

## 1. Jailer & Assistant Jailer (Graduate Level)
* **Written Examination (100 Marks / 100 MCQs):**
  1. Indian Constitution & Human Rights, Prison Administration & Criminology basics.
  2. History and Geography of Assam and India.
  3. General English & Reading Comprehension.
  4. Mental Ability, Logical Reasoning & Quantitative Aptitude.
  5. Current National & State Affairs.

---

## 2. Jail Warder (Male & Female - HSLC Level)
* Elementary Mathematics, General English, Assam GK, Reasoning, and Physical Fitness.
""")

    write_file("03_Assam_Police_SLPRB/Prisons_Jailer_Jail_Warder/EXAM_PATTERN.md", """# Assam Prisons Recruitment - Selection Pattern

* **Written Test:** 100 Marks (Jailer) / 50 Marks (Jail Warder).
* **Physical Standards & PET:** Running, long jump, chin-ups.
* **Viva-Voce:** For Jailer/Assistant Jailer posts.
""")

    write_file("03_Assam_Police_SLPRB/Excise_Inspector_Constable/SYLLABUS.md", """# Assam Excise Department (Inspector of Excise, Assistant Inspector & Excise Constable) - Syllabus

---

## 1. Inspector & Assistant Inspector of Excise
* **Written Exam (100 Marks):**
  * Assam Excise Act & Rules basics, Narcotic Drugs and Psychotropic Substances (NDPS) Act.
  * Assam History, Geography, Polity, Economy.
  * General English, Quantitative Aptitude & Analytical Reasoning.
  * Current Events, National Policies.

---

## 2. Excise Constable
* HSLC Standard Mathematics, General English, General Science, Assam GK, Reasoning.
""")

    write_file("03_Assam_Police_SLPRB/Excise_Inspector_Constable/EXAM_PATTERN.md", """# Excise Recruitment - Pattern

* Written Exam (OMR Based) + PST/PET (Physical fitness) + Document Verification.
""")

    # ==========================================
    # 04. Health Expanded (NHM CHO)
    # ==========================================
    write_file("04_Health_DME_DHS/NHM_Community_Health_Officer_CHO/SYLLABUS.md", """# NHM Assam Community Health Officer (CHO) - Official Syllabus

**Recruiting Agency:** National Health Mission (NHM Assam)  
**Eligibility:** B.Sc (Nursing) / Post Basic B.Sc (Nursing) with integrated Certificate in Community Health (BPCCHN) or Ayurvedic Medical Graduate (BAMS).

---

## 1. Examination Syllabus (100 MCQs / 100 Marks)

### Section A: Community Health Nursing & Primary Health Care (60 Marks)
* **National Health Programs:** RMNCH+A, National Tuberculosis Elimination Program (NTEP), National Vector Borne Disease Control Program (NVBDCP), National Leprosy Eradication Program (NLEP), Non-Communicable Diseases (NCD) screening (Hypertension, Diabetes, Oral/Breast/Cervical Cancers).
* **Maternal Health:** Antenatal care, identification of high-risk pregnancies, essential obstetric care, postpartum care.
* **Child Health & Immunization:** Universal Immunization Program (UIP), cold chain maintenance, IMNCI guidelines, management of diarrhea and acute respiratory infections.
* **Family Planning & Contraceptive Methods:** Spacing methods, permanent methods, emergency contraception.
* **Epidemiology & Communicable Diseases:** Transmission dynamics, surveillance, outbreak investigation, water and vector-borne diseases.
* **Ayushman Bharat Health & Wellness Centres (HWC):** Roles & responsibilities of CHO, teleconsultation (e-Sanjeevani), basic diagnostic tests at Sub-centre level.

### Section B: General Medical & Pharmacology Knowledge (20 Marks)
* Common essential drugs list, emergency management of snake bites, burns, anaphylaxis, shock, minor ailments management.

### Section C: General Awareness, Reasoning & English (20 Marks)
* Assam Health schemes, National Current Affairs, basic reasoning and reading comprehension.
""")

    write_file("04_Health_DME_DHS/NHM_Community_Health_Officer_CHO/EXAM_PATTERN.md", """# NHM Assam CHO - Exam Pattern

* **Total Marks:** 100 Marks (100 MCQs).
* **Duration:** 2 Hours.
* **Negative Marking:** No negative marking (or 0.25 as specified).
* **Selection:** Direct merit based on CBT / OMR Written Exam.
""")

    # ==========================================
    # 05. Education Expanded (Universities)
    # ==========================================
    write_file("05_TET_Education/State_Universities_Non_Teaching_Staff/SYLLABUS.md", """# Assam State Universities Non-Teaching Staff Recruitment - Syllabus

**Universities:** Gauhati University, Dibrugarh University, Cotton University, Bodoland University, Bhattadev University, Madhabdev University, Kumar Bhaskar Varma Sanskrit & Ancient Studies University.

---

## 1. Junior Administrative Assistant (JAA) / Junior Assistant
* **General English (30 Marks):** Grammar, vocabulary, sentence correction, drafting and official correspondence.
* **General Awareness & Assam Affairs (30 Marks):** Assam history, geography, Higher education system in Assam & India, current events.
* **Quantitative Aptitude & Reasoning (20 Marks):** Arithmetic, percentages, ratios, logical deductions.
* **Computer Fundamentals & Office Automation (20 Marks):** MS Word, MS Excel, internet, email drafting.

---

## 2. Technical Assistant & Laboratory Assistant
* Basic Science / Domain subject (Physics, Chemistry, Botany, Zoology, Computer Science) up to Degree standard + General Awareness.
""")

    write_file("05_TET_Education/State_Universities_Non_Teaching_Staff/EXAM_PATTERN.md", """# State Universities Staff - Exam Scheme

* **Written Test:** 100 Marks.
* **Computer Practical & Typing Test:** 50 Marks.
* **Interview:** (Where applicable for technical posts).
""")

    # ==========================================
    # 08. PnRD Expanded
    # ==========================================
    write_file("08_PnRD_Rural_Development/ASRLM_State_Rural_Livelihoods/SYLLABUS.md", """# Assam State Rural Livelihoods Mission (ASRLM - Jeevika) - Syllabus

**Target Posts:** Block Program Manager (BPM), District Functional Expert (DFE), Project Executive, Block Coordinator.

---

## 1. Written Examination Topics (100 Marks)
1. **Rural Livelihoods & Social Mobilization (30 Marks):**
   * DAY-NRLM core principles, Self Help Groups (SHGs), Village Organizations (VOs), Cluster Level Federations (CLFs).
   * Micro-finance, Community Investment Fund (CIF), Vulnerability Reduction Fund (VRF).
   * Farm and Non-farm livelihoods, organic farming clusters, skill development (DDU-GKY, RSETI).
2. **General Knowledge & Assam Rural Scenario (25 Marks):**
   * Rural demographic profile of Assam, geography, tribal communities, agricultural patterns.
   * State and Central Govt poverty alleviation schemes.
3. **General English & Communication (20 Marks):** Comprehension, reporting, drafting.
4. **Logical Reasoning & Quantitative Aptitude (25 Marks):** Data interpretation, arithmetic, analytical puzzles.
""")

    write_file("08_PnRD_Rural_Development/ASRLM_State_Rural_Livelihoods/EXAM_PATTERN.md", """# ASRLM Recruitment - Exam Pattern

* **Stage 1:** Written Test (100 Marks).
* **Stage 2:** Group Discussion (GD) & Personal Interview (for Managerial / Expert posts).
""")

    write_file("08_PnRD_Rural_Development/Accredited_Junior_Engineers/SYLLABUS.md", """# P&RD Accredited Engineer & Junior Engineer - Syllabus

---

## 1. Domain Engineering (Civil Engineering - 70 Marks)
* Building Construction, Rural Roads (PMGSY guidelines), Estimation & Costing, RCC Structures, Rural Water Supply & Sanitation (Swachh Bharat Mission Grameen), Soil Mechanics, Surveying.

## 2. General Studies & Panchayati Raj (30 Marks)
* Assam Panchayat Act 1994, MGNREGA works manual, PMAY-G housing guidelines, basic reasoning and general awareness.
""")

    write_file("08_PnRD_Rural_Development/Accredited_Junior_Engineers/EXAM_PATTERN.md", """# P&RD Engineers - Exam Pattern

* **Written Test:** 100 Marks (70 Core + 30 General).
""")

    # ==========================================
    # 09. Transport & IWT
    # ==========================================
    write_file("09_Transport_IWT_ASTC/Inland_Water_Transport_IWT/SYLLABUS.md", """# Inland Water Transport (IWT Assam) - Syllabus

**Target Posts:** Section Assistant, Master, Engine Driver, Lascar, Ghat Incharge, Junior Engineer (Naval/Mechanical).

---

## 1. Navigation & Marine Mechanics (For Marine Cadres)
* River navigation rules on Brahmaputra & Barak (National Waterway 2 & National Waterway 16).
* Marine diesel engine operation, cooling, fuel injection, daily maintenance, propeller systems, steering gear.
* Life-saving appliances (life jackets, lifebuoys), fire fighting on vessels, emergency collision/grounding protocols.

## 2. General Studies & Arithmetic
* Rivers of Assam, bridges, ports/terminals (Pandu, Dhubri, Neamati, Silghat), basic arithmetic, English, and reasoning.
""")

    write_file("09_Transport_IWT_ASTC/Inland_Water_Transport_IWT/EXAM_PATTERN.md", """# IWT Assam - Selection Pattern

* Written Test (100 Marks) + Practical Vessel Handling / Trade Test + Medical Fitness.
""")

    # ==========================================
    # 10. Corporations & State Enterprises
    # ==========================================
    write_file("10_Corporations_Cooperatives_Boards/AGCL_Gas_Company_APL_Petrochem/SYLLABUS.md", """# Assam Gas Company Ltd (AGCL) & Assam Petro-chemicals Ltd (APL) - Syllabus

**Target Posts:** Graduate Engineer Trainee (GET), Management Trainee, Junior Officer, Plant Operator.

---

## 1. Technical / Domain Section (70 Marks)
* **Chemical Engineering / Plant Operation:** Fluid mechanics, chemical reaction engineering, heat transfer, mass transfer (distillation, absorption), thermodynamics, petrochemical technology (Methanol, Formaldehyde synthesis), process instrumentation and control, plant safety.
* **Mechanical / Electrical / Instrumentation Engineering:** Core engineering gate syllabus concepts.

## 2. General Aptitude (30 Marks)
* Quantitative Aptitude, Logical Reasoning, General English, General Knowledge of Assam oil and gas sector (Digboi, Duliajan, Numaligarh, Namrup).
""")

    write_file("10_Corporations_Cooperatives_Boards/AGCL_Gas_Company_APL_Petrochem/EXAM_PATTERN.md", """# AGCL & APL - Exam Pattern

* **Written Test:** 100 Marks CBT.
* **Interview:** For Executive / Trainee positions.
""")

    write_file("10_Corporations_Cooperatives_Boards/Sericulture_Handloom_Textiles/SYLLABUS.md", """# Sericulture & Handloom Textiles Assam (Demonstrator & Inspector) - Syllabus

---

## 1. Sericulture (Muga, Eri, Mulberry, Tasar)
* Silkworm biology, host plants (Som, Soalu for Muga; Castor, Kesseru for Eri; Mulberry), silkworm rearing techniques, disease management (Pebrine, Flacherie, Grasserie, Muscardine), grainage operations, cocoon harvesting, silk reeling and spinning.

## 2. Handloom & Textiles
* Textile fibers, yarn manufacturing, weaving technology (Handloom mechanisms, Jacquard, Dobby, Fly shuttle looms), traditional Assamese textiles (Gamosa, Mekhela Chador, Dokhona, Eri chador), dyeing and printing.

## 3. General Awareness & Language
* Assam geography, culture, basic mathematics, and Assamese/English language.
""")

    write_file("10_Corporations_Cooperatives_Boards/Sericulture_Handloom_Textiles/EXAM_PATTERN.md", """# Sericulture & Handloom - Selection Scheme

* **Written OMR Test:** 100 Marks.
* **Practical Demonstration:** 25 Marks.
""")

    # ==========================================
    # 11. Revenue & Disaster Management
    # ==========================================
    write_file("11_Revenue_Disaster_Management/Lot_Mandal_Patwari_Recruitment/SYLLABUS.md", """# Assam Lot Mandal (Patwari / Land Record Cadre) - Official Syllabus

**Recruiting Authority:** Directorate of Land Records & Surveys / Respective District Commissioner (DC) Offices

---

## 1. Written Examination (100 Marks / 100 MCQs)
* **General English (25 Marks):** Grammar, vocabulary, comprehension, error spotting.
* **General Knowledge & Assam Affairs (25 Marks):** Assam history, geography, land tenure systems, administrative divisions.
* **General Mathematics & Mensuration (25 Marks):** Arithmetic, Area and perimeter calculations of land plots, geometry, unit conversions (Bigha, Katha, Lessa, Acre, Hectare).
* **Proficiency in Official Language (Assamese/Bengali/Bodo) (25 Marks):** Grammar, translation, official terminologies.

---

## 2. Computer Proficiency & Survey Practical Test (50 Marks)
* **Computer Test:** MS Word, MS Excel, Geographic Information System (GIS) and Dharitree portal operations.
* **Survey Practical:** Chain survey, Plane table survey, Prismatic compass survey, calculation of area from field book.
""")

    write_file("11_Revenue_Disaster_Management/Lot_Mandal_Patwari_Recruitment/EXAM_PATTERN.md", """# Assam Lot Mandal - Exam Pattern

* **Stage 1:** Written OMR Examination (100 Marks).
* **Stage 2:** Computer Proficiency & Practical Survey Test (50 Marks).
* **Merit List:** Combined score of Stage 1 + Stage 2.
""")

    write_file("11_Revenue_Disaster_Management/ASDMA_Disaster_Management/SYLLABUS.md", """# Assam State Disaster Management Authority (ASDMA) - Syllabus

**Target Posts:** Field Officer (Disaster Management) at Revenue Circle level, Project Officer.

---

## 1. Disaster Management & Geography of Assam (40 Marks)
* Disaster Management Act 2005, Assam State Disaster Management Policy.
* Hazards in Assam: Floods, Riverbank Erosion, Earthquakes (Seismic Zone V), Landslides, Urban Flooding, Forest Fires, Cyclones/Storms.
* Disaster preparedness, early warning systems, search and rescue, relief management, Incident Response System (IRS), Sendai Framework.

## 2. General Studies, Reasoning & English (60 Marks)
* Assam History, Polity, Geography, Quantitative Aptitude, Logical Reasoning, English Comprehension.
""")

    write_file("11_Revenue_Disaster_Management/ASDMA_Disaster_Management/EXAM_PATTERN.md", """# ASDMA Field Officer - Exam Scheme

* **Written Test:** 100 Marks.
* **Computer Test & Interview:** 50 Marks.
""")

    # ==========================================
    # 12. Legislative Assembly Secretariat
    # ==========================================
    write_file("12_Legislative_Assembly_Secretariat/Junior_Admin_Assistant_JAA/SYLLABUS.md", """# Assam Legislative Assembly Secretariat (JAA & Typist) - Syllabus

---

## 1. Written Examination (100 Marks / 100 MCQs)
* **General English (30 Marks):** Grammar, drafting, vocabulary, comprehension.
* **General Knowledge & Parliamentary Affairs (30 Marks):** Constitution of India, State Legislature structure, Rules of Procedure and Conduct of Business in Assam Legislative Assembly, Assam History and Culture.
* **General Mathematics & Aptitude (20 Marks):** Arithmetic, reasoning, numerical series.
* **Assamese / Regional Language (20 Marks):** Official terminology, grammar, translation.

---

## 2. Computer Practical & Typing Test
* English and Assamese typing on computer (speed and accuracy test).
""")

    write_file("12_Legislative_Assembly_Secretariat/Junior_Admin_Assistant_JAA/EXAM_PATTERN.md", """# Assam Legislative Assembly JAA - Selection Scheme

* **Stage 1:** Written Screening Test (100 Marks).
* **Stage 2:** Computer Typing Test (50 Marks).
* **Stage 3:** Viva-Voce (25 Marks).
""")

    write_file("12_Legislative_Assembly_Secretariat/Language_Reporters_Translators/SYLLABUS.md", """# Assam Legislative Assembly Language Reporter & Translator - Syllabus

---

## 1. Language Reporter (Assamese, English, Bengali)
* Shorthand Speed Test at 140 / 120 words per minute in the respective language.
* Transcription test on computer.
* Written Test on Grammar, Parliamentary Terminology, and General Knowledge.

## 2. Translation Officer
* Translation of legislative bills, proceedings, questions, and administrative documents between English and Assamese/Bengali/Bodo.
""")

    write_file("12_Legislative_Assembly_Secretariat/Language_Reporters_Translators/EXAM_PATTERN.md", """# Reporter & Translator - Exam Pattern

* **Phase 1:** Speed Shorthand / Translation Practical Test (100 Marks).
* **Phase 2:** Written Language Proficiency Test (50 Marks).
* **Phase 3:** Interview (25 Marks).
""")

gen_remaining()
print("All remaining expanded exam files generated!")
