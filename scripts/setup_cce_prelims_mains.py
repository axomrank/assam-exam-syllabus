import os
import shutil
import requests
import urllib3

urllib3.disable_warnings()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 1. Create dedicated Prelims Syllabus
prelims_syllabus = """# APSC CCE Preliminary Examination - Official Syllabus & Scheme

**Conducting Authority:** Assam Public Service Commission (APSC)  
**Official Portal:** [apsc.nic.in](https://apsc.nic.in)  
**Cadres:** Assam Civil Service (ACS), Assam Police Service (APS), Assam Taxation Service, Assam Finance Service, District Transport Officer (DTO), Labour Officer, ARCS, BDO, Inspector of Taxes, Sub-Registrar.

---

## 📋 Preliminary Examination Overview
* **Stage Type:** Screening / Qualifying Test for shortlisting candidates to Mains (1:10 to 1:12 ratio).
* **Format:** Objective Type (Multiple Choice Questions - OMR based).
* **Total Marks:** 400 Marks (2 Papers $\\times$ 200 Marks).
* **Negative Marking:** **0.25 marks deducted** for each incorrect response in both papers.

---

## 1. Paper I: General Studies I (GS-I)
* **Total Marks:** 200 Marks
* **Number of Questions:** 100 MCQs (2 Marks each)
* **Duration:** 2 Hours (120 Minutes)
* **Mandatory Assam Context:** **30% to 35% of total questions are compulsorily based on Assam.**
* **Merit Status:** The marks obtained in Paper-I determine the cutoff list for qualifying for the Main Examination.

### Detailed Topic-by-Topic Syllabus Breakdown:

#### A. History of India & Indian National Movement
* **Ancient India:** Indus Valley Civilization, Vedic Society, Mahajanapadas, Buddhism & Jainism, Mauryan Empire, Gupta Golden Age, Harshavardhana, Southern Dynasties (Cholas, Pallavas, Chalukyas).
* **Medieval India:** Delhi Sultanate (Slave, Khilji, Tughlaq, Lodi), Mughal Empire (Babur to Aurangzeb), Vijayanagara Empire, Maratha Confederacy, Bhakti and Sufi Saints.
* **Modern India:** Advent of Europeans, British conquest of Bengal, Governor Generals and Viceroys, Revolt of 1857, Socio-Religious Reform Movements (Brahmo Samaj, Arya Samaj, Ramakrishna Mission, Aligarh Movement), Freedom struggle phases (Moderates, Extremists, Gandhian Era 1915–1947), Revolutionary Nationalists, INA and Subhas Chandra Bose, Independence & Partition.

#### B. History, Art & Culture of Assam (Special Focus)
* **Pre-History & Proto-History:** Pragjyotisha, Kamarupa kingdom, Epigraphic and Archaeological sources (Nidhanpur copperplate, Doobi plates).
* **Ancient Dynasties:** Varman dynasty (Pushyavarman, Kumar Bhaskaravarman, Xuanzang's visit), Salastambha dynasty, Pala dynasty of Kamarupa.
* **Medieval Assam:**
  * The Chutiya Kingdom, Kachari Kingdom, Koch Kingdom (Naranarayan and Chilarai).
  * The Ahom Dynasty (1228–1826): Chaolung Sukapha, consolidation, Paik and Khel systems, Ahom administration (Borpatragohain, Borgohain, Burhagohain, Borphukan, Barbarua).
  * Mughals vs. Ahoms: Battles, Mir Jumla's invasion, Battle of Saraighat (1671) under Lachit Borphukan, Battle of Itakhuli (1682).
  * Decline of Ahoms: Moamoria Rebellion, Purnananda Burhagohain, Burmese Invasions (Maanar Din), Treaty of Yandaboo (1826).
* **Modern History & Freedom Movement in Assam:**
  * Annexation of Assam by British, David Scott, Robertson, Jenkins administration.
  * Peasant Uprisings & Resistance: Gomdhar Konwar, Piyoli Phukan, Revolt of 1857 in Assam (Maniram Dewan & Piyoli Baruah execution).
  * Peasant Rebellions (Ryot Sabhas): Phulaguri Dhawa (1861 - First peasant uprising against opium tax), Patharughat Ran (1894 - Assam's Jallianwala Bagh), Rangiya & Lachima revolts.
  * Socio-Literary Renaissance: Orunodoi era, Anandaram Dhekial Phukan, Hemchandra Baruah, Gunabhiram Baruah, Asam Sahitya Sabha (1917).
  * National Movement in Assam: Non-Cooperation Movement (1920-22), Civil Disobedience Movement (1930-34), Quit India Movement (1942 - Kanaklata Barua, Kushal Konwar, Mukunda Kakati, Bhogeswari Phukanani martyrs).
  * Grouping Scheme & Cabinet Mission: Role of Lokapriya Gopinath Bordoloi in keeping Assam in India.
  * Post-Independence Assam: Assam Accord (1985), Language movements, Bodoland movement, Reorganization of Assam.

#### C. Indian & World Geography
* **Physical Geography:** Earth's interior, plate tectonics, earthquakes, volcanoes, geomorphology, atmosphere structure, planetary winds, monsoon mechanism, cyclones, ocean currents, tides, marine resources.
* **Economic & Human Geography of India:** Mineral distribution (Iron ore, Coal, Petroleum, Bauxite), agriculture patterns, major irrigation projects, transport corridors (Golden Quadrilateral, Dedicated Freight Corridors), demographic trends, census statistics.

#### D. Geography of Assam & North East
* **Physiography:** Brahmaputra Valley, Barak Valley, Karbi Anglong & Dima Hasao hill regions.
* **Drainage Systems:** Brahmaputra River system (Northern tributaries: Subansiri, Jia Bharali, Manas, Sankosh; Southern tributaries: Burhi Dihing, Dhansiri, Kopili), Barak River system (Surma, Kushiyara).
* **Geological Resources:** Petroleum & Natural Gas (Digboi, Naharkatiya, Moran), Coal (Makum, Ledo), Limestone (Dillai, Umrangso), Sillimanite, Quartz.
* **Flora, Fauna & Protected Areas:**
  * 7 National Parks: Kaziranga, Manas, Orang, Nameri, Raimona, Dihing Patkai, Dibru-Saikhowa.
  * Wildlife Sanctuaries: Pobitora, Chakrashila, Hoollongapar Gibbon, Laokhowa, Bornadi, Panidihing Bird Sanctuary.
  * Ramsar Wetland: Deepor Beel; Floodplain wetland ecosystems (Beels).
  * Endemic Fauna: Greater One-Horned Rhinoceros, Pygmy Hog, Golden Langur, Hoolock Gibbon, White-Winged Wood Duck (*Deo Hah* - State Bird).

#### E. Indian Polity and Governance
* **Constitutional Framework:** Preamble, Fundamental Rights (Articles 12-35), Directive Principles of State Policy (Part IV), Fundamental Duties (Article 51A), Basic Structure Doctrine.
* **Union & State Government:** President, Governor, Prime Minister, Chief Minister, Union Council of Ministers, Parliament, State Legislative Assemblies, Legislative Councils.
* **Judiciary:** Supreme Court, High Courts (Jurisdiction of Gauhati High Court over Assam, Nagaland, Mizoram, Arunachal Pradesh), Subordinate Courts, Judicial Review, Public Interest Litigation (PIL).
* **Local Self-Government:** 73rd and 74th Constitutional Amendments, Panchayati Raj Institutions (3-tier PRIs in Assam: Gaon Panchayat, Anchalik Panchayat, Zilla Parishad).
* **Special Provisions & Sixth Schedule:** Sixth Schedule areas in Assam (Bodoland Territorial Region - BTR, Karbi Anglong Autonomous Council - KAAC, North Cachar Hills Autonomous Council - NCHAC). Statutory Autonomous Councils (Mising, Rabha Hasong, Tiwa, Deori, Sonowal Kachari, Thengal Kachari).

#### F. Economic and Social Development
* **Indian Economy:** National Income accounting (GDP, GVA), Fiscal Policy, Union Budget, Taxation & GST, Monetary Policy (RBI, Repo rate, Reverse repo, CRR, SLR), Inflation (CPI, WPI), Banking sector reforms, Capital markets (SEBI).
* **Economy of Assam:**
  * Agricultural sector: Rice cultivation, Flood-induced distress, Assam Agribusiness and Rural Transformation Project (APART).
  * Plantation Industry: Tea Industry of Assam (1823 discovery by Robert Bruce, small tea growers, auction centres at Guwahati and Tea Board).
  * Petrochemical & Mineral Industry: Oil India Ltd (Duliajan), ONGC, Digboi Refinery (Asia's oldest refinery - 1901), Guwahati Refinery (Noonmati), Bongaigaon Refinery (BGR), Numaligarh Refinery (NRL), Assam Petro-chemicals Ltd (Namrup), Brahmaputra Cracker and Polymer Limited (BCPL, Lepetkata).
  * Traditional Crafts: Muga Silk (Golden Silk of Assam - GI Tag), Eri Silk (Ahimsa Silk), Pat Silk (Sualkuchi - Manchester of Assam), Bell metal craft of Sarthebari (GI Tag), Brass craft of Hajo, Terracotta craft of Asharikandi (Dhubri), Cane & Bamboo industries.
  * State Flagship Schemes: Orunodoi 3.0, Mission Basundhara 3.0, Mukhya Mantri Nijut Moina, Atmanirbhar Asom Abhijan, Pragyan Bharati, Arundhati Gold Scheme, Amrit Brikshya Andolan.

#### G. General Science, Environment, & Emerging Tech
* Physics, Chemistry, and Biology in everyday life, diseases, human nutrition, vaccines.
* Space technology (ISRO Chandrayaan, Aditya-L1, Gaganyaan), Defense technology, AI & Cyber security.
* Ecology, Climate Change, Biodiversity conservation, Paris Agreement, COP summits, Pollution Control Boards.

#### H. Current Affairs
* Major National and International summits (G20, BRICS, ASEAN, SCO, UN), Sports tournaments (Olympics, National Games, Cricket World Cup), Prestigious awards (Bharat Ratna, Padma Awards, Jnanpith, Sahitya Akademi, Nobel Prizes).

---

## 2. Paper II: General Studies II (CSAT / Aptitude)
* **Total Marks:** 200 Marks
* **Number of Questions:** 80 Objective MCQs (2.5 Marks each)
* **Duration:** 2 Hours (120 Minutes)
* **Qualifying Nature:** **Must score a minimum of 33% (66 out of 200 Marks).** Marks are NOT counted in the merit ranking, but failure to secure 33% results in disqualification.

### Detailed Topic-by-Topic Syllabus Breakdown:
1. **Comprehension:** Unseen reading comprehension passages, testing logical deductions, contextual inference, and central theme identification.
2. **Interpersonal Skills including Communication Skills:** Situational judgment, workplace communication, interpersonal conflict handling.
3. **Logical Reasoning & Analytical Ability:**
   * Syllogisms, Statement and Assumptions, Statement and Arguments, Statement and Conclusions.
   * Blood Relations, Seating Arrangements (Linear, Circular, Matrix).
   * Direction Sense Test, Coding-Decoding, Series (Number, Alphabet, Alpha-Numeric), Puzzles.
   * Venn Diagrams, Clocks and Calendars, Cube and Dice.
4. **Decision Making & Problem Solving:** Administrative scenarios requiring objective analysis and priority setting.
5. **General Mental Ability:** Analogies, Classification (Odd one out), Figure series, Pattern completion, Embedded figures.
6. **Basic Numeracy (Class X Standard):**
   * Number System, Divisibility Rules, Prime numbers, Fractions, Decimals.
   * HCF and LCM, Simplification, Square roots and Cube roots.
   * Percentages, Profit, Loss and Discount, Ratio and Proportion, Partnership.
   * Simple Interest (SI) and Compound Interest (CI), Averages, Mixtures and Alligations.
   * Time and Work, Pipes and Cisterns, Speed, Time and Distance, Problems on Trains, Boats and Streams.
   * Mensuration: Perimeter, Area, Surface Area, Volume of 2D and 3D figures (Rectangles, Circles, Cylinders, Spheres, Cones).
7. **Data Interpretation & Data Sufficiency (Class X Standard):**
   * Tables, Line Graphs, Bar Charts, Pie Charts, Histogram analysis.
   * Data Sufficiency questions determining whether statement 1 or 2 is adequate.
"""

