import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated: {path}")

# ==========================================
# 01. APSC Expanded
# ==========================================
def gen_apsc_expanded():
    # Medical, Food & Drug
    write_file("01_APSC/Medical_Food_Drug_Services/SYLLABUS.md", """# APSC Medical Officer, Food Safety Officer (FSO) & Drug Inspector (DI) - Syllabus

**Conducting Authority:** Assam Public Service Commission (APSC)  
**Departments:** Health & Family Welfare Department / Food Safety & Drug Administration, Assam

---

## 1. Food Safety Officer (FSO)
* **Paper I: General Studies (100 Marks / 100 MCQs):**
  * Indian & Assam History, Geography, Indian Constitution, Economy, General English, Basic Arithmetic & Mental Ability.
* **Paper II: Food Safety & Food Chemistry / Microbiology (100 Marks / 100 MCQs):**
  * Food Safety and Standards Act 2006 (FSSA), Rules & Regulations 2011, Codex Alimentarius Commission (CAC), ISO standards (ISO 22000, HACCP, GMP, GHP).
  * Food Chemistry: Carbohydrates, proteins, lipids, vitamins, minerals, food additives, preservatives, colorants, flavor enhancers, adulteration testing.
  * Food Microbiology: Foodborne pathogens (Salmonella, E. coli, Clostridium, Listeria), food spoilage, fermentation, thermal destruction kinetics, PCR/ELISA detection.
  * Food Processing & Preservation: Canning, drying, freezing, pasteurization, irradiation, packaging materials and migration testing.

---

## 2. Drug Inspector (DI)
* **Paper I: General Knowledge (100 Marks):** General awareness, current affairs, Assam affairs, basic reasoning.
* **Paper II: Pharmacy & Pharmaceutical Jurisprudence (100 Marks):**
  * Drugs and Cosmetics Act 1940 & Rules 1945 (Schedules M, Y, G, H, X, etc.), Pharmacy Act 1948, NDPS Act, DPCO.
  * Pharmacology & Toxicology: Pharmacokinetics, pharmacodynamics, adverse drug reactions, drug-drug interactions, bioassays.
  * Pharmaceutics & Quality Control: Formulation, sterility testing, pyrogen testing, dissolution testing, cGMP guidelines.
  * Medicinal Chemistry & Pharmacognosy: Chemical structure, mechanism of action, crude drugs, chromatography (HPLC, GC, TLC).

---

## 3. Medical Officer (Ayurvedic / Homeopathic / Allopathic)
* **Part A (General Knowledge):** Current events, state health policies, socio-economic scenario of Assam.
* **Part B (Core Medical Discipline):**
  * *Ayurvedic:* Samhita, Sharir, Dravyaguna, Rasashastra, Rog Nidan, Kayachikitsa, Shalya, Shalakya, Prasuti Tantra.
  * *Homeopathic:* Organon of Medicine, Homeopathic Materia Medica, Repertory, Practice of Medicine, Pathology.
  * *Allopathic (GDMO):* Medicine, Surgery, Pediatrics, Obstetrics & Gynecology, Preventive & Social Medicine (PSM).
""")

    write_file("01_APSC/Medical_Food_Drug_Services/EXAM_PATTERN.md", """# APSC Medical, Food & Drug Services - Exam Pattern

* **Screening Test:** 200 Marks (Paper I: General Studies @ 100M + Paper II: Domain Specialization @ 100M).
* **Negative Marking:** 0.25 marks per incorrect response.
* **Viva-Voce / Interview:** 37 to 50 Marks for shortlisted candidates.
""")

    # Agriculture, Veterinary & Fishery
    write_file("01_APSC/Agriculture_Veterinary_Fishery/SYLLABUS.md", """# APSC Agricultural Development Officer (ADO), Veterinary Officer (VO) & Fishery Development Officer (FDO) - Syllabus

---

## 1. Agricultural Development Officer (ADO)
* **General Studies (100 Marks):** General knowledge, Assam history, geography, economy, polity, current events.
* **Core Agriculture (100 Marks):**
  * Agronomy & Crop Production: Major crops of Assam (Rice, Jute, Mustard, Pulses, Tea), cropping systems, organic farming, weed management.
  * Soil Science: Soils of Assam, soil fertility, macro & micronutrients, integrated nutrient management (INM), soil erosion and conservation.
  * Genetics & Plant Breeding: Mendelian principles, hybridization, transgenic crops, seed production technology.
  * Horticulture: Fruit, vegetable, and plantation crops cultivation, post-harvest technology, green houses.
  * Plant Protection: Entomology and Plant Pathology, major pests & diseases of rice and tea, integrated pest management (IPM).
  * Agricultural Economics & Extension: Microeconomics, farm management, agricultural marketing, MSP, KVKs, extension methodologies.

---

## 2. Veterinary Officer (VO / BVO)
* **Core Veterinary Science & Animal Husbandry (100 Marks):**
  * Animal Genetics & Breeding, Animal Nutrition (feed formulation, fodder conservation), Livestock Production & Management (Cattle, Buffalo, Goat, Swine, Poultry).
  * Veterinary Anatomy, Physiology, Pharmacology, Pathology, Parasitology, Microbiology, Public Health & Epidemiology.
  * Veterinary Medicine (Infectious diseases: FMD, HS, BQ, PPR, Anthrax, Swine Fever), Veterinary Surgery & Radiology, Animal Reproduction & Gynecology (AI, ET).

---

## 3. Fishery Development Officer (FDO)
* **Core Fishery Sciences (100 Marks):**
  * Aquaculture systems, fish breeding (Induced breeding of Indian Major Carps - Rohu, Catla, Mrigal), hatchery management, fish nutrition.
  * Inland Fisheries: Riverine, wetland/beels, reservoir fisheries of Assam, floodplain wetland management, fish taxonomy of North-East India.
  * Fish Pathology: Common bacterial, viral, fungal, and parasitic diseases of fish, water quality parameters (DO, pH, Alkalinity).
  * Post-harvest technology, fish processing, freezing, value addition, fishery economics and cooperative management.
""")

    write_file("01_APSC/Agriculture_Veterinary_Fishery/EXAM_PATTERN.md", """# APSC ADO, VO & FDO - Exam Pattern

* **Stage 1 (Screening Test):** 200 Marks (Paper I: GS @ 100 Marks + Paper II: Technical Subject @ 100 Marks).
* **Stage 2 (Interview):** 37 - 50 Marks.
""")

    # Lecturer & Asst Prof Poly/Engg
    write_file("01_APSC/Lecturer_Assistant_Professor_Poly_Engg/SYLLABUS.md", """# APSC Lecturer in Polytechnics & Assistant Professor in Govt Engineering Colleges - Syllabus

**Institutions:** Assam Engineering College (AEC), Jorhat Engineering College (JEC), Bineswar Brahma EC, Jorhat Institute of Science & Technology (JIST), Barak Valley EC, State Polytechnics.

---

## 1. Written Screening Test
* **Paper I: General Awareness, Aptitude & Teaching Aptitude (100 Marks):**
  * General Knowledge, Current Affairs, Assam History & Geography.
  * Quantitative Aptitude, Logical Reasoning, Analytical Ability.
  * Teaching & Research Aptitude: Teaching methods, classroom communication, learner characteristics, higher education policies (NEP 2020), ICT tools in technical education.
* **Paper II: Core Discipline (Civil, Mechanical, Electrical, CSE, Chemical, Physics, Chemistry, Mathematics, Humanities) (100 Marks):**
  * Standard GATE / UGC NET level syllabus corresponding to the respective engineering or basic science branch.
""")

    write_file("01_APSC/Lecturer_Assistant_Professor_Poly_Engg/EXAM_PATTERN.md", """# APSC Technical Faculty - Selection Scheme

* **Screening Test:** 200 Marks (OMR MCQs).
* **Classroom Teaching Demonstration & Interview:** 50 Marks.
""")

    # Specialized Inspectors
    write_file("01_APSC/Specialized_Inspectors_Legal_MVI_Factories/SYLLABUS.md", """# APSC Specialized Inspectors (Legal Metrology, MVI, Factories, Labour) - Syllabus

---

## 1. Inspector of Legal Metrology
* Legal Metrology Act 2009 & Assam Legal Metrology Rules.
* Units and Standards of weights and measures, calibration techniques, verification procedures.
* General Studies, Basic Physics, Mathematics & General English.

---

## 2. Motor Vehicle Inspector (MVI)
* Mechanical / Automobile Engineering diploma standard subjects: Automobile chassis, engines, braking systems, transmission, steering, suspension, electrical systems, emission standards (BS-VI).
* Motor Vehicles Act 1988, Central Motor Vehicles Rules 1989, Assam Motor Vehicle Rules.
* General Studies, Assam Affairs, Reasoning.

---

## 3. Inspector of Factories & Labour Inspector
* Factories Act 1948, Industrial Disputes Act, Occupational Safety, Health and Working Conditions Code 2020.
* Industrial safety engineering, hazardous chemical handling, fire safety in industries.
* Indian Constitution, Labour Laws, General Studies.
""")

    write_file("01_APSC/Specialized_Inspectors_Legal_MVI_Factories/EXAM_PATTERN.md", """# APSC Specialized Inspectors - Exam Pattern

* **Written Test:** 200 Marks (100 Marks GS + 100 Marks Technical / Domain).
* **Interview:** 37 / 50 Marks.
""")

gen_apsc_expanded()
print("APSC Expanded generated.")
