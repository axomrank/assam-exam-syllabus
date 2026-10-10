import os
import json

# Define the full expanded directory structure
EXPANDED_DIRS = [
    # 01 APSC
    "01_APSC/CCE_Civil_Services",
    "01_APSC/AE_JE_Engineering_Services",
    "01_APSC/Forestry_Services",
    "01_APSC/Medical_Food_Drug_Services",
    "01_APSC/Agriculture_Veterinary_Fishery",
    "01_APSC/Lecturer_Assistant_Professor_Poly_Engg",
    "01_APSC/Specialized_Inspectors_Legal_MVI_Factories",
    # 02 ADRE
    "02_ADRE_SLRC/Grade_III_Graduate_Level",
    "02_ADRE_SLRC/Grade_III_Higher_Secondary_Level",
    "02_ADRE_SLRC/Grade_III_Driver_Technical",
    "02_ADRE_SLRC/Grade_IV_HSLC_ClassVIII_Posts",
    # 03 Police & Uniformed
    "03_Assam_Police_SLPRB/SI_UB_AB_Commando",
    "03_Assam_Police_SLPRB/Constable_UB_AB_Commando",
    "03_Assam_Police_SLPRB/APRO_Communication_Radio",
    "03_Assam_Police_SLPRB/Fire_Emergency_Services",
    "03_Assam_Police_SLPRB/Prisons_Jailer_Jail_Warder",
    "03_Assam_Police_SLPRB/Excise_Inspector_Constable",
    "03_Assam_Police_SLPRB/Forest_Guard_Forester_I_AFPF",
    "03_Assam_Police_SLPRB/Civil_Defence_Home_Guards",
    # 04 Health & Medical
    "04_Health_DME_DHS/Grade_III_Technical_Paramedical",
    "04_Health_DME_DHS/Grade_III_Non_Technical_Administrative",
    "04_Health_DME_DHS/Grade_IV_Hospital_Staff",
    "04_Health_DME_DHS/NHM_Community_Health_Officer_CHO",
    # 05 Education & TET
    "05_TET_Education/Assam_TET_LP_UP_General_Special",
    "05_TET_Education/Secondary_TET_High_School",
    "05_TET_Education/Higher_Secondary_TET_PGT",
    "05_TET_Education/DEE_DSE_Regular_Teacher_Recruitment",
    "05_TET_Education/DHE_Colleges_Assistant_Professor",
    "05_TET_Education/State_Universities_Non_Teaching_Staff",
    # 06 Judiciary
    "06_Judiciary_Gauhati_HC/Assam_Judicial_Service_AJS",
    "06_Judiciary_Gauhati_HC/Gauhati_HC_Registry_Staff",
    "06_Judiciary_Gauhati_HC/District_Judiciary_Staff",
    # 07 Power Sector
    "07_Power_Sector_APDCL/Assistant_Junior_Manager_Engg_HR",
    "07_Power_Sector_APDCL/AAO_JAA_Accounts_Cadre",
    "07_Power_Sector_APDCL/Office_Field_Assistant_OFA",
    "07_Power_Sector_APDCL/Sahayak_Lineman_Technical",
    # 08 PnRD & Rural Dev
    "08_PnRD_Rural_Development/Gaon_Panchayat_Secretary_GPS",
    "08_PnRD_Rural_Development/Tax_Collector_Road_Mohorrir",
    "08_PnRD_Rural_Development/ASRLM_State_Rural_Livelihoods",
    "08_PnRD_Rural_Development/Accredited_Junior_Engineers",
    # 09 Transport & IWT
    "09_Transport_IWT_ASTC/Transport_Enforcement_Branch",
    "09_Transport_IWT_ASTC/ASTC_State_Transport_Corp",
    "09_Transport_IWT_ASTC/Inland_Water_Transport_IWT",
    # 10 State Public Enterprises & Corporations
    "10_Corporations_Cooperatives_Boards/Apex_Bank_Assistant_Manager",
    "10_Corporations_Cooperatives_Boards/AGCL_Gas_Company_APL_Petrochem",
    "10_Corporations_Cooperatives_Boards/Sericulture_Handloom_Textiles",
    "10_Corporations_Cooperatives_Boards/Fisheries_Agri_Marketing_Board",
    # 11 Land Revenue & Disaster Management
    "11_Revenue_Disaster_Management/Lot_Mandal_Patwari_Recruitment",
    "11_Revenue_Disaster_Management/ASDMA_Disaster_Management",
    # 12 Legislative Assembly Secretariat
    "12_Legislative_Assembly_Secretariat/Junior_Admin_Assistant_JAA",
    "12_Legislative_Assembly_Secretariat/Language_Reporters_Translators"
]

for d in EXPANDED_DIRS:
    os.makedirs(d, exist_ok=True)

print(f"Created {len(EXPANDED_DIRS)} specialized exam directories.")
