import os
import json

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated: {path}")

# ==========================================
# 1. APSC Engineering & Specialized
# ==========================================
def gen_apsc_other():
    # AE / JE
    write_file("01_APSC/AE_JE_Engineering/SYLLABUS.md", """# APSC Assistant Engineer (AE) & Junior Engineer (JE) - Official Syllabus

**Recruiting Authority:** Assam Public Service Commission (APSC)  
**Departments:** Public Works Department (PWD), Water Resources Department (WRD), Public Health Engineering (PHE), Irrigation Department.

---

## 1. Exam Scheme & Structure
The Screening Examination / Written Test consists of two papers:
1. **Paper I:** General Studies (100 Marks / 100 MCQs / 2 Hours)
2. **Paper II:** Core Engineering Discipline (Civil / Mechanical / Electrical / Agricultural / Chemical) (100 Marks / 100 MCQs / 2 Hours)

---

## 2. Paper I: General Studies (Common to all Disciplines)
* **General Awareness & Current Affairs:** National, International, and Assam State specific current developments, sports, awards, science & technology updates.
* **History & Culture of Assam:** Ancient Kamarupa, Ahom dynasty, British period, Freedom movement in Assam, folk culture, festivals, literature, and monuments.
* **Geography of Assam & India:** Rivers of Assam (Brahmaputra & Barak), topography, natural resources, climate, wetlands, national parks & sanctuaries.
* **Indian Constitution & Polity:** Preamble, Fundamental Rights & Duties, Executive, Judiciary, Assam Administration, Sixth Schedule.
* **Basic Quantitative Aptitude & Reasoning:** Arithmetic, percentages, ratio-proportion, time & work, data interpretation, series, analogies, syllogism.
* **General English:** Synonyms, antonyms, sentence correction, prepositions, comprehension, idioms & phrases.

---

## 3. Paper II: Core Discipline Syllabus

### A. Civil Engineering
1. **Building Materials & Construction:** Stones, bricks, cement, concrete, mortar, timber, steel, modern composites.
2. **Solid Mechanics / Strength of Materials:** Stress, strain, Mohr's circle, shear force & bending moment diagrams, deflection of beams, torsion, columns & struts.
3. **Structural Analysis:** Determinate & indeterminate structures, truss analysis, moment distribution method, slope deflection, matrix methods.
4. **Design of RC & Steel Structures:** Limit state design of beams, slabs, columns, footings, prestressed concrete; Steel tension/compression members, welded/bolted connections, plate girders.
5. **Fluid Mechanics & Hydraulics:** Fluid statics, kinematics, Bernoulli's equation, pipe flow, open channel flow (Manning/Chezy), hydraulic jump, pumps & turbines.
6. **Hydrology & Water Resources:** Hydrological cycle, rainfall-runoff, hydrographs, flood routing, irrigation methods, canal design, gravity dams, spillways, flood mitigation in Assam.
7. **Geotechnical Engineering / Soil Mechanics:** Soil properties, classification, compaction, consolidation, shear strength, bearing capacity, shallow & deep foundations, slope stability, retaining walls.
8. **Transportation Engineering:** Highway geometric design, pavement design (flexible & rigid), traffic engineering, highway materials (bitumen/aggregates), railways & airport engineering basics.
9. **Environmental Engineering:** Water supply systems, water quality parameters, water treatment processes, wastewater treatment (activated sludge, trickling filter), solid waste management, air pollution.
10. **Surveying & Estimation:** Chain, compass, leveling, theodolite, total station, GPS/GIS basics, rate analysis, estimation & costing, specifications.

### B. Mechanical Engineering
1. **Thermodynamics & Heat Transfer:** Laws of thermodynamics, Carnot cycle, entropy, heat conduction, convection, radiation, heat exchangers.
2. **IC Engines & Power Plant:** Otto, Diesel, Dual cycles, 2-stroke/4-stroke engines, fuel injection, cooling, steam turbines, gas turbines, boilers.
3. **Fluid Mechanics & Machinery:** Flow through pipes, boundary layer theory, Pelton, Francis, Kaplan turbines, centrifugal and reciprocating pumps.
4. **Theory of Machines & Vibrations:** Kinematic pairs, gears, gear trains, flywheels, governors, balancing, free and forced single-degree-of-freedom vibrations.
5. **Machine Design:** Design of shafts, keys, couplings, springs, bearings, welded & threaded joints, fatigue failure (S-N curve).
6. **Manufacturing Science & Materials:** Casting, welding, forming, machining processes, CNC machines, crystal structures, heat treatment of steel, metrology.
7. **Industrial Engineering & Operations Research:** Linear programming, CPM/PERT, inventory control, forecasting, production planning and control.

### C. Electrical Engineering
1. **Circuit Theory & Networks:** KCL, KVL, nodal/mesh analysis, Thevenin, Norton, Superposition, Maximum Power Transfer theorems, AC circuits, transient analysis.
2. **Electromagnetic Fields:** Maxwell's equations, electrostatic and magnetostatic fields, boundary conditions, wave propagation.
3. **Electrical Machines:** DC generators and motors, single-phase and three-phase transformers, 3-phase induction motors, synchronous generators and motors.
4. **Power Systems:** Generation, transmission line parameters, corona, insulators, power cables, load flow analysis, fault analysis, power system protection (relays and circuit breakers).
5. **Control Systems:** Transfer functions, block diagrams, signal flow graphs, Routh-Hurwitz stability, Bode plots, Nyquist plots, Root locus, State space analysis.
6. **Electrical & Electronic Measurements:** Moving coil/iron meters, wattmeters, energy meters, bridges (Wheatstone, Schering, Maxwell), digital multimeters, oscilloscopes.
7. **Analog & Digital Electronics:** Diodes, BJT, MOSFET, Op-Amps, rectifiers, Boolean algebra, logic gates, flip-flops, multiplexers, counters, microprocessors (8085/8086).
8. **Power Electronics:** SCR, MOSFET, IGBT, rectifiers, choppers, inverters, voltage controllers.
""")

    write_file("01_APSC/AE_JE_Engineering/EXAM_PATTERN.md", """# APSC AE / JE - Exam Pattern & Selection Scheme

| Stage | Component | Marks | Duration | Negative Marking |
|---|---|---|---|---|
| **Stage 1: Screening Test** | Paper I: General Studies (MCQ) | 100 Marks (100 Q) | 2 Hours | 0.25 marks |
| | Paper II: Core Engineering (MCQ) | 100 Marks (100 Q) | 2 Hours | 0.25 marks |
| **Stage 2: Viva-Voce / Interview** | Personality & Domain Interview | 37 Marks / 50 Marks | ~20 Mins | - |

* **Total Written Marks:** 200 Marks
* **Interview:** Conducted for candidates qualifying the written cutoff in 1:2 to 1:3 ratio.
""")

    # Forest Ranger
    write_file("01_APSC/Forestry_Services/SYLLABUS.md", """# APSC Forest Ranger & Assam Forest Service (AFS) - Syllabus

**Recruiting Authority:** Assam Public Service Commission (APSC) / Environment & Forest Department

---

## 1. Examination Scheme
* **Compulsory Papers:**
  1. **General English:** 100 Marks (Essay, Precis, Comprehension, Grammar).
  2. **General Knowledge:** 100 Marks (Indian & Assam History, Geography, Environment, Biodiversity, Science, Current Affairs).
* **Optional Subjects (Choose 2 Subjects, 200 Marks each = 400 Marks):**
  * Agriculture, Botany, Chemistry, Computer Science, Engineering (Civil/Mech/Elect/Agri), Environmental Science, Forestry, Geology, Mathematics, Physics, Statistics, Zoology.
* **Interview / Personality Test:** 100 Marks.
* **Walking / Physical Endurance Test:** 
  * Male: 25 km walk in 4 hours
  * Female: 16 km walk in 4 hours
  * Followed by Medical Examination.
""")

    write_file("01_APSC/Forestry_Services/EXAM_PATTERN.md", """# APSC Forest Ranger - Pattern & Selection

* **Total Written Exam:** 600 Marks (2 Compulsory @ 100 + 2 Optionals @ 200)
* **Interview:** 100 Marks
* **Physical Test:** 25 km (Male) / 16 km (Female) walk within 4 hours (Mandatory Qualifying).
""")

    # Research Assistant
    write_file("01_APSC/Research_Assistant_Specialized/SYLLABUS.md", """# APSC Research Assistant (Planning Services) - Syllabus

**Department:** Transformation & Development Department, Govt. of Assam

---

## Written Exam Structure
* **Total Marks:** 200 Marks (Single / Two-part OMR Screening test)
* **Topics Covered:**
  1. **Economics & Planning:** Principles of Micro & Macroeconomics, Economic Growth & Development, Indian Planning history, NITI Aayog, Fiscal & Monetary Policies, Public Finance, State Budgeting, Industrial & Agricultural Policies.
  2. **Statistics & Data Analytics:** Measures of Central Tendency, Dispersion, Probability, Sampling Techniques, Correlation & Regression, Index Numbers, Time Series, National Income Accounting, Census data of Assam & India.
  3. **General Knowledge & Assam Affairs:** Assam Economy, Tea Industry, Oil & Gas, Agriculture, Infrastructure, Govt of Assam Flagship Schemes (Orunodoi, Atmanirbhar Assam, Mission Basundhara), Geography & History of Assam.
  4. **General English & Logical Reasoning:** Comprehension, vocabulary, verbal reasoning, data interpretation.
""")

    write_file("01_APSC/Research_Assistant_Specialized/EXAM_PATTERN.md", """# APSC Research Assistant - Exam Pattern

* **Written Test:** 200 MCQs / 200 Marks (2 Hours duration).
* **Negative Marking:** 0.25 marks per wrong answer.
* **Viva-Voce / Interview:** Conducted for shortlisted candidates.
""")

