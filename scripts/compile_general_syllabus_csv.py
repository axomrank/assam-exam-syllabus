#!/usr/bin/env python3
"""
Generate Clutter-Free Checklist Syllabus Dataset for Assam Government Examinations.
Each row represents an ATOMIC CHECKLIST ITEM (Sub_Subtopic) under clean hierarchical headers.

Columns:
- Domain
- Subject
- Topic
- Subtopic
- Sub_Subtopic (Atomic Checklist Item)
- Assam_Specific (Yes / No)
- Applicable_Exams
"""

import os
import csv
import json

BASE_DIR = "/home/angsuman/extra_spac/Study_Assam"

def build_checklist_dataset():
    rows = []

    def add(domain, subject, topic, subtopic, sub_subtopic, assam_specific, applicable_exams="All Assam Exams (APSC CCE, ADRE III & IV, Police SI/Constable, TET, APDCL)"):
        rows.append({
            "Domain": domain,
            "Subject": subject,
            "Topic": topic,
            "Subtopic": subtopic,
            "Sub_Subtopic": sub_subtopic,
            "Assam_Specific": assam_specific,
            "Applicable_Exams": applicable_exams
        })

    # =========================================================================
    # 1. HISTORY
    # =========================================================================
    # 1.1 Ancient Indian History
    t = "Indus Valley Civilization"
    s = "Town Planning & Architecture"
    add("History", "Ancient Indian History", t, s, "Grid Pattern & Urban Layout", "No")
    add("History", "Ancient Indian History", t, s, "Covered Drainage & Sanitation System", "No")
    add("History", "Ancient Indian History", t, s, "Great Bath of Mohenjodaro", "No")
    add("History", "Ancient Indian History", t, s, "Great Granary & Storage Architecture", "No")
    add("History", "Ancient Indian History", t, s, "Burnt Brick Standardization", "No")

    s = "Major Harappan Sites"
    add("History", "Ancient Indian History", t, s, "Harappa (Citadel & Granaries)", "No")
    add("History", "Ancient Indian History", t, s, "Mohenjodaro (Dancing Girl & Pashupati Seal)", "No")
    add("History", "Ancient Indian History", t, s, "Lothal (Tidal Dockyard & Commercial Seals)", "No")
    add("History", "Ancient Indian History", t, s, "Dholavira (Water Reservoirs & Giant Signboard)", "No")
    add("History", "Ancient Indian History", t, s, "Kalibangan (Ploughed Field & Fire Altars)", "No")
    add("History", "Ancient Indian History", t, s, "Rakhigarhi & Chanhudaro (Craft Production)", "No")

    s = "Economy, Religion & Decline"
    add("History", "Ancient Indian History", t, s, "Bronze Metallurgy & Lost-Wax Casting", "No")
    add("History", "Ancient Indian History", t, s, "Mesopotamian Trade Links (Meluhha)", "No")
    add("History", "Ancient Indian History", t, s, "Steatite Seals, Script & Terracotta Figurines", "No")
    add("History", "Ancient Indian History", t, s, "Theories of Harappan Decline (Floods, Climate)", "No")

    t = "Vedic Period & Literature"
    s = "Early Vedic (Rigvedic) Era"
    add("History", "Ancient Indian History", t, s, "Sapta Sindhu Geography & Tribal Settlement", "No")
    add("History", "Ancient Indian History", t, s, "Early Vedic Tribal Polity (Rajan, Sabha, Samiti)", "No")
    add("History", "Ancient Indian History", t, s, "Pastoral Economy & Cattle Warfare (Gavishti)", "No")
    add("History", "Ancient Indian History", t, s, "Rigvedic Deities (Indra, Agni, Varuna, Soma)", "No")

    s = "Later Vedic Transformations"
    add("History", "Ancient Indian History", t, s, "Sedentary Agriculture & Iron Tools (Ayas)", "No")
    add("History", "Ancient Indian History", t, s, "Evolution of Four Varnas & Ashramas", "No")
    add("History", "Ancient Indian History", t, s, "Sacrificial Rituals (Ashvamedha, Rajasuya)", "No")
    add("History", "Ancient Indian History", t, s, "Vedic Literature: Samaveda, Yajurveda, Atharvaveda", "No")
    add("History", "Ancient Indian History", t, s, "Upanishads & Philosophical Concepts (Atman, Brahman)", "No")

    t = "Buddhism & Jainism"
    s = "Buddhism Core Philosophy"
    add("History", "Ancient Indian History", t, s, "Gautama Buddha Life & Enlightenment (Bodh Gaya)", "No")
    add("History", "Ancient Indian History", t, s, "Four Noble Truths (Chatvari Arya Satyani)", "No")
    add("History", "Ancient Indian History", t, s, "Noble Eightfold Path (Ashtangika Marga)", "No")
    add("History", "Ancient Indian History", t, s, "Doctrine of Dependent Origination (Pratityasamutpada)", "No")

    s = "Buddhist Councils & Literature"
    add("History", "Ancient Indian History", t, s, "First Buddhist Council (Rajgriha - 483 BC)", "No")
    add("History", "Ancient Indian History", t, s, "Second Buddhist Council (Vaishali - 383 BC)", "No")
    add("History", "Ancient Indian History", t, s, "Third Buddhist Council (Pataliputra - Ashoka)", "No")
    add("History", "Ancient Indian History", t, s, "Fourth Buddhist Council (Kundalvana - Kanishka)", "No")
    add("History", "Ancient Indian History", t, s, "Sects: Hinayana (Theravada) vs Mahayana", "No")
    add("History", "Ancient Indian History", t, s, "Tripitakas (Vinaya, Sutta, Abhidhamma Pitaka)", "No")

    s = "Jainism & Teachings"
    add("History", "Ancient Indian History", t, s, "Vardhamana Mahavira & 24 Tirthankaras", "No")
    add("History", "Ancient Indian History", t, s, "Three Jewels of Jainism (Triratna)", "No")
    add("History", "Ancient Indian History", t, s, "Five Great Vows (Pancha Mahavratas & Ahimsa)", "No")
    add("History", "Ancient Indian History", t, s, "Jain Doctrines: Anekantavada & Syadvada", "No")
    add("History", "Ancient Indian History", t, s, "Jain Schism: Digambara vs Svetambara", "No")

    t = "Mahajanapadas & Mauryan Empire"
    s = "Rise of Magadha"
    add("History", "Ancient Indian History", t, s, "16 Mahajanapadas Overview (Anga to Gandhara)", "No")
    add("History", "Ancient Indian History", t, s, "Haryanka Dynasty (Bimbisara & Ajatashatru)", "No")
    add("History", "Ancient Indian History", t, s, "Shishunaga & Nanda Dynasties of Magadha", "No")
    add("History", "Ancient Indian History", t, s, "Alexander's Invasion of Northwest India (326 BC)", "No")

    s = "Mauryan Administration & Ashoka"
    add("History", "Ancient Indian History", t, s, "Chandragupta Maurya & Seleucid War", "No")
    add("History", "Ancient Indian History", t, s, "Kautilya's Arthashastra & Saptanga Theory", "No")
    add("History", "Ancient Indian History", t, s, "Megasthenes' Account in 'Indica'", "No")
    add("History", "Ancient Indian History", t, s, "Kalinga War (261 BC) & Ashoka's Dharmavijaya", "No")
    add("History", "Ancient Indian History", t, s, "Policy of Dhamma & Dhamma Mahamattas", "No")
    add("History", "Ancient Indian History", t, s, "Ashokan Inscriptions: Major Rock & Pillar Edicts", "No")
    add("History", "Ancient Indian History", t, s, "Sarnath Lion Capital (National Emblem of India)", "No")
    add("History", "Ancient Indian History", t, s, "Mauryan Bureaucracy, Taxation & Decline", "No")

    t = "Gupta Empire & South Indian Kingdoms"
    s = "Gupta Golden Age"
    add("History", "Ancient Indian History", t, s, "Chandragupta I & Gupta Era (319-320 AD)", "No")
    add("History", "Ancient Indian History", t, s, "Samudragupta & Allahabad Pillar Inscription", "No")
    add("History", "Ancient Indian History", t, s, "Chandragupta II Vikramaditya & Navratnas", "No")
    add("History", "Ancient Indian History", t, s, "Kalidasa's Literature (Abhijnanasakuntalam, Meghaduta)", "No")
    add("History", "Ancient Indian History", t, s, "Aryabhata (Aryabhatiya, Solar Eclipse, Zero)", "No")
    add("History", "Ancient Indian History", t, s, "Nalanda Mahavihara University (Kumaragupta I)", "No")
    add("History", "Ancient Indian History", t, s, "Harshavardhana of Kannauj & Banabhatta", "No")
    add("History", "Ancient Indian History", t, s, "Xuanzang (Hiuen Tsang) Travelogue Across India", "No")

    s = "South Indian Dynasties"
    add("History", "Ancient Indian History", t, s, "Chola Empire: Rajaraja I & Rajendra I", "No")
    add("History", "Ancient Indian History", t, s, "Chola Village Autonomy & Uttaramerur Inscription", "No")
    add("History", "Ancient Indian History", t, s, "Brihadisvara Temple Tanjore Architecture", "No")
    add("History", "Ancient Indian History", t, s, "Pallava Monolithic Rathas at Mahabalipuram", "No")
    add("History", "Ancient Indian History", t, s, "Kailash Rock-Cut Temple at Ellora (Rashtrakutas)", "No")

    # 1.2 Medieval Indian History
    t = "Delhi Sultanate (1206-1526)"
    s = "Sultanate Dynasties & Administration"
    add("History", "Medieval Indian History", t, s, "Qutb-ud-din Aibak & Qutub Minar Construction", "No")
    add("History", "Medieval Indian History", t, s, "Iltutmish & Turkan-i-Chahalgani (Group of 40)", "No")
    add("History", "Medieval Indian History", t, s, "Razia Sultana: First Woman Monarch of Delhi", "No")
    add("History", "Medieval Indian History", t, s, "Ghiyas-ud-din Balban: Blood & Iron Policy, Sijda", "No")
    add("History", "Medieval Indian History", t, s, "Alauddin Khilji: Market Price Control System", "No")
    add("History", "Medieval Indian History", t, s, "Alauddin Khilji: Dagh (Branding) & Chehra (Roll)", "No")
    add("History", "Medieval Indian History", t, s, "Malik Kafur's Southern Military Campaigns", "No")
    add("History", "Medieval Indian History", t, s, "Muhammad bin Tughlaq: Token Currency Experiment", "No")
    add("History", "Medieval Indian History", t, s, "Muhammad bin Tughlaq: Capital Shift to Daulatabad", "No")
    add("History", "Medieval Indian History", t, s, "Firoz Shah Tughlaq: Canals, Hospitals & Works", "No")
    add("History", "Medieval Indian History", t, s, "Ibrahim Lodi & First Battle of Panipat (1526)", "No")

    t = "Vijayanagara & Bahmani Empires"
    s = "South Medieval Empires"
    add("History", "Medieval Indian History", t, s, "Foundation of Vijayanagara by Harihara & Bukka (1336)", "No")
    add("History", "Medieval Indian History", t, s, "Reign of Krishnadevaraya (Tuluva Dynasty)", "No")
    add("History", "Medieval Indian History", t, s, "Krishnadevaraya's Amuktamalyada & Ashtadiggajas", "No")
    add("History", "Medieval Indian History", t, s, "Battle of Talikota (1565) & Decline of Vijayanagara", "No")
    add("History", "Medieval Indian History", t, s, "Hampi Monuments & Vitthala Stone Chariot Temple", "No")
    add("History", "Medieval Indian History", t, s, "Bahmani Sultanate (Alauddin Hasan) & Mahmud Gawan", "No")

    t = "Mughal Empire & Sur Dynasty"
    s = "Babur, Humayun & Sher Shah"
    add("History", "Medieval Indian History", t, s, "Babur: Panipat (1526), Khanwa (1527) & Tuzuk-i-Baburi", "No")
    add("History", "Medieval Indian History", t, s, "Humayun's Exile & Sher Shah Suri's Ascension", "No")
    add("History", "Medieval Indian History", t, s, "Sher Shah Suri: Grand Trunk Road & Rupiya Coin", "No")
    add("History", "Medieval Indian History", t, s, "Sher Shah Suri: Land Revenue & Postal Reforms", "No")

    s = "Akbar the Great"
    add("History", "Medieval Indian History", t, s, "Second Battle of Panipat (1556) vs Hemu", "No")
    add("History", "Medieval Indian History", t, s, "Mansabdari & Jagirdari Administrative System", "No")
    add("History", "Medieval Indian History", t, s, "Todar Mal's Bandobast / Dahsala Revenue System", "No")
    add("History", "Medieval Indian History", t, s, "Akbar's Religious Policy: Din-i-Ilahi & Sulh-i-Kul", "No")
    add("History", "Medieval Indian History", t, s, "Ibadat Khana Debates & Abolition of Jizya", "No")
    add("History", "Medieval Indian History", t, s, "Akbar's Navratnas (Birbal, Tansen, Abul Fazl)", "No")

    s = "Later Mughals & Marathas"
    add("History", "Medieval Indian History", t, s, "Jahangir: Chain of Justice & Miniature Painting", "No")
    add("History", "Medieval Indian History", t, s, "Shah Jahan: Taj Mahal & Golden Age of Architecture", "No")
    add("History", "Medieval Indian History", t, s, "Aurangzeb: Deccan Wars, Reimposition of Jizya", "No")
    add("History", "Medieval Indian History", t, s, "Chhatrapati Shivaji Maharaj: Guerrilla Warfare (Ganimi Kava)", "No")
    add("History", "Medieval Indian History", t, s, "Treaty of Purandar (1665) & Shivaji's Coronation (1674)", "No")
    add("History", "Medieval Indian History", t, s, "Shivaji's Ashta Pradhan Council & Chauth/Sardeshmukhi", "No")
    add("History", "Medieval Indian History", t, s, "Peshwas: Baji Rao I & Third Battle of Panipat (1761)", "No")
    add("History", "Medieval Indian History", t, s, "Bhakti Saints: Kabir, Guru Nanak Dev, Mirabai", "No")
    add("History", "Medieval Indian History", t, s, "Sufi Orders: Chishti (Moinuddin Chishti) & Suhrawardi", "No")

    # 1.3 Modern Indian History & National Movement
    t = "British Conquest of India"
    s = "Colonial Battles & Policies"
    add("History", "Modern Indian History", t, s, "Advent of European Trading Companies in India", "No")
    add("History", "Modern Indian History", t, s, "Battle of Plassey (1757): Clive & Siraj-ud-Daulah", "No")
    add("History", "Modern Indian History", t, s, "Battle of Buxar (1764) & Treaty of Allahabad (1765)", "No")
    add("History", "Modern Indian History", t, s, "Robert Clive's Dual Government in Bengal", "No")
    add("History", "Modern Indian History", t, s, "Regulating Act 1773 & Pitt's India Act 1784", "No")
    add("History", "Modern Indian History", t, s, "Lord Wellesley's Subsidiary Alliance System", "No")
    add("History", "Modern Indian History", t, s, "Lord Dalhousie's Doctrine of Lapse (Satara, Jhansi)", "No")
    add("History", "Modern Indian History", t, s, "Permanent Settlement / Zamindari System (Cornwallis 1793)", "No")
    add("History", "Modern Indian History", t, s, "Ryotwari System (Munro) & Mahalwari System (Mackenzie)", "No")
    add("History", "Modern Indian History", t, s, "Dadabhai Naoroji's Drain of Wealth Theory", "No")

    t = "Revolt of 1857 & Social Reforms"
    s = "1857 Mutiny & Proclamation"
    add("History", "Modern Indian History", t, s, "Revolt of 1857: Enfield Greased Cartridge Trigger", "No")
    add("History", "Modern Indian History", t, s, "Mangal Pandey Execution at Barrackpore", "No")
    add("History", "Modern Indian History", t, s, "Revolt Leaders: Rani Lakshmibai, Tantia Tope, Nana Saheb", "No")
    add("History", "Modern Indian History", t, s, "Government of India Act 1858: End of Company Rule", "No")
    add("History", "Modern Indian History", t, s, "Queen Victoria's 1858 Proclamation & Viceroy Role", "No")

    s = "19th Century Reform Movements"
    add("History", "Modern Indian History", t, s, "Raja Ram Mohan Roy: Brahmo Samaj & Abolition of Sati (1829)", "No")
    add("History", "Modern Indian History", t, s, "Ishwar Chandra Vidyasagar: Widow Remarriage Act (1856)", "No")
    add("History", "Modern Indian History", t, s, "Swami Dayananda: Arya Samaj & 'Go Back to Vedas'", "No")
    add("History", "Modern Indian History", t, s, "Swami Vivekananda: Ramakrishna Mission & Chicago 1893", "No")
    add("History", "Modern Indian History", t, s, "Jyotirao Phule: Satyashodhak Samaj & Gulamgiri", "No")
    add("History", "Modern Indian History", t, s, "Sir Syed Ahmad Khan: Aligarh Movement & Scientific Society", "No")

    t = "Indian National Movement (1885-1947)"
    s = "Early INC & Extremist Phase"
    add("History", "Modern Indian History", t, s, "Founding of Indian National Congress (1885 - AO Hume)", "No")
    add("History", "Modern Indian History", t, s, "First INC Session Bombay (WC Bonnerjee)", "No")
    add("History", "Modern Indian History", t, s, "Moderate Agitation: Naoroji, Pherozeshah Mehta, Gokhale", "No")
    add("History", "Modern Indian History", t, s, "Partition of Bengal (1905) by Lord Curzon", "No")
    add("History", "Modern Indian History", t, s, "Swadeshi & Boycott Movement (Lal-Bal-Pal)", "No")
    add("History", "Modern Indian History", t, s, "Bal Gangadhar Tilak: 'Swaraj is My Birthright'", "No")
    add("History", "Modern Indian History", t, s, "Surat Split of INC (1907)", "No")
    add("History", "Modern Indian History", t, s, "Morley-Minto Reforms (1909: Separate Electorates)", "No")
    add("History", "Modern Indian History", t, s, "Home Rule League Movement (1916: Tilak & Besant)", "No")
    add("History", "Modern Indian History", t, s, "Lucknow Pact (1916): INC-Muslim League Accord", "No")

    s = "Gandhian Mass Movements"
    add("History", "Modern Indian History", t, s, "Champaran Satyagraha (1917: Indigo Tinkathia)", "No")
    add("History", "Modern Indian History", t, s, "Ahmedabad Mill Strike (1918) & Kheda Satyagraha (1918)", "No")
    add("History", "Modern Indian History", t, s, "Rowlatt Act (1919) & Rowlatt Satyagraha", "No")
    add("History", "Modern Indian History", t, s, "Jallianwala Bagh Massacre (13 April 1919, Dyer)", "No")
    add("History", "Modern Indian History", t, s, "Montagu-Chelmsford Reforms / GoI Act 1919 (Dyarchy)", "No")
    add("History", "Modern Indian History", t, s, "Non-Cooperation Movement (1920-22) & Khilafat Movement", "No")
    add("History", "Modern Indian History", t, s, "Chauri Chaura Incident (1922) & Movement Withdrawal", "No")
    add("History", "Modern Indian History", t, s, "Swaraj Party (1923: CR Das & Motilal Nehru)", "No")
    add("History", "Modern Indian History", t, s, "Revolutionary Action: Bhagat Singh, Azad, Kakori, Saunders", "No")
    add("History", "Modern Indian History", t, s, "Simon Commission (1927) & Lala Lajpat Rai Martyrdom", "No")
    add("History", "Modern Indian History", t, s, "Lahore Congress (1929: Purna Swaraj Declaration)", "No")
    add("History", "Modern Indian History", t, s, "Dandi Salt March & Civil Disobedience Movement (1930)", "No")
    add("History", "Modern Indian History", t, s, "Gandhi-Irwin Pact (1931) & Round Table Conferences", "No")
    add("History", "Modern Indian History", t, s, "Poona Pact (1932: Gandhi & Dr. BR Ambedkar)", "No")
    add("History", "Modern Indian History", t, s, "Government of India Act 1935 (Provincial Autonomy)", "No")
    add("History", "Modern Indian History", t, s, "Quit India Movement (August 1942: 'Do or Die')", "No")
    add("History", "Modern Indian History", t, s, "Subhas Chandra Bose & Indian National Army (INA)", "No")
    add("History", "Modern Indian History", t, s, "Cabinet Mission Plan (1946) & Interim Government", "No")
    add("History", "Modern Indian History", t, s, "Mountbatten Plan & Indian Independence Act 1947", "No")
    add("History", "Modern Indian History", t, s, "Integration of Princely States (Sardar Patel & VP Menon)", "No")

    # 1.4 Assam History (Compulsory State Core)
    t = "Ancient Assam (Pragjyotisha & Kamarupa)"
    s = "Inscriptions & Early Rulers"
    add("History", "Assam History", t, s, "Mythological Kings: Naraka, Bhagadatta & Banasura", "Yes")
    add("History", "Assam History", t, s, "Nidhanpur & Doobi Copperplate Inscriptions", "Yes")
    add("History", "Assam History", t, s, "Allahabad Pillar Mention of Kamarupa & Davaka", "Yes")
    add("History", "Assam History", t, s, "Tezpur Rock Inscription of Harjaravarman", "Yes")
    add("History", "Assam History", t, s, "Varman Dynasty: Pushyavarman (Founder)", "Yes")
    add("History", "Assam History", t, s, "Kumar Bhaskaravarman's Diplomatic Alliance with Harsha", "Yes")
    add("History", "Assam History", t, s, "Xuanzang's Account of King Bhaskaravarman & Kamarupa", "Yes")
    add("History", "Assam History", t, s, "Salastambha Dynasty (Mlechha Rulers)", "Yes")
    add("History", "Assam History", t, s, "Pala Dynasty of Kamarupa: Brahmapala & Dharmapala", "Yes")
    add("History", "Assam History", t, s, "Ancient Kamarupa Saivism, Saktism & Rock Architecture", "Yes")

    t = "Medieval Assam: Ahoms & Regional Kingdoms"
    s = "Foundation of Ahom Rule"
    add("History", "Assam History", t, s, "Chaolung Sukapha Migration across Patkai (1228 AD)", "Yes")
    add("History", "Assam History", t, s, "Establishment of First Ahom Capital at Charaideo", "Yes")
    add("History", "Assam History", t, s, "Early Ahom Tribal Assimilation (Morans & Borahis)", "Yes")
    add("History", "Assam History", t, s, "Suhungmung (Dihingia Raja): Inclusion of Chutiya Kingdom", "Yes")
    add("History", "Assam History", t, s, "Suhungmung: Defeat of Turbak & Introduction of Saka Era", "Yes")
    add("History", "Assam History", t, s, "First State Census under Suhungmung", "Yes")

    s = "Chutiya, Kachari & Koch Dynasties"
    add("History", "Assam History", t, s, "Chutiya Kingdom: King Gaurinarayan & Sati Sadhani", "Yes")
    add("History", "Assam History", t, s, "Kachari Kingdom: Dimapur Ruins, Maibang & Khaspur", "Yes")
    add("History", "Assam History", t, s, "Establishment of Koch Kingdom by Biswa Singha", "Yes")
    add("History", "Assam History", t, s, "Golden Era of King Naranarayan & General Chilarai", "Yes")
    add("History", "Assam History", t, s, "Chilarai's Military Campaigns across Assam & Bengal", "Yes")
    add("History", "Assam History", t, s, "Reconstruction of Kamakhya Temple by Koches (1565 AD)", "Yes")
    add("History", "Assam History", t, s, "Division of Koch Kingdom into Koch Hajo & Koch Behar", "Yes")

    s = "Ahom Administration & Reforms"
    add("History", "Assam History", t, s, "Momai Tamuli Barbarua's Village Organization", "Yes")
    add("History", "Assam History", t, s, "Paik System: Got Unit (4 paiks reduced to 3 paiks)", "Yes")
    add("History", "Assam History", t, s, "Paik Hierarchy: Mula Paik, Chamua, Likchou", "Yes")
    add("History", "Assam History", t, s, "Khel Administrative System in Ahom State", "Yes")
    add("History", "Assam History", t, s, "Posha System of Tribute with Frontier Hill Tribes", "Yes")
    add("History", "Assam History", t, s, "Ahom Council of Ministers: Patra Mantris & Barbarua/Borphukan", "Yes")
    add("History", "Assam History", t, s, "Buranjis: Official Court Chronicles of Ahom Rule", "Yes")

    s = "Mughal Wars & Saraighat"
    add("History", "Assam History", t, s, "Mir Jumla's Invasion of Assam (1662-63 AD)", "Yes")
    add("History", "Assam History", t, s, "Treaty of Ghilajharighat & Ramani Gabharu's Exile", "Yes")
    add("History", "Assam History", t, s, "King Chakradhwaj Singha's Preparations for War", "Yes")
    add("History", "Assam History", t, s, "Battle of Alaboi (1669 AD) & Sacrifice of Assamese Troops", "Yes")
    add("History", "Assam History", t, s, "Lachit Borphukan's Appointment as Commander-in-Chief", "Yes")
    add("History", "Assam History", t, s, "Battle of Saraighat (1671 AD): Naval Tactics on Brahmaputra", "Yes")
    add("History", "Assam History", t, s, "Ismail Siddiqui (Bagh Hazarika) in Saraighat Defense", "Yes")
    add("History", "Assam History", t, s, "Raja Ram Singh I Defeat & Withdrawal of Mughal Army", "Yes")
    add("History", "Assam History", t, s, "Battle of Itakhuli (1682 AD): Final Expulsion of Mughals", "Yes")
    add("History", "Assam History", t, s, "Western Boundary Fixed at Manas River", "Yes")

    s = "Late Ahoms & Decline"
    add("History", "Assam History", t, s, "Gadadhar Singha & Foundation of Tungkhungia Dynasty", "Yes")
    add("History", "Assam History", t, s, "Rudra Singha: Construction of Rang Ghar & Kareng Ghar", "Yes")
    add("History", "Assam History", t, s, "Siva Singha, Queen Phuleswari & Saktism Dominance", "Yes")
    add("History", "Assam History", t, s, "Sati Joymoti Konwari's Martyrdom at Jerenga Pathar", "Yes")
    add("History", "Assam History", t, s, "Moamoria Rebellion: Mayamara Satra & Socio-Religious Causes", "Yes")
    add("History", "Assam History", t, s, "Three Phases of Moamoria Uprising & Naharkhora/Ragha Moran", "Yes")
    add("History", "Assam History", t, s, "Prime Minister Purnananda Burhagohain's Counter-Offensive", "Yes")
    add("History", "Assam History", t, s, "Captain Welsh's British Expedition to Assam (1792-94)", "Yes")
    add("History", "Assam History", t, s, "Burmese Invasions of Assam (Maanar Din: 1817, 1819, 1821)", "Yes")
    add("History", "Assam History", t, s, "Badan Chandra Borphukan's Treachery & Burmese Alliance", "Yes")
    add("History", "Assam History", t, s, "Atrocities during Burmese Occupation (1821-1824)", "Yes")
    add("History", "Assam History", t, s, "First Anglo-Burmese War (1824-1826) in Assam", "Yes")
    add("History", "Assam History", t, s, "Treaty of Yandaboo (24th February 1826: End of Ahom Sovereignty)", "Yes")

    t = "Modern Assam & Freedom Struggle"
    s = "Early British Resistance"
    add("History", "Assam History", t, s, "David Scott's Administration as Agent to Governor-General", "Yes")
    add("History", "Assam History", t, s, "Deposition of King Purandar Singha (1838)", "Yes")
    add("History", "Assam History", t, s, "Gomdhar Konwar's Anti-British Rebellion (1828)", "Yes")
    add("History", "Assam History", t, s, "Piyoli Phukan & Jeuram Dulia Barua's Martyrdom (1830)", "Yes")
    add("History", "Assam History", t, s, "U Tirot Sing's Khasi War of Independence (1829-1833)", "Yes")
    add("History", "Assam History", t, s, "Revolt of 1857 in Assam: Maniram Dewan's Leadership", "Yes")
    add("History", "Assam History", t, s, "Piyoli Baruah & Kandarpeswar Singha's Conspiracy", "Yes")
    add("History", "Assam History", t, s, "Execution of Maniram Dewan & Piyoli Baruah at Jorhat (1858)", "Yes")

    s = "Peasant Uprisings (Raijmels)"
    add("History", "Assam History", t, s, "Phulaguri Dawa (1861): Assam's First Peasant Uprising", "Yes")
    add("History", "Assam History", t, s, "Death of British Officer Lt. Singer at Phulaguri", "Yes")
    add("History", "Assam History", t, s, "Rangia & Lachima Peasant Revolts (1894)", "Yes")
    add("History", "Assam History", t, s, "Patharughat Battle / Patharughator Ran (28 Jan 1894)", "Yes")
    add("History", "Assam History", t, s, "Martyrdom of 140 Unarmed Peasants at Patharughat (Darrang)", "Yes")

    s = "National Movement in Assam"
    add("History", "Assam History", t, s, "Jorhat Sarbajanik Sabha (1884, Jagannath Baruah)", "Yes")
    add("History", "Assam History", t, s, "Assam Association (1903, Manik Chandra Baruah)", "Yes")
    add("History", "Assam History", t, s, "Asom Chatra Sanmilan (1916, Lakshminath Bezbaroa)", "Yes")
    add("History", "Assam History", t, s, "Assam Provincial Congress Committee (APCC 1921)", "Yes")
    add("History", "Assam History", t, s, "Mahatma Gandhi's First Historic Tour of Assam (Aug 1921)", "Yes")
    add("History", "Assam History", t, s, "Non-Cooperation Movement in Assam: Opium Picketing", "Yes")
    add("History", "Assam History", t, s, "Chargola Tea Garden Laborers Exodus (1921)", "Yes")
    add("History", "Assam History", t, s, "Assam-Bengal Railway Strike Led by JM Sengupta", "Yes")
    add("History", "Assam History", t, s, "Civil Disobedience: Cunningham Circular Student Boycott (1930)", "Yes")
    add("History", "Assam History", t, s, "Quit India Movement (1942): Gohpur Police Station March", "Yes")
    add("History", "Assam History", t, s, "Martyrdom of 14-Year-Old Kanaklata Barua (1942)", "Yes")
    add("History", "Assam History", t, s, "Martyr Mukunda Kakati at Gohpur Police Station (1942)", "Yes")
    add("History", "Assam History", t, s, "Kushal Konwar: Only Indian Executed by Hanging in 1942 Movement", "Yes")
    add("History", "Assam History", t, s, "Bhogeswari Phukanani Martyrdom at Barhampur (Nagaon 1942)", "Yes")
    add("History", "Assam History", t, s, "Cabinet Mission Plan (1946) & Grouping Scheme (Section C)", "Yes")
    add("History", "Assam History", t, s, "Lokpriya Gopinath Bordoloi's Campaign to Save Assam from Pakistan", "Yes")
    add("History", "Assam History", t, s, "Sylhet Referendum (July 1947) & Transfer to East Pakistan", "Yes")
    add("History", "Assam History", t, s, "Retention of Karimganj Subdivision in Assam", "Yes")
    add("History", "Assam History", t, s, "Lokpriya Gopinath Bordoloi: First CM & Bharat Ratna (1999)", "Yes")

    t = "Post-Independence Assam History"
    s = "Reorganization & Accords"
    add("History", "Assam History", t, s, "Separation of Nagaland (1963) from Assam", "Yes")
    add("History", "Assam History", t, s, "Creation of Meghalaya (1972) & Mizoram (1972/1987)", "Yes")
    add("History", "Assam History", t, s, "Assam Movement (1979-1985) by AASU & AAGSP", "Yes")
    add("History", "Assam History", t, s, "Assam Accord (15 August 1985): Clause 5 Cut-off Dates", "Yes")
    add("History", "Assam History", t, s, "Assam Accord Clause 6: Cultural & Linguistic Safeguards", "Yes")
    add("History", "Assam History", t, s, "Bodoland Territorial Council (BTC 2003) & BTR Accord (2020)", "Yes")

    # 1.5 Art, Culture & Literature of Assam
    t = "Sankardeva & Neo-Vaishnavite Culture"
    s = "Ekasarana Dharma & Satras"
    add("History", "Art, Culture & Literature", t, s, "Srimanta Sankardeva (1449-1568 AD, Batadrava) Life", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Madhavdeva: Chief Disciple & Author of Naam Ghosha", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Ekasarana Dharma: Four Pillars (Nama, Deva, Guru, Bhakta)", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Satra Institution: Majuli Kamalabari Satra", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Majuli Satras: Auniati, Dakhinpat & Garmur Satra", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Barpeta Satra & Batadrava Than Heritage", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Namghar: Community Religious, Social & Judicial Institution", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Manikut & Guru Asana Architecture of Namghar", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Borgeet: Classical Devotional Songs of Assam", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Ankiya Nat Plays: Chinhayatra, Rukmini Harana, Parijat Harana", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Bhaona: Traditional Mythological Theater & Mask Art (Mukha)", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Khol, Bor-Taal & Tokari Musical Instruments", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Sattriya Classical Dance: 8th Classical Dance of India (2000)", "Yes")

    t = "Festivals, Folk Dances & Textiles of Assam"
    s = "Three Bihus of Assam"
    add("History", "Art, Culture & Literature", t, s, "Rongali / Bohag Bihu (Assamese New Year & Spring)", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Rongali Bihu Seven Days (Goru, Manuh, Gosai, Kutum, Senehi)", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Bihu Husori Groups & Traditional Bihu Dance", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Bhogali / Magh Bihu: Harvest Festival & Uruka Feast", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Meji & Bhelaghar Bonfire Architecture on Magh Bihu", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Traditional Assamese Pitha: Til Pitha, Ghila Pitha, Sunga Pitha", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Kongali / Kati Bihu: Saki at Tulsi Than & Akash Banti", "Yes")

    s = "Tribal Festivals & Attires"
    add("History", "Art, Culture & Literature", t, s, "Bodo Culture: Baishagu Festival & Kherai Dance", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Bodo Bathou Religion & Sijou Tree Worship", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Bodo Attires: Dokhona & Traditional Aronai", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Mising Festival: Ali-Aye-Ligang (Spring Sowing)", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Mising Gumrag Dance & Traditional Mirjem / Dumer Attires", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Karbi Festivals: Rongker & Chomangkan Death Ritual", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Tiwa Culture: Jonbeel Mela Barter System in Morigaon", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Rabha Baikho Festival & Dimasa Rajini Gabra Festival", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Traditional Instruments: Dhol, Pepa (Buffalo Horn), Gogona, Toka", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Assamese Traditional Silk: Muga (Golden Silk), Eri & Pat", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Assam Gamosa: GI Tagged Cultural Symbol", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Assam Japi (Conical Headgear) & Xorai (Bell Metal Offerings)", "Yes")

    t = "Assamese Literature & Cultural Icons"
    s = "Literature Eras & Icons"
    add("History", "Art, Culture & Literature", t, s, "Charyapada: Earliest Specimen of Proto-Assamese Language", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Madhava Kandali: Saptakanda Ramayana in Assamese Verse", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Bhattadeva: Katha Gita (Pioneer of Early Assamese Prose)", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Nathan Brown & Miles Bronson (First Assamese Dictionary 1867)", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Orunodoi (1846): First Assamese Newspaper / Periodical", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Hemchandra Baruah: Hemkosh Etymological Dictionary (1900)", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Jonaki Magazine (1889): Dawn of Romantic Assamese Era", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Trimurti of Jonaki: Chandrakumar, Bezbaroa, Hemchandra", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Lakshminath Bezbaroa: Burhi Aair Sadhu & Roxoraj", "Yes")
    add("History", "Art, Culture & Literature", t, s, "'O Mur Apunar Dex': Adoption as Official State Anthem (1927)", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Asam Sahitya Sabha: Established 1917, Padmanath Gohain Baruah", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Birendra Kumar Bhattacharya: Jnanpith 1979 ('Mrityunjay')", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Mamoni Raisom Goswami: Jnanpith 2000 & Subordinate Studies", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Nilmani Phookan Jr: 56th Jnanpith Award (2021) for Poetry", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Jyoti Prasad Agarwala: Joymoti (First Assamese Film 1935)", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Bishnu Prasad Rabha (Kalaguru): Revolutionary Artist & Thinker", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Phani Sarma (Natasurya): Theater Legend & Cinema Pioneer", "Yes")
    add("History", "Art, Culture & Literature", t, s, "Dr. Bhupen Hazarika: Bharat Ratna (2019) & Dadasaheb Phalke", "Yes")

    # =========================================================================
    # 2. GEOGRAPHY
    # =========================================================================
    # 2.1 Physical & Indian Geography
    t = "Physical Geography Fundamentals"
    s = "Earth, Atmosphere & Oceans"
    add("Geography", "Physical & Indian Geography", t, s, "Solar System & Planetary Orbits", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Earth Rotation, Revolution, Equinoxes & Solstices", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Latitudes, Longitudes & International Date Line", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Indian Standard Time Meridian (82°30' E at Mirzapur)", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Interior of Earth: Crust, Mantle, Outer Core, Inner Core", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Plate Tectonics & Continental Drift Theory", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Earthquakes: Focus, Epicenter, P, S & L Waves", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Atmospheric Layers: Troposphere, Stratosphere, Ionosphere", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Atmospheric Pressure Belts & Planetary Winds", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Ocean Currents: Warm Gulf Stream vs Cold Labrador", "No")
    add("Geography", "Physical & Indian Geography", t, s, "El Niño, La Niña & Southern Oscillation (ENSO)", "No")

    t = "Physiography of India"
    s = "Himalayas, Plains & Plateaus"
    add("Geography", "Physical & Indian Geography", t, s, "Himalayan Ranges: Greater Himadri, Himachal, Shiwalik", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Key Passes: Nathu La, Zoji La, Shipki La, Bomdi La", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Northern Plains: Bhabar, Tarai, Bhangar & Khadar", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Peninsular Plateau: Malwa, Deccan & Chota Nagpur", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Western Ghats (Anamudi Peak) vs Eastern Ghats", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Coastal Plains: Konkan, Malabar, Coromandel, Circars", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Islands: Andaman & Nicobar (Ten Degree Channel, Indira Point)", "No")

    t = "Indian Drainage Systems & Climate"
    s = "Rivers, Monsoon & Agriculture"
    add("Geography", "Physical & Indian Geography", t, s, "Indus River Basin & Five Punjab Tributaries", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Ganga River: Bhagirathi-Alaknanda Devprayag Confluence", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Ganga Tributaries: Yamuna, Son, Gandak, Kosi", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Peninsular East Rivers: Godavari, Krishna, Kaveri, Mahanadi", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Peninsular West Rivers: Narmada & Tapti Rift Valleys", "No")
    add("Geography", "Physical & Indian Geography", t, s, "South-West Monsoon Mechanism & ITCZ Shifts", "No")
    add("Geography", "Physical & Indian Geography", t, s, "North-East Retreating Monsoon & Tamil Nadu Winter Rains", "No")
    add("Geography", "Physical & Indian Geography", t, s, "ICAR Soils: Alluvial, Black (Regur), Red & Laterite", "No")
    add("Geography", "Physical & Indian Geography", t, s, "Cropping Seasons: Kharif, Rabi & Zaid Crops in India", "No")

    # 2.2 Assam Geography & Rivers
    t = "Physiography & Borders of Assam"
    s = "Boundaries & Relief"
    add("Geography", "Assam Geography", t, s, "Assam Geographic Coordinates & Latitudinal/Longitudinal Extent", "Yes")
    add("Geography", "Assam Geography", t, s, "International Borders with Bhutan (267 km) & Bangladesh (262 km)", "Yes")
    add("Geography", "Assam Geography", t, s, "Inter-State Borders with 7 North-Eastern States & West Bengal", "Yes")
    add("Geography", "Assam Geography", t, s, "Brahmaputra Valley Physiography & Floodplains", "Yes")
    add("Geography", "Assam Geography", t, s, "Barak Valley (Surma Valley) Physiography", "Yes")
    add("Geography", "Assam Geography", t, s, "Barail Range (Highest Mountain Range in Assam)", "Yes")
    add("Geography", "Assam Geography", t, s, "Karbi Plateau & North Cachar (Dima Hasao) Hills", "Yes")

    t = "Brahmaputra & Barak River Systems"
    s = "Brahmaputra Basin & Island"
    add("Geography", "Assam Geography", t, s, "Brahmaputra Origin in Chemayungdung Glacier (Tibet)", "Yes")
    add("Geography", "Assam Geography", t, s, "Yarlung Tsangpo Course & Great Bend at Namcha Barwa", "Yes")
    add("Geography", "Assam Geography", t, s, "Entry into Assam via Siang, Dibang & Lohit at Kobo", "Yes")
    add("Geography", "Assam Geography", t, s, "North-Bank Tributary: Subansiri River (Gold River)", "Yes")
    add("Geography", "Assam Geography", t, s, "North-Bank Tributary: Ranganadi & Dikrong", "Yes")
    add("Geography", "Assam Geography", t, s, "North-Bank Tributary: Jia Bharali (Kameng River)", "Yes")
    add("Geography", "Assam Geography", t, s, "North-Bank Tributary: Manas & Beki River System", "Yes")
    add("Geography", "Assam Geography", t, s, "North-Bank Tributary: Sankosh River (Assam-Bengal Border)", "Yes")
    add("Geography", "Assam Geography", t, s, "South-Bank Tributary: Burhi Dihing & Disang Rivers", "Yes")
    add("Geography", "Assam Geography", t, s, "South-Bank Tributary: Dhansiri River & Dikhow River", "Yes")
    add("Geography", "Assam Geography", t, s, "South-Bank Tributary: Kopili River (Kopili Hydroelectric)", "Yes")
    add("Geography", "Assam Geography", t, s, "South-Bank Tributary: Kulsi River (Gangetic Dolphin Habitat)", "Yes")
    add("Geography", "Assam Geography", t, s, "Majuli: World's Largest Inhabited River Island", "Yes")
    add("Geography", "Assam Geography", t, s, "Umananda (Peacock Island): Smallest River Island in Guwahati", "Yes")

    s = "Barak River Basin"
    add("Geography", "Assam Geography", t, s, "Barak River Origin in Japvo Peak (Nagaland/Manipur)", "Yes")
    add("Geography", "Assam Geography", t, s, "Barak Tributaries: Jiri, Chiri, Madhura, Dhaleswari, Longai", "Yes")
    add("Geography", "Assam Geography", t, s, "Bifurcation of Barak into Surma & Kushiyara at Haritikar", "Yes")

    t = "Climate, Floods & Minerals of Assam"
    s = "Disasters & Natural Wealth"
    add("Geography", "Assam Geography", t, s, "Tropical Monsoon Climate & Bordoichila Pre-Monsoon Storms", "Yes")
    add("Geography", "Assam Geography", t, s, "Annual Floods: High Siltation, Heavy Rainfall, Riverbank Erosion", "Yes")
    add("Geography", "Assam Geography", t, s, "Seismic Profile: Assam in High Risk Seismic Zone V", "Yes")
    add("Geography", "Assam Geography", t, s, "Great Assam Earthquakes of 1897 & 1950 (Course Changes)", "Yes")
    add("Geography", "Assam Geography", t, s, "Crude Oil: Digboi (1901), Naharkatiya & Moran Fields", "Yes")
    add("Geography", "Assam Geography", t, s, "Coal Deposits: Makum, Ledo, Borgolai & Nazira Fields", "Yes")
    add("Geography", "Assam Geography", t, s, "Limestone & China Clay Deposits: Umrangso (Dima Hasao)", "Yes")

    # 2.3 Environment & National Parks of Assam
    t = "7 National Parks of Assam"
    s = "National Parks Profile"
    add("Geography", "Environment & Ecology", t, s, "Kaziranga National Park: UNESCO World Heritage (One-horned Rhino)", "Yes")
    add("Geography", "Environment & Ecology", t, s, "Manas National Park: UNESCO World Heritage (Pygmy Hog, Golden Langur)", "Yes")
    add("Geography", "Environment & Ecology", t, s, "Nameri National Park: White-winged Wood Duck (Deo Hah)", "Yes")
    add("Geography", "Environment & Ecology", t, s, "Dibru-Saikhowa National Park: Feral Horses & Biosphere Reserve", "Yes")
    add("Geography", "Environment & Ecology", t, s, "Orang National Park: Mini Kaziranga Rhino Habitat", "Yes")
    add("Geography", "Environment & Ecology", t, s, "Raimona National Park (BTR / Kokrajhar): Golden Langur Habitat", "Yes")
    add("Geography", "Environment & Ecology", t, s, "Dihing Patkai National Park: Amazon of the East Rainforest", "Yes")
    add("Geography", "Environment & Ecology", t, s, "Pobitora Wildlife Sanctuary: World's Highest Rhino Density", "Yes")
    add("Geography", "Environment & Ecology", t, s, "Hoollongapar Gibbon Sanctuary (Jorhat): Hoolock Gibbon", "Yes")
    add("Geography", "Environment & Ecology", t, s, "Deepor Beel: Assam's Only Ramsar Wetland Site", "Yes")
    add("Geography", "Environment & Ecology", t, s, "Assam Official State Symbols (Rhino, Deo Hah, Hollong, Kopou)", "Yes")

    t = "Ecology & Climate Action"
    s = "Ecosystems & Conservation"
    add("Geography", "Environment & Ecology", t, s, "Food Chains, Food Webs & 10% Energy Transfer Law", "No")
    add("Geography", "Environment & Ecology", t, s, "Biodiversity Hotspots: Western Ghats & Eastern Himalayas", "No")
    add("Geography", "Environment & Ecology", t, s, "In-situ Conservation (Parks) vs Ex-situ (Zoos, Seed Banks)", "No")
    add("Geography", "Environment & Ecology", t, s, "Project Tiger (1973) & Project Elephant (1992)", "No")
    add("Geography", "Environment & Ecology", t, s, "Air Pollution: PM2.5, Smog & Acid Rain (SO2, NO2)", "No")
    add("Geography", "Environment & Ecology", t, s, "Ozone Layer Depletion & Montreal Protocol (1987)", "No")
    add("Geography", "Environment & Ecology", t, s, "Greenhouse Effect, Kyoto Protocol & Paris Agreement (1.5°C)", "No")
    add("Geography", "Environment & Ecology", t, s, "India's Panchamrit Targets, Net Zero 2070 & Mission LiFE", "No")

    # =========================================================================
    # 3. POLITY
    # =========================================================================
    # 3.1 Indian Polity & Constitution
    t = "Constitutional Framework & Fundamental Rights"
    s = "Making of Constitution & Preamble"
    add("Polity", "Indian Polity & Constitution", t, s, "Constituent Assembly (1946) & Dr. Rajendra Prasad President", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Drafting Committee Chairman: Dr. B.R. Ambedkar", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Adoption (26 Nov 1949) & Republic Day (26 Jan 1950)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Preamble: Sovereign, Socialist, Secular, Democratic, Republic", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "42nd Amendment (1976): Added Socialist, Secular, Integrity", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Kesavananda Bharati Judgment (1973): Basic Structure Doctrine", "No")

    s = "Fundamental Rights (Articles 12-35)"
    add("Polity", "Indian Polity & Constitution", t, s, "Definition of State (Article 12) & Judicial Review (Article 13)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Article 14: Equality before Law & Equal Protection of Laws", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Article 15: Prohibition of Discrimination on Religion, Race, Caste", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Article 16: Equality of Opportunity in Public Employment", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Article 17: Abolition of Untouchability & Punishable Offence", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Article 18: Abolition of Titles (Except Military & Academic)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Article 19: Six Freedoms (Speech, Assembly, Association, Movement)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Article 20: Protection against Retrospective Law & Double Jeopardy", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Article 21: Protection of Life & Personal Liberty", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Puttaswamy Judgment: Right to Privacy as Fundamental Right", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Article 21A: Right to Free & Compulsory Education (RTE Act)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Article 23: Prohibition of Human Trafficking & Forced Labour", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Article 24: Prohibition of Child Labour in Hazardous Employments", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Articles 25-28: Freedom of Conscience, Religion & Religious Taxes", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Articles 29-30: Cultural & Educational Rights of Minorities", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Article 32: Right to Constitutional Remedies (Heart & Soul)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Five Prerogative Writs: Habeas Corpus (To have the body)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Five Prerogative Writs: Mandamus (We Command Public Duty)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Five Prerogative Writs: Prohibition (To Forbid Lower Court)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Five Prerogative Writs: Certiorari (To be Certified / Quashed)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Five Prerogative Writs: Quo-Warranto (By What Authority/Warrant)", "No")

    t = "DPSPs, Duties & Union-State Organs"
    s = "DPSPs & Fundamental Duties"
    add("Polity", "Indian Polity & Constitution", t, s, "DPSPs (Part IV, Articles 36-51): Non-Justiciable Principles", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Article 39A: Equal Justice & Free Legal Aid to Poor", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Article 40: Organization of Village Panchayats", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Article 44: Uniform Civil Code (UCC) for All Citizens", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Article 50: Separation of Judiciary from Executive", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Fundamental Duties (Part IVA, Article 51A): 11 Civic Duties", "No")

    s = "President, Prime Minister & Parliament"
    add("Polity", "Indian Polity & Constitution", t, s, "President of India: Electoral College (MPs + MLAs)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Presidential Powers: Ordinance (Art 123) & Pardoning (Art 72)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Impeachment of President (Article 61) by Parliament", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Vice-President of India: Ex-Officio Chairman of Rajya Sabha", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Prime Minister & Council of Ministers: Collective Responsibility", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Rajya Sabha: Composition, 250 Members, 12 Nominated, Permanent", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Lok Sabha: 543 Members, 5-Year Term, Speaker's Role", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Parliament Sessions: Budget, Monsoon, Winter & Question Hour", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Money Bill (Article 110): Speaker's Sole Certifying Authority", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Annual Financial Statement (Article 112 / Budget)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Joint Sitting of Parliament (Article 108) Presided by Speaker", "No")

    s = "Judiciary & Constitutional Bodies"
    add("Polity", "Indian Polity & Constitution", t, s, "Supreme Court of India: CJI Appointment & Collegium System", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Original Jurisdiction (Art 131) & Advisory Jurisdiction (Art 143)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "High Courts: Writ Jurisdiction under Article 226", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Election Commission of India (Article 324) & EVM/VVPAT", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Comptroller and Auditor General of India (CAG - Article 148)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "Finance Commission of India (Article 280)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "NITI Aayog: Replaced Planning Commission in 2015", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "73rd Amendment 1992: Panchayati Raj (11th Schedule, 29 Subjects)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "74th Amendment 1992: Urban Municipalities (12th Schedule)", "No")
    add("Polity", "Indian Polity & Constitution", t, s, "National Emergency (Art 352) & President's Rule (Art 356)", "No")

    # 3.2 Assam Polity & State Schemes
    t = "Assam State Governance & 6th Schedule"
    s = "State Assembly & High Court"
    add("Polity", "Assam Governance & Administration", t, s, "Assam Legislative Assembly: 126 Single-Member Constituencies", "Yes")
    add("Polity", "Assam Governance & Administration", t, s, "Shifting of State Capital from Shillong to Dispur (1972-73)", "Yes")
    add("Polity", "Assam Governance & Administration", t, s, "Gauhati High Court (1948): Jurisdiction over 4 NE States", "Yes")

    s = "Sixth Schedule & Local Governance"
    add("Polity", "Assam Governance & Administration", t, s, "Sixth Schedule: Tribal Area Administrative Autonomy", "Yes")
    add("Polity", "Assam Governance & Administration", t, s, "Bodoland Territorial Council (BTC / BTR - Kokrajhar, Baksa, Udalguri, Chirang, Tamulpur)", "Yes")
    add("Polity", "Assam Governance & Administration", t, s, "Karbi Anglong Autonomous Council (KAAC - Diphu)", "Yes")
    add("Polity", "Assam Governance & Administration", t, s, "Dima Hasao Autonomous Council (DHAC - Haflong)", "Yes")
    add("Polity", "Assam Governance & Administration", t, s, "Assam Panchayat Act 1994: 3-Tier System (Gaon, Anchalik, Zilla)", "Yes")

    t = "Flagship Schemes of Assam Government"
    s = "Welfare & Digital Missions"
    add("Polity", "Assam Governance & Administration", t, s, "Orunodoi 1.0, 2.0 & 3.0: Monthly DBT to Underprivileged Women", "Yes")
    add("Polity", "Assam Governance & Administration", t, s, "Nijut Moina Scheme: Monthly Financial Stipends for Girl Students", "Yes")
    add("Polity", "Assam Governance & Administration", t, s, "Mission Basundhara (1.0, 2.0, 3.0): Digital Land Records & Pattas", "Yes")
    add("Polity", "Assam Governance & Administration", t, s, "Mission Bhumiputra: Digital Issuance of Caste Certificates", "Yes")
    add("Polity", "Assam Governance & Administration", t, s, "Mukhyamantri Atmanirbharshil Asom (CMAAA): Youth Seed Funding", "Yes")
    add("Polity", "Assam Governance & Administration", t, s, "Swanirbhar Naari: Direct Handloom Procurement from Weavers", "Yes")
    add("Polity", "Assam Governance & Administration", t, s, "Ayushman Asom: Rs. 5 Lakh Cashless Medical Scheme per Family", "Yes")
    add("Polity", "Assam Governance & Administration", t, s, "Pragyan Bharati Scheme: Free Textbooks & Scooty Awards", "Yes")

    # =========================================================================
    # 4. ECONOMY (CONCISE ESSENTIALS)
    # =========================================================================
    t = "Indian Economy & Banking Essentials"
    s = "Macroeconomics & Monetary Policy"
    add("Economy", "Indian Economy Essentials", t, s, "Gross Domestic Product (GDP): Real vs Nominal GDP", "No")
    add("Economy", "Indian Economy Essentials", t, s, "Inflation Indices: CPI (Consumer Price) vs WPI (Wholesale Price)", "No")
    add("Economy", "Indian Economy Essentials", t, s, "Reserve Bank of India (RBI 1935): Monetary Policy Committee (MPC)", "No")
    add("Economy", "Indian Economy Essentials", t, s, "RBI Policy Rates: Repo Rate, Reverse Repo Rate, CRR, SLR", "No")
    add("Economy", "Indian Economy Essentials", t, s, "Union Budget Deficits: Fiscal Deficit & Revenue Deficit", "No")
    add("Economy", "Indian Economy Essentials", t, s, "Goods & Services Tax (GST Implemented 1 July 2017)", "No")
    add("Economy", "Indian Economy Essentials", t, s, "Unified Payments Interface (UPI) & Digital Financial Inclusion", "No")

    t = "Assam Economy, Tea, Oil & Infrastructure"
    s = "Tea, Refineries & Waterways"
    add("Economy", "Assam Economy Essentials", t, s, "Assam Tea Industry: Robert Bruce Wild Tea Discovery (1823)", "Yes")
    add("Economy", "Assam Economy Essentials", t, s, "First Commercial Tea Garden at Chabua (1837) & Assam Company", "Yes")
    add("Economy", "Assam Economy Essentials", t, s, "Guwahati Tea Auction Centre (GTAC 1970) & Orthodox GI Tag", "Yes")
    add("Economy", "Assam Economy Essentials", t, s, "Digboi Refinery (1901): Asia's Oldest Operating Refinery", "Yes")
    add("Economy", "Assam Economy Essentials", t, s, "Guwahati Noonmati Refinery (1962: India's First PSU Refinery)", "Yes")
    add("Economy", "Assam Economy Essentials", t, s, "Numaligarh Refinery (NRL 1999: Assam Accord Refinery)", "Yes")
    add("Economy", "Assam Economy Essentials", t, s, "Bongaigaon Refinery (BGR 1979) & BCPL Petrochemicals Lepetkata", "Yes")
    add("Economy", "Assam Economy Essentials", t, s, "National Waterway 2 (NW-2): Sadiya to Dhubri (891 km) & Pandu Port", "Yes")
    add("Economy", "Assam Economy Essentials", t, s, "Bogibeel Rail-Cum-Road Bridge (4.94 km Longest in India)", "Yes")
    add("Economy", "Assam Economy Essentials", t, s, "Dhola-Sadiya / Bhupen Hazarika Setu (9.15 km over Lohit River)", "Yes")

    # =========================================================================
    # 5. APTITUDE (MATH, REASONING, VERBAL REASONING)
    # =========================================================================
    # 5.1 Quantitative Aptitude / Mathematics
    t = "Number Systems & Simplification"
    s = "Core Numbers & Calculations"
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Classification of Numbers (Prime, Composite, Real, Rational)", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Divisibility Rules for 2, 3, 4, 5, 6, 7, 8, 9, 11, 13", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Unit Digit Calculation of Exponents", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Remainder Theorem & Factors of Numbers", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "HCF & LCM Prime Factorization and Division Methods", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "HCF & LCM Word Problems (Bells Ringing Together)", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "VBODMAS Rule of Calculation Order", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Fractions, Decimals, Surds & Indices Simplification", "No")

    t = "Commercial Arithmetic"
    s = "Percentages & Profit-Loss"
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Percentage to Fraction Conversion Chart", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Percentage Increase, Decrease & Successive Changes", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Population Growth & Machine Depreciation Formula", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Profit & Loss: Cost Price, Selling Price & Profit %", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Marked Price & Successive Discounts Formula", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Dishonest Dealer & Faulty Weight Problems", "No")

    s = "Simple & Compound Interest"
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Simple Interest Formula: SI = (P x R x T) / 100", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Compound Interest Formula: Annual & Half-Yearly Compounding", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Difference between CI and SI for 2 Years: D = P(R/100)^2", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Difference between CI and SI for 3 Years Formula", "No")

    t = "Ratios, Proportions & Averages"
    s = "Ratios, Ages & Mixtures"
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Ratio & Proportion: Mean, Third & Fourth Proportional", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Dividing Amounts into Given Ratios", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Problems on Ages (Father-Son Age Equations)", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Partnership: Capital Investment & Profit Sharing Ratio", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Arithmetic Average & Consecutive Numbers Average", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Average Problems on Joining, Leaving & Replacement", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Mixtures & Alligation: Rule of Alligation Cross Method", "No")

    t = "Time, Work, Speed & Distance"
    s = "Work, Speed, Trains & Boats"
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Time & Work: LCM Total Work Method & Worker Efficiency", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Men-Days-Hours Formula: (M1 D1 H1)/W1 = (M2 D2 H2)/W2", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Pipes & Cisterns: Inlet and Emptying Outlet Leaks", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Speed Conversion: km/h to m/s by Multiplying 5/18", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Average Speed Formula: 2xy / (x + y) for Equal Distances", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Trains: Passing a Pole/Man (Distance = Train Length)", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Trains: Passing a Platform (Distance = Train + Platform)", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Relative Speed: Same Direction (u-v) vs Opposite (u+v)", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Boats & Streams: Downstream (u+v) & Upstream (u-v)", "No")

    t = "Mensuration & Data Interpretation"
    s = "2D/3D Mensuration & Charts"
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "2D Triangles: Area (1/2 x b x h) & Heron's Formula", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "2D Quadrilaterals: Square, Rectangle, Rhombus, Trapezium", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "2D Circles: Circumference (2πr) & Area (πr^2)", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "3D Cube & Cuboid: Volume & Total Surface Area", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "3D Cylinder & Cone: Volume & Curved Surface Area", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "3D Sphere & Hemisphere: Volume & Surface Area", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Data Interpretation: Tabular Numerical Charts", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Data Interpretation: Bar Graphs & Line Graphs", "No")
    add("Aptitude", "Quantitative Aptitude (Mathematics)", t, s, "Data Interpretation: Pie Charts (360 Degrees = 100%)", "No")

    # 5.2 Logical Reasoning
    t = "Logical & Analytical Reasoning"
    s = "Series, Coding & Relations"
    add("Aptitude", "Logical Reasoning", t, s, "Number Series: Difference, Double Difference, Square Patterns", "No")
    add("Aptitude", "Logical Reasoning", t, s, "Alphabet & Alpha-Numeric Series Completion", "No")
    add("Aptitude", "Logical Reasoning", t, s, "Coding-Decoding: Letter Shifting & Number Coding", "No")
    add("Aptitude", "Logical Reasoning", t, s, "Blood Relations: Family Tree Diagrams & Decoded Relations", "No")
    add("Aptitude", "Logical Reasoning", t, s, "Direction Sense: Compass 8 Directions & Pythagoras Distance", "No")
    add("Aptitude", "Logical Reasoning", t, s, "Order & Ranking: Total Persons = (Left + Right - 1)", "No")
    add("Aptitude", "Logical Reasoning", t, s, "Linear Seating Arrangement (Facing North/South)", "No")
    add("Aptitude", "Logical Reasoning", t, s, "Circular Seating Arrangement (Facing In/Out)", "No")
    add("Aptitude", "Logical Reasoning", t, s, "Clock: Angle Between Hands = |30H - 5.5M|", "No")
    add("Aptitude", "Logical Reasoning", t, s, "Calendar: Odd Days Calculation & Day of Any Date", "No")
    add("Aptitude", "Logical Reasoning", t, s, "Logical Venn Diagrams (Overlapping Sets)", "No")
    add("Aptitude", "Logical Reasoning", t, s, "Syllogisms: Statements, Conclusions & Venn Method", "No")

    # 5.3 Verbal Reasoning / Critical Logic
    t = "Verbal Reasoning & Non-Verbal Figures"
    s = "Critical Logic & Figures"
    add("Aptitude", "Verbal Reasoning (Critical Logic)", t, s, "Statement & Assumptions (Identifying Implicit Assumptions)", "No")
    add("Aptitude", "Verbal Reasoning (Critical Logic)", t, s, "Statement & Arguments (Strong vs Weak Arguments)", "No")
    add("Aptitude", "Verbal Reasoning (Critical Logic)", t, s, "Statement & Course of Action (Administrative Decisions)", "No")
    add("Aptitude", "Verbal Reasoning (Critical Logic)", t, s, "Cause & Effect Reasoning Relationships", "No")
    add("Aptitude", "Verbal Reasoning (Critical Logic)", t, s, "Non-Verbal: Mirror Images (Left-Right Inversion)", "No")
    add("Aptitude", "Verbal Reasoning (Critical Logic)", t, s, "Non-Verbal: Water Images (Top-Bottom Inversion)", "No")
    add("Aptitude", "Verbal Reasoning (Critical Logic)", t, s, "Paper Folding & Paper Cutting Patterns", "No")
    add("Aptitude", "Verbal Reasoning (Critical Logic)", t, s, "Counting of Figures: Counting Triangles & Squares", "No")
    add("Aptitude", "Verbal Reasoning (Critical Logic)", t, s, "Dice & Cube Problems (Opposite Faces Calculation)", "No")

    # =========================================================================
    # 6. ENGLISH
    # =========================================================================
    t = "English Grammar & Syntax"
    s = "Parts of Speech & Tenses"
    add("English", "English Grammar", t, s, "Nouns: Common, Proper, Collective, Abstract & Plural Rules", "No")
    add("English", "English Grammar", t, s, "Pronouns: Personal, Relative, Demonstrative & Reflexive", "No")
    add("English", "English Grammar", t, s, "Adjectives: Degrees of Comparison (Positive, Comparative, Superlative)", "No")
    add("English", "English Grammar", t, s, "Verbs: Finite, Non-Finite, Gerunds & Infinitives", "No")
    add("English", "English Grammar", t, s, "Modal Auxiliaries: Can, Could, May, Might, Must, Should", "No")
    add("English", "English Grammar", t, s, "Prepositions of Time, Place, Movement (In, At, On, Into, Between)", "No")
    add("English", "English Grammar", t, s, "Fixed Prepositions with Verbs & Adjectives", "No")
    add("English", "English Grammar", t, s, "Conjunctions: Neither-Nor, Either-Or, Not Only-But Also", "No")
    add("English", "English Grammar", t, s, "Articles: Definite 'The', Indefinite 'A/An' & Zero Article", "No")
    add("English", "English Grammar", t, s, "Tenses: Simple, Continuous, Perfect & Perfect Continuous", "No")
    add("English", "English Grammar", t, s, "Conditional Sentences (If Clauses & 'If I were you')", "No")
    add("English", "English Grammar", t, s, "Subject-Verb Agreement (Singular/Plural Alignment Rules)", "No")
    add("English", "English Grammar", t, s, "Active & Passive Voice Transformation Rules", "No")
    add("English", "English Grammar", t, s, "Direct & Indirect Speech (Narration Changes)", "No")
    add("English", "English Grammar", t, s, "Spotting Grammatical Errors in Sentences", "No")
    add("English", "English Grammar", t, s, "Sentence Improvement & Fill in the Blanks", "No")

    t = "Vocabulary & Word Power"
    s = "Vocabulary & Idioms"
    add("English", "Vocabulary & Word Power", t, s, "Synonyms: High-Frequency Competitive Exam Words", "No")
    add("English", "Vocabulary & Word Power", t, s, "Antonyms: Opposites & Contextual Antonyms", "No")
    add("English", "Vocabulary & Word Power", t, s, "Idioms & Phrases: Meanings & Usage", "No")
    add("English", "Vocabulary & Word Power", t, s, "Phrasal Verbs (Give up, Call on, Put off, Look after)", "No")
    add("English", "Vocabulary & Word Power", t, s, "One Word Substitution: Specialists, Phobias, Governments", "No")
    add("English", "Vocabulary & Word Power", t, s, "Homonyms: Affect/Effect, Principal/Principle, Compliment/Complement", "No")
    add("English", "Vocabulary & Word Power", t, s, "Spelling Rules & Identifying Misspelt Words", "No")

    t = "Reading Comprehension & Composition"
    s = "Comprehension & Sequencing"
    add("English", "Reading Comprehension & Composition", t, s, "Unseen Prose Passages Reading & Fact Retrieval", "No")
    add("English", "Reading Comprehension & Composition", t, s, "Inference-Based Reading Questions", "No")
    add("English", "Reading Comprehension & Composition", t, s, "Identifying Central Idea & Tone of the Passage", "No")
    add("English", "Reading Comprehension & Composition", t, s, "Cloze Test: Contextual Word Filling in Paragraphs", "No")
    add("English", "Reading Comprehension & Composition", t, s, "Para-Jumbles: Jumbled Sentences (PQRS Reordering)", "No")

    # =========================================================================
    # 7. GENERAL AWARENESS & SCIENCE
    # =========================================================================
    # 7.1 Everyday Science
    t = "Everyday Physics"
    s = "Mechanics, Heat, Light & Electricity"
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "SI Units: Force (Newton), Energy (Joule), Power (Watt)", "No")
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "Newton's Three Laws of Motion & Momentum", "No")
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "Gravitational Force: g = 9.8 m/s^2 & Escape Velocity (11.2 km/s)", "No")
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "Kinetic Energy (1/2 mv^2) & Potential Energy (mgh)", "No")
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "Archimedes' Principle, Buoyancy & Hydrometer", "No")
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "Pascal's Law & Hydraulic Brakes Mechanism", "No")
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "Temperature Scales: Celsius, Fahrenheit, Kelvin (-273.15 °C)", "No")
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "Heat Transfer: Conduction, Convection & Radiation", "No")
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "Light Reflection, Refraction & Snell's Law", "No")
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "Total Internal Reflection: Optical Fibers & Mirages", "No")
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "Dispersion (Rainbow) & Scattering (Blue Sky Rayleigh Effect)", "No")
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "Myopia (Short Sight) Corrected by Concave Lens", "No")
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "Hypermetropia (Long Sight) Corrected by Convex Lens", "No")
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "Sound Waves: Speed in Media, Echo & Ultrasound SONAR", "No")
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "Ohm's Law (V = IR), Series & Parallel Resistors", "No")
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "Electric Fuse Wire (Lead-Tin Alloy Low Melting Point)", "No")
    add("General Awareness & Science", "Everyday Science (Physics)", t, s, "Electromagnetic Induction: Generators & Transformers", "No")

    t = "Everyday Chemistry"
    s = "Matter, Acids, Bases & Metals"
    add("General Awareness & Science", "Everyday Science (Chemistry)", t, s, "States of Matter: Solid, Liquid, Gas, Plasma & BEC", "No")
    add("General Awareness & Science", "Everyday Science (Chemistry)", t, s, "Physical vs Chemical Changes Examples", "No")
    add("General Awareness & Science", "Everyday Science (Chemistry)", t, s, "Subatomic Particles: Electrons, Protons & Neutrons", "No")
    add("General Awareness & Science", "Everyday Science (Chemistry)", t, s, "Modern Periodic Table (Henry Moseley): Periods & Groups", "No")
    add("General Awareness & Science", "Everyday Science (Chemistry)", t, s, "Acids & Bases: Litmus Indicator & pH Scale", "No")
    add("General Awareness & Science", "Everyday Science (Chemistry)", t, s, "Common Salt (Sodium Chloride - NaCl)", "No")
    add("General Awareness & Science", "Everyday Science (Chemistry)", t, s, "Baking Soda (Sodium Hydrogen Carbonate - NaHCO3)", "No")
    add("General Awareness & Science", "Everyday Science (Chemistry)", t, s, "Washing Soda (Sodium Carbonate - Na2CO3.10H2O)", "No")
    add("General Awareness & Science", "Everyday Science (Chemistry)", t, s, "Bleaching Powder (Calcium Oxychloride - CaOCl2)", "No")
    add("General Awareness & Science", "Everyday Science (Chemistry)", t, s, "Plaster of Paris (Calcium Sulphate Hemihydrate - CaSO4.1/2 H2O)", "No")
    add("General Awareness & Science", "Everyday Science (Chemistry)", t, s, "Rusting of Iron & Galvanization using Zinc", "No")
    add("General Awareness & Science", "Everyday Science (Chemistry)", t, s, "Alloy: Brass (Copper + Zinc)", "No")
    add("General Awareness & Science", "Everyday Science (Chemistry)", t, s, "Alloy: Bronze (Copper + Tin)", "No")
    add("General Awareness & Science", "Everyday Science (Chemistry)", t, s, "Alloy: Stainless Steel (Iron + Chromium + Nickel + Carbon)", "No")
    add("General Awareness & Science", "Everyday Science (Chemistry)", t, s, "Carbon Allotropes: Diamond (Hardest) & Graphite (Conductor)", "No")

    t = "Life Sciences & Biology"
    s = "Cell, Physiology & Diseases"
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Cell as Basic Unit of Life & Cell Theory", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Mitochondria: Powerhouse of the Cell (ATP)", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Lysosomes: Suicide Bags of the Cell", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Human Heart: 4 Chambers & Double Circulation", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Red Blood Cells (RBCs): Hemoglobin & 120-Day Lifespan", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "White Blood Cells (WBCs): Immune Defense Mechanism", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Blood Platelets: Blood Clotting Mechanism", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "ABO Blood Groups: Universal Donor O-ve, Recipient AB+ve", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Kidneys & Nephrons: Urine Filtration & Dialysis", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Endocrine Glands: Pituitary (Master Gland)", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Thyroid Gland: Thyroxine Hormone & Iodine Goitre", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Pancreas: Insulin Hormone & Diabetes Mellitus", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Vitamin A Deficiency: Night Blindness", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Vitamin B1 Deficiency: Beriberi Disease", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Vitamin C Deficiency: Scurvy & Bleeding Gums", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Vitamin D Deficiency: Rickets in Children", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Vitamin K Deficiency: Blood Clotting Failure", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Bacterial Diseases: Tuberculosis (BCG), Typhoid, Cholera", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Viral Diseases: Dengue, Polio, Rabies, Hepatitis, HIV", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Malaria: Plasmodium Parasite & Female Anopheles Mosquito", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "Gregor Mendel's Laws of Inheritance & Genetics", "No")
    add("General Awareness & Science", "Everyday Science (Biology)", t, s, "DNA Double Helix Structure (Watson & Crick)", "No")

    # 7.2 Static GK & International Bodies
    t = "Static GK & International Organizations"
    s = "Organizations & Honors"
    add("General Awareness & Science", "Static GK", t, s, "United Nations (UN): Headquarters New York (1945)", "No")
    add("General Awareness & Science", "Static GK", t, s, "UN Security Council: 5 Permanent Members with Veto", "No")
    add("General Awareness & Science", "Static GK", t, s, "UNESCO Headquarters (Paris) & World Heritage Sites", "No")
    add("General Awareness & Science", "Static GK", t, s, "World Health Organization (WHO Headquarters Geneva)", "No")
    add("General Awareness & Science", "Static GK", t, s, "IMF & World Bank Headquarters (Washington DC)", "No")
    add("General Awareness & Science", "Static GK", t, s, "World Trade Organization (WTO Headquarters Geneva)", "No")
    add("General Awareness & Science", "Static GK", t, s, "International Court of Justice (ICJ at Peace Palace, The Hague)", "No")
    add("General Awareness & Science", "Static GK", t, s, "Regional Blocs: ASEAN (Jakarta), SAARC (Kathmandu), BIMSTEC (Dhaka)", "No")
    add("General Awareness & Science", "Static GK", t, s, "Multilateral Blocs: BRICS, SCO (Beijing), G20 / G21, European Union", "No")
    add("General Awareness & Science", "Static GK", t, s, "Highest Civilian Award: Bharat Ratna Guidelines & Peepal Leaf", "No")
    add("General Awareness & Science", "Static GK", t, s, "Padma Awards: Padma Vibhushan, Padma Bhushan, Padma Shri", "No")
    add("General Awareness & Science", "Static GK", t, s, "Wartime Gallantry Awards: Param Vir Chakra, Maha Vir Chakra", "No")
    add("General Awareness & Science", "Static GK", t, s, "Peacetime Gallantry Awards: Ashoka Chakra, Kirti Chakra", "No")
    add("General Awareness & Science", "Static GK", t, s, "Dadasaheb Phalke Award for Cinema & Jnanpith for Literature", "No")
    add("General Awareness & Science", "Static GK", t, s, "Khel Ratna Award & Arjuna Award for Sports Excellence", "No")
    add("General Awareness & Science", "Static GK", t, s, "Important Days: World Environment Day (5 June)", "No")
    add("General Awareness & Science", "Static GK", t, s, "Important Days: Earth Day (22 April) & Yoga Day (21 June)", "No")
    add("General Awareness & Science", "Static GK", t, s, "Important Days: National Science Day (28 Feb - Raman Effect)", "No")
    add("General Awareness & Science", "Static GK", t, s, "Important Days: National Voters Day (25 January)", "No")

    # 7.3 Contemporary Current Affairs
    t = "Contemporary Current Affairs"
    s = "Current Events, Space & Defense"
    add("General Awareness & Science", "Current Affairs", t, s, "Key National & International Summits of the Year", "No")
    add("General Awareness & Science", "Current Affairs", t, s, "Major Parliamentary Acts & Landmark Supreme Court Rulings", "No")
    add("General Awareness & Science", "Current Affairs", t, s, "ISRO Chandrayaan-3: Moon South Pole (Shiv Shakti Point)", "No")
    add("General Awareness & Science", "Current Awareness & Science", t, s, "National Space Day Celebrated on 23 August", "No")
    add("General Awareness & Science", "Current Affairs", t, s, "ISRO Aditya-L1 Solar Observation Mission (Lagrange Point 1)", "No")
    add("General Awareness & Science", "Current Affairs", t, s, "Gaganyaan: India's Human Spaceflight Program", "No")
    add("General Awareness & Science", "Current Affairs", t, s, "Nobel Prizes of the Current Year Across 6 Fields", "No")
    add("General Awareness & Science", "Current Affairs", t, s, "Bilateral Military Exercises: Yudh Abhyas, Mitra Shakti", "No")
    add("General Awareness & Science", "Current Affairs", t, s, "Naval Exercises: Malabar, Varuna & Sampriti", "No")
    add("General Awareness & Science", "Current Affairs", t, s, "Olympic Games, Asian Games & Commonwealth Games Records", "No")
    add("General Awareness & Science", "Current Affairs", t, s, "Cricket World Cup & Major International Tournaments", "No")
    add("General Awareness & Science", "Current Affairs", t, s, "Assam Sports Champions: Lovlina Borgohain (Boxing Olympic Medal)", "Yes")
    add("General Awareness & Science", "Current Affairs", t, s, "Assam Sports Champions: Hima Das (Dhing Express Sprinting)", "Yes")

    # 7.4 Computer Fundamentals & Digital Literacy
    t = "Computer Fundamentals & Office Productivity"
    s = "Hardware, Software & Applications"
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "Generations of Computers (1st Vacuum Tubes to 5th AI)", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "CPU Components: ALU, Control Unit, Registers", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "Primary Memory: RAM (Volatile) vs ROM (Non-Volatile)", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "Secondary Storage: SSD, HDD, Optical Discs, Flash Drives", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "Input Devices (Keyboard, Mouse, OCR, OMR, Barcode Scanner)", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "Output Devices (Monitors, Laser & Inkjet Printers, Plotters)", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "System Software (Operating Systems, Compilers) vs Applications", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "Operating Systems: Windows Desktop Navigation & Linux Basics", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "MS Word: Document Formatting, Page Layout, Tables", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "MS Word: Mail Merge (Data Source & Form Letters)", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "MS Excel: Cell References (Relative vs Absolute with $)", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "MS Excel Formulas: SUM, AVERAGE, COUNT, IF, VLOOKUP", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "MS Excel: Bar Charts, Pie Charts, Column Charts", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "MS PowerPoint: Slides, Animations & Slide Show (F5)", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "Common Shortcuts: Ctrl+C, Ctrl+V, Ctrl+Z, Ctrl+S, Alt+Tab", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "Network Topologies: Star, Bus, Ring, Mesh", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "Internet Protocols: HTTP, HTTPS, FTP, SMTP, DNS, IP Address", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "Cyber Security: Viruses, Ransomware, Phishing & Firewalls", "No")
    add("General Awareness & Science", "Computer Fundamentals & Digital Literacy", t, s, "Digital India: UPI (NPCI), DigiLocker, Information Technology Act", "No")

    return rows

def generate_checklist():
    os.chdir(BASE_DIR)
    rows = build_checklist_dataset()

    fieldnames = [
        "Domain",
        "Subject",
        "Topic",
        "Subtopic",
        "Sub_Subtopic",
        "Assam_Specific",
        "Applicable_Exams"
    ]

    csv_path = os.path.join(BASE_DIR, "csv", "assam_general_papers_syllabus.csv")
    json_path = os.path.join(BASE_DIR, "json", "assam_general_papers_syllabus.json")

    with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

    with open(json_path, mode="w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)

    print(f"Generated Clutter-Free Checklist CSV: {csv_path} ({len(rows)} atomic checklist rows)")
    print(f"Generated Clutter-Free Checklist JSON: {json_path}")

if __name__ == "__main__":
    generate_checklist()
