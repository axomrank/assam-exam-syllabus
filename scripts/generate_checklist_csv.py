"""
Master Checklist Generator for Assam State-Level & National Examinations
Generates:
  - csv/MAster_topics_checklist.csv
  - json/MAster_topics_checklist.json

Schema (9 Columns):
  1. Domain
  2. Subject
  3. Topic
  4. Subtopic
  5. Sub_Subtopic
  6. Study_Format (Chronology, Listicle, Conceptual, Formula, Spatial/Map, Constitutional/Legal, Case Study/Current Affair)
  7. Chronology_Era (Specific Date/Year/Era Anchors or 'N/A')
  8. Assam_Specific (Yes/No)
  9. Checklist ([ ])
"""

import os
import re
import csv
import json

BASE_DIR = "/home/angsuman/extra_spac/Study_Assam"
SRC_CSV = os.path.join(BASE_DIR, "csv", "MAster tpics.csv")
OUT_CSV = os.path.join(BASE_DIR, "csv", "MAster_topics_checklist.csv")
OUT_JSON = os.path.join(BASE_DIR, "json", "MAster_topics_checklist.json")

# Import the complete, verified 174 items from step 595
ADDITIONAL_ROWS = [
    # ----------------------------------------------------
    # 1. ECONOMY: Inflation, Markets, Bad Loans, Federalism & Assam Mega Projects (17 items)
    # ----------------------------------------------------
    ("Economy", "Indian Economy Essentials", "Macroeconomic Fundamentals & Inflation", "Inflation Dynamics", "Demand-Pull vs Cost-Push Inflation Mechanisms", "No"),
    ("Economy", "Indian Economy Essentials", "Macroeconomic Fundamentals & Inflation", "Inflation Dynamics", "Stagflation, Deflation & Core vs Headline Inflation", "No"),
    ("Economy", "Indian Economy Essentials", "Macroeconomic Fundamentals & Inflation", "Inflation Dynamics", "Phillips Curve Concept (Inflation vs Unemployment Tradeoff)", "No"),
    ("Economy", "Indian Economy Essentials", "Financial Markets & Banking Reforms", "Financial Markets & Regulatory Framework", "SEBI: Capital Market Regulation & Investor Protection", "No"),
    ("Economy", "Indian Economy Essentials", "Financial Markets & Banking Reforms", "Financial Markets & Regulatory Framework", "Primary Market (IPOs) vs Secondary Stock Exchanges (BSE, NSE)", "No"),
    ("Economy", "Indian Economy Essentials", "Financial Markets & Banking Reforms", "Financial Markets & Regulatory Framework", "Foreign Investment: FDI vs Foreign Portfolio Investment (FPI)", "No"),
    ("Economy", "Indian Economy Essentials", "Financial Markets & Banking Reforms", "Bad Loans Resolution & NPAs", "Insolvency and Bankruptcy Code (IBC 2016) Process", "No"),
    ("Economy", "Indian Economy Essentials", "Financial Markets & Banking Reforms", "Bad Loans Resolution & NPAs", "SARFAESI Act & Debt Recovery Tribunals (DRT)", "No"),
    ("Economy", "Indian Economy Essentials", "Financial Markets & Banking Reforms", "Bad Loans Resolution & NPAs", "National Asset Reconstruction Company (Bad Bank / NARCL)", "No"),
    ("Economy", "Indian Economy Essentials", "Fiscal Federalism & Development Planning", "Finance Commission & Devolution", "15th & 16th Finance Commission Mandate & Horizontal Devolution Formula", "No"),
    ("Economy", "Indian Economy Essentials", "Fiscal Federalism & Development Planning", "Finance Commission & Devolution", "Special Category Status & NE States Funding Pattern (90:10)", "Yes"),
    ("Economy", "Indian Economy Essentials", "Fiscal Federalism & Development Planning", "Aspirational & Poverty Indices", "NITI Aayog Aspirational Districts Programme in Assam (Baksa, Barpeta, etc.)", "Yes"),
    ("Economy", "Indian Economy Essentials", "Fiscal Federalism & Development Planning", "Aspirational & Poverty Indices", "Multidimensional Poverty Index (MPI) Indicators & Dimensions", "No"),
    ("Economy", "Assam Economy Essentials", "Major Industrial Infrastructure of Assam", "Key Enterprises & Mega Projects", "BCPL: Brahmaputra Cracker and Polymer Limited at Lepetkata", "Yes"),
    ("Economy", "Assam Economy Essentials", "Major Industrial Infrastructure of Assam", "Key Enterprises & Mega Projects", "BVFCL: Brahmaputra Valley Fertilizer Corporation Limited at Namrup", "Yes"),
    ("Economy", "Assam Economy Essentials", "Major Industrial Infrastructure of Assam", "Key Enterprises & Mega Projects", "APART: Assam Agribusiness and Rural Transformation Project", "Yes"),
    ("Economy", "Assam Economy Essentials", "Major Industrial Infrastructure of Assam", "Key Enterprises & Mega Projects", "Assam Microfinance Incentive & Relief Scheme (AMFIRS)", "Yes"),

    # Assam State Budget, Public Finance & Economic Survey (6 items)
    ("Economy", "Assam Economy Essentials", "Assam State Budget, Public Finance & Economic Survey", "Budgetary Indicators & Revenue Composition", "Assam State Budget: Annual Financial Statement (Article 202) Structure", "Yes"),
    ("Economy", "Assam Economy Essentials", "Assam State Budget, Public Finance & Economic Survey", "Budgetary Indicators & Revenue Composition", "Assam GSDP Growth Rate & Debt-to-GSDP Fiscal Deficit Thresholds", "Yes"),
    ("Economy", "Assam Economy Essentials", "Assam State Budget, Public Finance & Economic Survey", "Budgetary Indicators & Revenue Composition", "Own Tax Revenue Pillars: State GST (SGST), Petroleum Sales Tax & State Excise", "Yes"),
    ("Economy", "Assam Economy Essentials", "Assam State Budget, Public Finance & Economic Survey", "Budgetary Indicators & Revenue Composition", "Capital Outlay vs Revenue Expenditure: Infrastructure Focus in Assam", "Yes"),
    ("Economy", "Assam Economy Essentials", "Assam State Budget, Public Finance & Economic Survey", "Livelihood Missions & Rural Finance", "ASRLM: Assam State Rural Livelihoods Mission & SHG Credit Linkage", "Yes"),
    ("Economy", "Assam Economy Essentials", "Assam State Budget, Public Finance & Economic Survey", "Livelihood Missions & Rural Finance", "Mukhya Mantri Mahila Udyamita Abhiyan & Lakhpati Baideo Scheme", "Yes"),

    # GI Tags of Assam (5 items)
    ("Economy", "Assam Economy Essentials", "Geographical Indications (GI Tags) of Assam", "Agricultural, Handloom & Manufactured GI Products", "Judima: Traditional Dimasa Rice Wine (First Traditional Brew in North East with GI Tag)", "Yes"),
    ("Economy", "Assam Economy Essentials", "Geographical Indications (GI Tags) of Assam", "Agricultural, Handloom & Manufactured GI Products", "Kaji Nemu: Assam Lemon (State Fruit of Assam & Indigenous Citrus with GI Tag)", "Yes"),
    ("Economy", "Assam Economy Essentials", "Geographical Indications (GI Tags) of Assam", "Agricultural, Handloom & Manufactured GI Products", "Boka Chaul (Magic Mud-Rice) & Chokuwa Rice (Soft Parboiled Rice of Assam)", "Yes"),
    ("Economy", "Assam Economy Essentials", "Geographical Indications (GI Tags) of Assam", "Agricultural, Handloom & Manufactured GI Products", "Tezpur Litchi & Karbi Anglong Organic Ginger GI Registration", "Yes"),
    ("Economy", "Assam Economy Essentials", "Geographical Indications (GI Tags) of Assam", "Agricultural, Handloom & Manufactured GI Products", "Assam Gamosa (Registered 2022) & Sarthebari Bell Metal Craft GI Status", "Yes"),

    # ----------------------------------------------------
    # 2. APTITUDE / CSAT: Permutations, Combinations, Probability, Data Sufficiency (8 items)
    # ----------------------------------------------------
    ("Aptitude", "Quantitative Aptitude (Mathematics)", "Permutations, Combinations & Probability", "Combinatorics Basics", "Fundamental Principle of Counting (Multiplication & Addition Rules)", "No"),
    ("Aptitude", "Quantitative Aptitude (Mathematics)", "Permutations, Combinations & Probability", "Combinatorics Basics", "Permutations: Linear Arrangements & Factorial Notation", "No"),
    ("Aptitude", "Quantitative Aptitude (Mathematics)", "Permutations, Combinations & Probability", "Combinatorics Basics", "Combinations: Group Selection Formula nCr", "No"),
    ("Aptitude", "Quantitative Aptitude (Mathematics)", "Permutations, Combinations & Probability", "Probability Concepts", "Classical Probability: Single & Multiple Coin Tosses", "No"),
    ("Aptitude", "Quantitative Aptitude (Mathematics)", "Permutations, Combinations & Probability", "Probability Concepts", "Dice Rolling Probability (Single & Pair of Dice)", "No"),
    ("Aptitude", "Quantitative Aptitude (Mathematics)", "Permutations, Combinations & Probability", "Probability Concepts", "Card Deck Probability (Suits, Face Cards, Honor Cards)", "No"),
    ("Aptitude", "Logical Reasoning", "CSAT Specialized Reasoning", "Data Sufficiency", "Data Sufficiency: Evaluating Statement 1 vs Statement 2 Adequacy", "No"),
    ("Aptitude", "Logical Reasoning", "CSAT Specialized Reasoning", "Administrative Decision Making", "Situational Judgment & Administrative Problem-Solving Scenarios", "No"),

    # ----------------------------------------------------
    # 3. POLITY: Lokpal, Lokayukta, NHRC, AHRC, Amendments, Secretariat, Delimitation, Officers, Swaran Singh (22 items)
    # ----------------------------------------------------
    ("Polity", "Indian Polity & Constitution", "Anti-Corruption & Transparency Bodies", "Ombudsman & Vigilance Institutions", "Lokpal & Lokayuktas Act 2013: Jurisdiction & Structure", "No"),
    ("Polity", "Indian Polity & Constitution", "Anti-Corruption & Transparency Bodies", "Ombudsman & Vigilance Institutions", "Assam Lokayukta and Upa-Lokayuktas Act & Jurisdiction", "Yes"),
    ("Polity", "Indian Polity & Constitution", "Anti-Corruption & Transparency Bodies", "Ombudsman & Vigilance Institutions", "Central Vigilance Commission (CVC): Mandate & Structure", "No"),
    ("Polity", "Indian Polity & Constitution", "Anti-Corruption & Transparency Bodies", "Ombudsman & Vigilance Institutions", "Right to Information (RTI Act 2005) & Central/State Information Commissions", "No"),
    ("Polity", "Indian Polity & Constitution", "Anti-Corruption & Transparency Bodies", "Human Rights Commissions", "National Human Rights Commission (NHRC): Powers & Protection of HR Act", "No"),
    ("Polity", "Indian Polity & Constitution", "Anti-Corruption & Transparency Bodies", "Human Rights Commissions", "Assam Human Rights Commission (AHRC): Composition & Functions", "Yes"),
    ("Polity", "Indian Polity & Constitution", "Recent Landmark Constitutional Amendments", "Key Amendments (103rd to 106th)", "103rd Amendment: 10% EWS Quota in Admissions & Jobs", "No"),
    ("Polity", "Indian Polity & Constitution", "Recent Landmark Constitutional Amendments", "Key Amendments (103rd to 106th)", "104th Amendment: SC/ST Reservation Extension & Anglo-Indian Abolition", "No"),
    ("Polity", "Indian Polity & Constitution", "Recent Landmark Constitutional Amendments", "Key Amendments (103rd to 106th)", "105th Amendment: Restoring States Power to Specify SEBC/OBC Lists", "No"),
    ("Polity", "Indian Polity & Constitution", "Recent Landmark Constitutional Amendments", "Key Amendments (103rd to 106th)", "106th Amendment: Nari Shakti Vandan Adhiniyam (33% Women Reservation)", "No"),
    ("Polity", "Indian Polity & Constitution", "DPSPs, Duties & Union-State Organs", "DPSPs & Fundamental Duties", "Fundamental Duties (Article 51A): 42nd Amendment (Swaran Singh Committee) & 86th Amendment", "No"),
    ("Polity", "Assam Governance & Administration", "Assam Administrative Machinery & Secretariat", "State Executive & Secretariat Organization", "Assam Secretariat (Janata Bhawan, Dispur): Structure & Departments", "Yes"),
    ("Polity", "Assam Governance & Administration", "Assam Administrative Machinery & Secretariat", "State Executive & Secretariat Organization", "Directorates vs Secretariat: Policy Formulation vs Implementation", "Yes"),
    ("Polity", "Assam Governance & Administration", "Assam Administrative Machinery & Secretariat", "State Executive & Secretariat Organization", "District Administration: Statutory Powers of District Commissioner (DC)", "Yes"),
    ("Polity", "Assam Governance & Administration", "Assam Administrative Machinery & Secretariat", "State Executive & Secretariat Organization", "Sub-Divisional & Circle Administration: SDO (Civil), Circle Officer & Mouzadars", "Yes"),
    ("Polity", "Assam Governance & Administration", "Assam Administrative Machinery & Secretariat", "Commissions & Delimitation", "Assam Public Service Commission (APSC): Article 315-323 Constitutional Mandate", "Yes"),
    ("Polity", "Assam Governance & Administration", "Assam Administrative Machinery & Secretariat", "Commissions & Delimitation", "Assam State Election Commission: PRIs & Urban Local Bodies Conduct", "Yes"),
    ("Polity", "Assam Governance & Administration", "Assam Administrative Machinery & Secretariat", "Commissions & Delimitation", "Assam Delimitation 2023: 126 Assembly & 14 Lok Sabha Constituencies Re-alignment", "Yes"),
    ("Polity", "Assam Governance & Administration", "Assam Administrative Machinery & Secretariat", "Commissions & Delimitation", "Assam Inter-State Border Settlement Agreements (Meghalaya, Arunachal Pradesh)", "Yes"),
    ("Polity", "Assam Governance & Administration", "Constitutional Law Officers & State Judicial Bodies", "State Legal Machinery & High Court Framework", "Advocate General of Assam (Article 165): Appointment, Qualifications & Rights in Legislature", "Yes"),
    ("Polity", "Assam Governance & Administration", "Constitutional Law Officers & State Judicial Bodies", "State Legal Machinery & High Court Framework", "State Finance Commission of Assam (Article 243-I & 243-Y): Municipal & Panchayat Devolution", "Yes"),
    ("Polity", "Assam Governance & Administration", "Constitutional Law Officers & State Judicial Bodies", "State Legal Machinery & High Court Framework", "Gauhati High Court: Principal Seat at Guwahati & 3 Outlying Benches (Kohima, Aizawl, Itanagar)", "Yes"),

    # ----------------------------------------------------
    # 4. ASSAM HISTORY & CULTURE: Architecture, Literature, Tribal Ethnography, Accords, Archaeology (34 items)
    # ----------------------------------------------------
    ("History", "Assam History", "Medieval Assam: Ahoms & Regional Kingdoms", "Ahom Royal Architecture & Fortifications", "Talatal Ghar: Underground Tunnels & Secret Military Escape Architecture", "Yes"),
    ("History", "Assam History", "Medieval Assam: Ahoms & Regional Kingdoms", "Ahom Royal Architecture & Fortifications", "Kareng Ghar at Garhgaon: Multi-storied Royal Palace", "Yes"),
    ("History", "Assam History", "Medieval Assam: Ahoms & Regional Kingdoms", "Ahom Royal Architecture & Fortifications", "Sivasagar Sivadol: Architecture, Tallest Shikhara & Sivasagar Tank", "Yes"),
    ("History", "Assam History", "Medieval Assam: Ahoms & Regional Kingdoms", "Ahom Royal Architecture & Fortifications", "Namdang Stone Bridge: Built on Single Solid Rock with Indigenous Mortar", "Yes"),
    ("History", "Assam History", "Medieval Assam: Ahoms & Regional Kingdoms", "Ahom Royal Architecture & Fortifications", "Charaideo Moidams: Ahom Mound-Burial System & 1st Cultural UNESCO World Heritage Site in NE (2024)", "Yes"),
    ("History", "Art, Culture & Literature", "Sankardeva & Neo-Vaishnavite Culture", "Ekasarana Dharma & Satras", "Madhavdev Namghosa (Hazari Ghosa): Philosophical Essence of Ekasarana Dharma", "Yes"),
    ("History", "Art, Culture & Literature", "Assamese Literature & Cultural Icons", "Pre-Vaishnavite Literature", "Madhava Kandali: Saptakanda Ramayana (First Regional Ramayana Translation)", "Yes"),
    ("History", "Art, Culture & Literature", "Assamese Literature & Cultural Icons", "Pre-Vaishnavite Literature", "Hem Saraswati: Prahlad Charitra & Haragauri Samvada", "Yes"),

    # Tribal Communities & Ethnography of Assam (8 items)
    ("History", "Art, Culture & Literature", "Tribal Communities & Ethnography of Assam", "Tribal Social Structures & Customs", "Bodo Community: Bathou Religion, Kherai Dance & Dokhona Attire", "Yes"),
    ("History", "Art, Culture & Literature", "Tribal Communities & Ethnography of Assam", "Tribal Social Structures & Customs", "Mising Community: Murong Okum (Youth Hall), Ali-Aye-Ligang & Gero Weaving", "Yes"),
    ("History", "Art, Culture & Literature", "Tribal Communities & Ethnography of Assam", "Tribal Social Structures & Customs", "Karbi Community: Jirnam Organization, Chojun Puja, Rongker & Phoroi Attire", "Yes"),
    ("History", "Art, Culture & Literature", "Tribal Communities & Ethnography of Assam", "Tribal Social Structures & Customs", "Dimasa Community: Nodrang (Youth Dormitory), Busu Dima & Rigu-Rikhaosa", "Yes"),
    ("History", "Art, Culture & Literature", "Tribal Communities & Ethnography of Assam", "Tribal Social Structures & Customs", "Tiwa (Lalung) Community: Boroghar Institution, Yangli & Sogra Misawa", "Yes"),
    ("History", "Art, Culture & Literature", "Tribal Communities & Ethnography of Assam", "Tribal Social Structures & Customs", "Rabha Community: Baikho Festival (Dehal Puja) & Farkhanti Dance", "Yes"),
    ("History", "Art, Culture & Literature", "Tribal Communities & Ethnography of Assam", "Tribal Social Structures & Customs", "Deori & Sonowal Kachari Communities: Traditional Village Customs & Folk Songs", "Yes"),
    ("History", "Art, Culture & Literature", "Tribal Communities & Ethnography of Assam", "Tribal Social Structures & Customs", "Tea Tribes of Assam: Karam Puja, Jhumur Dance & Cultural Integration", "Yes"),

    # Post-Independence Reorganization & Accords of Assam (8 items)
    ("History", "Assam History", "Post-Independence Reorganization & Accords of Assam", "Reorganization of Greater Assam", "Creation of Nagaland (1963) from Naga Hills District of Assam", "Yes"),
    ("History", "Assam History", "Post-Independence Reorganization & Accords of Assam", "Reorganization of Greater Assam", "North-Eastern Areas (Reorganisation) Act 1971: Meghalaya, Mizoram & Arunachal", "Yes"),
    ("History", "Assam History", "Post-Independence Reorganization & Accords of Assam", "Social Movements & Language Acts", "Assam Official Language Act 1960: Movement & Provisions", "Yes"),
    ("History", "Assam History", "Post-Independence Reorganization & Accords of Assam", "Social Movements & Language Acts", "Medium of Instruction Movement 1972 in Assam Colleges & Universities", "Yes"),
    ("History", "Assam History", "Post-Independence Reorganization & Accords of Assam", "Assam Accord & Peace Settlements", "Assam Movement (1979-1985) Led by AASU & AAGSP: Historical Background", "Yes"),
    ("History", "Assam History", "Post-Independence Reorganization & Accords of Assam", "Assam Accord & Peace Settlements", "Assam Accord (15 August 1985): Clause 5 (Foreigners Detection Cut-off 25 March 1971)", "Yes"),
    ("History", "Assam History", "Post-Independence Reorganization & Accords of Assam", "Assam Accord & Peace Settlements", "Assam Accord Clause 6: Constitutional, Legislative & Cultural Safeguards Committee", "Yes"),
    ("History", "Assam History", "Post-Independence Reorganization & Accords of Assam", "Assam Accord & Peace Settlements", "Bodo Peace Accords: 1993 (BAC), 2003 (BTC 6th Schedule), 2020 (BTR Accord)", "Yes"),

    # Archaeological & Ancient Heritage Sites of Assam (5 items)
    ("History", "Assam History", "Archaeological & Ancient Heritage Sites of Assam", "Ancient Architectural Remains & Stone Sculptures", "Madan Kamdev (Baihatta Chariali): Khajuraho of Assam & 10th-12th Century Pala Sculptures", "Yes"),
    ("History", "Assam History", "Archaeological & Ancient Heritage Sites of Assam", "Ancient Architectural Remains & Stone Sculptures", "Sri Surya Pahar (Goalpara): Confluence of Hinduism, Buddhism & Jainism Rock-Cut Relics", "Yes"),
    ("History", "Assam History", "Archaeological & Ancient Heritage Sites of Assam", "Ancient Architectural Remains & Stone Sculptures", "Dah Parbatia (Tezpur): Oldest 5th-6th Century Gupta Temple Doorframe with Ganga-Yamuna Carvings", "Yes"),
    ("History", "Assam History", "Archaeological & Ancient Heritage Sites of Assam", "Ancient Architectural Remains & Stone Sculptures", "Deopahar Ruins (Numaligarh): Ancient 9th-Century Stone Temple & Terracotta Sculptures", "Yes"),
    ("History", "Assam History", "Archaeological & Ancient Heritage Sites of Assam", "Ancient Architectural Remains & Stone Sculptures", "Ambari Archaeological Site (Guwahati): Shunga-Kushana to Medieval Urban Trade Pottery Excavation", "Yes"),

    # Indian History Additions: Santhal, Birsa Munda, Sangam, Chittagong, Lord Ripon (5 items)
    ("History", "Modern Indian History", "Revolt of 1857 & Social Reforms", "Tribal & Peasant Uprisings", "Santhal Rebellion (1855): Sidhu & Kanhu Leadership against Dikus & British Revenue System", "No"),
    ("History", "Modern Indian History", "Revolt of 1857 & Social Reforms", "Tribal & Peasant Uprisings", "Birsa Munda & Ulgulan Movement (1899-1900): Chotanagpur Tribal Land Rights Resistance", "No"),
    ("History", "Ancient Indian History", "Gupta Empire & South Indian Kingdoms", "Gupta Golden Age", "Sangam Literature: Assemblies at Madurai, Tolkappiyam Grammar & Silappadikaram Epic", "No"),
    ("History", "Modern Indian History", "Indian National Movement (1885-1947)", "Gandhian Mass Movements", "Chittagong Armoury Raid (1930): Surya Sen (Masterda), Pritilata Waddedar & Kalpana Datta", "No"),
    ("History", "Modern Indian History", "British Conquest of India", "Colonial Battles & Policies", "Lord Ripon: Father of Local Self-Government (1882) & Ilbert Bill Racial Controversy (1883)", "No"),

    # ----------------------------------------------------
    # 5. GEOGRAPHY: Protected Areas, State Symbols, Sanctuaries, Demographics, Bridges, Wetlands, Peaks (27 items)
    # ----------------------------------------------------
    ("Geography", "Environment & Ecology", "7 National Parks of Assam", "State Symbols & Endemic Aquatic Wildlife", "Gangetic River Dolphin (Xihu): Assam State Aquatic Animal & Habitat", "Yes"),
    ("Geography", "Environment & Ecology", "7 National Parks of Assam", "State Symbols & Endemic Aquatic Wildlife", "Pobitora Wildlife Sanctuary: Highest Density of One-Horned Rhinoceros", "Yes"),
    ("Geography", "Environment & Ecology", "7 National Parks of Assam", "State Symbols & Endemic Aquatic Wildlife", "Hoollongapar Gibbon Sanctuary: Home to India's Only Ape Species", "Yes"),

    # Protected Areas & Biodiversity Conservation of Assam (7 items)
    ("Geography", "Environment & Ecology", "Protected Areas & Biodiversity of Assam", "Protected Area Networks & Conservation", "Elephant Reserves of Assam: Sonitpur, Dihing Patkai, Kaziranga-Karbi Anglong, Dhansiri, Chirang-Ripu", "Yes"),
    ("Geography", "Environment & Ecology", "Protected Areas & Biodiversity of Assam", "Protected Area Networks & Conservation", "Tiger Reserves of Assam: Kaziranga, Manas, Nameri & Orang Tiger Reserves", "Yes"),
    ("Geography", "Environment & Ecology", "Protected Areas & Biodiversity of Assam", "Protected Area Networks & Conservation", "UNESCO World Natural Heritage Sites: Kaziranga National Park (1985) & Manas Wildlife Sanctuary (1985)", "Yes"),
    ("Geography", "Environment & Ecology", "Protected Areas & Biodiversity of Assam", "Protected Area Networks & Conservation", "Ramsar Sites: Deepor Beel Wetland Ecology, Threats & Proposed Additional Ramsar Sites", "Yes"),
    ("Geography", "Environment & Ecology", "Protected Areas & Biodiversity of Assam", "Protected Area Networks & Conservation", "Latest National Parks: Raimona (6th - Ripu Reserve Forest) & Dihing Patkai (7th - Rainforest)", "Yes"),
    ("Geography", "Environment & Ecology", "Protected Areas & Biodiversity of Assam", "Protected Area Networks & Conservation", "Biodiversity Hotspots: Assam Location at Junction of Indo-Burma & Eastern Himalaya Hotspots", "Yes"),
    ("Geography", "Environment & Ecology", "Protected Areas & Biodiversity of Assam", "Protected Area Networks & Conservation", "Biosphere Reserves of Assam: Manas Biosphere Reserve & Dibru-Saikhowa Biosphere Reserve", "Yes"),

    # Demographics, Census & Transportation Bridges of Assam (9 items)
    ("Geography", "Assam Geography", "Demographics, Census & Transportation Bridges", "Census 2011 Demographic Indicators", "Assam Census 2011: Total Population (3.12 Cr), Density (398/sq km) & Growth Rate", "Yes"),
    ("Geography", "Assam Geography", "Demographics, Census & Transportation Bridges", "Census 2011 Demographic Indicators", "Assam Literacy Rate (72.19%): Male vs Female & District Variations", "Yes"),
    ("Geography", "Assam Geography", "Demographics, Census & Transportation Bridges", "Census 2011 Demographic Indicators", "Assam Sex Ratio (958 females per 1000 males) & Child Sex Ratio (962)", "Yes"),
    ("Geography", "Assam Geography", "Demographics, Census & Transportation Bridges", "Strategic River Bridges over Brahmaputra & Barak", "Saraighat Bridge (First Rail-cum-Road 1962) & New Saraighat Bridge", "Yes"),
    ("Geography", "Assam Geography", "Demographics, Census & Transportation Bridges", "Strategic River Bridges over Brahmaputra & Barak", "Kolia Bhomora Setu (Tezpur): Connecting Sonitpur with Nagaon", "Yes"),
    ("Geography", "Assam Geography", "Demographics, Census & Transportation Bridges", "Strategic River Bridges over Brahmaputra & Barak", "Naranarayan Setu (Jogighopa-Pancharatna): Rail-cum-Road over Brahmaputra", "Yes"),
    ("Geography", "Assam Geography", "Demographics, Census & Transportation Bridges", "Strategic River Bridges over Brahmaputra & Barak", "Bogibeel Bridge (Dibrugarh-Dhemaji): Longest Rail-cum-Road Bridge in India (4.94 km)", "Yes"),
    ("Geography", "Assam Geography", "Demographics, Census & Transportation Bridges", "Strategic River Bridges over Brahmaputra & Barak", "Bhupen Hazarika Setu (Dhola-Sadiya): India Longest Water Bridge (9.15 km on Lohit)", "Yes"),
    ("Geography", "Assam Geography", "Demographics, Census & Transportation Bridges", "Strategic River Bridges over Brahmaputra & Barak", "Dhubri-Phulbari Proposed Bridge: 19 km Connecting Assam & Meghalaya", "Yes"),

    # Major Wetlands, Lakes (Beels) of Assam (4 items)
    ("Geography", "Assam Geography", "Wetlands, Lakes (Beels) & Fluvial Dynamics", "Major Tectonic & Floodplain Beels of Assam", "Son Beel (Karimganj / Barak Valley): Largest Tectonic Wetland in Assam & 2nd Largest in Asia", "Yes"),
    ("Geography", "Assam Geography", "Wetlands, Lakes (Beels) & Fluvial Dynamics", "Major Tectonic & Floodplain Beels of Assam", "Deepor Beel (Kamrup Metro): Fluvial Freshwater Lake & Major Elephant Migratory Corridor", "Yes"),
    ("Geography", "Assam Geography", "Wetlands, Lakes (Beels) & Fluvial Dynamics", "Major Tectonic & Floodplain Beels of Assam", "Urpad Beel (Goalpara) & Samaguri Beel / Pokhi Teertha (Nagaon): Aquatic Bird Habitats", "Yes"),
    ("Geography", "Assam Geography", "Wetlands, Lakes (Beels) & Fluvial Dynamics", "Major Tectonic & Floodplain Beels of Assam", "Rata Beel & Chilarai Park Ecosystems in Western Assam", "Yes"),

    # Mountain Ranges, Peaks & Plateaus of Assam (4 items)
    ("Geography", "Assam Geography", "Mountain Ranges, Peaks & Plateaus of Assam", "Physiographic Hills & Highest Elevations", "Barail Range: Highest Mountain Range in Assam & Water Divide between Brahmaputra and Barak", "Yes"),
    ("Geography", "Assam Geography", "Mountain Ranges, Peaks & Plateaus of Assam", "Physiographic Hills & Highest Elevations", "Mahadeo Peak / Laike Peak: Highest Mountain Peak in Assam (~1,959 m in Dima Hasao)", "Yes"),
    ("Geography", "Assam Geography", "Mountain Ranges, Peaks & Plateaus of Assam", "Physiographic Hills & Highest Elevations", "Karbi Plateau & Mikir Hills: Geological Origin as Fragment of Ancient Deccan / Meghalaya Plateau", "Yes"),
    ("Geography", "Assam Geography", "Mountain Ranges, Peaks & Plateaus of Assam", "Physiographic Hills & Highest Elevations", "Rengma Hills & Southern Foothills Bordering Nagaland", "Yes"),

    # ----------------------------------------------------
    # 6. GENERAL SCIENCE & TECH: Vaccine Types, AMR, AI, Quantum, Clean Energy, Nuclear Physics (10 items)
    # ----------------------------------------------------
    ("General Awareness & Science", "Everyday Science (Biology)", "Biotechnology & Modern Health Sciences", "Immunology & Vaccine Technology", "Vaccine Types: mRNA, Viral Vector, Inactivated & Subunit Vaccines", "No"),
    ("General Awareness & Science", "Everyday Science (Biology)", "Biotechnology & Modern Health Sciences", "Immunology & Vaccine Technology", "Antimicrobial Resistance (AMR) & Antibiotics vs Antivirals", "No"),
    ("General Awareness & Science", "Everyday Science (Biology)", "Biotechnology & Modern Health Sciences", "Immunology & Vaccine Technology", "CRISPR-Cas9 Gene Editing & Stem Cell Therapy Basics", "No"),
    ("General Awareness & Science", "Current Affairs & Contemporary Issues", "Frontier Technologies & Clean Energy", "Emerging Digital & Energy Technologies", "Artificial Intelligence: Generative AI, Large Language Models & Deep Learning", "No"),
    ("General Awareness & Science", "Current Affairs & Contemporary Issues", "Frontier Technologies & Clean Energy", "Emerging Digital & Energy Technologies", "Quantum Computing: Qubits, Superposition & Quantum Supremacy", "No"),
    ("General Awareness & Science", "Current Affairs & Contemporary Issues", "Frontier Technologies & Clean Energy", "Emerging Digital & Energy Technologies", "National Green Hydrogen Mission: Electrolysis & Decarbonization Targets", "No"),
    ("General Awareness & Science", "Current Affairs & Contemporary Issues", "Frontier Technologies & Clean Energy", "Emerging Digital & Energy Technologies", "Lithium-Ion Batteries & EV Battery Ecosystem in India", "No"),

    # Nuclear Physics & Energy (3 items)
    ("General Awareness & Science", "Everyday Science (Physics)", "Nuclear Physics & Energy", "Radioactivity, Reactions & Nuclear Technology", "Nuclear Fission vs Nuclear Fusion: Reactions in Atomic Bomb, Hydrogen Bomb & Solar Energy", "No"),
    ("General Awareness & Science", "Everyday Science (Physics)", "Nuclear Physics & Energy", "Radioactivity, Reactions & Nuclear Technology", "Radioactive Emissions: Alpha, Beta & Gamma Rays, Half-Life & Penetrating Power", "No"),
    ("General Awareness & Science", "Everyday Science (Physics)", "Nuclear Physics & Energy", "Radioactivity, Reactions & Nuclear Technology", "India Three-Stage Nuclear Power Programme: Uranium, Thorium & Fast Breeder Reactors", "No"),

    # ----------------------------------------------------
    # 7. INDIA-LEVEL HERITAGE, HOTSPOTS, PROTECTED AREAS & DANCES/LANGUAGES (45 items)
    # ----------------------------------------------------
    # UNESCO Natural World Heritage Sites of India (6 items)
    ("Geography", "Environment & Ecology", "India UNESCO Natural World Heritage Sites", "Natural Heritage & Conservation Areas", "Keoladeo National Park (Bharatpur, Rajasthan): Wetland & Avian Sanctuary (1985)", "No"),
    ("Geography", "Environment & Ecology", "India UNESCO Natural World Heritage Sites", "Natural Heritage & Conservation Areas", "Sundarbans National Park (West Bengal): Mangrove Ecosystem & Royal Bengal Tiger (1987)", "No"),
    ("Geography", "Environment & Ecology", "India UNESCO Natural World Heritage Sites", "Natural Heritage & Conservation Areas", "Nanda Devi & Valley of Flowers National Parks (Uttarakhand): Alpine Flora (1988/2005)", "No"),
    ("Geography", "Environment & Ecology", "India UNESCO Natural World Heritage Sites", "Natural Heritage & Conservation Areas", "Western Ghats (Sub-Clusters in MH, GA, KA, TN, KL): Global Biodiversity Hotspot (2012)", "No"),
    ("Geography", "Environment & Ecology", "India UNESCO Natural World Heritage Sites", "Natural Heritage & Conservation Areas", "Great Himalayan National Park Conservation Area (Himachal Pradesh, 2014)", "No"),
    ("Geography", "Environment & Ecology", "India UNESCO Natural World Heritage Sites", "Natural Heritage & Conservation Areas", "Khangchendzonga National Park (Sikkim): India Only Mixed World Heritage Site (2016)", "No"),

    # India's 4 Global Biodiversity Hotspots (4 items)
    ("Geography", "Environment & Ecology", "Global Biodiversity Hotspots in India", "Hotspot Boundaries & Endemism", "Himalaya Hotspot: Entire Indian Himalayan Region & High-Altitude Flora/Fauna", "No"),
    ("Geography", "Environment & Ecology", "Global Biodiversity Hotspots in India", "Hotspot Boundaries & Endemism", "Indo-Burma Hotspot: North-Eastern States (Assam, Meghalaya, Mizoram, Manipur, etc.)", "No"),
    ("Geography", "Environment & Ecology", "Global Biodiversity Hotspots in India", "Hotspot Boundaries & Endemism", "Western Ghats & Sri Lanka Hotspot: Tropical Wet Evergreen Forests & Endemic Species", "No"),
    ("Geography", "Environment & Ecology", "Global Biodiversity Hotspots in India", "Hotspot Boundaries & Endemism", "Sundaland Hotspot: Nicobar Group of Islands Ecosystems & Marine Biodiversity", "No"),

    # India's Biosphere Reserves & UNESCO MAB (6 items)
    ("Geography", "Environment & Ecology", "Biosphere Reserves & UNESCO MAB Programme", "Biosphere Reserve Network", "Nilgiri Biosphere Reserve (1986): India First Biosphere Reserve (TN, KL, KA)", "No"),
    ("Geography", "Environment & Ecology", "Biosphere Reserves & UNESCO MAB Programme", "Biosphere Reserve Network", "Gulf of Mannar (Tamil Nadu) & Great Nicobar: Marine & Coastal Biosphere Reserves", "No"),
    ("Geography", "Environment & Ecology", "Biosphere Reserves & UNESCO MAB Programme", "Biosphere Reserve Network", "Cold Desert (Himachal Pradesh) & Nanda Devi: Himalayan High-Altitude Biospheres", "No"),
    ("Geography", "Environment & Ecology", "Biosphere Reserves & UNESCO MAB Programme", "Biosphere Reserve Network", "Pachmarhi, Achanakmar-Amarkantak & Panna: Central Indian UNESCO MAB Reserves", "No"),
    ("Geography", "Environment & Ecology", "Biosphere Reserves & UNESCO MAB Programme", "Biosphere Reserve Network", "Similipal (Odisha) & Nokrek (Meghalaya): Eastern & North-Eastern MAB Reserves", "No"),
    ("Geography", "Environment & Ecology", "Biosphere Reserves & UNESCO MAB Programme", "Biosphere Reserve Network", "Great Rann of Kutch (Gujarat): India Largest Biosphere Reserve by Geographic Area", "No"),

    # India's Major Ramsar Wetland Sites (6 items)
    ("Geography", "Environment & Ecology", "Ramsar Wetlands of National & International Importance", "Ramsar Sites & Wetland Ecology", "Chilika Lake (Odisha) & Keoladeo Ghana (Rajasthan): India First Ramsar Sites (1981)", "No"),
    ("Geography", "Environment & Ecology", "Ramsar Wetlands of National & International Importance", "Ramsar Sites & Wetland Ecology", "Sundarbans Wetland (WB): Largest Ramsar Site in India & Coastal Mangrove Buffer", "No"),
    ("Geography", "Environment & Ecology", "Ramsar Wetlands of National & International Importance", "Ramsar Sites & Wetland Ecology", "Loktak Lake (Manipur): Montreux Record, Phumdis & Keibul Lamjao Floating Park", "No"),
    ("Geography", "Environment & Ecology", "Ramsar Wetlands of National & International Importance", "Ramsar Sites & Wetland Ecology", "Vembanad-Kol (Kerala - Longest Wetland) & Wular Lake (J&K - Freshwater)", "No"),
    ("Geography", "Environment & Ecology", "Ramsar Wetlands of National & International Importance", "Ramsar Sites & Wetland Ecology", "Sambhar Lake (Rajasthan): Largest Inland Saline Wetland in India", "No"),
    ("Geography", "Environment & Ecology", "Ramsar Wetlands of National & International Importance", "Ramsar Sites & Wetland Ecology", "Tamil Nadu (18 Sites) & Uttar Pradesh (10 Sites): Leading Ramsar States in India", "No"),

    # India's Wildlife Flagship Projects & Tiger Reserves (5 items)
    ("Geography", "Environment & Ecology", "Wildlife Conservation Missions & Tiger Reserves", "National Conservation Projects", "Project Tiger (1973) & NTCA Mandate: 55 Tiger Reserves & Tiger Census Methodology", "No"),
    ("Geography", "Environment & Ecology", "Wildlife Conservation Missions & Tiger Reserves", "National Conservation Projects", "Jim Corbett National Park (Uttarakhand): India First National Park & Tiger Reserve", "No"),
    ("Geography", "Environment & Ecology", "Wildlife Conservation Missions & Tiger Reserves", "National Conservation Projects", "Madhya Pradesh (Tiger State of India): Bandhavgarh, Kanha, Pench, Panna Reserves", "No"),
    ("Geography", "Environment & Ecology", "Wildlife Conservation Missions & Tiger Reserves", "National Conservation Projects", "Project Cheetah (2022): Intercontinental Translocation to Kuno National Park", "No"),
    ("Geography", "Environment & Ecology", "Wildlife Conservation Missions & Tiger Reserves", "National Conservation Projects", "Project Elephant (1992): MIKE Sites, Elephant Corridors & Human-Wildlife Conflict", "No"),

    # India's Major UNESCO Cultural Heritage Monuments (12 items)
    ("History", "Ancient Indian History", "India UNESCO World Cultural Heritage Sites", "Ancient Rock-Cut Caves & Temples", "Ajanta Caves (Maharashtra): 30 Rock-Cut Buddhist Monuments & Jataka Murals", "No"),
    ("History", "Ancient Indian History", "India UNESCO World Cultural Heritage Sites", "Ancient Rock-Cut Caves & Temples", "Ellora Caves (Maharashtra): Kailash Monolithic Rock-Cut Temple (Rashtrakuta Dynasty)", "No"),
    ("History", "Ancient Indian History", "India UNESCO World Cultural Heritage Sites", "Ancient Rock-Cut Caves & Temples", "Elephanta Caves (Maharashtra): Rock-Cut Trimurti Shiva Sculptures", "No"),
    ("History", "Ancient Indian History", "India UNESCO World Cultural Heritage Sites", "Ancient Rock-Cut Caves & Temples", "Group of Monuments at Mahabalipuram (Tamil Nadu): Shore Temple & Pancha Rathas", "No"),
    ("History", "Medieval Indian History", "India UNESCO World Cultural Heritage Sites", "Medieval Temples & Capitals", "Sun Temple at Konark (Odisha): Black Pagoda & Kalinga Architectural Style", "No"),
    ("History", "Medieval Indian History", "India UNESCO World Cultural Heritage Sites", "Medieval Temples & Capitals", "Khajuraho Monuments (Madhya Pradesh): Chandela Dynasty Nagara Temples", "No"),
    ("History", "Medieval Indian History", "India UNESCO World Cultural Heritage Sites", "Medieval Temples & Capitals", "Group of Monuments at Hampi (Karnataka): Vijayanagara Empire Capital & Stone Chariot", "No"),
    ("History", "Medieval Indian History", "India UNESCO World Cultural Heritage Sites", "Medieval Temples & Capitals", "Great Living Chola Temples: Brihadisvara (Thanjavur) & Gangaikonda Cholapuram", "No"),
    ("History", "Medieval Indian History", "India UNESCO World Cultural Heritage Sites", "Sultanate & Mughal Masterpieces", "Qutb Minar Complex (Delhi): Qutbuddin Aibak, Iltutmish & Alai Darwaza", "No"),
    ("History", "Medieval Indian History", "India UNESCO World Cultural Heritage Sites", "Sultanate & Mughal Masterpieces", "Humayun Tomb (Delhi): First Garden-Tomb on Indian Subcontinent (Charbagh)", "No"),
    ("History", "Medieval Indian History", "India UNESCO World Cultural Heritage Sites", "Sultanate & Mughal Masterpieces", "Taj Mahal, Agra Fort & Fatehpur Sikri: Peak of Mughal Architectural Grandeur", "No"),
    ("History", "Modern Indian History", "India UNESCO World Cultural Heritage Sites", "Recent Cultural Inscriptions", "Recent UNESCO Sites: Santiniketan (2023), Hoysala Temples (2023) & Dholavira (2021)", "No"),

    # Classical Languages of India & 2024 Assamese Recognition (2 items)
    ("History", "Art, Culture & Literature", "Classical Languages & Literary Traditions of India", "Classical Languages Framework", "Classical Language Criteria & Initial 6 Languages: Tamil, Sanskrit, Kannada, Telugu, Malayalam, Odia", "No"),
    ("History", "Art, Culture & Literature", "Classical Languages & Literary Traditions of India", "Classical Languages Framework", "Classical Language Recognition (Oct 2024): Assamese, Bengali, Marathi, Pali, Prakrit (11 Total)", "Yes"),

    # Indian Classical Dances (4 items)
    ("History", "Art, Culture & Literature", "Indian Classical Dances & Performing Arts", "Classical Dance Forms of India", "Bharatanatyam (Tamil Nadu) & Kathak (North India): Mudras, Expressions & Gharanas", "No"),
    ("History", "Art, Culture & Literature", "Indian Classical Dances & Performing Arts", "Classical Dance Forms of India", "Kathakali & Mohiniyattam (Kerala): Kathakali Elaborate Makeup & Mohiniyattam Lasya Style", "No"),
    ("History", "Art, Culture & Literature", "Indian Classical Dances & Performing Arts", "Classical Dance Forms of India", "Kuchipudi (Andhra Pradesh) & Odissi (Odisha): Tribhanga Posture & Temple Origins", "No"),
    ("History", "Art, Culture & Literature", "Indian Classical Dances & Performing Arts", "Classical Dance Forms of India", "Manipuri (Raas Leela), Sattriya (Assam Neo-Vaishnavite) & Chhau (Semi-Classical Martial)", "Yes"),
]