# ==========================================
# 2. ADRE (Assam Direct Recruitment)
# ==========================================
def gen_adre():
    # Grade III Graduate
    write_file("02_ADRE_SLRC/Grade_III_Graduate/SYLLABUS.md", """# ADRE Grade III (Graduate / Bachelor Degree Level) - Official Syllabus

**Recruiting Body:** State Level Recruitment Commission (SLRC) for Class III Posts / ASSEB  
**Target Posts:** Junior Assistant, Field Assistant, Lower Division Assistant (LDA), Computer Operator, Statistical Assistant, Tax Collector (Graduate posts) across all Assam Government Departments.

---

## 1. Subject-Wise Syllabus Breakdown

### A. Social Studies (Class X Standard)
* **History:** Freedom Struggle of India, Major Dynasties of India, Indian National Movement.
* **History of Assam:** Ancient Kamarupa, Ahom rule (Swargadeos, Battle of Saraighat, administration), Moamoria Rebellion, British annexation, 1857 in Assam, freedom fighters of Assam (Maniram Dewan, Kanaklata, Kushal Konwar, Bhogeswari Phukanani, Gopinath Bordoloi).
* **Geography:** Physical geography of India, rivers, mountains, minerals, climate.
* **Geography of Assam:** Rivers of Assam (Brahmaputra & Barak systems), National Parks & Wildlife Sanctuaries, wetlands (Deepor Beel), district topography, natural resources (petroleum, coal, tea, timber).
* **Civics & Indian Polity:** Constitution of India, Preamble, Fundamental Rights & Duties, President, Prime Minister, Governor, Assam Legislative Assembly, Panchayati Raj System.
* **Economics:** Basic economic concepts, Five Year Plans, NITI Aayog, Assam's Economy (Tea, Sericulture, Agriculture, Tourism, State Government Schemes).

### B. General Knowledge & Current Affairs
* Latest National & International Events, Summits, Sports, Honours & Awards.
* Assam Specific GK: Eminent personalities, Sahitya Akademi winners, Sangeet Natak Akademi winners, Jnanpith awardees (Birendra Kumar Bhattacharya, Mamoni Raisom Goswami), State symbols (Animal, Bird, Tree, Flower, State Anthem 'O Mur Apunar Dekh').
* Schemes of Assam Government (Mission Basundhara, Orunodoi, Nijut Moina, Pragyan Bharati, Amrit Brikshya Andolan).

### C. General Mathematics & Quantitative Aptitude (Class X Standard)
* Number System, Simplification, HCF & LCM.
* Fractions, Decimals, Square Roots & Cube Roots.
* Percentage, Ratio & Proportion, Partnership.
* Average, Profit & Loss, Simple Interest & Compound Interest.
* Time & Work, Pipes & Cisterns, Time, Speed & Distance, Boats & Streams.
* Basic Mensuration (Area, Perimeter, Volume of 2D/3D shapes).
* Basic Statistics (Mean, Median, Mode, Data Interpretation charts).

### D. Mental Ability & Logical Reasoning
* **Verbal Reasoning:** Analogy, Classification, Series (Number/Alphabet), Coding-Decoding, Blood Relations, Direction Sense Test, Sitting Arrangement, Syllogism, Venn Diagrams.
* **Non-Verbal Reasoning:** Pattern Completion, Mirror & Water Images, Embedded Figures, Paper Folding/Cutting, Figure Series.

### E. General English
* Spotting Errors, Sentence Improvement, Active & Passive Voice, Direct & Indirect Speech.
* Fill in the Blanks (Prepositions, Articles, Tenses, Modals).
* Synonyms, Antonyms, One Word Substitution, Idioms & Phrases, Spelling errors.
* Reading Comprehension Passages.

### F. Computer Knowledge & Applications
* Computer Fundamentals, Hardware & Software, Operating Systems (Windows/Linux).
* MS Office Suite: MS Word (formatting, mail merge), MS Excel (formulas, cell referencing, charts), MS PowerPoint.
* Internet, Email, Cyber Security Basics, Networking concepts, Shortcuts.
""")

    write_file("02_ADRE_SLRC/Grade_III_Graduate/EXAM_PATTERN.md", """# ADRE Grade III (Graduate Level) - Exam Pattern & Scheme

## Stage 1: Written Examination (OMR Based MCQ)
* **Total Questions:** 150 Questions (or 100/150 format depending on SLRC notice)
* **Total Marks:** 150 Marks (1 mark per question)
* **Duration:** 2 Hours (120 Minutes) / 2.5 Hours
* **Negative Marking:** **0.25 marks deducted** for each incorrect answer.
* **Language Medium:** English, Assamese, Bodo, Bengali.

| Section | Subject | Standard | Approx Marks |
|---|---|---|---|
| Section A | Social Studies & Assam Affairs | Class X Standard | 30 Marks |
| Section B | General Knowledge & Current Events | National & State | 30 Marks |
| Section C | General Mathematics | Class X Standard | 30 Marks |
| Section D | Mental Ability & Logical Reasoning | Analytical | 25 Marks |
| Section E | General English | High School Level | 25 Marks |
| Section F | Computer Awareness | Applied Basics | 10 Marks |

---

## Stage 2: Computer Proficiency / Skill Test
* Shortlisted candidates from Stage 1 (usually 1:2 ratio) are called for Computer Practical Test:
  * Typing Speed (English & Assamese/Regional).
  * Practical tasks in MS Word, MS Excel, MS PowerPoint (Formatting, Formulas, Tables).
  * Maximum Marks: 25 - 50 Marks (Qualifying / Added to Merit depending on SLRC Rules).
""")

    # Grade III Higher Secondary (10+2)
    write_file("02_ADRE_SLRC/Grade_III_HS_Level/SYLLABUS.md", """# ADRE Grade III (Higher Secondary / HSSLC 10+2 Level) - Syllabus

**Target Posts:** Data Entry Operator (DEO), Junior Assistant (HSSLC Level), Field Assistant, Typist.

---

## 1. Syllabus Sections (HSLC / Class X Standard)
1. **Social Studies & Assam Context:**
   * Freedom movement, Assam history (Ahoms, British rule, freedom fighters).
   * Geography of Assam & North East (Rivers, hills, national parks, flora & fauna).
   * Indian Polity, Constitution basics, Panchayati Raj.
2. **General Knowledge:**
   * Assam culture, festivals (Bihu, Ali-Aye-Ligang, etc.), historical monuments, state symbols.
   * Current national and state events, sports, awards.
3. **General Mathematics:**
   * Number system, LCM/HCF, Simplification, Percentages, Ratio-Proportion, Profit-Loss, Simple Interest, Average, Time-Work, Speed-Time-Distance, Area & Perimeter.
4. **Mental Ability & Logical Reasoning:**
   * Series completion, coding-decoding, blood relations, direction test, Venn diagrams, odd one out, analogies.
5. **General English:**
   * Tenses, Prepositions, Articles, Voice Change, Narration, Vocabulary (Synonyms/Antonyms), Sentence Correction, Reading Comprehension.
""")

    write_file("02_ADRE_SLRC/Grade_III_HS_Level/EXAM_PATTERN.md", """# ADRE Grade III (HS Level) - Exam Pattern

* **Total Marks:** 150 Marks
* **Number of Questions:** 150 Objective MCQs (1 Mark each)
* **Duration:** 2 Hours
* **Negative Marking:** 0.25 marks per wrong answer
* **Stage 2:** Computer Proficiency / Typing Skill Test.
""")

    # Grade III Driver
    write_file("02_ADRE_SLRC/Grade_III_Driver/SYLLABUS.md", """# ADRE Grade III (Driver Posts) - Official Syllabus

**Eligibility:** HSLC / Class X with Valid Light Motor Vehicle (LMV) or Heavy Motor Vehicle (HMV) Driving License.

---

## 1. Written Examination Topics
1. **Traffic Rules & Road Signs:** Mandatory road signs, cautionary signs, informatory signs, lane discipline, overtaking rules, parking regulations, Motor Vehicles Act 1988 & Amendments.
2. **Vehicle Maintenance & Motor Mechanics:** Basic engine components, cooling system, lubrication, braking system, battery maintenance, tyre care, dashboard warning lights, emergency breakdown procedures.
3. **Basic Arithmetic (Class VIII - X):** Addition, subtraction, multiplication, division, simple percentages, average, distance-fuel calculations.
4. **General Knowledge & Assam Awareness:** Assam geography, major highways (NH-27, NH-15, etc.), bridges over Brahmaputra (Saraighat, Kolia Bhomora, Bogibeel, Dhola-Sadiya, Naranarayan Setu), basic current affairs.
5. **Basic English & Language:** Common signs, reading vehicle documents, basic words and instructions.
""")

    write_file("02_ADRE_SLRC/Grade_III_Driver/EXAM_PATTERN.md", """# ADRE Grade III (Driver) - Exam Pattern

1. **Stage 1 (Written OMR Test):**
   * Total Marks: 100 Marks (100 MCQs)
   * Negative Marking: 0.25 marks
2. **Stage 2 (Driving Practical Skill Test):**
   * Driving on designated track (H-track, 8-track, parallel parking, slope restart).
   * Mechanical fault finding and road sign viva.
""")

    # Grade IV
    write_file("02_ADRE_SLRC/Grade_IV_HSLC_ClassVIII/SYLLABUS.md", """# ADRE Grade IV (Class VIII & HSLC Passed Posts) - Official Syllabus

**Target Posts:** Peon, Chowkidar, Mali, Ward Boy, Ward Girl, Daftari, Office Attendant, Messenger, Helper.

---

## 1. Subject Breakdown (Class VIII / X Standard)

### A. General Knowledge (Assam & India)
* Assam History: Sukapha, Lachit Borphukan, Chilarai, Kanaklata, Kushal Konwar.
* Assam Geography: Major rivers (Brahmaputra, Barak), Kaziranga & Manas National Parks, District headquarters.
* State symbols of Assam, festivals, Bihu types (Rongali, Kongali, Bhogali).
* Current affairs and prominent personalities of Assam.

### B. General Mathematics (Elementary Level)
* Basic operations: Addition, Subtraction, Multiplication, Division.
* Fractions, Decimals, LCM & HCF.
* Simple Percentages, Profit and Loss, Average, Ratio and Proportion.
* Simple Interest, Distance & Time basics.

### C. Mental Ability & Reasoning (Elementary Level)
* Simple Number and Alphabet Series.
* Odd one out, Picture matching, Relationship puzzles, Directions.

### D. General English (Elementary Level)
* Basic Grammar: Nouns, Pronouns, Verbs, Prepositions, Articles.
* Spelling checks, Plural forms, Opposite words, Simple sentence meanings.

### E. Assamese / Regional Language Knowledge
* Basic reading comprehension, vocabulary, and grammar.
""")

    write_file("02_ADRE_SLRC/Grade_IV_HSLC_ClassVIII/EXAM_PATTERN.md", """# ADRE Grade IV - Exam Pattern & Scheme

* **Total Questions:** 135 Questions (or 100/135 MCQs as per notification)
* **Total Marks:** 135 Marks
* **Duration:** 2 Hours
* **Negative Marking:** **0.25 marks deducted** for each wrong answer.
* **Candidate Categories:**
  1. Category 1: Read up to Class VIII.
  2. Category 2: HSLC (Class 10) or equivalent passed.
* **Selection:** Merit list directly prepared based on Written Examination score (No interview as per Assam Govt Grade IV abolition rules).
""")

