import os
import shutil
import json

BASE_DIR = "/home/angsuman/extra_spac/Study_Assam"

CANONICAL_DIRS = [
    # 01 APSC
    "01_APSC/Combined_Competitive_Exam_CCE/01_Prelims",
    "01_APSC/Combined_Competitive_Exam_CCE/02_Mains",
    "01_APSC/Combined_Competitive_Exam_CCE/03_Rules_Gazette",
    "01_APSC/Engineering_Services_AE_JE",
    "01_APSC/Forest_Services_AFS_Ranger",
    "01_APSC/Agriculture_Veterinary_Fisheries",
    "01_APSC/Health_Drug_Food_Services",
    "01_APSC/Higher_Education_Technical_Faculty",
    "01_APSC/Specialized_Administrative_Inspectors",

    # 02 ADRE
    "02_ADRE_SLRC/Class_III_Graduate_Level",
    "02_ADRE_SLRC/Class_III_Higher_Secondary_Level",
    "02_ADRE_SLRC/Class_III_Driver_Technical",
    "02_ADRE_SLRC/Class_IV_HSLC_ClassVIII",

    # 03 Police & Uniformed
    "03_Assam_Police_SLPRB/Sub_Inspector_UB_AB_Commando",
    "03_Assam_Police_SLPRB/Constable_UB_AB_Commando",
    "03_Assam_Police_SLPRB/APRO_Radio_Communication",
    "03_Assam_Police_SLPRB/Fire_Emergency_Services",
    "03_Assam_Police_SLPRB/Prisons_Jailer_Warder",
    "03_Assam_Police_SLPRB/Excise_Inspector_Constable",
    "03_Assam_Police_SLPRB/Forestry_Cadres_Forester_Guard",
    "03_Assam_Police_SLPRB/Civil_Defence_Home_Guards",

    # 04 Health & Medical
    "04_Health_DME_DHS_NHM/Grade_III_Technical_Paramedical",
    "04_Health_DME_DHS_NHM/Grade_III_Non_Technical_Admin",
    "04_Health_DME_DHS_NHM/Grade_IV_Hospital_Staff",
    "04_Health_DME_DHS_NHM/NHM_Community_Health_Officer_CHO",

    # 05 Education & Faculty
    "05_Education_TET_Faculty/Assam_TET_LP_UP",
    "05_Education_TET_Faculty/Secondary_TET_High_School",
    "05_Education_TET_Faculty/Higher_Secondary_TET_PGT",
    "05_Education_TET_Faculty/DEE_DSE_Teacher_Recruitment",
    "05_Education_TET_Faculty/DHE_College_Assistant_Professor",
    "05_Education_TET_Faculty/State_Universities_Staff",

    # 06 Judiciary
    "06_Judiciary_Gauhati_HC/Assam_Judicial_Service_AJS",
    "06_Judiciary_Gauhati_HC/High_Court_Registry_Staff",
    "06_Judiciary_Gauhati_HC/District_Courts_Staff",

    # 07 Power Sector
    "07_Power_Sector_APDCL/Assistant_Junior_Manager",
    "07_Power_Sector_APDCL/AAO_OFA_Sahayak",

    # 08 PnRD & Rural Development
    "08_PnRD_Rural_Development/Panchayat_Core_GPS_TaxCollector",
    "08_PnRD_Rural_Development/ASRLM_Jeevika_Mission",
    "08_PnRD_Rural_Development/PnRD_Engineers_Accredited_JE",

    # 09 Transport & IWT
    "09_Transport_IWT_ASTC/Transport_Enforcement_Branch",
    "09_Transport_IWT_ASTC/ASTC_State_Transport",
    "09_Transport_IWT_ASTC/Inland_Water_Transport_IWT",

    # 10 Corporations & Boards
    "10_Corporations_Cooperatives_Boards/Assam_Cooperative_Apex_Bank",
    "10_Corporations_Cooperatives_Boards/AGCL_Gas_Company_APL_Petrochem",
    "10_Corporations_Cooperatives_Boards/Sericulture_Handloom_Textiles",
    "10_Corporations_Cooperatives_Boards/Agri_Marketing_Fisheries_Boards",

    # 11 Revenue & Disaster
    "11_Revenue_Disaster_Management/Lot_Mandal_Patwari_Land_Records",
    "11_Revenue_Disaster_Management/ASDMA_Disaster_Management",

    # 12 Legislative Assembly
    "12_Legislative_Assembly_Secretariat/Junior_Admin_Assistant_JAA",
    "12_Legislative_Assembly_Secretariat/Language_Reporters_Translators"
]