# Combine with the 15 new user-confirmed high-yield gap additions
NEW_15_ROWS = [
    # Additional UNESCO Cultural Monuments of India (5 items)
    ("History", "Ancient Indian History", "India UNESCO World Cultural Heritage Sites", "Ancient Rock-Cut Caves & Stupas", "Sanchi Stupa (Madhya Pradesh): Great Stupa, Ashokan Pillars, Toranas & Jataka Reliefs", "No"),
    ("History", "Ancient Indian History", "India UNESCO World Cultural Heritage Sites", "Ancient Rock-Cut Caves & Stupas", "Mahabodhi Temple Complex (Bodh Gaya, Bihar): Site of Buddha Enlightenment, Bodhi Tree & Vajrasana", "No"),
    ("History", "Ancient Indian History", "India UNESCO World Cultural Heritage Sites", "Ancient Monastic Universities", "Nalanda Mahavihara (Bihar): Ancient Monastic University (Kumaragupta I, Xuanzang Records)", "No"),
    ("History", "Medieval Indian History", "India UNESCO World Cultural Heritage Sites", "Medieval Stepwells & Hill Forts", "Rani ki Vav (Patan, Gujarat): Solanki Queen Udayamati Subterranean Stepwell on Saraswati Riverbed", "No"),
    ("History", "Medieval Indian History", "India UNESCO World Cultural Heritage Sites", "Medieval Stepwells & Hill Forts", "Hill Forts of Rajasthan: Chittorgarh, Kumbhalgarh, Ranthambore, Amber, Jaisalmer & Gagron Forts", "No"),

    # UNESCO Intangible Cultural Heritage of Humanity (ICH - India) (5 items)
    ("History", "Art, Culture & Literature", "UNESCO Intangible Cultural Heritage of Humanity (ICH - India)", "UNESCO Representative List of Intangible Heritage", "UNESCO Intangible Cultural Heritage: Representative List Criteria & National Inventory of India", "No"),
    ("History", "Art, Culture & Literature", "UNESCO Intangible Cultural Heritage of Humanity (ICH - India)", "UNESCO Representative List of Intangible Heritage", "Vedic Chanting, Ramlila Performance & Sanskrit Theatre (Kutiyattam): Earliest Inscribed Elements (2008)", "No"),
    ("History", "Art, Culture & Literature", "UNESCO Intangible Cultural Heritage of Humanity (ICH - India)", "UNESCO Representative List of Intangible Heritage", "Ritual & Folk Performing Arts: Mudiyettu (Kerala), Kalbelia Dance (Rajasthan) & Chhau Dance (Eastern India)", "No"),
    ("History", "Art, Culture & Literature", "UNESCO Intangible Cultural Heritage of Humanity (ICH - India)", "UNESCO Representative List of Intangible Heritage", "Religious Gatherings & Celebrations: Kumbh Mela (2017), Durga Puja in Kolkata (2021) & Garba of Gujarat (2023)", "No"),
    ("History", "Art, Culture & Literature", "UNESCO Intangible Cultural Heritage of Humanity (ICH - India)", "UNESCO Representative List of Intangible Heritage", "Himalayan Chanting & Traditional Craft: Buddhist Chanting of Ladakh (2012), Sankirtana (2013) & Brass Utensils of Jandiala Guru (2014)", "No"),

    # Strategic Mountain Passes & Himalayan Border Infrastructure (3 items)
    ("Geography", "Physical & Indian Geography", "Strategic Mountain Passes & Border Infrastructure", "Himalayan Passes & Strategic Tunnels", "Western & Trans-Himalayan Passes: Zoji La (Srinagar-Leh), Banihal Pass, Shipki La & Lipulekh (Tibet Border)", "No"),
    ("Geography", "Physical & Indian Geography", "Strategic Mountain Passes & Border Infrastructure", "Himalayan Passes & Strategic Tunnels", "Eastern Himalayan & North-East Passes: Nathu La (Sikkim-Tibet), Jelep La & Bomdi La (Arunachal Pradesh)", "No"),
    ("Geography", "Physical & Indian Geography", "Strategic Mountain Passes & Border Infrastructure", "Himalayan Passes & Strategic Tunnels", "Strategic High-Altitude Tunnels: Atal Tunnel (Rohtang Pass), Sela Tunnel (Arunachal Pradesh - World Longest Bi-Lane) & Zojila Tunnel", "No"),

    # Major Harvest & Regional Festivals of India (2 items)
    ("History", "Art, Culture & Literature", "Major Harvest & Regional Festivals of India", "Harvest & Seasonal Celebrations", "National Harvest Festivals: Makar Sankranti, Pongal (Tamil Nadu), Onam (Kerala), Baisakhi (Punjab) & Bohag Bihu (Assam)", "No"),
    ("History", "Art, Culture & Literature", "Major Harvest & Regional Festivals of India", "Harvest & Seasonal Celebrations", "North-East Regional & Tribal Festivals: Hornbill Festival (Nagaland), Wangala 100 Drums (Meghalaya), Chapchar Kut (Mizoram) & Losar (Sikkim/Ladakh)", "No"),
]