# ==========================================
# 3. Assam Police (SLPRB)
# ==========================================
def gen_slprb():
    # SI
    write_file("03_Assam_Police_SLPRB/SI_UB_AB_Commando/SYLLABUS.md", """# Assam Police Sub-Inspector (UB / AB / Commando) - Official Syllabus

**Conducting Authority:** State Level Police Recruitment Board (SLPRB Assam)  
**Official Portal:** [slprbassam.in](https://slprbassam.in)

---

## 1. Written Examination (OMR Based - 100 Marks)
The written exam consists of 100 questions of 1 mark each (Duration: 3 Hours).  
**Negative Marking:** 0.50 (half mark) deducted per wrong answer.

### A. Logical Reasoning, Aptitude & Comprehension
* Analytical reasoning, syllogism, statements & assumptions, blood relations, coding-decoding, seating arrangement, puzzles, cubes & dice.
* Quantitative aptitude: Arithmetic, percentage, ratio, averages, speed-distance-time, data interpretation.
* Reading comprehension and logical deduction.

### B. Matters relating to History and Culture of Assam and India
* History of Assam (Ancient Kamarupa, Ahom rule, Moamoria rebellion, British period, Freedom movement in Assam).
* Culture, heritage, festivals, tribal communities of Assam, literature, folk dances (Bihu, Bagurumba, Jhumur, Sattriya).
* Indian History & Freedom Struggle.

### C. General Knowledge & Current Affairs
* Indian Polity & Constitution (Police administration, Criminal Justice basics, Fundamental Rights).
* Geography of India and Assam (Rivers, wildlife, national parks, natural resources).
* Economy, Science & Technology, Environment.
* National and International current affairs, sports, defense exercises, awards.
""")

    write_file("03_Assam_Police_SLPRB/SI_UB_AB_Commando/EXAM_PATTERN.md", """# Assam Police Sub-Inspector (SI) - Selection Scheme

```mermaid
flowchart TD
    A["Stage 1: Written Exam (100 Marks)"] --> B["Stage 2: PST & PET (Physical 40 Marks)"]
    B --> C["Stage 3: Viva-Voce / Psychometric Test (10 Marks)"]
    C --> D["Final Merit List (Total 150 Marks)"]
```

## Physical Efficiency Test (PET) Details:
* **Male Candidates:**
  * 1600 Meters Race (Max time: 450 seconds / 7.5 mins; points awarded based on time).
  * Long Jump (Minimum 335 cm in 3 attempts; higher distance gives higher marks).
* **Female Candidates:**
  * 800 Meters Race (Max time: 240 seconds / 4 mins).
  * Long Jump (Minimum 244 cm in 3 attempts).
""")

    # Constable
    write_file("03_Assam_Police_SLPRB/Constable_UB_AB_Commando/SYLLABUS.md", """# Assam Police Constable (UB / AB / Commando) - Syllabus

**Target Posts:** Constable (Unarmed Branch & Armed Branch), Commando Battalions, DGCD & CGHG Guardsman.

---

## 1. Written Examination (100 MCQs / 50 Marks - 0.5 Mark each)
* **Duration:** 2 Hours
* **Negative Marking:** No negative marking (or as per specific advertisement notice).

### Topics Covered:
1. **Elementary Arithmetic:** Numbers, LCM/HCF, Simplification, Percentages, Profit-Loss, Time-Work, Speed-Distance, Average.
2. **General English:** Prepositions, Articles, Tense correction, Synonyms, Antonyms, Basic vocabulary.
3. **General Science:** Everyday physics, chemistry, biology, nutrition, diseases, environmental awareness.
4. **Indian History, Assam History & Culture:** Freedom movement in Assam, Ahoms, Bihu, state symbols, historical monuments.
5. **Indian Geography & Assam Geography:** Districts, rivers, national parks, borders.
6. **General Knowledge & Current Affairs:** Basic polity, state government, sports, awards, recent events.
7. **Logical Reasoning & Mental Ability:** Series, patterns, classification, direction, relations.
""")

    write_file("03_Assam_Police_SLPRB/Constable_UB_AB_Commando/EXAM_PATTERN.md", """# Assam Police Constable - Exam Pattern & Physical Standards

1. **Physical Standard Test (PST):** Height and Chest measurement (Qualifying).
2. **Physical Efficiency Test (PET - 40 Marks for AB / 20 Marks for UB):**
   * 3.2 km race (Male) / 1.6 km race (Female).
   * Long jump (Male: 335 cm, Female: 244 cm).
   * Chin-ups / Pull-ups (Male only for Commando/AB).
3. **Written Examination:** 50 Marks (100 questions).
4. **Oral / Viva-Voce / NCC / Extra Qualification:** 5 Marks.
""")

    # Forest Guard & Forester I
    write_file("03_Assam_Police_SLPRB/Forest_Guard_Forester_I/SYLLABUS.md", """# Assam Forest Guard & Forester Grade-I (SLPRB) - Syllabus

**Recruiting Agency:** SLPRB Assam on behalf of Environment and Forest Department, Assam

---

## 1. Forester Grade-I (Graduate Level)
* **Written Exam (100 Marks):**
  1. General Mathematics (Class X level).
  2. General English & Comprehension.
  3. General Knowledge (with special focus on Forest, Wildlife, Biodiversity, National Parks of Assam, Climate Change).
  4. History, Geography & Polity of Assam.
  5. Logical Reasoning & Mental Ability.
* **Physical Test:** 26 km walk in 4 hours (Male) / 16 km walk in 4 hours (Female).

---

## 2. Forest Guard & AFPF Constable (HS / HSLC Level)
* **Written Exam (75 / 100 Marks):**
  1. Elementary Mathematics.
  2. English grammar basics.
  3. Wildlife, environment, geography, and general knowledge of Assam.
  4. Reasoning and mental aptitude.
* **Physical Test:** 26 km walk in 4 hours (Male) / 16 km walk in 4 hours (Female).
""")

    write_file("03_Assam_Police_SLPRB/Forest_Guard_Forester_I/EXAM_PATTERN.md", """# Assam Forest Guard & Forester Grade-I - Selection Pattern

* **Stage 1:** Written Examination (OMR based).
* **Stage 2:** Physical Standard Test (PST) & Physical Endurance Test (Walking test of 26 km for Male / 16 km for Female within 4 hours).
* **Stage 3:** Document Verification & Final Merit List.
""")

    # APRO / Fire Services / Jail Warder
    write_file("03_Assam_Police_SLPRB/APRO_FireServices_JailWarder/SYLLABUS.md", """# Assam Police Radio (APRO), Fire & Emergency Services, Jail Warder, Excise - Syllabus

---

## 1. APRO Constable (Communication)
* In addition to General Knowledge, English, and Arithmetic, questions include:
  * **Physics:** Mechanics, Heat, Sound, Optics, Electricity & Magnetism, Semiconductors, Electromagnetic Waves.
  * **Mathematics (10+2 Level):** Algebra, Trigonometry, Coordinate Geometry, Calculus basics.

---

## 2. Fire & Emergency Services (Fireman, Driver Operator, Station Officer)
* Basic Science (Physics & Chemistry relating to combustion, fire extinguishing methods).
* Arithmetic, General English, Assam GK, Reasoning.
* Driving & pump operation knowledge for Driver Operators.

---

## 3. Jail Warder & Excise Constable
* General English, Elementary Arithmetic, General Science, Assam History & Geography, Indian Polity, Current Affairs, Reasoning.
""")

    write_file("03_Assam_Police_SLPRB/APRO_FireServices_JailWarder/EXAM_PATTERN.md", """# APRO, Fire Services, Jail Warder - Selection Scheme

* **Written Test:** 100 MCQs (50 / 100 Marks depending on cadre).
* **PST & PET:** Physical fitness running and jumping.
* **Trade / Technical Test:** For APRO communication & Fire services equipment handling.
""")