def safe_copy_file(src, dst):
    if os.path.exists(src) and os.path.abspath(src) != os.path.abspath(dst):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        print(f"Copied: {src} -> {dst}")

def safe_copy_dir_contents(src_dir, dst_dir):
    if os.path.exists(src_dir) and os.path.abspath(src_dir) != os.path.abspath(dst_dir):
        os.makedirs(dst_dir, exist_ok=True)
        for item in os.listdir(src_dir):
            s = os.path.join(src_dir, item)
            d = os.path.join(dst_dir, item)
            if os.path.isfile(s):
                shutil.copy2(s, d)
                print(f"Copied: {s} -> {d}")

def restructure():
    os.chdir(BASE_DIR)
    
    # 1. Create canonical folders
    for d in CANONICAL_DIRS:
        os.makedirs(d, exist_ok=True)

    # 2. Migrate APSC CCE
    safe_copy_dir_contents("01_APSC/CCE_Prelims", "01_APSC/Combined_Competitive_Exam_CCE/01_Prelims")
    safe_copy_dir_contents("01_APSC/CCE_Mains", "01_APSC/Combined_Competitive_Exam_CCE/02_Mains")
    safe_copy_file("01_APSC/CCE_Prelims_Mains/Official_APSC_CCE_Amendment_Rules_Gazette.pdf", "01_APSC/Combined_Competitive_Exam_CCE/03_Rules_Gazette/Official_APSC_CCE_Amendment_Rules_Gazette.pdf")

    # 3. Migrate APSC other folders
    safe_copy_dir_contents("01_APSC/AE_JE_Engineering", "01_APSC/Engineering_Services_AE_JE")
    safe_copy_dir_contents("01_APSC/Forestry_Services", "01_APSC/Forest_Services_AFS_Ranger")
    safe_copy_dir_contents("01_APSC/Agriculture_Veterinary_Fishery", "01_APSC/Agriculture_Veterinary_Fisheries")
    safe_copy_dir_contents("01_APSC/Medical_Food_Drug_Services", "01_APSC/Health_Drug_Food_Services")
    safe_copy_dir_contents("01_APSC/Lecturer_Assistant_Professor_Poly_Engg", "01_APSC/Higher_Education_Technical_Faculty")
    safe_copy_dir_contents("01_APSC/Specialized_Inspectors_Legal_MVI_Factories", "01_APSC/Specialized_Administrative_Inspectors")
    safe_copy_dir_contents("01_APSC/Research_Assistant_Specialized", "01_APSC/Specialized_Administrative_Inspectors")

    # 4. Migrate ADRE
    safe_copy_dir_contents("02_ADRE_SLRC/Grade_III_Graduate", "02_ADRE_SLRC/Class_III_Graduate_Level")
    safe_copy_dir_contents("02_ADRE_SLRC/Grade_III_HS_Level", "02_ADRE_SLRC/Class_III_Higher_Secondary_Level")
    safe_copy_dir_contents("02_ADRE_SLRC/Grade_III_Driver", "02_ADRE_SLRC/Class_III_Driver_Technical")
    safe_copy_dir_contents("02_ADRE_SLRC/Grade_IV_HSLC_ClassVIII", "02_ADRE_SLRC/Class_IV_HSLC_ClassVIII")

    # 5. Migrate Police & Uniformed
    safe_copy_dir_contents("03_Assam_Police_SLPRB/SI_UB_AB_Commando", "03_Assam_Police_SLPRB/Sub_Inspector_UB_AB_Commando")
    safe_copy_dir_contents("03_Assam_Police_SLPRB/APRO_Communication_Radio", "03_Assam_Police_SLPRB/APRO_Radio_Communication")
    safe_copy_dir_contents("03_Assam_Police_SLPRB/APRO_FireServices_JailWarder", "03_Assam_Police_SLPRB/Fire_Emergency_Services")
    safe_copy_dir_contents("03_Assam_Police_SLPRB/Prisons_Jailer_Jail_Warder", "03_Assam_Police_SLPRB/Prisons_Jailer_Warder")
    safe_copy_dir_contents("03_Assam_Police_SLPRB/Excise_Inspector_Constable", "03_Assam_Police_SLPRB/Excise_Inspector_Constable")
    safe_copy_dir_contents("03_Assam_Police_SLPRB/Forest_Guard_Forester_I", "03_Assam_Police_SLPRB/Forestry_Cadres_Forester_Guard")

    # 6. Migrate Health (DME/DHS/NHM)
    safe_copy_dir_contents("04_Health_DME_DHS/Grade_III_Technical", "04_Health_DME_DHS_NHM/Grade_III_Technical_Paramedical")
    safe_copy_dir_contents("04_Health_DME_DHS/Grade_III_Non_Technical", "04_Health_DME_DHS_NHM/Grade_III_Non_Technical_Admin")
    safe_copy_dir_contents("04_Health_DME_DHS/Grade_IV", "04_Health_DME_DHS_NHM/Grade_IV_Hospital_Staff")
    safe_copy_dir_contents("04_Health_DME_DHS/NHM_Community_Health_Officer_CHO", "04_Health_DME_DHS_NHM/NHM_Community_Health_Officer_CHO")

    # 7. Migrate Education & Faculty
    safe_copy_dir_contents("05_TET_Education/Assam_TET_LP_UP", "05_Education_TET_Faculty/Assam_TET_LP_UP")
    safe_copy_dir_contents("05_TET_Education/Secondary_Higher_Secondary_TET", "05_Education_TET_Faculty/Secondary_TET_High_School")
    safe_copy_dir_contents("05_TET_Education/Secondary_Higher_Secondary_TET", "05_Education_TET_Faculty/Higher_Secondary_TET_PGT")
    safe_copy_dir_contents("05_TET_Education/DSE_DHE_Teacher_Recruitment", "05_Education_TET_Faculty/DEE_DSE_Teacher_Recruitment")
    safe_copy_dir_contents("05_TET_Education/DHE_Colleges_Assistant_Professor", "05_Education_TET_Faculty/DHE_College_Assistant_Professor")
    safe_copy_dir_contents("05_TET_Education/State_Universities_Non_Teaching_Staff", "05_Education_TET_Faculty/State_Universities_Staff")

    # 8. Migrate Judiciary
    safe_copy_dir_contents("06_Judiciary_Gauhati_HC/AJS_Grade_I_II_III", "06_Judiciary_Gauhati_HC/Assam_Judicial_Service_AJS")
    safe_copy_dir_contents("06_Judiciary_Gauhati_HC/HighCourt_District_Staff", "06_Judiciary_Gauhati_HC/High_Court_Registry_Staff")
    safe_copy_dir_contents("06_Judiciary_Gauhati_HC/District_Judiciary_Staff", "06_Judiciary_Gauhati_HC/District_Courts_Staff")

    # 9. Migrate PnRD
    safe_copy_dir_contents("08_PnRD_Rural_Development/Gaon_Panchayat_Secretary_GPS", "08_PnRD_Rural_Development/Panchayat_Core_GPS_TaxCollector")
    safe_copy_dir_contents("08_PnRD_Transport_Others/PnRD_ASRLM", "08_PnRD_Rural_Development/Panchayat_Core_GPS_TaxCollector")
    safe_copy_dir_contents("08_PnRD_Rural_Development/ASRLM_State_Rural_Livelihoods", "08_PnRD_Rural_Development/ASRLM_Jeevika_Mission")
    safe_copy_dir_contents("08_PnRD_Rural_Development/Accredited_Junior_Engineers", "08_PnRD_Rural_Development/PnRD_Engineers_Accredited_JE")

    # 10. Migrate Transport
    safe_copy_dir_contents("08_PnRD_Transport_Others/Transport_ASTC_ApexBank", "09_Transport_IWT_ASTC/Transport_Enforcement_Branch")
    safe_copy_dir_contents("09_Transport_IWT_ASTC/ASTC_State_Transport_Corp", "09_Transport_IWT_ASTC/ASTC_State_Transport")

    # 11. Migrate Corporations
    safe_copy_dir_contents("08_PnRD_Transport_Others/Transport_ASTC_ApexBank", "10_Corporations_Cooperatives_Boards/Assam_Cooperative_Apex_Bank")
    safe_copy_dir_contents("10_Corporations_Cooperatives_Boards/Fisheries_Agri_Marketing_Board", "10_Corporations_Cooperatives_Boards/Agri_Marketing_Fisheries_Boards")

    # 12. Migrate Revenue
    safe_copy_dir_contents("11_Revenue_Disaster_Management/Lot_Mandal_Patwari_Recruitment", "11_Revenue_Disaster_Management/Lot_Mandal_Patwari_Land_Records")

    # 13. Purge obsolete / duplicate directories
    obsolete_dirs = [
        "01_APSC/CCE_Civil_Services",
        "01_APSC/CCE_Prelims_Mains",
        "01_APSC/CCE_Prelims",
        "01_APSC/CCE_Mains",
        "01_APSC/AE_JE_Engineering",
        "01_APSC/AE_JE_Engineering_Services",
        "01_APSC/Forestry_Services",
        "01_APSC/Agriculture_Veterinary_Fishery",
        "01_APSC/Medical_Food_Drug_Services",
        "01_APSC/Lecturer_Assistant_Professor_Poly_Engg",
        "01_APSC/Research_Assistant_Specialized",
        "01_APSC/Specialized_Inspectors_Legal_MVI_Factories",
        "02_ADRE_SLRC/Grade_III_Driver",
        "02_ADRE_SLRC/Grade_III_Driver_Technical",
        "02_ADRE_SLRC/Grade_III_Graduate",
        "02_ADRE_SLRC/Grade_III_Graduate_Level",
        "02_ADRE_SLRC/Grade_III_Higher_Secondary_Level",
        "02_ADRE_SLRC/Grade_III_HS_Level",
        "02_ADRE_SLRC/Grade_IV_HSLC_ClassVIII",
        "02_ADRE_SLRC/Grade_IV_HSLC_ClassVIII_Posts",
        "03_Assam_Police_SLPRB/APRO_Communication_Radio",
        "03_Assam_Police_SLPRB/APRO_FireServices_JailWarder",
        "03_Assam_Police_SLPRB/Forest_Guard_Forester_I",
        "03_Assam_Police_SLPRB/Forest_Guard_Forester_I_AFPF",
        "03_Assam_Police_SLPRB/Prisons_Jailer_Jail_Warder",
        "03_Assam_Police_SLPRB/SI_UB_AB_Commando",
        "04_Health_DME_DHS",
        "05_TET_Education",
        "06_Judiciary_Gauhati_HC/AJS_Grade_I_II_III",
        "06_Judiciary_Gauhati_HC/HighCourt_District_Staff",
        "06_Judiciary_Gauhati_HC/Assam_Judicial_Service_AJS/Assam_Judicial_Service_AJS",
        "07_Power_Sector_APDCL/Assistant_Junior_Manager_Engg_HR",
        "07_Power_Sector_APDCL/AAO_JAA_Accounts_Cadre",
        "07_Power_Sector_APDCL/Office_Field_Assistant_OFA",
        "07_Power_Sector_APDCL/Sahayak_Lineman_Technical",
        "08_PnRD_Rural_Development/Accredited_Junior_Engineers",
        "08_PnRD_Rural_Development/ASRLM_State_Rural_Livelihoods",
        "08_PnRD_Rural_Development/Gaon_Panchayat_Secretary_GPS",
        "08_PnRD_Rural_Development/Tax_Collector_Road_Mohorrir",
        "08_PnRD_Transport_Others",
        "09_Transport_IWT_ASTC/ASTC_State_Transport_Corp",
        "10_Corporations_Cooperatives_Boards/Apex_Bank_Assistant_Manager",
        "10_Corporations_Cooperatives_Boards/Fisheries_Agri_Marketing_Board",
        "11_Revenue_Disaster_Management/Lot_Mandal_Patwari_Recruitment"
    ]

    for d in obsolete_dirs:
        if os.path.exists(d):
            shutil.rmtree(d, ignore_errors=True)
            print(f"Removed legacy directory: {d}")

    print("Restructuring finished successfully!")

if __name__ == "__main__":
    restructure()
