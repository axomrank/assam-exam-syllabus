# Assam Exam Syllabus: syllabi and exam patterns for every Assam recruitment board

> Syllabi, exam patterns, official notices and past papers for Assam government recruitment exams across 12 boards (APSC, SLRC ADRE, SLPRB, DME, TET, Gauhati HC, APDCL and more).

[Part of AxomRank](https://github.com/axomrank)

## At a glance

- **12 recruitment categories**, 40+ cadres, each with a syllabus, exam pattern and the official PDFs where available
- **Master topics checklist:** 842 atomic study items across 82 topics (CSV and JSON)
- **Master syllabus dataset** for all cadres, including technical and specialised posts
- **Diagrams** of the exam taxonomy (Mermaid and interactive HTML)

## Quick start

Browse the numbered folders, or load `csv/` and `json/` for programmatic use.

## Overview

A comprehensive, organized, and verified repository of **official syllabi, government gazettes, recruitment rules, previous question papers, and examination schemes** across all recruitment boards, commissions, directorates, and public enterprises under the **Government of Assam**.

---

## Master Structured Datasets (CSV & JSON)

For programmatic access, test series creation, syllabus tracking, and multi-exam preparation, the repository provides two structured datasets:

### 1. 🌟 [Universal Master Topics Checklist (842 Atomic Rows across 82 Topics)](./csv/MAster_topics_checklist.csv)
Focused on all **universal foundational subjects** across Assam competitive examinations (APSC CCE, ADRE III & IV, Assam Police SI/Constable, TET, APDCL, P&RD, etc.), organized into 842 bite-sized, atomic study items across 82 distinct pedagogical topics.
* 📥 **[Master Topics Checklist CSV (with `Checklist`, `Study_Format` & `Chronology_Era`)](./csv/MAster_topics_checklist.csv)** | 📥 **[Master Topics Checklist JSON](./json/MAster_topics_checklist.json)**
* 📥 **[Master Topics Reference CSV](./csv/MAster%20tpics.csv)**
* 🐍 **[Checklist Generator Script](./scripts/generate_checklist_csv.py)**
* **Actionable 9-Column Checklist Schema**: `Domain` ➔ `Subject` ➔ `Topic` ➔ `Subtopic` ➔ `Sub_Subtopic` ➔ `Study_Format` (`Chronology`, `Listicle`, `Conceptual`, `Formula`, `Spatial/Map`, `Constitutional/Legal`, `Case Study/Current Affair`) ➔ `Chronology_Era` (Year / Epoch / `N/A`) ➔ `Assam_Specific` (`Yes`/`No`) ➔ `Checklist` (`[ ]`).
* **Mentally Clear Domains & Study Formats**:
  * 📜 **History (356 rows)**: Strictly ordered chronologically from Prehistory, Indus Valley, Vedic, Mauryas, Medieval Sultanate & Mughals, Ancient & Medieval Assam, Ahoms, Freedom Struggle, to Post-Independence Accords & UNESCO Cultural Monuments.
  * 🗺️ **Geography (134 rows)**: Physical & Indian Geography, Assam Relief & Wetlands, 7 National Parks, All 7 Natural & 1 Mixed UNESCO Sites, 4 Biodiversity Hotspots, Biosphere Reserves, Ramsar Sites, and Mountain Passes/Tunnels.
  * 🏛️ **Polity (92 rows)**: Indian Constitution & Governance, Landmark SC Judgments, Autonomous Bodies (CAG, EC, FC), Assam State Administration, Sixth Schedule Councils, and Flagship State Schemes.
  * 📈 **Economy (45 rows)**: Indian Economy Fundamentals, Inflation & Banking Reforms, Assam Economy, Tea Industry, Oil, Mega Projects & Waterways.
  * 🔢 **Aptitude (72 rows)**: Quantitative Math Formulas, Speed-Time-Distance, Mensuration, Permutations/Probability, Data Interpretation, Logical Reasoning, and Critical Verbal Logic.
  * 📖 **English (28 rows)**: Grammar & Syntax Transformation Rules, Vocabulary & Word Power, Reading Comprehension Passages.
  * 🔬 **General Awareness & Science (115 rows)**: Everyday Physics, Chemistry, Biology, Static GK, Contemporary Issues & Computer Fundamentals.

### 2. 🏛️ [All-Cadres Master Syllabus Dataset (Including Technical & Specialized)](./csv/master_assam_exams_syllabus.csv)
The comprehensive dataset across all 12 recruitment categories and 40+ examination cadres (including specialized engineering, medical, judicial, and technical services).
* 📥 **[Master Syllabus CSV](./csv/master_assam_exams_syllabus.csv)** | 📥 **[Master Syllabus JSON](./json/master_assam_exams_syllabus.json)** | 🐍 **[Compiler Script](./scripts/compile_syllabus_csv.py)**

---

## Visual Architecture & Mermaid Diagrams

Visual representations of the examination taxonomy, recruitment boards, and universal syllabus domains:

* 🌀 **[Circular Radiating Diagram (Interactive HTML)](./Diagrams/circular_radiating_diagram.html)**: Dynamic concentric SVG visualization with animated light rays, glowing orbital nodes, and interactive click-to-inspect info panels.
* 🌀 **[Circular Radiating Architecture (Markdown)](./Diagrams/CIRCULAR_DIAGRAM.md)**: Conceptual guide and mindmap explaining the radial syllabus model.
* 📄 **[Syllabus Architecture Diagrams (Markdown)](./Diagrams/SYLLABUS_ARCHITECTURE.md)**: Embedded Mermaid diagrams covering 7-domain hierarchy, board mappings, and category trees.
* 🌐 **[Interactive HTML Diagram Viewer](./Diagrams/view_diagram.html)**: Clean, styled browser page rendering high-resolution Mermaid diagrams.
* 📐 **[Raw Mermaid Source File (.mmd)](./Diagrams/syllabus_architecture.mmd)**: Raw mermaid code for VS Code preview plugins and external editors.

---

## Master Index of Examinations (12 Canonical Categories)

### 1. [Assam Public Service Commission (APSC)](./01_APSC)

#### [Combined Competitive Examination (CCE) - Assam Civil Services](./01_APSC/Combined_Competitive_Exam_CCE)
* **Cadres:** ACS (Jr. Grade), APS (Jr. Grade), Assam Taxation Service, Assam Finance Service, District Transport Officer (DTO), Labour Officer, ARCS, BDO, Inspector of Taxes, Sub-Registrar.
* **Stage 1: Preliminary Examination**:
  * 📖 [Detailed Prelims Syllabus (GS-I & GS-II CSAT Breakdown)](./01_APSC/Combined_Competitive_Exam_CCE/01_Prelims/SYLLABUS.md)
  * 📋 [Prelims Exam Pattern & 33% CSAT Qualifying Criteria](./01_APSC/Combined_Competitive_Exam_CCE/01_Prelims/EXAM_PATTERN.md)
  * 📄 [Official Prelims GS-I Syllabus (PDF)](./01_APSC/Combined_Competitive_Exam_CCE/01_Prelims/Official_Syllabus_CCE_Prelims_GS_I.pdf)
  * 📄 [Official Prelims GS-II (CSAT) Syllabus (PDF)](./01_APSC/Combined_Competitive_Exam_CCE/01_Prelims/Official_Syllabus_CCE_Prelims_GS_II_CSAT.pdf)
  * 📝 [APSC CCE Prelims 2024 GS-I Question Paper (PDF)](./01_APSC/Combined_Competitive_Exam_CCE/01_Prelims/APSC_CCE_Prelims_GS_I_2024_Question_Paper.pdf)
  * 📝 [APSC CCE Prelims 2024 GS-II Question Paper (PDF)](./01_APSC/Combined_Competitive_Exam_CCE/01_Prelims/APSC_CCE_Prelims_GS_II_2024_Question_Paper.pdf)
  * 📝 [APSC CCE Prelims 2023 GS-I Question Paper (PDF)](./01_APSC/Combined_Competitive_Exam_CCE/01_Prelims/APSC_CCE_Prelims_GS_I_2023_Question_Paper.pdf)
  * 📝 [APSC CCE Prelims 2023 GS-II Question Paper (PDF)](./01_APSC/Combined_Competitive_Exam_CCE/01_Prelims/APSC_CCE_Prelims_GS_II_2023_Question_Paper.pdf)
* **Stage 2: Main Examination**:
  * 📖 [Detailed Mains Syllabus (Papers 1 to 6 - Essay, GS-I to GS-V)](./01_APSC/Combined_Competitive_Exam_CCE/02_Mains/SYLLABUS.md)
  * 📋 [Mains 1500M + 180M Interview Scheme](./01_APSC/Combined_Competitive_Exam_CCE/02_Mains/EXAM_PATTERN.md)
  * 📄 [Official Mains GS-I Syllabus (PDF)](./01_APSC/Combined_Competitive_Exam_CCE/02_Mains/Official_Syllabus_CCE_Mains_GS_I.pdf) | [GS-II (PDF)](./01_APSC/Combined_Competitive_Exam_CCE/02_Mains/Official_Syllabus_CCE_Mains_GS_II.pdf) | [GS-III (PDF)](./01_APSC/Combined_Competitive_Exam_CCE/02_Mains/Official_Syllabus_CCE_Mains_GS_III.pdf) | [GS-IV Ethics (PDF)](./01_APSC/Combined_Competitive_Exam_CCE/02_Mains/Official_Syllabus_CCE_Mains_GS_IV_Ethics.pdf) | [GS-V Assam (PDF)](./01_APSC/Combined_Competitive_Exam_CCE/02_Mains/Official_Syllabus_CCE_Mains_GS_V_Assam.pdf)
* **Statutory Rules & Gazette**:
  * 📜 [Official APSC CCE Amendment Rules Gazette (PDF)](./01_APSC/Combined_Competitive_Exam_CCE/03_Rules_Gazette/Official_APSC_CCE_Amendment_Rules_Gazette.pdf)

#### Other APSC Services
* **[Engineering Services (AE & JE)](./01_APSC/Engineering_Services_AE_JE)**: [Syllabus Guide](./01_APSC/Engineering_Services_AE_JE/SYLLABUS.md) | [Official AE Civil (PDF)](./01_APSC/Engineering_Services_AE_JE/Official_Syllabus_AE_Civil_PWD.pdf) | [Official JE Civil (PDF)](./01_APSC/Engineering_Services_AE_JE/Official_Syllabus_JE_Civil_PWD.pdf) | [Official AE Mech (PDF)](./01_APSC/Engineering_Services_AE_JE/Official_Syllabus_AE_Mechanical_Irrigation.pdf) | [Official AE Elect (PDF)](./01_APSC/Engineering_Services_AE_JE/Official_Syllabus_AE_Electrical_Irrigation.pdf) | [Official AE Chem (PDF)](./01_APSC/Engineering_Services_AE_JE/Official_Syllabus_AE_Chemical_PHE.pdf)
* **[Forest Services (Forest Ranger & AFS)](./01_APSC/Forest_Services_AFS_Ranger)**: [Syllabus & Physical Walking Rules](./01_APSC/Forest_Services_AFS_Ranger/SYLLABUS.md)
* **[Agriculture, Veterinary & Fisheries](./01_APSC/Agriculture_Veterinary_Fisheries)**: [Syllabus Guide](./01_APSC/Agriculture_Veterinary_Fisheries/SYLLABUS.md) | [Official ADO Agri (PDF)](./01_APSC/Agriculture_Veterinary_Fisheries/Official_Syllabus_Agricultural_Development_Officer_ADO.pdf) | [Official VO Domain (PDF)](./01_APSC/Agriculture_Veterinary_Fisheries/Official_Syllabus_Veterinary_Officer_VO_BVO.pdf) | [Official VO GS (PDF)](./01_APSC/Agriculture_Veterinary_Fisheries/Official_Syllabus_VO_BVO_General_Studies.pdf)
* **[Health, Drug & Food Services](./01_APSC/Health_Drug_Food_Services)**: [Medical Officers, FSO & Drug Inspector Syllabus](./01_APSC/Health_Drug_Food_Services/SYLLABUS.md)
* **[Higher Education & Technical Faculty](./01_APSC/Higher_Education_Technical_Faculty)**: [Polytechnic Lecturer & Engineering College Assistant Professor Syllabus](./01_APSC/Higher_Education_Technical_Faculty/SYLLABUS.md)
* **[Specialized Administrative Inspectors](./01_APSC/Specialized_Administrative_Inspectors)**: [Syllabus Guide](./01_APSC/Specialized_Administrative_Inspectors/SYLLABUS.md) | [Official Legal Metrology (PDF)](./01_APSC/Specialized_Administrative_Inspectors/Official_Syllabus_Inspector_Legal_Metrology.pdf) | [Official Boilers Inspector (PDF)](./01_APSC/Specialized_Inspectors_Legal_MVI_Factories/Official_Syllabus_Inspector_of_Boilers.pdf) | [Official Planning RA (PDF)](./01_APSC/Specialized_Administrative_Inspectors/Official_Syllabus_Research_Assistant_Planning_TDD.pdf)

---

### 2. [Assam Direct Recruitment Examination (ADRE - SLRC / ASSEB)](./02_ADRE_SLRC)
* **[Class III (Graduate Level)](./02_ADRE_SLRC/Class_III_Graduate_Level)**: [Syllabus Guide](./02_ADRE_SLRC/Class_III_Graduate_Level/SYLLABUS.md) | [Exam Pattern & Computer Skill Test](./02_ADRE_SLRC/Class_III_Graduate_Level/EXAM_PATTERN.md)
* **[Class III (Higher Secondary 10+2 Level)](./02_ADRE_SLRC/Class_III_Higher_Secondary_Level)**: [Syllabus Guide](./02_ADRE_SLRC/Class_III_Higher_Secondary_Level/SYLLABUS.md) | [Exam Pattern](./02_ADRE_SLRC/Class_III_Higher_Secondary_Level/EXAM_PATTERN.md)
* **[Class III (Driver & Technical Posts)](./02_ADRE_SLRC/Class_III_Driver_Technical)**: [Syllabus Guide](./02_ADRE_SLRC/Class_III_Driver_Technical/SYLLABUS.md) | [Driving Track Practical Scheme](./02_ADRE_SLRC/Class_III_Driver_Technical/EXAM_PATTERN.md)
* **[Class IV (HSLC & Class VIII Passed)](./02_ADRE_SLRC/Class_IV_HSLC_ClassVIII)**: [Syllabus Guide](./02_ADRE_SLRC/Class_IV_HSLC_ClassVIII/SYLLABUS.md) | [Exam Pattern](./02_ADRE_SLRC/Class_IV_HSLC_ClassVIII/EXAM_PATTERN.md)

---

### 3. [Assam Police & Uniformed Services (SLPRB)](./03_Assam_Police_SLPRB)
* **[Sub-Inspector (UB / AB / Commando)](./03_Assam_Police_SLPRB/Sub_Inspector_UB_AB_Commando)**: [Syllabus](./03_Assam_Police_SLPRB/Sub_Inspector_UB_AB_Commando/SYLLABUS.md) | [Selection Pattern & PST/PET](./03_Assam_Police_SLPRB/Sub_Inspector_UB_AB_Commando/EXAM_PATTERN.md)
* **[Police Constable (UB / AB / Commando)](./03_Assam_Police_SLPRB/Constable_UB_AB_Commando)**: [Syllabus](./03_Assam_Police_SLPRB/Constable_UB_AB_Commando/SYLLABUS.md) | [Physical Test Standards](./03_Assam_Police_SLPRB/Constable_UB_AB_Commando/EXAM_PATTERN.md)
* **[APRO Radio & Communication](./03_Assam_Police_SLPRB/APRO_Radio_Communication)**: [Physics, EM Waves & Electronics Syllabus](./03_Assam_Police_SLPRB/APRO_Radio_Communication/SYLLABUS.md)
* **[Prisons Department (Jailer & Warder)](./03_Assam_Police_SLPRB/Prisons_Jailer_Warder)**: [Syllabus](./03_Assam_Police_SLPRB/Prisons_Jailer_Warder/SYLLABUS.md)
* **[Excise Department (Inspector & Constable)](./03_Assam_Police_SLPRB/Excise_Inspector_Constable)**: [Syllabus](./03_Assam_Police_SLPRB/Excise_Inspector_Constable/SYLLABUS.md)
* **[Forestry Cadres (Forester Grade-I & Forest Guard)](./03_Assam_Police_SLPRB/Forestry_Cadres_Forester_Guard)**: [Syllabus & 26km/16km Walk Rules](./03_Assam_Police_SLPRB/Forestry_Cadres_Forester_Guard/SYLLABUS.md)
* **[Fire Services & Civil Defence](./03_Assam_Police_SLPRB/Fire_Emergency_Services)**: [Syllabus](./03_Assam_Police_SLPRB/Fire_Emergency_Services/SYLLABUS.md)

---

### 4. [Health & Medical (DME, DHS, DHS-FW, AYUSH, NHM)](./04_Health_DME_DHS_NHM)
* **[Grade III Technical & Paramedical](./04_Health_DME_DHS_NHM/Grade_III_Technical_Paramedical)**: [Staff Nurse, Pharmacist, Lab Tech, Radiographer Syllabus](./04_Health_DME_DHS_NHM/Grade_III_Technical_Paramedical/SYLLABUS.md) | [Official Recruitment Rules (PDF)](./04_Health_DME_DHS_NHM/Grade_III_Technical_Paramedical/Official_DME_Grade_III_Technical_Recruitment_Rules.pdf)
* **[Grade III Non-Technical / Admin](./04_Health_DME_DHS_NHM/Grade_III_Non_Technical_Admin)**: [LDA & Store Keeper Syllabus](./04_Health_DME_DHS_NHM/Grade_III_Non_Technical_Admin/SYLLABUS.md)
* **[Grade IV Hospital Staff](./04_Health_DME_DHS_NHM/Grade_IV_Hospital_Staff)**: [Syllabus](./04_Health_DME_DHS_NHM/Grade_IV_Hospital_Staff/SYLLABUS.md) | [Official Written Scheme (PDF)](./04_Health_DME_DHS_NHM/Grade_IV_Hospital_Staff/Official_DME_Grade_IV_Written_Test_Scheme.pdf)
* **[NHM Community Health Officer (CHO)](./04_Health_DME_DHS_NHM/NHM_Community_Health_Officer_CHO)**: [RMNCH+A & Primary Health Care Syllabus](./04_Health_DME_DHS_NHM/NHM_Community_Health_Officer_CHO/SYLLABUS.md)

---

### 5. [Education, Schools, Colleges & Universities](./05_Education_TET_Faculty)
* **[Assam Special & General TET (LP & UP)](./05_Education_TET_Faculty/Assam_TET_LP_UP)**: [Child Development, Pedagogy, Maths & EVS Syllabus](./05_Education_TET_Faculty/Assam_TET_LP_UP/SYLLABUS.md)
* **[Secondary TET (High School)](./05_Education_TET_Faculty/Secondary_TET_High_School)**: [GS & Pedagogy Syllabus](./05_Education_TET_Faculty/Secondary_TET_High_School/SYLLABUS.md)
* **[Higher Secondary TET (PGT)](./05_Education_TET_Faculty/Higher_Secondary_TET_PGT)**: [Subject Specialization & Pedagogy Syllabus](./05_Education_TET_Faculty/Higher_Secondary_TET_PGT/SYLLABUS.md)
* **[DHE College Assistant Professor](./05_Education_TET_Faculty/DHE_College_Assistant_Professor)**: [Selection Guidelines & API Scoring](./05_Education_TET_Faculty/DHE_College_Assistant_Professor/SYLLABUS.md)
* **[State Universities Staff](./05_Education_TET_Faculty/State_Universities_Staff)**: [Gauhati, Dibrugarh, Cotton Non-Teaching Syllabus](./05_Education_TET_Faculty/State_Universities_Staff/SYLLABUS.md)

---

### 6. [Judiciary & Gauhati High Court](./06_Judiciary_Gauhati_HC)
* **[Assam Judicial Service (AJS Grade I, II, III)](./06_Judiciary_Gauhati_HC/Assam_Judicial_Service_AJS)**: [Civil Law I & II, Criminal Law & English Syllabus](./06_Judiciary_Gauhati_HC/Assam_Judicial_Service_AJS/SYLLABUS.md)
* **[High Court Registry Staff](./06_Judiciary_Gauhati_HC/High_Court_Registry_Staff)**: [LDA, Stenographer, Typist Syllabus](./06_Judiciary_Gauhati_HC/High_Court_Registry_Staff/SYLLABUS.md)
* **[District Courts Staff](./06_Judiciary_Gauhati_HC/District_Courts_Staff)**: [Bench Assistant, Copyist Syllabus](./06_Judiciary_Gauhati_HC/District_Courts_Staff/SYLLABUS.md)

---

### 7. [Power Sector Utilities (APDCL, AEGCL, APGCL)](./07_Power_Sector_APDCL)
* **[Assistant Manager & Junior Manager](./07_Power_Sector_APDCL/Assistant_Junior_Manager)**
  * 📖 [Engineering & Aptitude Syllabus Guide](./07_Power_Sector_APDCL/Assistant_Junior_Manager/SYLLABUS.md)
  * 📥 [Official AM GS Syllabus (PDF)](./07_Power_Sector_APDCL/Assistant_Junior_Manager/Official_Syllabus_Assistant_Manager_GS.pdf) | [Official AM Electrical (PDF)](./07_Power_Sector_APDCL/Assistant_Junior_Manager/Official_Syllabus_AM_Electrical_Engg.pdf) | [Official AM Mechanical (PDF)](./07_Power_Sector_APDCL/Assistant_Junior_Manager/Official_Syllabus_AM_Mechanical_Engg.pdf) | [Official AM Civil (PDF)](./07_Power_Sector_APDCL/Assistant_Junior_Manager/Official_Syllabus_AM_Civil_Engg.pdf) | [Official AM HR (PDF)](./07_Power_Sector_APDCL/Assistant_Junior_Manager/Official_Syllabus_AM_Human_Resources.pdf) | [Official JM GS (PDF)](./07_Power_Sector_APDCL/Assistant_Junior_Manager/Official_Syllabus_Junior_Manager_GS.pdf) | [Official JM Electrical (PDF)](./07_Power_Sector_APDCL/Assistant_Junior_Manager/Official_Syllabus_JM_Electrical_Engg.pdf)
* **[AAO, OFA & Sahayak](./07_Power_Sector_APDCL/AAO_OFA_Sahayak)**: [Accounts Officer & Lineman Syllabus](./07_Power_Sector_APDCL/AAO_OFA_Sahayak/SYLLABUS.md)

---

### 8. [Panchayat & Rural Development (P&RD & ASRLM)](./08_PnRD_Rural_Development)
* **[Panchayat Core Cadres (GPS, Tax Collector)](./08_PnRD_Rural_Development/Panchayat_Core_GPS_TaxCollector)**: [Syllabus](./08_PnRD_Rural_Development/Panchayat_Core_GPS_TaxCollector/SYLLABUS.md)
* **[ASRLM (Jeevika Mission)](./08_PnRD_Rural_Development/ASRLM_Jeevika_Mission)**: [Block Program Manager Syllabus](./08_PnRD_Rural_Development/ASRLM_Jeevika_Mission/SYLLABUS.md)
* **[P&RD Junior Engineers (Civil)](./08_PnRD_Rural_Development/PnRD_Engineers_Accredited_JE)**: [Syllabus](./08_PnRD_Rural_Development/PnRD_Engineers_Accredited_JE/SYLLABUS.md) | [Official P&RD JE Civil (PDF)](./08_PnRD_Rural_Development/PnRD_Engineers_Accredited_JE/Official_Syllabus_JE_Civil_PnRD.pdf)

---

### 9. [Transport, ASTC & Inland Waterways](./09_Transport_IWT_ASTC)
* **[Transport Enforcement Branch](./09_Transport_IWT_ASTC/Transport_Enforcement_Branch)**: [Assistant Enforcement Inspector Syllabus](./09_Transport_IWT_ASTC/Transport_Enforcement_Branch/SYLLABUS.md)
* **[ASTC State Transport](./09_Transport_IWT_ASTC/ASTC_State_Transport)**: [Superintendent, Conductor, Driver Syllabus](./09_Transport_IWT_ASTC/ASTC_State_Transport/SYLLABUS.md)
* **[Inland Water Transport (IWT)](./09_Transport_IWT_ASTC/Inland_Water_Transport_IWT)**: [Syllabus Guide](./09_Transport_IWT_ASTC/Inland_Water_Transport_IWT/SYLLABUS.md) | [Official AE IWT Transport (PDF)](./09_Transport_IWT_ASTC/Inland_Water_Transport_IWT/Official_Syllabus_AE_IWT_Transport.pdf)

---

### 10. [State Public Enterprises, Cooperatives & Boards](./10_Corporations_Cooperatives_Boards)
* **[Assam Cooperative Apex Bank](./10_Corporations_Cooperatives_Boards/Assam_Cooperative_Apex_Bank)**: [Banking Aptitude Syllabus](./10_Corporations_Cooperatives_Boards/Assam_Cooperative_Apex_Bank/SYLLABUS.md)
* **[AGCL Gas & APL Petro-chemicals](./10_Corporations_Cooperatives_Boards/AGCL_Gas_Company_APL_Petrochem)**: [Chemical & Mechanical Plant Engineering Syllabus](./10_Corporations_Cooperatives_Boards/AGCL_Gas_Company_APL_Petrochem/SYLLABUS.md)
* **[Sericulture & Handloom Textiles](./10_Corporations_Cooperatives_Boards/Sericulture_Handloom_Textiles)**: [Muga/Eri Biology & Handloom Weaving Syllabus](./10_Corporations_Cooperatives_Boards/Sericulture_Handloom_Textiles/SYLLABUS.md)
* **[Agri Marketing & Fisheries Boards (ASAMB & AFDC)](./10_Corporations_Cooperatives_Boards/Agri_Marketing_Fisheries_Boards)**: [Market Inspector & Fishery Officer Syllabus](./10_Corporations_Cooperatives_Boards/Agri_Marketing_Fisheries_Boards/SYLLABUS.md)

---

### 11. [Revenue, Land Records & Disaster Management](./11_Revenue_Disaster_Management)
* **[Lot Mandal (Patwari / Land Record Cadre)](./11_Revenue_Disaster_Management/Lot_Mandal_Patwari_Land_Records)**: [Land Records, Mensuration & Survey Practical Scheme](./11_Revenue_Disaster_Management/Lot_Mandal_Patwari_Land_Records/SYLLABUS.md)
* **[ASDMA Disaster Management](./11_Revenue_Disaster_Management/ASDMA_Disaster_Management)**: [Field Officer Disaster Management Syllabus](./11_Revenue_Disaster_Management/ASDMA_Disaster_Management/SYLLABUS.md)

---

### 12. [Assam Legislative Assembly Secretariat](./12_Legislative_Assembly_Secretariat)
* **[Junior Administrative Assistant (JAA) & Typist](./12_Legislative_Assembly_Secretariat/Junior_Admin_Assistant_JAA)**: [Parliamentary Procedures & English Syllabus](./12_Legislative_Assembly_Secretariat/Junior_Admin_Assistant_JAA/SYLLABUS.md)
* **[Language Reporters & Translation Officers](./12_Legislative_Assembly_Secretariat/Language_Reporters_Translators)**: [120/140 wpm Shorthand & Translation Syllabus](./12_Legislative_Assembly_Secretariat/Language_Reporters_Translators/SYLLABUS.md)

---

## Structured JSON Metadata
All official PDF file paths, syllabus files, and portal URLs are indexed in [`metadata_catalog.json`](./metadata_catalog.json).

## Roadmap: future improvements

- [ ] Fill the 12 README links that point to files never committed (for example the APSC CCE Mains syllabus)
- [ ] Add a "last verified" date and source URL for every syllabus
- [ ] Turn the master checklist into a progress tracker inside the AxomRank app
- [ ] Generate one blog page per exam from this data (syllabus, pattern, past-paper links)
- [ ] Move large official PDFs to releases or R2 to slim the repo

## For AI agents and contributors

Read [AGENTS.md](AGENTS.md). Never present an unverified syllabus as official. Keep the source and date with every record.

Commit as the `axomrank` account. Keep changes small and reviewable, and run the repository's checks before pushing.

## Part of AxomRank

[AxomRank](https://axomrank.pages.dev) offers free, bilingual preparation for Assam government exams. Related repositories:

- **Learn:** [axomrank.github.io](https://github.com/axomrank/axomrank.github.io) (the AxomRank learning app), [ahom-kings-lessons](https://github.com/axomrank/ahom-kings-lessons) (41 bilingual Ahom reign lessons), [floor-test-simulator](https://github.com/axomrank/floor-test-simulator) (parliamentary majority simulator)
- **Explore Assam history:** [ahom-kingdom-history](https://github.com/axomrank/ahom-kingdom-history) (illustrated Ahom kingdom website), [assam-history-map](https://github.com/axomrank/assam-history-map) (year-by-year historical map), [assam-history-characters](https://github.com/axomrank/assam-history-characters) (character sheets for Assam's history), [assam-visual-archive](https://github.com/axomrank/assam-visual-archive) (gallery of Assam scenes and photographs), [assam-heritage-ai-art](https://github.com/axomrank/assam-heritage-ai-art) (AI art gallery of Assamese heritage)
- **Open data:** [assam-exam-pyq](https://github.com/axomrank/assam-exam-pyq) (2,398 previous-year questions with answers), [assam-maps](https://github.com/axomrank/assam-maps) (map portal and GIS layers), [assam-history-sources](https://github.com/axomrank/assam-history-sources) (Kamarupa inscriptions and primary sources)
- **Publishing and brand:** [axomrank-blog](https://github.com/axomrank/axomrank-blog) (exam guides built from real papers), [assam-history-books](https://github.com/axomrank/assam-history-books) (13-book history of Assam), [axomrank-brand-assets](https://github.com/axomrank/axomrank-brand-assets) (brand kit and social media library)

## License and contact

No license file yet. Official documents belong to their issuing bodies.

Corrections and questions: open an issue in this repository. AxomRank is run by Angsuman Das (sole proprietor).