# ==========================================
# 4. Health & Family Welfare (DME / DHS)
# ==========================================
def gen_health():
    # Grade III Technical
    write_file("04_Health_DME_DHS/Grade_III_Technical/SYLLABUS.md", """# Health & Family Welfare Assam (DME, DHS, DHS-FW) Grade III Technical - Syllabus

**Target Posts:** Staff Nurse, Pharmacist, Laboratory Technician, Radiographer, OT Technician, Dialysis Technician, Physiotherapist, ICU Technician, ECG Technician, Ophthalmic Assistant.

---

## 1. Exam Scheme
* **Format:** 100 Objective MCQs (100 Marks) | **Duration:** 2 Hours.
* **Paper Composition:**
  * **Part A: Domain / Technical Knowledge (70% weightage - 70 Questions)**
  * **Part B: General Awareness, English, Mathematics & Reasoning (30% weightage - 30 Questions)**

---

## 2. Technical Domain Syllabus Breakdown

### A. Staff Nurse (GNM / B.Sc Nursing)
1. **Anatomy & Physiology:** Skeletal, muscular, circulatory, respiratory, nervous, digestive, endocrine, urinary, and reproductive systems.
2. **Microbiology & Pathology:** Bacteria, viruses, fungi, sterilization and disinfection, infection control, immunity.
3. **Fundamentals of Nursing:** Nursing process, vital signs, medication administration, wound care, catheterization, CPR, patient safety.
4. **Medical-Surgical Nursing:** Cardiovascular, respiratory, gastrointestinal, neurological disorders, oncology nursing, pre- and post-operative care.
5. **Pharmacology:** Common drug groups, dosage calculations, adverse drug reactions, emergency drugs.
6. **Community Health Nursing:** National health programs, epidemiology, immunization schedule (UIP), primary health care, sanitation.
7. **Midwifery & Obstetrical Nursing:** Antenatal care, stages of labour, management of normal and high-risk pregnancies, newborn care.
8. **Child Health Nursing (Pediatrics):** Growth and development, neonatal resuscitation, common pediatric disorders, IMNCI guidelines.
9. **Mental Health Nursing:** Common psychiatric disorders, therapeutic communication, psychotropic medications.

### B. Pharmacist (D.Pharm / B.Pharm)
1. **Pharmaceutics:** Dosage forms, formulation, packaging, sterilization, calculation of doses.
2. **Pharmaceutical Chemistry:** Inorganic and organic pharmaceutical chemistry, structure-activity relationship, storage conditions.
3. **Pharmacology & Toxicology:** Drugs acting on CNS, ANS, CVS, renal, GIT, antibiotics, chemotherapy, toxicity and antidotes.
4. **Pharmacognosy:** Classification of crude drugs, extraction, medicinal plants.
5. **Hospital & Clinical Pharmacy:** Drug distribution in hospitals, ADR monitoring, drug interactions, patient counseling.
6. **Drug Store & Business Management:** Inventory control, ABC/VED analysis, supply chain.
7. **Pharmaceutical Jurisprudence:** Drugs and Cosmetics Act 1940 & Rules 1945, Pharmacy Act 1948, NDPS Act, DPCO.

### C. Laboratory Technician (DMLT / BMLT)
1. **Hematology & Blood Banking:** Blood cell counts (CBC, TLC, DLC), ESR, hemoglobin estimation, coagulation studies (PT/INR, APTT), ABO & Rh blood grouping, cross-matching, blood component preparation.
2. **Clinical Biochemistry:** Blood glucose, renal function tests (Urea, Creatinine), liver function tests (Bilirubin, SGOT, SGPT, ALP), lipid profile, electrolytes, urinalysis, spectrophotometry, automation.
3. **Medical Microbiology:** Culture media, Gram staining, AFB staining (Ziehl-Neelsen), antibiotic susceptibility testing, bacteriology, virology (HIV, Hepatitis), parasitology (Malaria, Amoeba), mycology.
4. **Histopathology & Cytology:** Tissue processing, fixation, microtomy, H&E staining, Pap smear, FNAC processing.

### D. Radiographer / X-Ray Technician
* Radiation physics, X-ray generation, darkroom techniques, radiographic positioning, radiation protection (ALARA, lead aprons, TLD badges), CT scan and MRI basics.

---

## 3. General Subjects (Part B - 30 Questions)
* **General English:** Grammar, vocabulary, error correction, prepositions.
* **General Mathematics:** Arithmetic (Class X level).
* **General Knowledge & Assam Context:** National health initiatives, geography, history of Assam, current events.
""")

    write_file("04_Health_DME_DHS/Grade_III_Technical/EXAM_PATTERN.md", """# Health DME / DHS Grade III Technical - Exam Pattern

* **Total Marks:** 100 Marks (100 MCQs)
* **Duration:** 2 Hours
* **Negative Marking:** As per specific examination notification.
* **Selection:** 100% based on Written OMR Examination performance.
""")

    # Grade III Non-Technical
    write_file("04_Health_DME_DHS/Grade_III_Non_Technical/SYLLABUS.md", """# Health & Family Welfare Grade III (Non-Technical) - Syllabus

**Target Posts:** Lower Division Assistant (LDA), Store Keeper, Record Keeper, Health Educator, Computer Operator.

---

## Written Exam Syllabus (100 Marks / 100 MCQs)
1. **General Knowledge & Current Affairs (30 Marks):** Assam history, geography, culture, state schemes, Indian constitution, national health programs.
2. **General English (25 Marks):** Grammar, vocabulary, comprehension, error spotting.
3. **General Mathematics (25 Marks):** Arithmetic, percentages, ratio-proportion, simple interest, average, time and work.
4. **Reasoning & Computer Awareness (20 Marks):** Logical reasoning, verbal/non-verbal ability, MS Office, computer basics.
""")

    write_file("04_Health_DME_DHS/Grade_III_Non_Technical/EXAM_PATTERN.md", """# Health Grade III Non-Technical - Exam Pattern

* **Written Test:** 100 Marks
* **Computer Skill Test:** For LDA / Computer Operator posts (Typing and MS Office).
""")

    # Grade IV
    write_file("04_Health_DME_DHS/Grade_IV/SYLLABUS.md", """# Health (DME, DHS, Medical Colleges) Grade IV - Syllabus

**Target Posts:** Ward Boy, Ward Girl, Peon, Ayah, Stretcher Bearer, Dark Room Attendant, Sweeper, Lab Attendant.

---

## Written Exam Syllabus (50 Marks / 50 MCQs or 100 Marks)
* **General Knowledge:** Assam symbols, prominent personalities, festivals, districts, hospitals & health awareness.
* **Elementary Arithmetic:** Basic arithmetic operations, simple calculations.
* **General English & Language:** Basic words, simple comprehension, spelling.
""")

    write_file("04_Health_DME_DHS/Grade_IV/EXAM_PATTERN.md", """# Health Grade IV - Exam Scheme

* **Total Marks:** 50 / 100 Marks
* **Format:** Objective OMR Test
* **Standard:** Class VIII Standard
""")