ALL_ADDITIONAL_ROWS = ADDITIONAL_ROWS + NEW_15_ROWS

# -------------------------------------------------------------------------
# METADATA INFERENCE FOR STUDY_FORMAT & CHRONOLOGY_ERA
# -------------------------------------------------------------------------
def assign_metadata(row):
    domain = row["Domain"]
    subj = row["Subject"]
    topic = row["Topic"]
    subtopic = row["Subtopic"]
    subsub = row["Sub_Subtopic"]
    
    s_format = "Conceptual"
    c_era = "N/A"
    
    # 1. Aptitude & English
    if domain == "Aptitude":
        if "Quantitative Aptitude" in subj or "Geometry" in topic or "Mensuration" in topic:
            s_format = "Formula"
        else:
            s_format = "Conceptual"
        c_era = "N/A"
        return s_format, c_era
        
    if domain == "English":
        if "Grammar" in topic or "Syntax" in topic or "Transformation" in topic:
            s_format = "Formula"
        elif "Vocabulary" in topic:
            s_format = "Listicle"
        else:
            s_format = "Conceptual"
        c_era = "N/A"
        return s_format, c_era

    # 2. Polity
    if domain == "Polity":
        if any(w in subsub.lower() for w in ["mission", "scheme", "orunodoi", "basundhara", "nijut moina", "svayem", "arundhati", "amrit brikshya", "atmanirbhar", "swachh bharat"]):
            s_format = "Case Study/Current Affair"
            c_era = "2020 - 2024"
        elif any(w in subsub.lower() for w in ["article", "amendment", "schedule", "act", "tribunal", "provision", "ordinance", "habeas corpus", "writs", "statutory", "election commission", "finance commission", "cag", "attorney general", "advocate general", "lokpal", "lokayukta", "nhrc", "human rights", "swaran singh"]):
            s_format = "Constitutional/Legal"
            yr = re.search(r'\b(19\d\d|20\d\d)\b', subsub)
            if yr:
                c_era = yr.group(1)
            elif "amendment" in subsub.lower():
                c_era = "Post-1950"
            else:
                c_era = "1950 (Constitution)"
        else:
            s_format = "Conceptual"
            c_era = "1950 (Constitution)"
        return s_format, c_era

    # 3. Economy
    if domain == "Economy":
        if any(w in subsub.lower() for w in ["scheme", "mission", "project", "corridor", "semiconductor", "tatapower", "refinery expansion", "waterways", "pm gati"]):
            s_format = "Case Study/Current Affair"
            c_era = "2020 - 2024"
        elif any(w in subsub.lower() for w in ["act", "code", "ibc", "sarfaesi", "finance commission", "niti aayog"]):
            s_format = "Constitutional/Legal"
            yr = re.search(r'\b(19\d\d|20\d\d)\b', subsub)
            c_era = yr.group(1) if yr else "Contemporary"
        elif any(w in subsub.lower() for w in ["industry", "tea", "oil", "coal", "gi tag", "ranking", "aspirational"]):
            s_format = "Listicle"
            c_era = "Contemporary"
        else:
            s_format = "Conceptual"
            c_era = "N/A"
        return s_format, c_era

    # 4. Geography
    if domain == "Geography":
        if any(w in subsub.lower() for w in ["river", "tributary", "bridge", "border", "pass", "tunnel", "range", "peak", "plateau", "physiograph", "boundary", "soil", "climate zone"]):
            s_format = "Spatial/Map"
            yr = re.search(r'\b(19\d\d|20\d\d)\b', subsub)
            c_era = yr.group(1) if yr else "N/A"
        elif any(w in subsub.lower() for w in ["national park", "wildlife sanctuary", "sanctuaries", "ramsar", "biosphere", "hotspot", "heritage site", "elephant reserve", "tiger reserve", "wetland", "beel", "census", "literacy", "population"]):
            s_format = "Listicle"
            yr = re.search(r'\b(19\d\d|20\d\d)\b', subsub)
            c_era = yr.group(1) if yr else "Contemporary"
        elif any(w in subsub.lower() for w in ["act", "project tiger", "project elephant", "project cheetah"]):
            s_format = "Constitutional/Legal"
            yr = re.search(r'\b(19\d\d|20\d\d)\b', subsub)
            c_era = yr.group(1) if yr else "Contemporary"
        else:
            s_format = "Conceptual"
            c_era = "N/A"
        return s_format, c_era

    # 5. General Awareness & Science
    if domain == "General Awareness & Science":
        if subj == "Current Affairs & Contemporary Issues":
            s_format = "Case Study/Current Affair"
            c_era = "2023 - 2024"
        elif subj == "Static GK":
            s_format = "Listicle"
            yr = re.search(r'\b(19\d\d|20\d\d)\b', subsub)
            c_era = yr.group(1) if yr else "Static / Contemporary"
        elif "Computer" in subj:
            if any(w in subsub.lower() for w in ["shortcut", "extension", "protocol", "port", "generation"]):
                s_format = "Listicle"
            else:
                s_format = "Conceptual"
            c_era = "Contemporary"
        else: # Physics, Chemistry, Biology
            if any(w in subsub.lower() for w in ["vaccine types", "disease", "vitamin", "hormone", "isotope", "ore", "mineral", "periodic table"]):
                s_format = "Listicle"
            elif any(w in subsub.lower() for w in ["law", "formula", "reaction", "fission"]):
                s_format = "Formula"
            else:
                s_format = "Conceptual"
            c_era = "N/A"
        return s_format, c_era

    # 6. History
    if domain == "History":
        if any(w in subsub.lower() for w in ["unesco", "cave", "temple", "moidam", "stupa", "rock-cut", "fort", "jnanpith", "film", "magazine", "dictionary", "dance", "classical language", "festival", "gi tag", "archaeological site", "ruins", "sculpture", "stepwell"]):
            s_format = "Listicle"
        elif any(w in subsub.lower() for w in ["act", "reorganisation", "accord", "treaty", "charter", "code", "cabinet mission", "mountbatten", "ripon", "ilbert"]):
            s_format = "Constitutional/Legal"
        elif any(w in subsub.lower() for w in ["rebellion", "battle", "war", "movement", "uprising", "dynasty", "reign", "conquest", "invasion", "timeline", "expedition", "phase"]):
            s_format = "Chronology"
        else:
            s_format = "Chronology"

        # Chronology Era Assignment
        if "Indus Valley" in topic:
            c_era = "c. 2500 - 1750 BCE"
        elif "Vedic" in topic:
            c_era = "c. 1500 - 600 BCE"
        elif "Buddhism" in topic or "Jainism" in topic or "Mahajanapadas" in topic:
            c_era = "6th - 4th Century BCE"
        elif "Mauryan" in topic:
            c_era = "c. 321 - 185 BCE"
        elif "Gupta" in topic or "Post-Mauryan" in topic:
            c_era = "c. 320 - 550 CE"
        elif "Harsha" in topic or "Pala" in topic:
            c_era = "c. 606 - 1100 CE"
        elif "Ancient Assam" in topic:
            c_era = "c. 350 - 1100 CE"
        elif "Medieval Assam" in topic:
            c_era = "1228 - 1826 CE"
        elif "Delhi Sultanate" in topic:
            c_era = "1206 - 1526 CE"
        elif "Mughal" in topic:
            c_era = "1526 - 1857 CE"
        elif "Bhakti" in topic or "Sufi" in topic or "Neo-Vaishnavite" in topic:
            c_era = "15th - 17th Century CE"
        elif "Early Resistance" in topic or "Peasant" in topic:
            c_era = "1826 - 1894 CE"
        elif "Freedom Movement" in topic or "National Movement" in topic:
            c_era = "1885 - 1947 CE"
        elif "Post-Independence" in topic or "Accord" in topic:
            c_era = "1947 - 2023 CE"
        else:
            yr = re.search(r'\b(19\d\d|20\d\d|18\d\d|17\d\d|16\d\d|15\d\d|14\d\d|13\d\d|12\d\d)\b', subsub)
            if yr:
                c_era = yr.group(1)
            else:
                c_era = "Historical / Ancient to Modern"
                
        return s_format, c_era

    return s_format, c_era


