import os
import json

def update_metadata():
    catalog = {
        "project": "Assam Government Examinations - Comprehensive Syllabi & Schemes Catalog",
        "last_updated": "2026-10-01",
        "total_categories": 12,
        "categories": [
            {
                "id": "01_APSC",
                "name": "Assam Public Service Commission (APSC)",
                "official_website": "https://apsc.nic.in",
                "exams": [
                    {
                        "name": "Combined Competitive Examination (CCE)",
                        "posts": "ACS (Jr. Grade), APS (Jr. Grade), Assam Taxation Service, Assam Finance Service, DTO, Labour Officer, ARCS, BDO, Sub-Registrar",
                        "folder": "01_APSC/CCE_Prelims_Mains",
                        "syllabus_file": "01_APSC/CCE_Prelims_Mains/SYLLABUS.md",
                        "pattern_file": "01_APSC/CCE_Prelims_Mains/EXAM_PATTERN.md",
                        "qualification": "Graduate / Bachelor's Degree"
                    },
                    {
                        "name": "Assistant Engineer (AE) & Junior Engineer (JE)",
                        "posts": "AE & JE in PWD (Roads & Building), Water Resources, PHE, Irrigation, Housing & Urban Affairs",
                        "folder": "01_APSC/AE_JE_Engineering",
                        "syllabus_file": "01_APSC/AE_JE_Engineering/SYLLABUS.md",
                        "pattern_file": "01_APSC/AE_JE_Engineering/EXAM_PATTERN.md",
                        "qualification": "B.E./B.Tech (AE) or 3-Year Diploma (JE) in Civil/Mechanical/Electrical/Chemical"
                    },
                    {
                        "name": "Forest Ranger & Assam Forest Service (AFS)",
                        "posts": "Forest Ranger, Assistant Conservator of Forests (AFS)",
                        "folder": "01_APSC/Forestry_Services",
                        "syllabus_file": "01_APSC/Forestry_Services/SYLLABUS.md",
                        "pattern_file": "01_APSC/Forestry_Services/EXAM_PATTERN.md",
                        "qualification": "Bachelor's Degree in Science or Engineering"
                    },
                    {
                        "name": "Medical, Food Safety & Drug Administration",
                        "posts": "Medical Officer (Ayurvedic/Homeopathic/Allopathic), Food Safety Officer (FSO), Drug Inspector (DI)",
                        "folder": "01_APSC/Medical_Food_Drug_Services",
                        "syllabus_file": "01_APSC/Medical_Food_Drug_Services/SYLLABUS.md",
                        "pattern_file": "01_APSC/Medical_Food_Drug_Services/EXAM_PATTERN.md",
                        "qualification": "MBBS / BAMS / BHMS / B.Pharm / B.Tech Food Tech / M.Sc Chemistry"
                    },
                    {
                        "name": "Agriculture, Veterinary & Fishery Services",
                        "posts": "Agricultural Development Officer (ADO), Veterinary Officer (VO/BVO), Fishery Development Officer (FDO), Soil Conservation Officer",
                        "folder": "01_APSC/Agriculture_Veterinary_Fishery",
                        "syllabus_file": "01_APSC/Agriculture_Veterinary_Fishery/SYLLABUS.md",
                        "pattern_file": "01_APSC/Agriculture_Veterinary_Fishery/EXAM_PATTERN.md",
                        "qualification": "B.Sc (Agri) / B.V.Sc & AH / B.F.Sc"
                    },
                    {
                        "name": "Technical Faculty (Polytechnics & Engineering Colleges)",
                        "posts": "Lecturer in Polytechnics, Assistant Professor in Govt Engineering Colleges (AEC, JEC, etc.), ITI Foreman",
                        "folder": "01_APSC/Lecturer_Assistant_Professor_Poly_Engg",
                        "syllabus_file": "01_APSC/Lecturer_Assistant_Professor_Poly_Engg/SYLLABUS.md",
                        "pattern_file": "01_APSC/Lecturer_Assistant_Professor_Poly_Engg/EXAM_PATTERN.md",
                        "qualification": "B.E./B.Tech (1st Class) / M.Tech / Ph.D"
                    },
                    {
                        "name": "Specialized Inspector Cadres & Research Assistant",
                        "posts": "Inspector of Legal Metrology, Factory Inspector, Motor Vehicle Inspector (MVI), Labour Inspector, Research Assistant (Planning)",
                        "folder": "01_APSC/Specialized_Inspectors_Legal_MVI_Factories",
                        "syllabus_file": "01_APSC/Specialized_Inspectors_Legal_MVI_Factories/SYLLABUS.md",
                        "pattern_file": "01_APSC/Specialized_Inspectors_Legal_MVI_Factories/EXAM_PATTERN.md",
                        "qualification": "Degree in Science/Engg/Law/Economics/Statistics"
                    }
                ]
            },
            {
                "id": "02_ADRE_SLRC",
                "name": "Assam Direct Recruitment Commission (ADRE - SLRC / ASSEB)",
                "official_website": "https://assam.gov.in",
                "exams": [
                    {
                        "name": "Grade III (Graduate / Bachelor Degree Level)",
                        "posts": "Junior Assistant, Field Assistant, LDA, Computer Operator, Statistical Assistant, Sub-Inspector of Statistics, Tax Collector, Village Executive",
                        "folder": "02_ADRE_SLRC/Grade_III_Graduate",
                        "syllabus_file": "02_ADRE_SLRC/Grade_III_Graduate/SYLLABUS.md",
                        "pattern_file": "02_ADRE_SLRC/Grade_III_Graduate/EXAM_PATTERN.md",
                        "qualification": "Bachelor's Degree + Computer Diploma / Certificate"
                    },
                    {
                        "name": "Grade III (Higher Secondary 10+2 Level)",
                        "posts": "Data Entry Operator (DEO), Junior Assistant (HS level), Typist, Laboratory Assistant, Section Assistant, Agril Demonstrator",
                        "folder": "02_ADRE_SLRC/Grade_III_HS_Level",
                        "syllabus_file": "02_ADRE_SLRC/Grade_III_HS_Level/SYLLABUS.md",
                        "pattern_file": "02_ADRE_SLRC/Grade_III_HS_Level/EXAM_PATTERN.md",
                        "qualification": "HSSLC (10+2) Pass"
                    },
                    {
                        "name": "Grade III (Driver & Technical Cadres)",
                        "posts": "Light Vehicle Driver, Heavy Vehicle Driver, Electrician, Plumber, Operator",
                        "folder": "02_ADRE_SLRC/Grade_III_Driver",
                        "syllabus_file": "02_ADRE_SLRC/Grade_III_Driver/SYLLABUS.md",
                        "pattern_file": "02_ADRE_SLRC/Grade_III_Driver/EXAM_PATTERN.md",
                        "qualification": "HSLC + Valid Driving License / ITI"
                    },
                    {
                        "name": "Grade IV (HSLC & Class VIII Passed Posts)",
                        "posts": "Peon, Chowkidar, Mali, Ward Boy/Girl, Daftari, Office Attendant, Khalasi, Chainman, Jugali, Sweeper",
                        "folder": "02_ADRE_SLRC/Grade_IV_HSLC_ClassVIII",
                        "syllabus_file": "02_ADRE_SLRC/Grade_IV_HSLC_ClassVIII/SYLLABUS.md",
                        "pattern_file": "02_ADRE_SLRC/Grade_IV_HSLC_ClassVIII/EXAM_PATTERN.md",
                        "qualification": "Class VIII Pass / HSLC Pass"
                    }
                ]
            },
            {
                "id": "03_Assam_Police_SLPRB",
                "name": "Assam Police & Uniformed Services (SLPRB)",
                "official_website": "https://slprbassam.in",
                "exams": [
                    {
                        "name": "Sub-Inspector (UB, AB & Commando Battalions)",
                        "posts": "Sub-Inspector (Unarmed Branch), Sub-Inspector (Armed Branch), Sub-Inspector (Assam Commando)",
                        "folder": "03_Assam_Police_SLPRB/SI_UB_AB_Commando",
                        "syllabus_file": "03_Assam_Police_SLPRB/SI_UB_AB_Commando/SYLLABUS.md",
                        "pattern_file": "03_Assam_Police_SLPRB/SI_UB_AB_Commando/EXAM_PATTERN.md",
                        "qualification": "Graduate in any discipline"
                    },
                    {
                        "name": "Police Constable (UB, AB & Commando)",
                        "posts": "Constable (Unarmed Branch), Constable (Armed Branch), Commando Constable",
                        "folder": "03_Assam_Police_SLPRB/Constable_UB_AB_Commando",
                        "syllabus_file": "03_Assam_Police_SLPRB/Constable_UB_AB_Commando/SYLLABUS.md",
                        "pattern_file": "03_Assam_Police_SLPRB/Constable_UB_AB_Commando/EXAM_PATTERN.md",
                        "qualification": "HSSLC (for UB) / HSLC (for AB & Commando)"
                    },
                    {
                        "name": "APRO (Assam Police Radio Organisation)",
                        "posts": "Sub-Inspector (Communication), Constable (Communication, Messenger, Carpenter, Dispatch Rider)",
                        "folder": "03_Assam_Police_SLPRB/APRO_Communication_Radio",
                        "syllabus_file": "03_Assam_Police_SLPRB/APRO_Communication_Radio/SYLLABUS.md",
                        "pattern_file": "03_Assam_Police_SLPRB/APRO_Communication_Radio/EXAM_PATTERN.md",
                        "qualification": "B.Sc / Diploma in ECE / 10+2 with Physics & Maths"
                    },
                    {
                        "name": "Fire & Emergency Services (F&ES)",
                        "posts": "Station Officer, Sub-Officer, Fireman, Driver Operator",
                        "folder": "03_Assam_Police_SLPRB/Fire_Emergency_Services",
                        "syllabus_file": "03_Assam_Police_SLPRB/APRO_FireServices_JailWarder/SYLLABUS.md",
                        "pattern_file": "03_Assam_Police_SLPRB/APRO_FireServices_JailWarder/EXAM_PATTERN.md",
                        "qualification": "B.Sc (Station Officer) / HSLC / HSSLC"
                    },
                    {
                        "name": "Prisons Department (Jailer, Assistant Jailer, Jail Warder)",
                        "posts": "Jailer, Assistant Jailer, Jail Warder (Male & Female)",
                        "folder": "03_Assam_Police_SLPRB/Prisons_Jailer_Jail_Warder",
                        "syllabus_file": "03_Assam_Police_SLPRB/Prisons_Jailer_Jail_Warder/SYLLABUS.md",
                        "pattern_file": "03_Assam_Police_SLPRB/Prisons_Jailer_Jail_Warder/EXAM_PATTERN.md",
                        "qualification": "Graduate (Jailer) / HSLC (Warder)"
                    },
                    {
                        "name": "Excise Department (Inspector, Assistant Inspector, Constable)",
                        "posts": "Inspector of Excise, Assistant Inspector of Excise, Excise Constable",
                        "folder": "03_Assam_Police_SLPRB/Excise_Inspector_Constable",
                        "syllabus_file": "03_Assam_Police_SLPRB/Excise_Inspector_Constable/SYLLABUS.md",
                        "pattern_file": "03_Assam_Police_SLPRB/Excise_Inspector_Constable/EXAM_PATTERN.md",
                        "qualification": "Graduate / HSLC"
                    },
                    {
                        "name": "Forest Department Cadres (SLPRB)",
                        "posts": "Forester Grade-I, Forest Guard, AFPF Constable",
                        "folder": "03_Assam_Police_SLPRB/Forest_Guard_Forester_I",
                        "syllabus_file": "03_Assam_Police_SLPRB/Forest_Guard_Forester_I/SYLLABUS.md",
                        "pattern_file": "03_Assam_Police_SLPRB/Forest_Guard_Forester_I/EXAM_PATTERN.md",
                        "qualification": "Graduate (Forester-I) / HSSLC (Forest Guard) / HSLC (AFPF)"
                    },
                    {
                        "name": "Civil Defence & Home Guards (DGCD & CGHG)",
                        "posts": "Sub-Inspector, Guardsman, Havildar, Constable",
                        "folder": "03_Assam_Police_SLPRB/Civil_Defence_Home_Guards",
                        "syllabus_file": "03_Assam_Police_SLPRB/APRO_FireServices_JailWarder/SYLLABUS.md",
                        "pattern_file": "03_Assam_Police_SLPRB/APRO_FireServices_JailWarder/EXAM_PATTERN.md",
                        "qualification": "Graduate / HSLC"
                    }
                ]
            },
            {
                "id": "04_Health_DME_DHS",
                "name": "Health & Family Welfare (DME, DHS, DHS-FW, AYUSH, NHM)",
                "official_website": "https://dme.assam.gov.in",
                "exams": [
                    {
                        "name": "Grade III Technical & Paramedical Cadres",
                        "posts": "Staff Nurse, Pharmacist, Lab Technician, Radiographer, OT Tech, Dialysis Tech, ICU Tech, Physiotherapist, ECG Tech, Ophthalmic Assistant, Dental Hygienist, ANM / MPHW",
                        "folder": "04_Health_DME_DHS/Grade_III_Technical",
                        "syllabus_file": "04_Health_DME_DHS/Grade_III_Technical/SYLLABUS.md",
                        "pattern_file": "04_Health_DME_DHS/Grade_III_Technical/EXAM_PATTERN.md",
                        "qualification": "B.Sc Nursing / GNM / D.Pharm / DMLT / Respective Paramedical Diploma"
                    },
                    {
                        "name": "Grade III Non-Technical / Hospital Administration",
                        "posts": "LDA, Store Keeper, Health Educator, Medical Record Officer/Keeper, Computer Operator, Statistical Assistant",
                        "folder": "04_Health_DME_DHS/Grade_III_Non_Technical",
                        "syllabus_file": "04_Health_DME_DHS/Grade_III_Non_Technical/SYLLABUS.md",
                        "pattern_file": "04_Health_DME_DHS/Grade_III_Non_Technical/EXAM_PATTERN.md",
                        "qualification": "Graduate / HSSLC + Computer Certificate"
                    },
                    {
                        "name": "Grade IV Hospital Support Staff",
                        "posts": "Ward Boy, Ward Girl, Ayah, Stretcher Bearer, Dark Room Attendant, Mortuary Attendant, Lab Attendant, OT Attendant, Sweeper",
                        "folder": "04_Health_DME_DHS/Grade_IV",
                        "syllabus_file": "04_Health_DME_DHS/Grade_IV/SYLLABUS.md",
                        "pattern_file": "04_Health_DME_DHS/Grade_IV/EXAM_PATTERN.md",
                        "qualification": "Class VIII Pass"
                    },
                    {
                        "name": "NHM Community Health Officer (CHO) & Program Cadres",
                        "posts": "Community Health Officer (CHO), Block Program Manager, District Consultant, Epidemiologist",
                        "folder": "04_Health_DME_DHS/NHM_Community_Health_Officer_CHO",
                        "syllabus_file": "04_Health_DME_DHS/NHM_Community_Health_Officer_CHO/SYLLABUS.md",
                        "pattern_file": "04_Health_DME_DHS/NHM_Community_Health_Officer_CHO/EXAM_PATTERN.md",
                        "qualification": "B.Sc Nursing (with CCH) / BAMS"
                    }
                ]
            },
            {
                "id": "05_TET_Education",
                "name": "Education, Schools, Colleges & Universities (TET, DSE, DEE, DHE)",
                "official_website": "https://ssa.assam.gov.in",
                "exams": [
                    {
                        "name": "Assam Special & General TET (LP & UP)",
                        "posts": "Paper I: Lower Primary (Classes 1-5) & Paper II: Upper Primary (Classes 6-8: Maths/Science & Social Studies)",
                        "folder": "05_TET_Education/Assam_TET_LP_UP",
                        "syllabus_file": "05_TET_Education/Assam_TET_LP_UP/SYLLABUS.md",
                        "pattern_file": "05_TET_Education/Assam_TET_LP_UP/EXAM_PATTERN.md",
                        "qualification": "D.El.Ed / B.Ed + 10+2 / Graduation"
                    },
                    {
                        "name": "Secondary TET (High School) & Higher Secondary TET (PGT)",
                        "posts": "Graduate Teacher (High School - Classes 9-10) & Post Graduate Teacher (Higher Secondary - Classes 11-12)",
                        "folder": "05_TET_Education/Secondary_Higher_Secondary_TET",
                        "syllabus_file": "05_TET_Education/Secondary_Higher_Secondary_TET/SYLLABUS.md",
                        "pattern_file": "05_TET_Education/Secondary_Higher_Secondary_TET/EXAM_PATTERN.md",
                        "qualification": "B.Ed + Bachelor's (50%) / Master's (50%)"
                    },
                    {
                        "name": "DEE & DSE Regular Teacher Recruitment",
                        "posts": "Regular Assistant Teacher (LP/UP) and Graduate Teacher (Arts/Science/Hindi/Sanskrit/Arabic)",
                        "folder": "05_TET_Education/DSE_DHE_Teacher_Recruitment",
                        "syllabus_file": "05_TET_Education/DSE_DHE_Teacher_Recruitment/SYLLABUS.md",
                        "pattern_file": "05_TET_Education/DSE_DHE_Teacher_Recruitment/EXAM_PATTERN.md",
                        "qualification": "TET Qualified + Professional Teacher Training"
                    },
                    {
                        "name": "DHE Provincialised College Assistant Professor & Librarian",
                        "posts": "Assistant Professor in Arts/Science/Commerce Provincialised Colleges, College Librarian",
                        "folder": "05_TET_Education/DHE_Colleges_Assistant_Professor",
                        "syllabus_file": "05_TET_Education/DSE_DHE_Teacher_Recruitment/SYLLABUS.md",
                        "pattern_file": "05_TET_Education/DSE_DHE_Teacher_Recruitment/EXAM_PATTERN.md",
                        "qualification": "UGC NET / SLET / Ph.D + Master's (55%)"
                    },
                    {
                        "name": "Assam State Universities Non-Teaching Staff",
                        "posts": "Junior Administrative Assistant (JAA), Technical Assistant, Lab Assistant, Peon (Gauhati Univ, Dibrugarh Univ, Cotton Univ, etc.)",
                        "folder": "05_TET_Education/State_Universities_Non_Teaching_Staff",
                        "syllabus_file": "05_TET_Education/State_Universities_Non_Teaching_Staff/SYLLABUS.md",
                        "pattern_file": "05_TET_Education/State_Universities_Non_Teaching_Staff/EXAM_PATTERN.md",
                        "qualification": "Graduate / B.Sc / HSLC"
                    }
                ]
            },
            {
                "id": "06_Judiciary_Gauhati_HC",
                "name": "Gauhati High Court & District Judiciary",
                "official_website": "https://ghconline.gov.in",
                "exams": [
                    {
                        "name": "Assam Judicial Service (AJS Grade I, II, III)",
                        "posts": "District Judge (Grade-I), Civil Judge Sr. Division / CJM (Grade-II), Civil Judge Jr. Division / JMFC (Grade-III)",
                        "folder": "06_Judiciary_Gauhati_HC/AJS_Grade_I_II_III",
                        "syllabus_file": "06_Judiciary_Gauhati_HC/AJS_Grade_I_II_III/SYLLABUS.md",
                        "pattern_file": "06_Judiciary_Gauhati_HC/AJS_Grade_I_II_III/EXAM_PATTERN.md",
                        "qualification": "LL.B / Degree in Law"
                    },
                    {
                        "name": "High Court Registry & District Courts Staff",
                        "posts": "LDA, Copyist, Typist, Stenographer (Gr. I, II, III), Computer Assistant, Bench Assistant, Process Server, Peon",
                        "folder": "06_Judiciary_Gauhati_HC/HighCourt_District_Staff",
                        "syllabus_file": "06_Judiciary_Gauhati_HC/HighCourt_District_Staff/SYLLABUS.md",
                        "pattern_file": "06_Judiciary_Gauhati_HC/HighCourt_District_Staff/EXAM_PATTERN.md",
                        "qualification": "Graduate / HSLC + Shorthand / Typing"
                    }
                ]
            },
            {
                "id": "07_Power_Sector_APDCL",
                "name": "Power Sector Utilities (APDCL, AEGCL, APGCL)",
                "official_website": "https://apdcl.org",
                "exams": [
                    {
                        "name": "Assistant Manager & Junior Manager",
                        "posts": "Assistant Manager & Junior Manager (Electrical, Civil, Mechanical, IT, HR, Finance & Accounts, PR)",
                        "folder": "07_Power_Sector_APDCL/Assistant_Junior_Manager",
                        "syllabus_file": "07_Power_Sector_APDCL/Assistant_Junior_Manager/SYLLABUS.md",
                        "pattern_file": "07_Power_Sector_APDCL/Assistant_Junior_Manager/EXAM_PATTERN.md",
                        "qualification": "B.E./B.Tech / Diploma / MBA HR"
                    },
                    {
                        "name": "AAO, OFA & Sahayak Cadres",
                        "posts": "Assistant Accounts Officer (AAO), Office-cum-Field Assistant (OFA), Junior Accounts Assistant, Meter Reader, Sahayak (Lineman / Substation Attendant)",
                        "folder": "07_Power_Sector_APDCL/AAO_OFA_Sahayak",
                        "syllabus_file": "07_Power_Sector_APDCL/AAO_OFA_Sahayak/SYLLABUS.md",
                        "pattern_file": "07_Power_Sector_APDCL/AAO_OFA_Sahayak/EXAM_PATTERN.md",
                        "qualification": "B.Com / Graduate / ITI Electrician/Wireman"
                    }
                ]
            },
            {
                "id": "08_PnRD_Rural_Development",
                "name": "Panchayat & Rural Development (P&RD & ASRLM)",
                "official_website": "https://rural.assam.gov.in",
                "exams": [
                    {
                        "name": "P&RD Core Cadres",
                        "posts": "Gaon Panchayat Secretary (GPS), Tax Collector-cum-Road Mohorrir, Junior Assistant, Gram Sevak/Sevika",
                        "folder": "08_PnRD_Rural_Development/Gaon_Panchayat_Secretary_GPS",
                        "syllabus_file": "08_PnRD_Transport_Others/PnRD_ASRLM/SYLLABUS.md",
                        "pattern_file": "08_PnRD_Transport_Others/PnRD_ASRLM/EXAM_PATTERN.md",
                        "qualification": "Graduate / HSSLC"
                    },
                    {
                        "name": "ASRLM (Assam State Rural Livelihoods Mission - Jeevika)",
                        "posts": "Block Program Manager (BPM), District Functional Expert (DFE), Project Executive, Block Coordinator",
                        "folder": "08_PnRD_Rural_Development/ASRLM_State_Rural_Livelihoods",
                        "syllabus_file": "08_PnRD_Rural_Development/ASRLM_State_Rural_Livelihoods/SYLLABUS.md",
                        "pattern_file": "08_PnRD_Rural_Development/ASRLM_State_Rural_Livelihoods/EXAM_PATTERN.md",
                        "qualification": "Post Graduate / Graduate in Rural Dev/MSW/Agriculture"
                    },
                    {
                        "name": "Accredited Engineers & Junior Engineers (P&RD)",
                        "posts": "Accredited Engineer, Junior Engineer (P&RD)",
                        "folder": "08_PnRD_Rural_Development/Accredited_Junior_Engineers",
                        "syllabus_file": "08_PnRD_Rural_Development/Accredited_Junior_Engineers/SYLLABUS.md",
                        "pattern_file": "08_PnRD_Rural_Development/Accredited_Junior_Engineers/EXAM_PATTERN.md",
                        "qualification": "Degree / Diploma in Civil Engineering"
                    }
                ]
            },
            {
                "id": "09_Transport_IWT_ASTC",
                "name": "Transport, ASTC & Inland Waterways",
                "official_website": "https://transport.assam.gov.in",
                "exams": [
                    {
                        "name": "Transport Enforcement Branch & ASTC",
                        "posts": "Assistant Enforcement Inspector (AEI), Enforcement Checker, ASTC Station Superintendent, Traffic Inspector, Conductor, Driver",
                        "folder": "09_Transport_IWT_ASTC/Transport_Enforcement_Branch",
                        "syllabus_file": "08_PnRD_Transport_Others/Transport_ASTC_ApexBank/SYLLABUS.md",
                        "pattern_file": "08_PnRD_Transport_Others/Transport_ASTC_ApexBank/EXAM_PATTERN.md",
                        "qualification": "Graduate / HSSLC / HSLC"
                    },
                    {
                        "name": "Inland Water Transport (IWT Assam)",
                        "posts": "Master, Engine Driver, Lascar, Section Assistant, Ghat Incharge, Junior Engineer",
                        "folder": "09_Transport_IWT_ASTC/Inland_Water_Transport_IWT",
                        "syllabus_file": "09_Transport_IWT_ASTC/Inland_Water_Transport_IWT/SYLLABUS.md",
                        "pattern_file": "09_Transport_IWT_ASTC/Inland_Water_Transport_IWT/EXAM_PATTERN.md",
                        "qualification": "Marine Certificate / ITI / HSLC"
                    }
                ]
            },
            {
                "id": "10_Corporations_Cooperatives_Boards",
                "name": "State Public Enterprises, Cooperatives & Corporations",
                "official_website": "https://assam.gov.in",
                "exams": [
                    {
                        "name": "Assam Cooperative Apex Bank Ltd",
                        "posts": "Assistant Manager, Assistant / Cashier",
                        "folder": "10_Corporations_Cooperatives_Boards/Apex_Bank_Assistant_Manager",
                        "syllabus_file": "08_PnRD_Transport_Others/Transport_ASTC_ApexBank/SYLLABUS.md",
                        "pattern_file": "08_PnRD_Transport_Others/Transport_ASTC_ApexBank/EXAM_PATTERN.md",
                        "qualification": "Graduate (Min 50%) / Post Graduate"
                    },
                    {
                        "name": "Assam Gas Company (AGCL) & Assam Petro-chemicals (APL)",
                        "posts": "Graduate Engineer Trainee (GET), Management Trainee, Plant Operator, Technician",
                        "folder": "10_Corporations_Cooperatives_Boards/AGCL_Gas_Company_APL_Petrochem",
                        "syllabus_file": "10_Corporations_Cooperatives_Boards/AGCL_Gas_Company_APL_Petrochem/SYLLABUS.md",
                        "pattern_file": "10_Corporations_Cooperatives_Boards/AGCL_Gas_Company_APL_Petrochem/EXAM_PATTERN.md",
                        "qualification": "B.E./B.Tech in Chemical/Mech/Elect/Instrumentation or B.Sc"
                    },
                    {
                        "name": "Sericulture & Handloom Textiles Directorates",
                        "posts": "Sericulture Demonstrator, Weaving Demonstrator, Inspector of Sericulture/Handloom",
                        "folder": "10_Corporations_Cooperatives_Boards/Sericulture_Handloom_Textiles",
                        "syllabus_file": "10_Corporations_Cooperatives_Boards/Sericulture_Handloom_Textiles/SYLLABUS.md",
                        "pattern_file": "10_Corporations_Cooperatives_Boards/Sericulture_Handloom_Textiles/EXAM_PATTERN.md",
                        "qualification": "Certificate in Sericulture/Handloom or B.Sc"
                    }
                ]
            },
            {
                "id": "11_Revenue_Disaster_Management",
                "name": "Revenue, Land Records & Disaster Management",
                "official_website": "https://landrecords.assam.gov.in",
                "exams": [
                    {
                        "name": "Lot Mandal (Patwari / Land Record Cadre)",
                        "posts": "Lot Mandal / Recorder across all District Commissioner (DC) Offices",
                        "folder": "11_Revenue_Disaster_Management/Lot_Mandal_Patwari_Recruitment",
                        "syllabus_file": "11_Revenue_Disaster_Management/Lot_Mandal_Patwari_Recruitment/SYLLABUS.md",
                        "pattern_file": "11_Revenue_Disaster_Management/Lot_Mandal_Patwari_Recruitment/EXAM_PATTERN.md",
                        "qualification": "HSLC / HSSLC + 6-Month RCCC (Recorders' Course Class Certificate)"
                    },
                    {
                        "name": "ASDMA (Assam State Disaster Management Authority)",
                        "posts": "Field Officer (Disaster Management) at Revenue Circle level, Project Officer",
                        "folder": "11_Revenue_Disaster_Management/ASDMA_Disaster_Management",
                        "syllabus_file": "11_Revenue_Disaster_Management/ASDMA_Disaster_Management/SYLLABUS.md",
                        "pattern_file": "11_Revenue_Disaster_Management/ASDMA_Disaster_Management/EXAM_PATTERN.md",
                        "qualification": "Bachelor's Degree in Science or Geography/Geology/Environmental Science"
                    }
                ]
            },
            {
                "id": "12_Legislative_Assembly_Secretariat",
                "name": "Assam Legislative Assembly Secretariat (ALA)",
                "official_website": "https://assamassembly.gov.in",
                "exams": [
                    {
                        "name": "Junior Administrative Assistant (JAA) & Typist",
                        "posts": "Junior Administrative Assistant, Typist, Computer Operator, Protocol Assistant",
                        "folder": "12_Legislative_Assembly_Secretariat/Junior_Admin_Assistant_JAA",
                        "syllabus_file": "12_Legislative_Assembly_Secretariat/Junior_Admin_Assistant_JAA/SYLLABUS.md",
                        "pattern_file": "12_Legislative_Assembly_Secretariat/Junior_Admin_Assistant_JAA/EXAM_PATTERN.md",
                        "qualification": "Graduate in Arts/Science/Commerce + Computer Diploma"
                    },
                    {
                        "name": "Language Reporters & Translation Officers",
                        "posts": "Reporter (Assamese, English, Bengali), Translation Officer, Research Officer",
                        "folder": "12_Legislative_Assembly_Secretariat/Language_Reporters_Translators",
                        "syllabus_file": "12_Legislative_Assembly_Secretariat/Language_Reporters_Translators/SYLLABUS.md",
                        "pattern_file": "12_Legislative_Assembly_Secretariat/Language_Reporters_Translators/EXAM_PATTERN.md",
                        "qualification": "Graduate + Shorthand (120/140 wpm)"
                    }
                ]
            }
        ]
    }
    
    with open("metadata_catalog.json", "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2)
    print("metadata_catalog.json updated with all 12 categories and 40+ exams.")

update_metadata()