# ==========================================
# 5. Assam TET & Education
# ==========================================
def gen_tet():
    # LP / UP
    write_file("05_TET_Education/Assam_TET_LP_UP/SYLLABUS.md", """# Assam General & Special TET (Paper I - LP & Paper II - UP) - Official Syllabus

**Conducting Authority:** Assam State School Education Board (ASSEB) / Sarba Shiksha Abhiyan (SSA) Assam

---

## 1. Paper I: Lower Primary (Classes I to V) - 150 Marks / 150 MCQs

### A. Child Development and Pedagogy (30 Marks)
* Understanding Child Development: Physical, cognitive, emotional, and social development.
* Factors influencing development: Heredity and environment.
* Learning process and theories (Piaget, Vygotsky, Bruner, Thorndike).
* Individual differences, inclusive education, addressing children with special needs (CWSN), learning disabilities (Dyslexia, Dysgraphia, etc.).
* Assessment and evaluation: Continuous and Comprehensive Evaluation (CCE), formative & summative assessment, diagnostic and remedial teaching.

### B. Language I (30 Marks) - Assamese / Bodo / Bengali / Hindi / Alternative English / Nepali / Garo / Karbi / Hmar
* Language learning principles, skills of language (LSRW: Listening, Speaking, Reading, Writing).
* Pedagogical approaches to language teaching.
* Reading comprehension unseen passages (prose and poem).
* Grammar: Sandhi, Samasa, Karak, Bibhakti, Synonyms, Antonyms, Idioms, Proverbs in the regional language.

### C. Language II: English (30 Marks)
* Development of English language skills (LSRW).
* Methods & approaches to English language teaching.
* Reading Comprehension (Prose and Poem passages).
* Grammar: Parts of speech, Tenses, Articles, Prepositions, Subject-Verb Agreement, Active & Passive Voice, Direct & Indirect Speech, Vocabulary.

### D. Mathematics (30 Marks)
* **Content (20 Marks):** Numbers and operations, Fractions, Money, Measurement (Length, Weight, Capacity, Time), Geometry (2D/3D shapes, perimeter, area), Data handling, Patterns.
* **Pedagogy (10 Marks):** Nature of mathematics, teaching methods, instructional materials, error analysis, diagnostic & remedial teaching in mathematics.

### E. Environmental Studies - EVS (30 Marks)
* **Content (20 Marks):** Family & Friends, Plants & Animals, Food & Nutrition, Shelter & Water, Travel, Things we make and do, Environment of Assam (Flora, fauna, Kaziranga, Manas, Brahmaputra river, climate, conservation), Disaster management.
* **Pedagogy (10 Marks):** Concept & scope of EVS, approaches to teaching EVS, activities, projects, continuous assessment.

---

## 2. Paper II: Upper Primary (Classes VI to VIII) - 150 Marks / 150 MCQs

### A. Child Development and Pedagogy (30 Marks)
* Adolescent development, cognitive & social changes, motivation and learning, theories of learning, inclusive education for diverse classrooms.

### B. Language I (30 Marks) & Language II English (30 Marks)
* Advanced grammar, pedagogy of language learning, literature appreciation, unseen comprehension passages.

### C. Mathematics & Science (60 Marks - For Maths/Science Teachers)
* **Mathematics (30 Marks):** Number system, Algebra (expressions, linear equations), Geometry (lines, angles, triangles, quadrilaterals, circles), Mensuration (surface area & volume of cylinder, cone, sphere), Data Handling & Probability.
* **Science (30 Marks):** Physics (Motion, Force, Gravitation, Light, Sound, Electricity), Chemistry (Matter, Elements, Compounds, Chemical reactions, Acids-Bases-Salts, Metals & Non-metals), Biology (Cell structure, Plant & Animal physiology, Reproduction, Microorganisms, Ecology & Natural Resources).

### D. Social Studies / Social Science (60 Marks - For Social Studies Teachers)
* **History:** Ancient, Medieval, Modern Indian History, History of Assam (Ahoms, Koch, Kachari, Freedom movement).
* **Geography:** Solar system, Globe, Earth's crust, Climate, Geography of India and Assam (Resources, agriculture, industries).
* **Polity & Social Life:** Diversity, Government, Democracy, Constitution, Judiciary, Gender issues.
* **Pedagogical issues:** Sources, project work, critical thinking in social sciences.
""")

    write_file("05_TET_Education/Assam_TET_LP_UP/EXAM_PATTERN.md", """# Assam TET (LP & UP) - Exam Scheme & Qualifying Marks

| Paper | Target Classes | Total MCQs | Total Marks | Duration |
|---|---|---|---|---|
| **Paper I** | Lower Primary (Class 1 to 5) | 150 | 150 Marks | 2.5 Hours (150 Mins) |
| **Paper II** | Upper Primary (Class 6 to 8) | 150 | 150 Marks | 2.5 Hours (150 Mins) |

* **Negative Marking:** **No negative marking**.
* **Qualifying Marks:**
  * **General Category:** Minimum **60%** (90 out of 150 Marks).
  * **SC / ST / OBC / MOBC / PwD:** Minimum **55%** (83 out of 150 Marks).
* **Certificate Validity:** Lifetime validity as per NCTE guidelines.
""")

    # Secondary & Higher Secondary TET
    write_file("05_TET_Education/Secondary_Higher_Secondary_TET/SYLLABUS.md", """# Assam Secondary TET (High School) & Higher Secondary TET (PGT) - Syllabus

**Target Positions:** High School Graduate Teachers (Arts / Science / Hindi / Sanskrit) and Higher Secondary Post Graduate Teachers (PGT).

---

## 1. Paper I: General Studies & Current Affairs (100 Marks)
* **General Studies (Assam & India):**
  * Indian History & Assam History (Ancient, Medieval, Modern).
  * Indian Constitution & Polity (Preamble, Fundamental Rights, Directive Principles, Local Self-Government).
  * Physical & Economic Geography of India and Assam.
  * Environmental Science & Ecology, Biodiversity of North East.
* **Current Affairs:** National, International, and State events, Sports, Literature, Awards.
* **General English:** Grammar, vocabulary, error detection, comprehension.
* **Basic Quantitative Aptitude & Reasoning:** Arithmetic, series, logical deductions.

---

## 2. Paper II: Pedagogy & General English / Subject Specialty (100 Marks)
* **Pedagogy & Teaching-Learning Process:**
  * Secondary education aims, National Education Policy (NEP 2020).
  * Adolescent psychology, classroom management, learning strategies, ICT in education.
  * Assessment techniques, rubric design, inclusive classroom teaching.
* **Subject Specific Domain (For PGT / Subject Teacher):**
  * Core Graduate / Post Graduate syllabus in respective subject (Physics, Chemistry, Mathematics, Botany, Zoology, History, Political Science, Economics, English, Assamese, etc.).
""")

    write_file("05_TET_Education/Secondary_Higher_Secondary_TET/EXAM_PATTERN.md", """# Secondary & Higher Secondary TET - Exam Pattern

* **Total Marks:** 200 Marks (Paper I: 100 Marks + Paper II: 100 Marks)
* **Duration:** 3 Hours
* **Qualifying Marks:** 60% for General (120/200), 55% for Reserved Categories (110/200).
""")

    # DSE / DHE Recruitment
    write_file("05_TET_Education/DSE_DHE_Teacher_Recruitment/SYLLABUS.md", """# DSE & DHE Assam Regular Teacher / Assistant Professor Recruitment

---

## 1. DSE Graduate Teacher Recruitment (High School)
Selection is based on a combined score comprising:
1. **TET Marks:** Weightage from High School TET / Secondary TET.
2. **Academic Scores:** B.Ed, Graduation (BA/B.Sc), HSLC, HSSLC percentage.
3. **Special Recruitment Examination (if conducted):** Subject domain, Pedagogy, and Assam General Awareness.

---

## 2. DHE Assam Assistant Professor (Provincialised Colleges)
Selection is conducted strictly under UGC & Govt. of Assam Guidelines:
* **Academic Record Assessment (Max 80 Marks):** HSLC, HSSLC, Degree, Master's Degree.
* **Research & Publications (Max 10 Marks):** Ph.D / M.Phil, UGC-CARE list research publications, books.
* **Teaching Experience (Max 10 Marks):** College level teaching experience.
* **Interview / Teaching Skill Demonstration (Max 10 Marks):** Domain presentation & interview before selection committee.
""")

    write_file("05_TET_Education/DSE_DHE_Teacher_Recruitment/EXAM_PATTERN.md", """# DSE & DHE Teacher Selection Rubrics

* Selection strictly based on standardized Government merit calculation rubrics and academic API scores.
""")