with open("01_APSC/CCE_Prelims/SYLLABUS.md", "w", encoding="utf-8") as f:
    f.write(prelims_syllabus.strip() + "\n")

# 2. Prelims Exam Pattern
prelims_pattern = """# APSC CCE Preliminary Exam - Pattern, Marking Scheme & Cutoff Rules

## 1. Exam Structure & Scheme

| Paper | Subject | No. of Questions | Marks | Duration | Negative Marking | Remarks |
|---|---|---|---|---|---|---|
| **Paper I** | General Studies I | 100 MCQs | 200 Marks (2 marks/Q) | 2 Hours | 0.25 marks deducted per wrong answer | **Merit Deciding Paper** for shortlisting to Mains (30-35% Assam GK) |
| **Paper II** | General Studies II (CSAT) | 80 MCQs | 200 Marks (2.5 marks/Q) | 2 Hours | 0.25 marks deducted per wrong answer | **Qualifying Only** (Minimum 33% / 66 Marks compulsory) |

---

## 2. Selection & Shortlisting Mechanics
1. **Paper-II Evaluation First:** The OMR sheet of Paper-I is evaluated only for candidates who secure at least **33% (66 marks)** in Paper-II (CSAT).
2. **Merit Cutoff:** The preliminary cutoff is determined exclusively by the marks obtained in **Paper-I (out of 200 marks)**.
3. **Ratio of Shortlisting:** Approximately **10 to 12 times** the total number of vacancies advertised across all categories are shortlisted for the Main Examination.
"""

