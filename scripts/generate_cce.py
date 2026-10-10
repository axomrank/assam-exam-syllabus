import os
import json

def create_all_syllabi():
    # 1. APSC CCE
    cce_dir = "01_APSC/CCE_Prelims_Mains"
    os.makedirs(cce_dir, exist_ok=True)
    
    with open(os.path.join(cce_dir, "SYLLABUS.md"), "w", encoding="utf-8") as f:
        f.write("""# APSC Combined Competitive Examination (CCE) - Comprehensive Syllabus

**Conducting Authority:** Assam Public Service Commission (APSC)  
**Official Portal:** [apsc.nic.in](https://apsc.nic.in)  
**Cadres Recruited:** Assam Civil Service (ACS Jr. Grade), Assam Police Service (APS Jr. Grade), Superintendent of Taxes, District Transport Officer (DTO), Labour Officer, Inspector of Taxes, Block Development Officer (BDO), Assistant Accounts Officer, etc.

---

## 1. Stage 1: Preliminary Examination (Objective Type - MCQs)

The Preliminary Examination consists of two mandatory papers of 200 marks each (Total 400 marks).

### Paper I: General Studies I (GS-I)
* **Total Marks:** 200 | **Duration:** 2 Hours | **Format:** 100 Objective MCQs (2 marks each)
* **Negative Marking:** 0.25 marks deducted for each wrong answer.
* **Note on Assam Context:** 30% to 35% of questions are compulsorily based on Assam.

#### Detailed Syllabus Breakdown:
1. **Current Events:** National and International importance, major initiatives, summits, bilateral relations, science discoveries, defense, and awards.
2. **History of India & Indian National Movement:**
   * Ancient India: Indus Valley Civilization, Vedic period, Buddhism & Jainism, Maurya, Gupta empires.
   * Medieval India: Delhi Sultanate, Mughal Empire, Vijayanagara, Bhakti & Sufi movements.
   * Modern India: British expansion, Revolt of 1857, Socio-religious reform movements, Freedom struggle, Gandhian era, Partition & Independence.
3. **History of Assam:**
   * Ancient Assam: Pragjyotisha/Kamarupa kingdom, Varman, Salastambha, Pala dynasties.
   * Medieval Assam: Chutiya, Kachari, Koch kingdoms, emergence and expansion of the Ahom Kingdom, Ahom administration, Paik system, Moamoria Rebellion, Burmese Invasions, Treaty of Yandaboo (1826).
   * Modern Assam: British annexation, 1857 revolt in Assam (Maniram Dewan), Phulaguri Dhawa (1861), Patharughat uprising (1894), Non-Cooperation, Civil Disobedience, Quit India Movement in Assam, Assam Accord, language movements.
4. **Indian & World Geography:**
   * Physical, Social, and Economic Geography of India and the World.
   * Geomorphology, climatology, oceanography, natural resources, demographic trends.
5. **Geography of Assam:**
   * Physiography of Assam (Brahmaputra Valley, Barak Valley, Karbi & Dima Hasao Hills).
   * River systems: Brahmaputra, Barak and their tributaries, flood & erosion dynamics.
   * Climate, soil types, natural resources (Oil, Coal, Natural Gas, Limestone).
   * Flora & Fauna, National Parks (Kaziranga, Manas, Orang, Nameri, Raimona, Dihing Patkai, Dibru-Saikhowa), Wildlife Sanctuaries, Ramsar Site (Deepor Beel), Forest cover.
6. **Indian Polity and Governance:**
   * Constitution of India: Preamble, Fundamental Rights, DPSP, Fundamental Duties, Amendments.
   * Union & State Executive, Parliament, State Legislature, Judiciary (Supreme Court, High Courts).
   * Federal structure, 73rd & 74th Constitutional Amendments (Panchayati Raj & Municipalities).
   * Sixth Schedule and autonomous district councils in Assam (BTAD, KAAC, NCHAC).
7. **Economic and Social Development:**
   * Sustainable Development, Poverty eradication, Inclusion, Demographics, Social Sector initiatives.
   * Indian Economy: Fiscal policy, Monetary policy, Banking, Budget, Inflation, NITI Aayog.
   * Economy of Assam: Agriculture, Tea industry, Oil & Gas sector, Handloom & Silk (Muga, Eri, Pat), Tourism, Act East Policy & North East trade corridor.
8. **General Science & Technology:**
   * Everyday science, Physics, Chemistry, Biology applications.
   * Space missions (ISRO), AI & Emerging Tech, Biotechnology, Defense tech, Cyber security.
9. **Environmental Ecology, Biodiversity, & Climate Change:**
   * Environmental pollution, conservation strategies, international conventions (COP, UNFCCC, CBD), disaster management in Assam (Floods, Landslides, Earthquakes).

---

### Paper II: General Studies II (CSAT)
* **Total Marks:** 200 | **Duration:** 2 Hours | **Format:** 80 Objective MCQs (2.5 marks each)
* **Qualifying Nature:** Candidates must score a minimum of **33% (66 marks)**.
* **Negative Marking:** 0.25 marks deducted per wrong response.

#### Detailed Syllabus Breakdown:
1. **Comprehension:** English reading passages, inference, central idea, critical assumptions.
2. **Interpersonal Skills & Communication:** Scenario evaluation, interpersonal dynamics.
3. **Logical Reasoning & Analytical Ability:** Syllogisms, blood relations, seating arrangements, coding-decoding, series, puzzles, statement-arguments.
4. **Decision Making & Problem Solving:** Administrative and situational judgement cases.
5. **General Mental Ability:** Direction sense, Venn diagrams, clocks & calendars, analogies.
6. **Basic Numeracy (Class X level):** Numbers, fractions, LCM/HCF, Ratio & Proportion, Percentages, Profit & Loss, Simple & Compound Interest, Time & Work, Speed-Time-Distance, Mensuration.
7. **Data Interpretation (Class X level):** Charts, graphs, tables, data sufficiency.

---

## 2. Stage 2: Main Examination (Written & Personality Test)

Total Written Examination Marks: **1500 Marks** + Personality Test (Interview): **180 Marks** = **Grand Total: 1680 Marks**.

| Paper | Subject | Type | Marks | Duration |
|---|---|---|---|---|
| **Paper 1** | Essay | Conventional Essay (2 topics) | 250 Marks | 3 Hours |
| **Paper 2** | General Studies I (Indian Heritage, Culture, History & Geography) | Descriptive | 250 Marks | 3 Hours |
| **Paper 3** | General Studies II (Governance, Constitution, Polity, Social Justice, IR) | Descriptive | 250 Marks | 3 Hours |
| **Paper 4** | General Studies III (Technology, Economic Dev, Biodiversity, Security, Disaster Mgmt) | Descriptive | 250 Marks | 3 Hours |
| **Paper 5** | General Studies IV (Ethics, Integrity, and Aptitude) | Descriptive | 250 Marks | 3 Hours |
| **Paper 6** | General Studies V (Assam: History, Heritage, Culture, Geography, Economy, Polity) | Descriptive | 250 Marks | 3 Hours |
| **Interview** | Personality Test / Viva-Voce | In-person Board Interview | 180 Marks | ~30 Mins |

---

### Detailed Syllabus for Mains Papers:

#### Paper 1: Essay (250 Marks)
* Candidates write two in-depth essays from multiple choice prompts spanning socio-economic issues, philosophical topics, national challenges, and North-East/Assam developmental themes.

#### Paper 2: General Studies I (250 Marks)
* **Indian Culture & Heritage:** Architecture, literature, performing arts from ancient to modern times.
* **Modern Indian History:** Significant events, personalities, freedom struggle and post-independence consolidation.
* **World History:** Industrial revolution, World Wars, decolonization, political philosophies (Communism, Capitalism, Socialism).
* **Society:** Salient features of Indian Society, Diversity, Women empowerment, Population issues, Urbanization, Globalization, Social empowerment, Communalism, Regionalism, Secularism.
* **Geography:** World & Indian physical geography, distribution of key natural resources, factors responsible for the location of industries, geophysical phenomena (earthquakes, tsunamis, volcanic activity, cyclones).

#### Paper 3: General Studies II (250 Marks)
* **Indian Constitution:** Historical underpinnings, evolution, features, amendments, significant provisions, basic structure doctrine.
* **Functions & Responsibilities of Union & States:** Federal structure, devolution of powers and finances up to local levels, separation of powers, dispute redressal mechanisms.
* **Comparison of Indian Constitutional Scheme** with other countries.
* **Parliament and State Legislatures:** Structure, functioning, conduct of business, powers & privileges.
* **Executive & Judiciary:** Structure, organization, functioning of Ministries, Departments, Statutory, Regulatory and Quasi-judicial bodies.
* **Welfare Schemes & Social Sector:** Health, Education, Human Resources, Poverty, Hunger issues.
* **Governance & Accountability:** E-governance, transparency, Citizen Charters, Civil services in democracy.
* **International Relations:** India and its neighbourhood relations, bilateral, regional and global groupings, Act East Policy.

#### Paper 4: General Studies III (250 Marks)
* **Indian Economy & Growth:** Planning, mobilization of resources, growth, development, employment, inclusive growth.
* **Government Budgeting:** Fiscal management, tax reforms, revenue trends.
* **Agriculture:** Major crops, cropping patterns, irrigation, storage, transport, agricultural marketing, e-technology for farmers, MSP, food security, PDS, food processing industries.
* **Science & Technology:** Developments and applications, indigenization of technology, IT, Space, Computers, Robotics, Nanotechnology, Bio-technology, Intellectual Property Rights (IPR).
* **Environment & Ecology:** Conservation, environmental pollution, environmental impact assessment (EIA), climate change mitigation.
* **Disaster Management:** Disaster prevention, mitigation, flood and erosion management in Assam.
* **Internal Security:** Linkages between development and spread of extremism, role of external state & non-state actors, cyber security, money laundering, border management.

#### Paper 5: General Studies IV - Ethics, Integrity & Aptitude (250 Marks)
* **Ethics and Human Interface:** Essence, determinants, consequences of ethics in human actions, dimensions of ethics, ethics in private and public relationships.
* **Human Values:** Lessons from great leaders, role of family, society, and educational institutions.
* **Attitude:** Content, structure, function; influence on thought and behavior; moral and political attitudes; social influence and persuasion.
* **Aptitude & Foundational Values for Civil Service:** Integrity, impartiality, non-partisanship, objectivity, dedication to public service, empathy, tolerance, compassion towards weaker sections.
* **Emotional Intelligence:** Concepts and utility in administration and governance.
* **Contributions of Moral Thinkers:** Philosophers from India and the world (including Srimanta Sankardeva, Madhavdeva, Gandhi, Vivekananda, etc.).
* **Public/Civil Service Values and Ethics in Public Administration:** Ethical dilemmas, laws, rules, regulations, conscience, accountability, corporate governance, Citizen Charters, Code of Conduct, Code of Ethics, RTI.
* **Probity in Governance:** Concept of public service, philosophical basis of governance, information sharing, transparency, work culture, quality of service delivery, utilization of public funds, corruption challenges.
* **Case Studies:** Applied practical ethical scenarios.

#### Paper 6: General Studies V - Assam Paper (250 Marks)
* **History, Art, Culture, Heritage of Assam:**
  * Pre-history and Proto-history of Assam.
  * Ancient dynasties: Varman, Salastambha, Pala; Kamata, Koch, Chutiya, Kachari kingdoms.
  * The Ahom Rule: Consolidation, administration, military strategies (Battle of Saraighat), religion, architecture, literature, decline.
  * British rule in Assam: Colonization, economic impacts, tea plantations, peasant revolts (Phulaguri, Patharughat).
  * Freedom Movement in Assam: Non-Cooperation, Civil Disobedience, 1942 movement, role of women and prominent leaders (Kanaklata, Kushal Konwar, Tarun Ram Phukan, Gopinath Bordoloi, etc.).
  * Socio-cultural ethos: Neo-Vaishnavite movement of Mahapurusha Srimanta Sankardeva, Satras and Namghars, tribal cultures (Bodo, Mishing, Karbi, Dimasa, Rabha, Tiwa, Sonowal, etc.), festivals (Bihu, Ali-Aye-Ligang, Baishagu, Rongker, etc.), folklore, music, crafts.
* **Geography of Assam:**
  * Geomorphological division, drainage systems, Brahmaputra & Barak basins.
  * Climate, agro-climatic zones, soils, mineral resources, forest wealth, national parks and protected areas.
  * Border issues, interstate & international boundaries.
* **Polity and Administration of Assam:**
  * State government structure, legislative assembly, secretariat administration.
  * Panchayati Raj in Assam, Autonomous District Councils (Sixth Schedule areas - BTAD, KAAC, NCHAC) and Autonomous Statutory Councils (Mising, Rabha, Tiwa, etc.).
* **Economy of Assam:**
  * State GDP composition, agriculture, tea industry, sericulture (Muga silk), handloom, oil, petroleum & natural gas, petrochemicals, coal, limestone.
  * Infrastructure development, power sector, transport & connectivity (waterways, bridges, rail, air), Act East connectivity.
  * Unemployment, skill development initiatives, state government schemes (Orunodoi, Mission Basundhara, Mukhya Mantri Nijut Moina, Atmanirbhar Asom).
* **Environment & Biodiversity of Assam:**
  * Rich flora & fauna, one-horned rhinoceros, golden langur, pygmy hog, hoolock gibbon.
  * Man-animal conflict, deforestation, wetlands preservation (Deepor Beel), flood, erosion, and siltation problems and management.
""")

    with open(os.path.join(cce_dir, "EXAM_PATTERN.md"), "w", encoding="utf-8") as f:
        f.write("""# APSC CCE - Examination Pattern & Selection Process

## Overview of Stages

```mermaid
flowchart TD
    A["Preliminary Exam (400 Marks)"] -->|Shortlisted 1:10 to 1:12| B["Main Written Exam (1500 Marks)"]
    B -->|Shortlisted 1:2 to 1:2.5| C["Interview / Personality Test (180 Marks)"]
    C --> D["Final Merit List (Out of 1680 Marks)"]
```

## 1. Preliminary Examination
* **Nature:** Screening / Qualifying test for shortlisting to Mains.
* **Marks Obtained:** Not counted in the final merit ranking.

| Paper | Marks | Questions | Duration | Negative Marking | Remarks |
|---|---|---|---|---|---|
| **GS Paper I** | 200 | 100 | 2 Hours | 0.25 marks | Merit deciding paper for Mains cutoff (30-35% Assam GK) |
| **GS Paper II (CSAT)** | 200 | 80 | 2 Hours | 0.25 marks | Qualifying only (Min 33% / 66 marks required) |

## 2. Main Examination (Written)
* **Total Papers:** 6 Compulsory Descriptive Papers (250 Marks each = 1500 Marks).
* **No Optional Subject Papers** (As per modern revised APSC CCE Regulations).

## 3. Personality Test (Interview)
* **Marks:** 180 Marks.
* **Criteria:** Board assessment of candidate's personality, leadership, intellectual curiosity, presence of mind, balance of judgement, understanding of Assam's socio-economic landscape, and administrative aptitude.

## 4. Final Merit
$$\\text{Final Score} = \\text{Mains Written (1500 Marks)} + \\text{Interview (180 Marks)} = \\mathbf{1680\\text{ Marks}}$$
""")

create_all_syllabi()
print("APSC CCE Syllabus generated.")