# ==========================================
# 6. Judiciary & Gauhati High Court
# ==========================================
def gen_judiciary():
    # AJS
    write_file("06_Judiciary_Gauhati_HC/AJS_Grade_I_II_III/SYLLABUS.md", """# Assam Judicial Service (AJS Grade I, II, III) - Official Syllabus

**Conducting Body:** Gauhati High Court  
**Posts:** Civil Judge (Junior Division) / Judicial Magistrate (Grade-III), Civil Judge (Senior Division) (Grade-II), District Judge (Grade-I).

---

## 1. Stage 1: Preliminary Examination (Screening - 100 Marks)
* **Format:** 100 Objective MCQs | **Duration:** 2 Hours
* **Topics:**
  1. General Knowledge & Current Affairs.
  2. Aptitude & English Proficiency.
  3. Constitution of India.
  4. Code of Civil Procedure (CPC), 1908.
  5. Code of Criminal Procedure (CrPC), 1973 / Bharatiya Nagarik Suraksha Sanhita (BNSS).
  6. Indian Penal Code (IPC), 1860 / Bharatiya Nyaya Sanhita (BNS).
  7. Indian Evidence Act, 1872 / Bharatiya Sakshya Adhiniyam (BSA).
  8. Law of Contract, 1872.
  9. Transfer of Property Act, 1882.
  10. Specific Relief Act, 1963.
  11. Limitation Act, 1963.
  12. Proficiency in Official Language of Assam (Assamese/Bengali/Bodo).

---

## 2. Stage 2: Main Written Examination (Descriptive - 400 Marks)

### Paper I: General English (100 Marks / 3 Hours)
* Translation (Assamese/Bengali/Bodo to English and vice versa) (25 Marks).
* Essay Writing on socio-legal topics (25 Marks).
* Precis Writing (15 Marks).
* Grammar, vocabulary, sentence correction, idioms (35 Marks).

### Paper II: Civil Law - I (100 Marks / 3 Hours)
* Code of Civil Procedure (CPC), 1908.
* Transfer of Property Act, 1882.
* Indian Contract Act, 1872.
* Specific Relief Act, 1963.
* Indian Partnership Act, 1932.
* Sale of Goods Act, 1930.

### Paper III: Civil Law - II (100 Marks / 3 Hours)
* Constitution of India.
* Law of Torts.
* Assam Land and Revenue Regulation, 1886.
* Assam Urban Areas Rent Control Act, 1972.
* Limitation Act, 1963.

### Paper IV: Criminal Law (100 Marks / 3 Hours)
* Indian Penal Code (IPC) / BNS.
* Code of Criminal Procedure (CrPC) / BNSS.
* Indian Evidence Act / BSA.
* Protection of Children from Sexual Offences (POCSO) Act, 2012.
* Negotiable Instruments Act, 1881 (Chapter XVII).
* Law of Bail, Framing of Charges, and Judgment Writing.

---

## 3. Stage 3: Viva-Voce / Interview (50 Marks)
* Comprehensive assessment of legal knowledge, judicial demeanor, character, and mental alertness.
""")

    write_file("06_Judiciary_Gauhati_HC/AJS_Grade_I_II_III/EXAM_PATTERN.md", """# Assam Judicial Service (AJS) - Exam Pattern

* **Prelims:** 100 Marks (Qualifying for Mains, Cutoff usually around 60%).
* **Mains Written:** 4 Papers $\\times$ 100 Marks = 400 Marks (Must secure at least 45% in each paper and 50% in aggregate for General candidates).
* **Viva-Voce:** 50 Marks.
* **Final Merit:** Mains Score (400) + Viva-Voce Score (50) = **450 Marks**.
""")

    # High Court & District Staff
    write_file("06_Judiciary_Gauhati_HC/HighCourt_District_Staff/SYLLABUS.md", """# Gauhati High Court & District Courts Staff Recruitment - Syllabus

**Target Posts:** LDA / Copyist / Typist, Computer Assistant, Stenographer (Grade II & III), Process Server, Peon.

---

## 1. Written Examination (100 Marks / 100 MCQs)
* **General English (30 Marks):** Grammar, vocabulary, error detection, spelling, comprehension.
* **General Knowledge & Assam Affairs (30 Marks):** History, geography, polity, judicial system basics, current affairs.
* **General Aptitude & Mathematics (20 Marks):** Arithmetic (Class X level), percentages, ratios, time-distance.
* **Proficiency in Official Language (Assamese/Bengali/Bodo) (20 Marks):** Reading, grammar, translation.

---

## 2. Skill Tests
* **Typing Test (For LDA / Typist):** Minimum 30 wpm in English on computer.
* **Shorthand Test (For Stenographers):** 80 wpm in English shorthand followed by transcription.
* **Computer Proficiency Test (For Computer Assistants):** MS Word, Excel, Access, PowerPoint.
""")

    write_file("06_Judiciary_Gauhati_HC/HighCourt_District_Staff/EXAM_PATTERN.md", """# Gauhati High Court Staff - Selection Pattern

* **Phase 1:** Written OMR Screening Test (100 Marks).
* **Phase 2:** Typing / Shorthand / Computer Practical Test (50 Marks).
* **Phase 3:** Viva-Voce (where applicable).
""")