# -------------------------------------------------------------------------
# CANONICAL DOMAIN & SUBJECT ORDERING
# -------------------------------------------------------------------------
DOMAIN_ORDER = [
    "History",
    "Geography",
    "Polity",
    "Economy",
    "Aptitude",
    "English",
    "General Awareness & Science"
]

SUBJECT_ORDER = [
    # History (Strict Chronological Flow)
    "Ancient Indian History",
    "Medieval Indian History",
    "Modern Indian History",
    "Assam History",
    "Art, Culture & Literature",
    # Geography (Spatial & Environmental Progression)
    "Physical & Indian Geography",
    "Assam Geography",
    "Environment & Ecology",
    # Polity (Constitutional & Governance Hierarchy)
    "Indian Polity & Constitution",
    "Assam Governance & Administration",
    # Economy (Macro to Regional)
    "Indian Economy Essentials",
    "Assam Economy Essentials",
    # Aptitude (Quantitative to Reasoning)
    "Quantitative Aptitude (Mathematics)",
    "Logical Reasoning",
    "Verbal Reasoning (Critical Logic)",
    # English
    "General English",
    # Science & Awareness (Core Sciences to Digital/Current)
    "Everyday Science (Physics)",
    "Everyday Science (Chemistry)",
    "Everyday Science (Biology)",
    "Static GK",
    "Current Affairs & Contemporary Issues",
    "Computer Fundamentals & Digital Literacy"
]

