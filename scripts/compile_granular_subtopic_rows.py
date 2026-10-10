import csv
import json
import os

BASE_DIR = "/home/angsuman/extra_spac/Study_Assam"

def build_checklist_dataset():
    rows = []

    def add(domain, subject, topic, subtopic, sub_subtopic, assam_specific):
        rows.append({
            "Domain": domain,
            "Subject": subject,
            "Topic": topic,
            "Subtopic": subtopic,
            "Sub_Subtopic": sub_subtopic,
            "Assam_Specific": assam_specific
        })

    # ==========================================
    # 1. HISTORY DOMAIN
    # ==========================================
    
    # 1.1 Ancient Indian History
    t = "Ancient Indian History"
    s = "Indus Valley Civilization"
    add("History", "Ancient India", t, s, "Harappan Town Planning: Grid Pattern", "No")
    add("History", "Ancient India", t, s, "Harappan Town Planning: Drainage System", "No")
    add("History", "Ancient India", t, s, "Harappan Sites: Mohenjodaro (Great Bath)", "No")
    add("History", "Ancient India", t, s, "Harappan Sites: Lothal (Dockyard)", "No")
    add("History", "Ancient India", t, s, "Harappan Sites: Dholavira (Water Management)", "No")
    add("History", "Ancient India", t, s, "Harappan Sites: Kalibangan (Ploughed Field)", "No")
    add("History", "Ancient India", t, s, "Harappan Economy: Trade Networks & Seals", "No")
    add("History", "Ancient India", t, s, "Harappan Religion: Pashupati Seal & Mother Goddess", "No")
    
    s = "Vedic Period"
    add("History", "Ancient India", t, s, "Early Vedic Era: Rig Veda & its Mandalas", "No")
    add("History", "Ancient India", t, s, "Early Vedic Era: Society & Pastoral Economy", "No")
    add("History", "Ancient India", t, s, "Later Vedic Era: Sama, Yajur, Atharva Vedas", "No")
    add("History", "Ancient India", t, s, "Later Vedic Era: Origin of Varna System", "No")
    add("History", "Ancient India", t, s, "Later Vedic Era: Upanishads & Philosophy", "No")

    s = "Buddhism & Jainism"
    add("History", "Ancient India", t, s, "Buddhism: Life & Teachings of Gautama Buddha", "No")
    add("History", "Ancient India", t, s, "Buddhism: Four Noble Truths & Eightfold Path", "No")
    add("History", "Ancient India", t, s, "Buddhism: The Four Buddhist Councils", "No")
    add("History", "Ancient India", t, s, "Buddhism: Sects (Mahayana, Hinayana, Vajrayana)", "No")
    add("History", "Ancient India", t, s, "Jainism: Life & Teachings of Mahavira", "No")
    add("History", "Ancient India", t, s, "Jainism: Triratnas & Ahimsa", "No")
    add("History", "Ancient India", t, s, "Jainism: Sects (Svetambara, Digambara)", "No")

    s = "Mauryan & Post-Mauryan Empires"
    add("History", "Ancient India", t, s, "Mauryan Empire: Chandragupta Maurya & Megasthenes", "No")
    add("History", "Ancient India", t, s, "Mauryan Empire: Chanakya's Arthashastra", "No")
    add("History", "Ancient India", t, s, "Mauryan Empire: Ashoka's Dhamma & Kalinga War", "No")
    add("History", "Ancient India", t, s, "Mauryan Empire: Ashoka's Rock & Pillar Edicts", "No")
    add("History", "Ancient India", t, s, "Post-Mauryan: Shungas & Satavahanas", "No")
    add("History", "Ancient India", t, s, "Post-Mauryan: Kushanas (Kanishka & Silk Route)", "No")

    s = "Gupta Empire & Harsha"
    add("History", "Ancient India", t, s, "Gupta Empire: Samudragupta (Napoleon of India)", "No")
    add("History", "Ancient India", t, s, "Gupta Empire: Chandragupta II & Navaratnas", "No")
    add("History", "Ancient India", t, s, "Gupta Period: Golden Age of Art & Literature", "No")
    add("History", "Ancient India", t, s, "Gupta Period: Science (Aryabhata, Varahamihira)", "No")
    add("History", "Ancient India", t, s, "Harshavardhana: Reign & Xuanzang's Visit", "No")

    # 1.2 Medieval Indian History
    t = "Medieval Indian History"
    s = "Delhi Sultanate"
    add("History", "Medieval India", t, s, "Slave Dynasty: Qutbuddin Aibak & Iltutmish", "No")
    add("History", "Medieval India", t, s, "Slave Dynasty: Razia Sultan & Balban (Blood & Iron)", "No")
    add("History", "Medieval India", t, s, "Khalji Dynasty: Alauddin's Market & Military Reforms", "No")
    add("History", "Medieval India", t, s, "Tughlaq Dynasty: Muhammad bin Tughlaq's Projects", "No")
    add("History", "Medieval India", t, s, "Tughlaq Dynasty: Firoz Shah Tughlaq's Public Works", "No")
    add("History", "Medieval India", t, s, "Sayyid & Lodi Dynasties", "No")
    
    s = "Mughal Empire"
    add("History", "Medieval India", t, s, "Babur & the First Battle of Panipat (1526)", "No")
    add("History", "Medieval India", t, s, "Humayun & Sher Shah Suri's Administration", "No")
    add("History", "Medieval India", t, s, "Akbar: Mansabdari System & Revenue Reforms", "No")
    add("History", "Medieval India", t, s, "Akbar: Din-i-Ilahi & Religious Tolerance", "No")
    add("History", "Medieval India", t, s, "Jahangir & Shah Jahan (Golden Age of Architecture)", "No")
    add("History", "Medieval India", t, s, "Aurangzeb & the Decline of the Mughal Empire", "No")
    
    s = "Maratha & Regional Powers"
    add("History", "Medieval India", t, s, "Rise of Marathas: Shivaji's Administration & Ashtapradhan", "No")
    add("History", "Medieval India", t, s, "Peshwas & Expansion of Maratha Power", "No")
    add("History", "Medieval India", t, s, "Vijayanagara Empire: Krishnadevaraya & Society", "No")

    s = "Bhakti & Sufi Movements"
    add("History", "Medieval India", t, s, "Bhakti Movement: Kabir, Nanak, Mirabai", "No")
    add("History", "Medieval India", t, s, "Bhakti Movement: Ramanuja & Shankaracharya", "No")
    add("History", "Medieval India", t, s, "Sufi Movement: Chishti & Suhrawardi Silsilas", "No")

    # 1.3 Modern Indian History
    t = "Modern Indian History"
    s = "Advent of Europeans"
    add("History", "Modern India", t, s, "Portuguese Establishments in India", "No")
    add("History", "Modern India", t, s, "Dutch & French Settlements (Carnatic Wars)", "No")
    add("History", "Modern India", t, s, "British East India Company Expansion", "No")
    add("History", "Modern India", t, s, "Battle of Plassey (1757) & Siraj-ud-Daulah", "No")
    add("History", "Modern India", t, s, "Battle of Buxar (1764) & Dual Government in Bengal", "No")

    s = "British Administrative & Economic Policies"
    add("History", "Modern India", t, s, "Land Revenue: Permanent Settlement (Zamindari)", "No")
    add("History", "Modern India", t, s, "Land Revenue: Ryotwari & Mahalwari Systems", "No")
    add("History", "Modern India", t, s, "Commercialization of Agriculture & Famines", "No")
    add("History", "Modern India", t, s, "Regulating Act 1773 & Pitt's India Act 1784", "No")
    add("History", "Modern India", t, s, "Charter Acts of 1813, 1833 & 1853", "No")
    add("History", "Modern India", t, s, "Educational Reforms (Macaulay's Minute, Wood's Despatch)", "No")

    s = "Socio-Religious Reforms & 1857 Revolt"
    add("History", "Modern India", t, s, "Raja Ram Mohan Roy & Brahmo Samaj", "No")
    add("History", "Modern India", t, s, "Swami Vivekananda & Ramakrishna Mission", "No")
    add("History", "Modern India", t, s, "Dayananda Saraswati & Arya Samaj", "No")
    add("History", "Modern India", t, s, "Revolt of 1857: Political & Economic Causes", "No")
    add("History", "Modern India", t, s, "Revolt of 1857: Key Centers & Leaders", "No")

    s = "Indian National Movement (1885-1947)"
    add("History", "Modern India", t, s, "Formation of INC (1885) & Moderate Phase", "No")
    add("History", "Modern India", t, s, "Extremist Phase & Partition of Bengal (1905)", "No")
    add("History", "Modern India", t, s, "Swadeshi & Boycott Movement", "No")
    add("History", "Modern India", t, s, "Surat Split (1907) & Morley-Minto Reforms (1909)", "No")
    add("History", "Modern India", t, s, "Home Rule Movement (Tilak & Annie Besant)", "No")
    add("History", "Modern India", t, s, "Gandhian Era: Champaran, Kheda, Ahmedabad", "No")
    add("History", "Modern India", t, s, "Rowlatt Act & Jallianwala Bagh Massacre (1919)", "No")
    add("History", "Modern India", t, s, "Non-Cooperation & Khilafat Movement", "No")
    add("History", "Modern India", t, s, "Simon Commission & Nehru Report", "No")
    add("History", "Modern India", t, s, "Civil Disobedience Movement & Dandi March (1930)", "No")
    add("History", "Modern India", t, s, "Round Table Conferences & Poona Pact", "No")
    add("History", "Modern India", t, s, "Government of India Act 1935", "No")
    add("History", "Modern India", t, s, "August Offer & Cripps Mission", "No")
    add("History", "Modern India", t, s, "Quit India Movement (1942)", "No")
    add("History", "Modern India", t, s, "Subhas Chandra Bose & Indian National Army (INA)", "No")
    add("History", "Modern India", t, s, "Cabinet Mission Plan & Partition of India (1947)", "No")

    # 1.4 Assam History - Ancient & Medieval
    t = "Ancient & Medieval Assam History"
    s = "Ancient Kamarupa"
    add("History", "Assam History", t, s, "Mythological Era: Danava Dynasty & Mahiranga Danava", "Yes")
    add("History", "Assam History", t, s, "Mythological Era: Narakasura & Bhagadatta (Mahabharata)", "Yes")
    add("History", "Assam History", t, s, "Varman Dynasty: Pushyavarman (Founder)", "Yes")
    add("History", "Assam History", t, s, "Varman Dynasty: Bhaskaravarman & Alliance with Harsha", "Yes")
    add("History", "Assam History", t, s, "Xuanzang's Visit to Kamarupa & Accounts", "Yes")
    add("History", "Assam History", t, s, "Mlechha Dynasty: Salasthambha", "Yes")
    add("History", "Assam History", t, s, "Pala Dynasty: Brahmapala to Dharmapala", "Yes")
    add("History", "Assam History", t, s, "Major Copper Plate Inscriptions of Kamarupa", "Yes")

    s = "The Ahom Kingdom (1228-1826)"
    add("History", "Assam History", t, s, "Chaolung Sukaphaa: Migration & Foundation (1228)", "Yes")
    add("History", "Assam History", t, s, "Establishment of the first capital at Charaideo", "Yes")
    add("History", "Assam History", t, s, "Ahom Administration: Paik System & Khels", "Yes")
    add("History", "Assam History", t, s, "Ahom Administration: Role of Burhagohain & Borgohain", "Yes")
    add("History", "Assam History", t, s, "Suhungmung (Dihingia Roja): Expansion & Consolidation", "Yes")
    add("History", "Assam History", t, s, "Pratap Singha: Creation of Borphukan & Borbarua posts", "Yes")
    add("History", "Assam History", t, s, "Rudra Singha (Kargoya Roja): Cultural & Economic Boom", "Yes")
    add("History", "Assam History", t, s, "Ahom-Mughal Conflicts: Mir Jumla's Invasion", "Yes")
    add("History", "Assam History", t, s, "Battle of Saraighat (1671): Lachit Borphukan's Valor", "Yes")
    add("History", "Assam History", t, s, "Battle of Itakhuli (1682): Final Expulsion of Mughals", "Yes")
    add("History", "Assam History", t, s, "Moamoria Rebellion: Causes & Socio-Political Impact", "Yes")
    add("History", "Assam History", t, s, "Moamoria Rebellion: Phases under Lakshmi Singha, Gaurinath Singha", "Yes")
    add("History", "Assam History", t, s, "Captain Welsh's Expedition to Assam", "Yes")

    s = "Other Contemporary Kingdoms in Assam"
    add("History", "Assam History", t, s, "Koch Kingdom: Biswa Singha & Consolidation", "Yes")
    add("History", "Assam History", t, s, "Koch Kingdom: Naranarayan & Chilarai's Military Campaigns", "Yes")
    add("History", "Assam History", t, s, "Kachari Kingdom: Capitals at Dimapur, Maibang, Khaspur", "Yes")
    add("History", "Assam History", t, s, "Chutiya Kingdom: Sadiya Khowa Gohain & Ahom Conquest", "Yes")

    # 1.5 Assam History - Modern & Freedom Struggle
    t = "Modern Assam History & Freedom Struggle"
    s = "British Annexation & Early Resistance"
    add("History", "Assam History", t, s, "Burmese Invasions (Manoranjan, Badan Chandra Borphukan)", "Yes")
    add("History", "Assam History", t, s, "Treaty of Yandaboo (1826) & British Administration begins", "Yes")
    add("History", "Assam History", t, s, "Revolt of Gomdhar Konwar (1828)", "Yes")
    add("History", "Assam History", t, s, "Piyoli Phukan & Jiuram Dulia Baruah's Rebellion", "Yes")
    add("History", "Assam History", t, s, "Assam in the Revolt of 1857: Role of Maniram Dewan", "Yes")

    s = "Peasant Uprisings in Assam"
    add("History", "Assam History", t, s, "Phulaguri Dhawa (1861): Causes & Impact", "Yes")
    add("History", "Assam History", t, s, "Patharughat Uprising (1894): The Peasant Massacre", "Yes")
    add("History", "Assam History", t, s, "Rangia & Lachima Revolts", "Yes")

    s = "Socio-Political Awakening & Organizations"
    add("History", "Assam History", t, s, "Role of Orunodoi (1846) in Assamese Awakening", "Yes")
    add("History", "Assam History", t, s, "Asamiya Bhasar Unnati Sadhini Sabha (1888)", "Yes")
    add("History", "Assam History", t, s, "Assam Association (1903) & Tarun Ram Phukan", "Yes")
    add("History", "Assam History", t, s, "Jorhat Sarbajanik Sabha (Jagannath Barooah)", "Yes")

    s = "Freedom Struggle in Assam"
    add("History", "Assam History", t, s, "Swadeshi Movement & its Impact on Assam", "Yes")
    add("History", "Assam History", t, s, "Formation of Assam Provincial Congress Committee", "Yes")
    add("History", "Assam History", t, s, "Non-Cooperation Movement in Assam", "Yes")
    add("History", "Assam History", t, s, "Civil Disobedience Movement & Cunningham Circular", "Yes")
    add("History", "Assam History", t, s, "Quit India Movement in Assam (1942)", "Yes")
    add("History", "Assam History", t, s, "Martyrdom of Kanaklata Barua & Mukunda Kakati", "Yes")
    add("History", "Assam History", t, s, "Martyrdom of Kushal Konwar (Only martyr hanged in 1942)", "Yes")
    add("History", "Assam History", t, s, "Cabinet Mission Plan & Grouping Clause resistance by Gopinath Bordoloi", "Yes")
    add("History", "Assam History", t, s, "Sylhet Referendum & Independence", "Yes")

    # 1.6 Assam Art & Culture
    t = "Art, Culture & Literature of Assam"
    s = "Neo-Vaishnavite Movement"
    add("History", "Assam Art & Culture", t, s, "Life & Works of Srimanta Sankardev", "Yes")
    add("History", "Assam Art & Culture", t, s, "Life & Works of Madhavdev", "Yes")
    add("History", "Assam Art & Culture", t, s, "Institution of Satras & Namghars (Majuli, Barpeta, Bardowa)", "Yes")
    add("History", "Assam Art & Culture", t, s, "Bargeet: Devotional Songs of Assam", "Yes")
    add("History", "Assam Art & Culture", t, s, "Ankiya Naat & Bhaona", "Yes")
    add("History", "Assam Art & Culture", t, s, "Satriya Dance (Recognition as Classical Dance)", "Yes")

    s = "Festivals, Folk Dance & Music"
    add("History", "Assam Art & Culture", t, s, "Bihu Festivals: Rongali (Bohag), Kongali (Kati), Bhogali (Magh)", "Yes")
    add("History", "Assam Art & Culture", t, s, "Ali-Aye-Ligang (Mising Spring Festival)", "Yes")
    add("History", "Assam Art & Culture", t, s, "Me-Dam-Me-Phi (Ahom Ancestor Worship)", "Yes")
    add("History", "Assam Art & Culture", t, s, "Bathou Puja & Bwisagu (Bodo Community)", "Yes")
    add("History", "Assam Art & Culture", t, s, "Rongker & Hacha-Kekan (Karbi Community)", "Yes")
    add("History", "Assam Art & Culture", t, s, "Ambubachi Mela at Kamakhya Temple", "Yes")
    add("History", "Assam Art & Culture", t, s, "Jonbeel Mela (Barter System tradition)", "Yes")
    add("History", "Assam Art & Culture", t, s, "Folk Dances: Bagurumba, Jhumur, Deodhani", "Yes")
    add("History", "Assam Art & Culture", t, s, "Folk Music: Goalparia Lokageet, Kamrupi Lokageet", "Yes")

    s = "Literature, Media & Personalities"
    add("History", "Assam Art & Culture", t, s, "Buranjis: Historical Chronicles of the Ahoms", "Yes")
    add("History", "Assam Art & Culture", t, s, "Jonaki Era: Romanticism in Assamese Literature", "Yes")
    add("History", "Assam Art & Culture", t, s, "Lakshminath Bezbaroa (Rasaraj) & Hemchandra Barua", "Yes")
    add("History", "Assam Art & Culture", t, s, "Asam Sahitya Sabha: Establishment & Role", "Yes")
    add("History", "Assam Art & Culture", t, s, "Birendra Kumar Bhattacharya & Mamoni Raisom Goswami (Jnanpith Winners)", "Yes")
    add("History", "Assam Art & Culture", t, s, "Nilmani Phookan (Jnanpith Winner)", "Yes")
    add("History", "Assam Art & Culture", t, s, "Jyoti Prasad Agarwala & Joymoti (First Assamese Film, 1935)", "Yes")
    add("History", "Assam Art & Culture", t, s, "Bishnu Prasad Rabha (Kalaguru)", "Yes")
    add("History", "Assam Art & Culture", t, s, "Bhupen Hazarika (Sudhakantha & Bharat Ratna)", "Yes")
    add("History", "Assam Art & Culture", t, s, "Traditional Attire: Mekhela Sador, Gamosa, Muga Silk", "Yes")
    add("History", "Assam Art & Culture", t, s, "Traditional Crafts: Bell Metal of Sarthebari, Bamboo & Cane", "Yes")

    # ==========================================
    # 2. GEOGRAPHY DOMAIN
    # ==========================================
    
    # 2.1 World & Physical Geography
    t = "Physical & World Geography"
    s = "Geomorphology & Earth System"
    add("Geography", "Physical Geography", t, s, "Solar System: Planets, Asteroids, Meteors", "No")
    add("Geography", "Physical Geography", t, s, "Earth's Motions: Rotation, Revolution, Seasons", "No")
    add("Geography", "Physical Geography", t, s, "Latitudes, Longitudes, Standard Time, IDL", "No")
    add("Geography", "Physical Geography", t, s, "Earth's Interior: Crust, Mantle, Core", "No")
    add("Geography", "Physical Geography", t, s, "Plate Tectonics, Continental Drift Theory", "No")
    add("Geography", "Physical Geography", t, s, "Earthquakes & Volcanism", "No")
    
    s = "Climatology & Oceanography"
    add("Geography", "Physical Geography", t, s, "Atmosphere: Composition & Layers (Troposphere to Exosphere)", "No")
    add("Geography", "Physical Geography", t, s, "Pressure Belts & Wind Systems (Trade, Westerlies)", "No")
    add("Geography", "Physical Geography", t, s, "Cyclones, Anticyclones & Monsoons", "No")
    add("Geography", "Physical Geography", t, s, "Ocean Bottom Relief (Continental Shelf, Trench)", "No")
    add("Geography", "Physical Geography", t, s, "Ocean Currents (Warm vs Cold, El Nino, La Nina)", "No")
    add("Geography", "Physical Geography", t, s, "Tides & Coral Reefs", "No")
    
    # 2.2 Indian Geography
    t = "Geography of India"
    s = "Physiography of India"
    add("Geography", "Indian Geography", t, s, "The Great Himalayas (Ranges, Peaks, Glaciers, Passes)", "No")
    add("Geography", "Indian Geography", t, s, "The Northern Plains & Bhabar, Terai, Khadar, Bhangar", "No")
    add("Geography", "Indian Geography", t, s, "The Peninsular Plateau (Western & Eastern Ghats)", "No")
    add("Geography", "Indian Geography", t, s, "The Coastal Plains & Islands (Andaman, Lakshadweep)", "No")
    
    s = "Indian Climate, Drainage & Soils"
    add("Geography", "Indian Geography", t, s, "Indian Monsoon Mechanism & Seasonal Variations", "No")
    add("Geography", "Indian Geography", t, s, "Himalayan Drainage System (Ganga, Indus, Brahmaputra)", "No")
    add("Geography", "Indian Geography", t, s, "Peninsular Drainage System (Godavari, Krishna, Narmada, Tapi)", "No")
    add("Geography", "Indian Geography", t, s, "Major Soil Types (Alluvial, Black, Red, Laterite, Desert)", "No")
    add("Geography", "Indian Geography", t, s, "Natural Vegetation & Forest Cover in India", "No")
    
    s = "Economic & Human Geography of India"
    add("Geography", "Indian Geography", t, s, "Major Crops & Agricultural Patterns (Kharif, Rabi)", "No")
    add("Geography", "Indian Geography", t, s, "Mineral Resources (Iron, Coal, Bauxite, Petroleum)", "No")
    add("Geography", "Indian Geography", t, s, "Major Industries (Iron & Steel, Textiles)", "No")
    add("Geography", "Indian Geography", t, s, "Transportation (Railways, NHAI, Ports, Airports)", "No")
    add("Geography", "Indian Geography", t, s, "Demographics: Census Data (Literacy, Sex Ratio, Density)", "No")
    
    # 2.3 Geography of Assam
    t = "Geography of Assam"
    s = "Physiographic Divisions of Assam"
    add("Geography", "Assam Geography", t, s, "Brahmaputra Valley: Characteristics & Floodplains", "Yes")
    add("Geography", "Assam Geography", t, s, "Barak Valley: Surma River System & Plains", "Yes")
    add("Geography", "Assam Geography", t, s, "Karbi Anglong Plateau: Geological Origins", "Yes")
    add("Geography", "Assam Geography", t, s, "Barail Range & Southern Hills", "Yes")
    
    s = "Climate, Soils & Water Resources of Assam"
    add("Geography", "Assam Geography", t, s, "Monsoon Climate in Assam & Pre-monsoon showers (Bordoisila)", "Yes")
    add("Geography", "Assam Geography", t, s, "Soil Types in Assam (Alluvial, Laterite, Red, Sandy)", "Yes")
    add("Geography", "Assam Geography", t, s, "Brahmaputra River System: North & South Bank Tributaries", "Yes")
    add("Geography", "Assam Geography", t, s, "Majuli River Island: Formation, Erosion & Fluvial Dynamics", "Yes")
    add("Geography", "Assam Geography", t, s, "Wetlands (Beels): Deepor Beel (Ramsar Site), Son Beel", "Yes")
    add("Geography", "Assam Geography", t, s, "Flood Disaster Management in Assam", "Yes")
    
    s = "Biodiversity, Flora & Fauna of Assam"
    add("Geography", "Assam Geography", t, s, "Kaziranga National Park (One-Horned Rhino, World Heritage)", "Yes")
    add("Geography", "Assam Geography", t, s, "Manas National Park (Biosphere Reserve, Tiger Project, Pygmy Hog)", "Yes")
    add("Geography", "Assam Geography", t, s, "Nameri National Park & Orang National Park (Mini Kaziranga)", "Yes")
    add("Geography", "Assam Geography", t, s, "Dibru-Saikhowa National Park (Feral Horses)", "Yes")
    add("Geography", "Assam Geography", t, s, "Raimona National Park (Golden Langur)", "Yes")
    add("Geography", "Assam Geography", t, s, "Dihing Patkai National Park (Amazon of the East)", "Yes")
    add("Geography", "Assam Geography", t, s, "Major Wildlife Sanctuaries (Pobitora, Gibbon, Garampani, Bura Chapori)", "Yes")
    add("Geography", "Assam Geography", t, s, "State Symbols (State Tree, Bird, Flower, Animal)", "Yes")
    
    s = "Demographics & Resources of Assam"
    add("Geography", "Assam Geography", t, s, "Population Distribution, Density & Growth Trends", "Yes")
    add("Geography", "Assam Geography", t, s, "Tribal Demography: Plains Tribes (Bodo, Mising) vs Hills Tribes (Karbi, Dimasa)", "Yes")
    add("Geography", "Assam Geography", t, s, "Mineral Resources: Petroleum (Digboi, Naharkatia)", "Yes")
    add("Geography", "Assam Geography", t, s, "Mineral Resources: Coal (Margherita), Limestone, Sillimanite", "Yes")
    add("Geography", "Assam Geography", t, s, "Transport: National Waterways (NW-2 Brahmaputra, NW-16 Barak)", "Yes")
    add("Geography", "Assam Geography", t, s, "Transport: Major Bridges over Brahmaputra (Bogibeel, Bhupen Hazarika Setu, Saraighat)", "Yes")

    # ==========================================
    # 3. POLITY DOMAIN
    # ==========================================
    
    # 3.1 Indian Constitution
    t = "Indian Constitution & Governance"
    s = "Constitutional Framework"
    add("Polity", "Indian Polity", t, s, "Constituent Assembly & Making of the Constitution", "No")
    add("Polity", "Indian Polity", t, s, "Salient Features & Sources of the Constitution", "No")
    add("Polity", "Indian Polity", t, s, "The Preamble & Basic Structure Doctrine (Kesavananda Bharati Case)", "No")
    add("Polity", "Indian Polity", t, s, "Union & Its Territories (Article 1-4)", "No")
    add("Polity", "Indian Polity", t, s, "Citizenship (CAA & Article 5-11)", "No")
    
    s = "Fundamental Rights, DPSP & Duties"
    add("Polity", "Indian Polity", t, s, "Fundamental Rights (Art 14-18): Right to Equality", "No")
    add("Polity", "Indian Polity", t, s, "Fundamental Rights (Art 19-22): Right to Freedom", "No")
    add("Polity", "Indian Polity", t, s, "Fundamental Rights (Art 23-24): Against Exploitation", "No")
    add("Polity", "Indian Polity", t, s, "Fundamental Rights (Art 25-28): Freedom of Religion", "No")
    add("Polity", "Indian Polity", t, s, "Fundamental Rights (Art 32): Constitutional Remedies & Writs", "No")
    add("Polity", "Indian Polity", t, s, "Directive Principles of State Policy (DPSP) (Art 36-51)", "No")
    add("Polity", "Indian Polity", t, s, "Fundamental Duties (Art 51A & Swaran Singh Committee)", "No")
    
    s = "Union & State Government"
    add("Polity", "Indian Polity", t, s, "Union Executive: President, Vice-President, PM", "No")
    add("Polity", "Indian Polity", t, s, "Council of Ministers & Cabinet Committees", "No")
    add("Polity", "Indian Polity", t, s, "Union Legislature: Lok Sabha & Rajya Sabha", "No")
    add("Polity", "Indian Polity", t, s, "Parliamentary Proceedings (Bills, Sessions, Budget Process)", "No")
    add("Polity", "Indian Polity", t, s, "State Executive: Governor, Chief Minister", "No")
    add("Polity", "Indian Polity", t, s, "State Legislature: Assembly & Council", "No")
    
    s = "Judiciary, Local Govt & Bodies"
    add("Polity", "Indian Polity", t, s, "Supreme Court (Jurisdiction & Judicial Review)", "No")
    add("Polity", "Indian Polity", t, s, "High Courts & Subordinate Courts", "No")
    add("Polity", "Indian Polity", t, s, "Panchayati Raj (73rd Amendment & Balwant Rai Mehta Comm.)", "No")
    add("Polity", "Indian Polity", t, s, "Municipalities (74th Amendment)", "No")
    add("Polity", "Indian Polity", t, s, "Constitutional Bodies (ECI, UPSC, Finance Commission, CAG, AGI)", "No")
    add("Polity", "Indian Polity", t, s, "Statutory Bodies (NHRC, NITI Aayog, CVC, CIC)", "No")
    add("Polity", "Indian Polity", t, s, "Emergency Provisions (National, State, Financial)", "No")
    add("Polity", "Indian Polity", t, s, "Major Amendments (42nd, 44th, 86th, 101st GST, 106th Women's Bill)", "No")
    
    # 3.2 Polity of Assam
    t = "Governance & Polity of Assam"
    s = "Sixth Schedule & Autonomous Councils"
    add("Polity", "Assam Polity", t, s, "Concept & Administration of Sixth Schedule Areas", "Yes")
    add("Polity", "Assam Polity", t, s, "Bodoland Territorial Region (BTR) Framework", "Yes")
    add("Polity", "Assam Polity", t, s, "Karbi Anglong Autonomous Council (KAAC)", "Yes")
    add("Polity", "Assam Polity", t, s, "North Cachar Hills Autonomous Council (NCHAC)", "Yes")
    
    s = "Statutory Councils & Decentralization"
    add("Polity", "Assam Polity", t, s, "Statutory Councils (Mising, Rabha, Tiwa, Deori, Thengal Kachari)", "Yes")
    add("Polity", "Assam Polity", t, s, "Assam Panchayat Act, 1994 (3-Tier System in Assam)", "Yes")
    add("Polity", "Assam Polity", t, s, "GMC (Guwahati Municipal Corporation) & Urban Bodies", "Yes")
    add("Polity", "Assam Polity", t, s, "Inner Line Permit (ILP) concepts in NE & Assam Accord (1985)", "Yes")
    
    s = "State Schemes & Public Policy"
    add("Polity", "Assam Polity", t, s, "Orunodoi Scheme (Women Empowerment & DBT)", "Yes")
    add("Polity", "Assam Polity", t, s, "Mission Basundhara (Land Rights & Records modernization)", "Yes")
    add("Polity", "Assam Polity", t, s, "Ayushman Asom & Chief Minister's Arogya Yojana", "Yes")
    add("Polity", "Assam Polity", t, s, "Chief Minister's Samagra Gramya Unnayan Yojana (CMSGUY)", "Yes")
    add("Polity", "Assam Polity", t, s, "Mission Bhumiputra (Caste Certificates)", "Yes")
    add("Polity", "Assam Polity", t, s, "Swanirbhar Naari (Handloom weavers support)", "Yes")

    # ==========================================
    # 4. ECONOMY DOMAIN
    # ==========================================
    
    # 4.1 Indian Economy
    t = "Indian Economy & Macro Fundamentals"
    s = "National Income, Planning & Infrastructure"
    add("Economy", "Indian Economy", t, s, "Macroeconomic aggregates: GDP, GNP, NNP, Per Capita Income", "No")
    add("Economy", "Indian Economy", t, s, "Economic Planning: Five Year Plans & Objectives", "No")
    add("Economy", "Indian Economy", t, s, "Economic Reforms of 1991 (LPG: Liberalization, Privatization, Globalization)", "No")
    add("Economy", "Indian Economy", t, s, "NITI Aayog Structure, Functions & Indices", "No")
    add("Economy", "Indian Economy", t, s, "Poverty Estimation Committees (Tendulkar, Rangarajan)", "No")
    add("Economy", "Indian Economy", t, s, "Unemployment Types (Disguised, Structural, Frictional)", "No")
    
    s = "Banking, Finance & Monetary Policy"
    add("Economy", "Indian Economy", t, s, "Reserve Bank of India (RBI): Functions & Nationalization", "No")
    add("Economy", "Indian Economy", t, s, "Monetary Policy: Repo, Reverse Repo, CRR, SLR, OMO", "No")
    add("Economy", "Indian Economy", t, s, "Inflation: Types & Measurement (CPI, WPI)", "No")
    add("Economy", "Indian Economy", t, s, "Commercial Banking, BASEL Norms & Non-Performing Assets (NPAs)", "No")
    add("Economy", "Indian Economy", t, s, "Financial Markets: Money Market vs Capital Market (SEBI)", "No")
    
    s = "Fiscal Policy & Trade"
    add("Economy", "Indian Economy", t, s, "Union Budget Framework & Fiscal Deficit", "No")
    add("Economy", "Indian Economy", t, s, "Taxation System: Direct vs Indirect Taxes", "No")
    add("Economy", "Indian Economy", t, s, "Goods & Services Tax (GST) Framework & Slabs", "No")
    add("Economy", "Indian Economy", t, s, "Balance of Payments (BoP) & Forex Reserves", "No")
    add("Economy", "Indian Economy", t, s, "Foreign Trade Policy & FDI vs FPI", "No")
    
    # 4.2 Economy of Assam
    t = "Economy of Assam"
    s = "Agriculture & Allied Sectors in Assam"
    add("Economy", "Assam Economy", t, s, "Role of Agriculture & Allied sectors in Assam's SGDP", "Yes")
    add("Economy", "Assam Economy", t, s, "Assam Tea Industry: History, Auctions, Export & Challenges", "Yes")
    add("Economy", "Assam Economy", t, s, "Sericulture in Assam: Muga (GI Tag), Eri, Pat Silk", "Yes")
    add("Economy", "Assam Economy", t, s, "Horticulture, Floriculture & Fishery Development", "Yes")
    
    s = "Industry, Infrastructure & Finance"
    add("Economy", "Assam Economy", t, s, "Oil & Gas Refineries: Digboi, Guwahati, Bongaigaon, Numaligarh", "Yes")
    add("Economy", "Assam Economy", t, s, "Handloom & Handicrafts Sector (Sualkuchi - Manchester of East)", "Yes")
    add("Economy", "Assam Economy", t, s, "Tourism Sector: Wildlife, Eco-tourism, Heritage & River Tourism", "Yes")
    add("Economy", "Assam Economy", t, s, "MSME Sector in Assam & Industrial Policy", "Yes")
    add("Economy", "Assam Economy", t, s, "Assam State Budget Highlights & Fiscal Allocations", "Yes")
    add("Economy", "Assam Economy", t, s, "Revenue Sources & State GST Collections", "Yes")
    add("Economy", "Assam Economy", t, s, "Act East Policy & Assam's strategic economic role", "Yes")

    # ==========================================
    # 5. GENERAL AWARENESS & SCIENCE
    # ==========================================
    
    # 5.1 General Science
    t = "General Science"
    s = "Physics"
    add("General Awareness", "Science", t, s, "Units & Dimensions, SI Units", "No")
    add("General Awareness", "Science", t, s, "Laws of Motion, Friction, Gravitation", "No")
    add("General Awareness", "Science", t, s, "Work, Energy & Power", "No")
    add("General Awareness", "Science", t, s, "Properties of Matter (Surface Tension, Viscosity, Archimedes Principle)", "No")
    add("General Awareness", "Science", t, s, "Light & Optics (Reflection, Refraction, TIR, Lenses)", "No")
    add("General Awareness", "Science", t, s, "Sound Waves, Ultrasound & Doppler Effect", "No")
    add("General Awareness", "Science", t, s, "Electricity Basics, Ohm's Law, Magnets", "No")
    
    s = "Chemistry"
    add("General Awareness", "Science", t, s, "Atomic Structure, Isotopes, Isobars", "No")
    add("General Awareness", "Science", t, s, "Elements, Compounds & Mixtures", "No")
    add("General Awareness", "Science", t, s, "Acids, Bases & Salts (pH Scale, Indicators)", "No")
    add("General Awareness", "Science", t, s, "Metals, Non-Metals, Ores & Alloys", "No")
    add("General Awareness", "Science", t, s, "Carbon & its Compounds (Allotropes, Hydrocarbons)", "No")
    add("General Awareness", "Science", t, s, "Common Chemical Names (Baking Soda, Bleaching Powder, Plaster of Paris)", "No")
    
    s = "Biology"
    add("General Awareness", "Science", t, s, "Cell Biology (Structure, Organelles, DNA/RNA)", "No")
    add("General Awareness", "Science", t, s, "Human Digestive & Respiratory Systems", "No")
    add("General Awareness", "Science", t, s, "Human Circulatory System (Blood Groups, Heart)", "No")
    add("General Awareness", "Science", t, s, "Human Nervous System & Endocrine Glands", "No")
    add("General Awareness", "Science", t, s, "Vitamins, Minerals & Deficiency Diseases", "No")
    add("General Awareness", "Science", t, s, "Communicable & Non-Communicable Diseases (Pathogens)", "No")
    add("General Awareness", "Science", t, s, "Plant Biology (Photosynthesis, Transpiration, Hormones)", "No")
    
    # 5.2 Environment & Technology
    t = "Environment & Technology"
    s = "Environmental Ecology"
    add("General Awareness", "Environment", t, s, "Ecosystem Concepts, Food Chains & Webs", "No")
    add("General Awareness", "Environment", t, s, "Greenhouse Effect, Global Warming & Climate Change", "No")
    add("General Awareness", "Environment", t, s, "Ozone Layer Depletion & Acid Rain", "No")
    add("General Awareness", "Environment", t, s, "Biodiversity Conservation (In-situ vs Ex-situ, Red Data Book)", "No")
    add("General Awareness", "Environment", t, s, "Major Environmental Protocols (Kyoto, Montreal, Paris Agreement)", "No")
    add("General Awareness", "Environment", t, s, "Pollution Types (Air, Water, Soil, E-Waste)", "No")
    
    s = "Science & Technology"
    add("General Awareness", "Sci & Tech", t, s, "ISRO Space Missions (Chandrayaan-3, Aditya L1, Gaganyaan, Mangalyaan)", "No")
    add("General Awareness", "Sci & Tech", t, s, "Defense Technology (Agni, BrahMos, DRDO Achievements)", "No")
    add("General Awareness", "Sci & Tech", t, s, "IT & Emerging Tech (AI, Machine Learning, Blockchain Basics)", "No")
    add("General Awareness", "Sci & Tech", t, s, "Biotechnology (GMOs, CRISPR, Vaccines)", "No")
    
    # 5.3 Static GK & Current Affairs
    t = "Static GK & Current Events"
    s = "Static General Knowledge"
    add("General Awareness", "Static GK", t, s, "First in India (Men & Women in Various Fields)", "No")
    add("General Awareness", "Static GK", t, s, "Superlatives (Longest, Largest, Highest in India & World)", "No")
    add("General Awareness", "Static GK", t, s, "International Organizations & HQs (UN, WHO, WTO, IMF, World Bank)", "No")
    add("General Awareness", "Static GK", t, s, "Major Awards (Nobel, Bharat Ratna, Padma Awards, Jnanpith, Khel Ratna)", "No")
    add("General Awareness", "Static GK", t, s, "Important National & International Days (e.g. Yoga Day, Earth Day)", "No")
    add("General Awareness", "Static GK", t, s, "Classical & Folk Dances of India", "No")
    add("General Awareness", "Static GK", t, s, "Important Monuments & UNESCO World Heritage Sites in India", "No")
    
    s = "Current Affairs"
    add("General Awareness", "Current Affairs", t, s, "National Summits, Bills & Key Appointments of the Year", "No")
    add("General Awareness", "Current Affairs", t, s, "International Events, Bilateral Summits (G20, BRICS, SCO)", "No")
    add("General Awareness", "Current Affairs", t, s, "Sports Tournaments (Olympics, Asian Games, World Cups, Grand Slams)", "No")
    add("General Awareness", "Current Affairs", t, s, "Recent Space Launches & Technological Milestones", "No")
    add("General Awareness", "Current Affairs", t, s, "Assam Specific Current Events, State Awards (Asom Baibhav), Appts", "Yes")

    # 5.4 Computer Fundamentals
    t = "Computer Fundamentals & Applications"
    s = "Hardware & Software"
    add("General Awareness", "Computers", t, s, "Generations of Computers & Architecture (Von Neumann)", "No")
    add("General Awareness", "Computers", t, s, "CPU, ALU, CU & Registers", "No")
    add("General Awareness", "Computers", t, s, "Input & Output Devices", "No")
    add("General Awareness", "Computers", t, s, "Memory Hierarchy (RAM, ROM, Cache, Secondary Storage)", "No")
    add("General Awareness", "Computers", t, s, "System Software (Operating Systems) vs Application Software", "No")
    add("General Awareness", "Computers", t, s, "Open Source vs Proprietary Software", "No")
    
    s = "Office Productivity & Internet"
    add("General Awareness", "Computers", t, s, "MS Word (Formatting, Mail Merge, Shortcuts)", "No")
    add("General Awareness", "Computers", t, s, "MS Excel (Formulas, Functions, Cell Referencing, Charts)", "No")
    add("General Awareness", "Computers", t, s, "MS PowerPoint (Slides, Transitions, Animations)", "No")
    add("General Awareness", "Computers", t, s, "Common Keyboard Shortcuts", "No")
    add("General Awareness", "Computers", t, s, "Internet Basics (TCP/IP, HTTP, DNS, Web Browsers, Search Engines)", "No")
    add("General Awareness", "Computers", t, s, "Network Topologies (Star, Bus, Ring, Mesh)", "No")
    add("General Awareness", "Computers", t, s, "Cyber Security (Viruses, Malware, Phishing, Firewalls, Antivirus)", "No")

    # ==========================================
    # 6. APTITUDE & REASONING
    # ==========================================
    
    # 6.1 Quantitative Aptitude
    t = "Quantitative Aptitude (Numeracy)"
    s = "Number System & Arithmetic"
    add("Aptitude", "Mathematics", t, s, "Number System (Fractions, Decimals, Divisibility Rules, Unit Digit)", "No")
    add("Aptitude", "Mathematics", t, s, "HCF & LCM", "No")
    add("Aptitude", "Mathematics", t, s, "Simplification & BODMAS Rule", "No")
    add("Aptitude", "Mathematics", t, s, "Percentage Basics & Applications", "No")
    add("Aptitude", "Mathematics", t, s, "Profit & Loss, Discount, Successive Discount", "No")
    add("Aptitude", "Mathematics", t, s, "Ratio & Proportion, Partnership", "No")
    add("Aptitude", "Mathematics", t, s, "Simple Interest & Compound Interest", "No")
    add("Aptitude", "Mathematics", t, s, "Average, Problems on Ages", "No")
    
    s = "Speed, Time & Advanced Math"
    add("Aptitude", "Mathematics", t, s, "Time & Work, Pipes & Cisterns", "No")
    add("Aptitude", "Mathematics", t, s, "Time, Speed & Distance, Problems on Trains", "No")
    add("Aptitude", "Mathematics", t, s, "Boats & Streams", "No")
    add("Aptitude", "Mathematics", t, s, "Mensuration (Area & Perimeter of 2D shapes: Circles, Triangles, Quads)", "No")
    add("Aptitude", "Mathematics", t, s, "Mensuration (Volume & Surface Area of 3D shapes: Cubes, Cylinders, Spheres)", "No")
    add("Aptitude", "Mathematics", t, s, "Basic Algebra (Polynomials, Linear Equations, Identities)", "No")
    add("Aptitude", "Mathematics", t, s, "Probability & Combinatorics Basics", "No")
    add("Aptitude", "Mathematics", t, s, "Data Interpretation (Bar Graphs, Pie Charts, Line Graphs)", "No")
    
    # 6.2 Logical Reasoning
    t = "Logical & Analytical Reasoning"
    s = "Verbal & Analytical Reasoning"
    add("Aptitude", "Reasoning", t, s, "Coding & Decoding (Letter, Number, Substitution)", "No")
    add("Aptitude", "Reasoning", t, s, "Blood Relations (Family Tree & Pointing format)", "No")
    add("Aptitude", "Reasoning", t, s, "Direction Sense Test (Angles & Shadows)", "No")
    add("Aptitude", "Reasoning", t, s, "Number, Alphabet & Alphanumeric Series", "No")
    add("Aptitude", "Reasoning", t, s, "Analogy & Classification (Odd One Out)", "No")
    add("Aptitude", "Reasoning", t, s, "Syllogism (Logical Deduction using Venn Diagrams)", "No")
    add("Aptitude", "Reasoning", t, s, "Venn Diagrams (Logical relationships)", "No")
    add("Aptitude", "Reasoning", t, s, "Seating Arrangement (Circular, Linear, Square)", "No")
    add("Aptitude", "Reasoning", t, s, "Puzzles (Floor, Scheduling, Tabular)", "No")
    add("Aptitude", "Reasoning", t, s, "Clock & Calendar Problems", "No")
    add("Aptitude", "Reasoning", t, s, "Ranking & Order Test", "No")
    add("Aptitude", "Reasoning", t, s, "Mathematical Operations & Inequality", "No")
    
    s = "Non-Verbal Reasoning"
    add("Aptitude", "Reasoning", t, s, "Mirror & Water Images", "No")
    add("Aptitude", "Reasoning", t, s, "Paper Folding & Cutting", "No")
    add("Aptitude", "Reasoning", t, s, "Figure Matrix & Completion of Figure", "No")
    add("Aptitude", "Reasoning", t, s, "Embedded Figures & Counting of Figures", "No")

    # ==========================================
    # 7. ENGLISH DOMAIN
    # ==========================================
    
    # 7.1 General English
    t = "General English"
    s = "Grammar & Usage"
    add("English", "Grammar", t, s, "Parts of Speech (Nouns, Pronouns, Adjectives, Adverbs, Conjunctions)", "No")
    add("English", "Grammar", t, s, "Subject-Verb Agreement Rules", "No")
    add("English", "Grammar", t, s, "Tenses & Sequence of Tenses", "No")
    add("English", "Grammar", t, s, "Articles (A, An, The) & Determiners", "No")
    add("English", "Grammar", t, s, "Prepositions & Appropriate Prepositions (Fixed prepositions)", "No")
    add("English", "Grammar", t, s, "Active & Passive Voice Rules & Conversion", "No")
    add("English", "Grammar", t, s, "Direct & Indirect Speech (Narration Conversion)", "No")
    add("English", "Grammar", t, s, "Error Spotting (Grammatical Error Detection)", "No")
    add("English", "Grammar", t, s, "Sentence Improvement & Correction", "No")
    
    s = "Vocabulary & Comprehension"
    add("English", "Vocabulary", t, s, "Synonyms & Antonyms", "No")
    add("English", "Vocabulary", t, s, "Idioms & Phrases Meanings", "No")
    add("English", "Vocabulary", t, s, "One Word Substitution", "No")
    add("English", "Vocabulary", t, s, "Spelling Errors (Correctly/Incorrectly spelt words)", "No")
    add("English", "Vocabulary", t, s, "Phrasal Verbs", "No")
    add("English", "Vocabulary", t, s, "Cloze Test (Fill in the blanks in a passage)", "No")
    add("English", "Vocabulary", t, s, "Fill in the Blanks (Single/Double fillers)", "No")
    add("English", "Reading", t, s, "Reading Comprehension (Passage Analysis, Tone, Inference)", "No")
    add("English", "Reading", t, s, "Sentence Rearrangement (Para Jumbles)", "No")

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
        "Assam_Specific"
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

    print(f"Generated Deep Checklist CSV: {csv_path} ({len(rows)} atomic checklist rows)")
    print(f"Generated Deep Checklist JSON: {json_path}")

if __name__ == "__main__":
    generate_checklist()