# ==========================================
# 7. Power Sector (APDCL / AEGCL / APGCL)
# ==========================================
def gen_power():
    # AM / JM
    write_file("07_Power_Sector_APDCL/Assistant_Junior_Manager/SYLLABUS.md", """# APDCL / AEGCL / APGCL Assistant Manager & Junior Manager - Official Syllabus

**Conducting Body:** Assam Power Distribution Company Limited (APDCL) / Guwahati University / TCS iON

---

## 1. Examination Scheme
* **Format:** Computer Based Test (CBT) or OMR Test | **Total Marks:** 100 Marks (100 MCQs) | **Duration:** 2 Hours.
* **Marking:** 1 mark for correct answer; **0.25 negative marking** for incorrect answer.

---

## 2. Paper Structure & Syllabus Breakdown

### Part A: General Aptitude & Awareness (40 Marks)
1. **General English (10 Marks):** Comprehension, grammar, synonyms, antonyms, sentence correction.
2. **Quantitative Aptitude & Reasoning (15 Marks):** Arithmetic, data interpretation, series, analogies, syllogism.
3. **General Knowledge & Current Affairs (15 Marks):** Power sector in India and Assam, Assam history & geography, renewable energy initiatives, state current events.

### Part B: Core Engineering / Domain Knowledge (60 Marks)
* **Electrical Discipline:** Power systems, transmission & distribution, transformers, switchgear & protection, electrical machines, power electronics, circuit theory, control systems, smart grids, electrical safety rules.
* **Mechanical Discipline:** Thermodynamics, power plant engineering, fluid machinery, manufacturing technology, strength of materials, IC engines.
* **Civil Discipline:** Structural engineering, soil mechanics, concrete technology, hydraulics, survey, estimation.
* **Information Technology / Computer Science:** DBMS, networking, cyber security, Python/C++, operating systems, web technologies.
* **Human Resources (HR):** Principles of management, industrial relations, labour laws in India, performance management.
""")

    write_file("07_Power_Sector_APDCL/Assistant_Junior_Manager/EXAM_PATTERN.md", """# APDCL AM & JM - Exam Pattern

* **Total Marks:** 100 Marks (40 Non-Tech + 60 Technical)
* **Duration:** 2 Hours
* **Negative Marking:** 0.25 marks per wrong answer
* **Stage 2:** Document Verification & Viva-Voce (for Assistant Manager).
""")

    # AAO / OFA / Sahayak
    write_file("07_Power_Sector_APDCL/AAO_OFA_Sahayak/SYLLABUS.md", """# APDCL Assistant Accounts Officer (AAO), Office-cum-Field Assistant (OFA), Sahayak - Syllabus

---

## 1. Assistant Accounts Officer (AAO) - 100 Marks
* **Domain / Commerce (60 Marks):** Financial Accounting, Cost Accounting, Auditing, Income Tax, GST, Corporate Finance, Company Law basics, Tally ERP.
* **General Aptitude (40 Marks):** English, Quantitative Aptitude, Reasoning, General Awareness of Assam.

---

## 2. Office-cum-Field Assistant (OFA) - 100 Marks
* **General English:** 20 Marks
* **General Mathematics (Class X):** 30 Marks
* **General Awareness & Assam GK:** 30 Marks
* **Reasoning & Computer Basics:** 20 Marks

---

## 3. Sahayak / Lineman - 100 Marks
* **ITI Trade (Electrician / Wireman):** Basic electrical safety, wiring, earthing, transformer connections, tools, Ohm's law, AC/DC basics.
* **Elementary Arithmetic & General Knowledge:** Simple calculations, road signs, Assam awareness.
""")

    write_file("07_Power_Sector_APDCL/AAO_OFA_Sahayak/EXAM_PATTERN.md", """# APDCL AAO, OFA & Sahayak - Exam Pattern

* **Format:** Written / CBT Test (100 Marks).
* **Physical Fitness & Pole Climbing Test:** Mandatory for Sahayak (Lineman) posts.
""")