def generate():
    raw_rows = []

    # 1. Read base rows from SRC_CSV
    with open(SRC_CSV, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            new_row = {
                "Domain": r.get("Domain", "").strip(),
                "Subject": r.get("Subject", "").strip(),
                "Topic": r.get("Topic", "").strip(),
                "Subtopic": r.get("Subtopic", "").strip(),
                "Sub_Subtopic": r.get("Sub_Subtopic", "").strip(),
                "Assam_Specific": r.get("Assam_Specific", "No").strip(),
                "Checklist": "[ ]"
            }

            # Normalize English Topics
            if new_row["Domain"] == "English":
                if "Grammar" in new_row["Subtopic"]:
                    new_row["Topic"] = "English Grammar & Sentence Structure"
                    new_row["Subtopic"] = "Core Grammar & Syntax Rules"
                elif "Vocabulary" in new_row["Subtopic"]:
                    new_row["Topic"] = "Vocabulary, Idioms & Word Power"
                    new_row["Subtopic"] = "Word Power & Idiomatic Usage"
                elif "Comprehension & Sequencing" in new_row["Subtopic"]:
                    new_row["Topic"] = "Reading Comprehension & Verbal Ability"
                    new_row["Subtopic"] = "Comprehension Passages & Jumbled Sentences"

            # Refine Aptitude Topics
            if new_row["Topic"] == "Mensuration & Data Interpretation":
                if "Data Interpretation" in new_row["Sub_Subtopic"]:
                    new_row["Topic"] = "Data Interpretation (Charts, Tables & Graphs)"
                    new_row["Subtopic"] = "Statistical Charts & Data Sets"
                else:
                    new_row["Topic"] = "Geometry & Mensuration (2D & 3D)"
                    new_row["Subtopic"] = "2D & 3D Geometric Formulas"

            # Normalize Science/Current Affairs Subjects
            if new_row["Domain"] == "General Awareness & Science" and new_row["Subject"] in ["Current Affairs", "Current Awareness & Science"]:
                new_row["Subject"] = "Current Affairs & Contemporary Issues"

            raw_rows.append(new_row)

    # 2. Append all additional high-yield rows (189 rows total)
    for domain, subject, topic, subtopic, sub_subtopic, assam in ALL_ADDITIONAL_ROWS:
        raw_rows.append({
            "Domain": domain,
            "Subject": subject,
            "Topic": topic,
            "Subtopic": subtopic,
            "Sub_Subtopic": sub_subtopic,
            "Assam_Specific": assam,
            "Checklist": "[ ]"
        })

    # 3. Assign Study_Format and Chronology_Era
    enriched_rows = []
    for r in raw_rows:
        s_format, c_era = assign_metadata(r)
        enriched_rows.append({
            "Domain": r["Domain"],
            "Subject": r["Subject"],
            "Topic": r["Topic"],
            "Subtopic": r["Subtopic"],
            "Sub_Subtopic": r["Sub_Subtopic"],
            "Study_Format": s_format,
            "Chronology_Era": c_era,
            "Assam_Specific": r["Assam_Specific"],
            "Checklist": r["Checklist"]
        })

    # 4. Group rows strictly by canonical Domain and Subject order
    grouped_rows = []
    for subj in SUBJECT_ORDER:
        subj_rows = [r for r in enriched_rows if r["Subject"] == subj]
        grouped_rows.extend(subj_rows)

    # Any remaining rows not in SUBJECT_ORDER
    remaining_rows = [r for r in enriched_rows if r["Subject"] not in SUBJECT_ORDER]
    grouped_rows.extend(remaining_rows)

    fieldnames = [
        "Domain",
        "Subject",
        "Topic",
        "Subtopic",
        "Sub_Subtopic",
        "Study_Format",
        "Chronology_Era",
        "Assam_Specific",
        "Checklist"
    ]

    # Write CSV
    with open(OUT_CSV, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for r in grouped_rows:
            writer.writerow(r)

    # Write JSON
    with open(OUT_JSON, mode="w", encoding="utf-8") as f:
        json.dump(grouped_rows, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated:")
    print(f"  CSV:  {OUT_CSV} ({len(grouped_rows)} atomic checklist rows across {len(set(r['Topic'] for r in grouped_rows))} unique topics)")
    print(f"  JSON: {OUT_JSON}")

if __name__ == "__main__":
    generate()