with open("01_APSC/CCE_Prelims/EXAM_PATTERN.md", "w", encoding="utf-8") as f:
    f.write(prelims_pattern.strip() + "\n")

# Copy official PDFs to 01_APSC/CCE_Prelims/
prelim_pdfs = [
    "Official_Syllabus_CCE_Prelims_GS_I.pdf",
    "Official_Syllabus_CCE_Prelims_GS_II_CSAT.pdf",
    "Official_APSC_CCE_Amendment_Rules_Gazette.pdf"
]
for p in prelim_pdfs:
    src = os.path.join("01_APSC/CCE_Prelims_Mains", p)
    dst = os.path.join("01_APSC/CCE_Prelims", p)
    if os.path.exists(src):
        shutil.copy2(src, dst)

# Download Prelims Question Papers for 2024 / 2023 directly into 01_APSC/CCE_Prelims/
cce_qps = [
    {
        "url": "https://apsc.nic.in/misc_2025/GS%20I_CCEP_2024.pdf",
        "path": "01_APSC/CCE_Prelims/APSC_CCE_Prelims_GS_I_2024_Question_Paper.pdf",
        "title": "APSC CCE Prelims 2024 GS-I Question Paper"
    },
    {
        "url": "https://apsc.nic.in/misc_2025/GS%20II_CCEP_2024.pdf",
        "path": "01_APSC/CCE_Prelims/APSC_CCE_Prelims_GS_II_2024_Question_Paper.pdf",
        "title": "APSC CCE Prelims 2024 GS-II Question Paper"
    },
    {
        "url": "https://apsc.nic.in/misc_2024/GS_I_CCEP_2023.pdf",
        "path": "01_APSC/CCE_Prelims/APSC_CCE_Prelims_GS_I_2023_Question_Paper.pdf",
        "title": "APSC CCE Prelims 2023 GS-I Question Paper"
    },
    {
        "url": "https://apsc.nic.in/misc_2024/GS_II_CCEP_2023.pdf",
        "path": "01_APSC/CCE_Prelims/APSC_CCE_Prelims_GS_II_2023_Question_Paper.pdf",
        "title": "APSC CCE Prelims 2023 GS-II Question Paper"
    }
]