# ==========================================
# 8. PnRD, Transport & Others
# ==========================================
def gen_pnrd_other():
    # PnRD & ASRLM
    write_file("08_PnRD_Transport_Others/PnRD_ASRLM/SYLLABUS.md", """# Panchayat & Rural Development (P&RD Assam & ASRLM) - Syllabus

**Target Posts:** Gaon Panchayat Secretary (GPS), Tax Collector-cum-Road Mohorrir, Junior Assistant, Block Program Manager / Coordinator (ASRLM), Accredited Engineer.

---

## 1. P&RD Recruitment Syllabus (100 Marks / 100 MCQs)
1. **Logical Reasoning & Mental Ability (25 Marks):** Series, coding-decoding, blood relations, puzzles, analogies.
2. **General Mathematics (Class X) (25 Marks):** Arithmetic, percentage, ratio-proportion, profit-loss, time & work, simple interest.
3. **General Knowledge & Rural Development (25 Marks):**
   * Assam History, Geography, Culture.
   * Panchayati Raj Act (Assam Panchayat Act, 1994), 73rd Amendment, 3-tier PRIs (Gaon Panchayat, Anchalik Panchayat, Zilla Parishad).
   * Flagship Rural Schemes: MGNREGA, PMAY-G, DAY-NRLM, Swachh Bharat Mission (Grameen), NSAP.
4. **General English (25 Marks):** Grammar, vocabulary, reading comprehension, sentence improvement.
""")

    write_file("08_PnRD_Transport_Others/PnRD_ASRLM/EXAM_PATTERN.md", """# P&RD Assam - Exam Pattern

* **Total Marks:** 100 Marks
* **Duration:** 2 Hours
* **Negative Marking:** 0.50 / 0.25 marks as per notification
* **Stage 2:** Computer Proficiency Test for Junior Assistant / GPS.
""")

    # Transport & Apex Bank
    write_file("08_PnRD_Transport_Others/Transport_ASTC_ApexBank/SYLLABUS.md", """# Transport Department (ASTC) & Assam Apex Bank - Syllabus

---

## 1. Transport Department (Assistant Enforcement Inspector & Enforcement Checker)
* **General English (25 Marks):** Vocabulary, error spotting, comprehension.
* **General Mathematics (25 Marks):** Arithmetic (Class X level).
* **General Knowledge & Assam GK (30 Marks):** Assam geography, rivers, bridges, national parks, motor vehicle rules, state current affairs.
* **Logical Reasoning (20 Marks):** Verbal and non-verbal reasoning.

---

## 2. Assam Cooperative Apex Bank (Assistant & Assistant Manager)
* **Reasoning Ability:** Puzzles, seating arrangement, syllogism, input-output, blood relation.
* **Quantitative Aptitude:** Data interpretation (pie chart, bar graph), quadratic equations, number series, arithmetic word problems.
* **General Awareness & Banking/Economy:** Banking awareness, RBI guidelines, Cooperative banking system, current affairs, Assam economy.
* **English Language:** Reading comprehension, cloze test, error detection, para jumbles.
* **Computer Aptitude:** Basics of networking, DBMS, MS Office, cyber security.
""")

    write_file("08_PnRD_Transport_Others/Transport_ASTC_ApexBank/EXAM_PATTERN.md", """# Transport & Apex Bank - Exam Pattern

* **Written Test:** 100 - 200 Marks (Objective CBT/OMR).
* **Negative Marking:** 0.25 marks per wrong question.
* **Interview:** For Assistant Manager posts.
""")

if __name__ == "__main__":
    gen_apsc_other()
    gen_adre()
    gen_slprb()
    gen_health()
    gen_tet()
    gen_judiciary()
    gen_power()
    gen_pnrd_other()
    print("All exam syllabi generated successfully!")