for qp in cce_qps:
    out = qp["path"]
    print(f"Fetching: {qp['title']}...")
    try:
        r = requests.get(qp["url"], headers=headers, verify=False, timeout=20)
        if r.status_code == 200 and len(r.content) > 1000:
            with open(out, "wb") as f:
                f.write(r.content)
            print(f"  [SAVED] {out} ({len(r.content)/1024:.1f} KB)")
    except Exception as e:
        print(f"  [ERROR] {e}")

# Copy Mains files to 01_APSC/CCE_Mains/
mains_pdfs = [
    "Official_Syllabus_CCE_Mains_GS_I.pdf",
    "Official_Syllabus_CCE_Mains_GS_II.pdf",
    "Official_Syllabus_CCE_Mains_GS_III.pdf",
    "Official_Syllabus_CCE_Mains_GS_IV_Ethics.pdf",
    "Official_Syllabus_CCE_Mains_GS_V_Assam.pdf",
    "Official_APSC_CCE_Amendment_Rules_Gazette.pdf"
]
for p in mains_pdfs:
    src = os.path.join("01_APSC/CCE_Prelims_Mains", p)
    dst = os.path.join("01_APSC/CCE_Mains", p)
    if os.path.exists(src):
        shutil.copy2(src, dst)

print("APSC CCE Prelims and Mains dedicated folders setup completed!")
