import os
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

DOWNLOAD_LIST = [
    # ----------------------------------------------------
    # APSC CCE Official Syllabi
    # ----------------------------------------------------
    {
        "url": "https://apsc.nic.in/cce_2019/Syllabus_CCE(P)_GS_I.pdf",
        "path": "01_APSC/CCE_Prelims_Mains/Official_Syllabus_CCE_Prelims_GS_I.pdf",
        "title": "APSC CCE Prelims GS-I Official Syllabus"
    },
    {
        "url": "https://apsc.nic.in/cce_2019/Syllabus_CCE(P)_GS_II.pdf",
        "path": "01_APSC/CCE_Prelims_Mains/Official_Syllabus_CCE_Prelims_GS_II_CSAT.pdf",
        "title": "APSC CCE Prelims GS-II (CSAT) Official Syllabus"
    },
    {
        "url": "https://apsc.nic.in/cce_2019/Syll_CCE_Mains_GS-I.pdf",
        "path": "01_APSC/CCE_Prelims_Mains/Official_Syllabus_CCE_Mains_GS_I.pdf",
        "title": "APSC CCE Mains GS-I Official Syllabus"
    },
    {
        "url": "https://apsc.nic.in/cce_2019/Syll_CCE_Mains_GS-II.pdf",
        "path": "01_APSC/CCE_Prelims_Mains/Official_Syllabus_CCE_Mains_GS_II.pdf",
        "title": "APSC CCE Mains GS-II Official Syllabus"
    },
    {
        "url": "https://apsc.nic.in/cce_2019/Syll_CCE_Mains_GS-III.pdf",
        "path": "01_APSC/CCE_Prelims_Mains/Official_Syllabus_CCE_Mains_GS_III.pdf",
        "title": "APSC CCE Mains GS-III Official Syllabus"
    },
    {
        "url": "https://apsc.nic.in/cce_2019/Syll_CCE_Mains_GS-IV.pdf",
        "path": "01_APSC/CCE_Prelims_Mains/Official_Syllabus_CCE_Mains_GS_IV_Ethics.pdf",
        "title": "APSC CCE Mains GS-IV (Ethics) Official Syllabus"
    },
    {
        "url": "https://apsc.nic.in/cce_2019/Syll_CCE_Mains_GS-V.pdf",
        "path": "01_APSC/CCE_Prelims_Mains/Official_Syllabus_CCE_Mains_GS_V_Assam.pdf",
        "title": "APSC CCE Mains GS-V (Assam Paper) Official Syllabus"
    },
    {
        "url": "https://apsc.nic.in/misc_2025/CCE_Amendment_Rules_ALL.pdf",
        "path": "01_APSC/CCE_Prelims_Mains/Official_APSC_CCE_Amendment_Rules_Gazette.pdf",
        "title": "APSC CCE Examination Rules & Gazette Notification"
    },

    # ----------------------------------------------------
    # APSC Engineering (AE & JE)
    # ----------------------------------------------------
    {
        "url": "https://apsc.nic.in/misc_2020/Syll_AE(Civil)_PWD_12Aug2020.pdf",
        "path": "01_APSC/AE_JE_Engineering/Official_Syllabus_AE_Civil_PWD.pdf",
        "title": "APSC Assistant Engineer (Civil) PWD Syllabus"
    },
    {
        "url": "https://apsc.nic.in/misc_2020/Syll_JE(Civil)_PWD_12_Aug_2020.pdf",
        "path": "01_APSC/AE_JE_Engineering/Official_Syllabus_JE_Civil_PWD.pdf",
        "title": "APSC Junior Engineer (Civil) PWD Syllabus"
    },
    {
        "url": "https://apsc.nic.in/misc_2020/Syll_Degree_AE(Mech)_Irrigation_09Dec2020.pdf",
        "path": "01_APSC/AE_JE_Engineering/Official_Syllabus_AE_Mechanical_Irrigation.pdf",
        "title": "APSC Assistant Engineer (Mechanical) Irrigation Syllabus"
    },
    {
        "url": "https://apsc.nic.in/misc_2020/Syll_Degree_AE(Elc)_Irrigation_09Dec2020.pdf",
        "path": "01_APSC/AE_JE_Engineering/Official_Syllabus_AE_Electrical_Irrigation.pdf",
        "title": "APSC Assistant Engineer (Electrical) Irrigation Syllabus"
    },
    {
        "url": "https://apsc.nic.in/misc_2021/Syllabus_AE_Chem_PHE_19Feb2021.pdf",
        "path": "01_APSC/AE_JE_Engineering/Official_Syllabus_AE_Chemical_PHE.pdf",
        "title": "APSC Assistant Engineer (Chemical) PHE Syllabus"
    },
    {
        "url": "https://apsc.nic.in/misc_2020/Syllabus_JE_C_P&RD_18Nov2020.pdf",
        "path": "08_PnRD_Rural_Development/Accredited_Junior_Engineers/Official_Syllabus_JE_Civil_PnRD.pdf",
        "title": "APSC / P&RD Junior Engineer (Civil) Official Syllabus"
    },
    {
        "url": "https://apsc.nic.in/misc_2020/Syll_AE_IWT_TD_31Oct2020.pdf",
        "path": "09_Transport_IWT_ASTC/Inland_Water_Transport_IWT/Official_Syllabus_AE_IWT_Transport.pdf",
        "title": "APSC Assistant Engineer (IWT Transport) Official Syllabus"
    },

    # ----------------------------------------------------
    # APSC Agriculture, Veterinary, Fishery & Specialized
    # ----------------------------------------------------
    {
        "url": "https://apsc.nic.in/Syllabus_ADO_28Jan2019.pdf",
        "path": "01_APSC/Agriculture_Veterinary_Fishery/Official_Syllabus_Agricultural_Development_Officer_ADO.pdf",
        "title": "APSC Agricultural Development Officer (ADO) Syllabus"
    },
    {
        "url": "https://apsc.nic.in/misc_2026/VO_BVO_Animal_Husbandry_Vet_Science_Syllabus_11_2026.pdf",
        "path": "01_APSC/Agriculture_Veterinary_Fishery/Official_Syllabus_Veterinary_Officer_VO_BVO.pdf",
        "title": "APSC Veterinary Officer (VO/BVO) Domain Syllabus"
    },
    {
        "url": "https://apsc.nic.in/misc_2026/VO_BVO_GS_Syllabus_11_2026.pdf",
        "path": "01_APSC/Agriculture_Veterinary_Fishery/Official_Syllabus_VO_BVO_General_Studies.pdf",
        "title": "APSC Veterinary Officer General Studies Syllabus"
    },
    {
        "url": "https://apsc.nic.in/JE%20Civil%20Syllabus%20%20Fishery%20Deptt..pdf",
        "path": "01_APSC/Agriculture_Veterinary_Fishery/Official_Syllabus_JE_Civil_Fishery_Dept.pdf",
        "title": "APSC JE Civil Fishery Department Syllabus"
    },
    {
        "url": "https://apsc.nic.in/misc_2020/Syllabus_RA_TDD_Advt_%2007_2019.pdf",
        "path": "01_APSC/Research_Assistant_Specialized/Official_Syllabus_Research_Assistant_Planning_TDD.pdf",
        "title": "APSC Research Assistant (Planning Services) Syllabus"
    },
    {
        "url": "https://apsc.nic.in/Syllabus_Inspector%20of%20Legal%20Metrology.pdf",
        "path": "01_APSC/Specialized_Inspectors_Legal_MVI_Factories/Official_Syllabus_Inspector_Legal_Metrology.pdf",
        "title": "APSC Inspector of Legal Metrology Syllabus"
    },
    {
        "url": "https://apsc.nic.in/LE%20Syllabus%20Insp.of%20Boiler.pdf",
        "path": "01_APSC/Specialized_Inspectors_Legal_MVI_Factories/Official_Syllabus_Inspector_of_Boilers.pdf",
        "title": "APSC Inspector of Boilers Syllabus"
    },

    # ----------------------------------------------------
    # Power Sector APDCL / APGCL Syllabi via APSC
    # ----------------------------------------------------
    {
        "url": "https://apsc.nic.in/misc_2026/APGCL_AM_GS_Syllabus.pdf",
        "path": "07_Power_Sector_APDCL/Assistant_Junior_Manager/Official_Syllabus_Assistant_Manager_GS.pdf",
        "title": "Power Utilities Assistant Manager GS Syllabus"
    },
    {
        "url": "https://apsc.nic.in/misc_2026/APGCL_AM_Elec_Engg_Syllabus.pdf",
        "path": "07_Power_Sector_APDCL/Assistant_Junior_Manager/Official_Syllabus_AM_Electrical_Engg.pdf",
        "title": "Power Utilities Assistant Manager Electrical Engg Syllabus"
    },
    {
        "url": "https://apsc.nic.in/misc_2026/APGCL_AM_Mech_Engg_Syllabus.pdf",
        "path": "07_Power_Sector_APDCL/Assistant_Junior_Manager/Official_Syllabus_AM_Mechanical_Engg.pdf",
        "title": "Power Utilities Assistant Manager Mechanical Engg Syllabus"
    },
    {
        "url": "https://apsc.nic.in/misc_2026/APGCL_AM_Civil_Engg_Syllabus.pdf",
        "path": "07_Power_Sector_APDCL/Assistant_Junior_Manager/Official_Syllabus_AM_Civil_Engg.pdf",
        "title": "Power Utilities Assistant Manager Civil Engg Syllabus"
    },
    {
        "url": "https://apsc.nic.in/misc_2026/APGCL_AM_HR_Syllabus.pdf",
        "path": "07_Power_Sector_APDCL/Assistant_Junior_Manager/Official_Syllabus_AM_Human_Resources.pdf",
        "title": "Power Utilities Assistant Manager HR Syllabus"
    },
    {
        "url": "https://apsc.nic.in/misc_2026/APGCL_JM_GS_Syllabus_10_2026.pdf",
        "path": "07_Power_Sector_APDCL/Assistant_Junior_Manager/Official_Syllabus_Junior_Manager_GS.pdf",
        "title": "Power Utilities Junior Manager GS Syllabus"
    },
    {
        "url": "https://apsc.nic.in/misc_2026/APGCL_JM_Elec_Engg_Syllabus_10_2026.pdf",
        "path": "07_Power_Sector_APDCL/Assistant_Junior_Manager/Official_Syllabus_JM_Electrical_Engg.pdf",
        "title": "Power Utilities Junior Manager Electrical Engg Syllabus"
    },

    # ----------------------------------------------------
    # DME Health Official PDFs
    # ----------------------------------------------------
    {
        "url": "https://dme.assam.gov.in/sites/default/files/swf_utility_folder/departments/dme_lipl_in_oid_8/menu/document/recruitment_notice-grade-iiitechnical_posts_of_a.h.m.c.r.i._diphu.pdf",
        "path": "04_Health_DME_DHS/Grade_III_Technical/Official_DME_Grade_III_Technical_Recruitment_Rules.pdf",
        "title": "DME Grade III Technical Official Recruitment Scheme"
    },
    {
        "url": "https://dme.assam.gov.in/sites/default/files/swf_utility_folder/departments/dme_lipl_in_oid_8/menu/document/Notice%20Regarding%20Written%20Test%20for%20the%20post%20of%20Ward%20Boy-Ward%20Girl.pdf",
        "path": "04_Health_DME_DHS/Grade_IV/Official_DME_Grade_IV_Written_Test_Scheme.pdf",
        "title": "DME Grade IV Written Test Scheme"
    }
]

def download_all_official_pdfs():
    success_count = 0
    total_count = len(DOWNLOAD_LIST)
    print(f"Starting download of {total_count} official syllabus and scheme PDFs...\n")

    for item in DOWNLOAD_LIST:
        out_path = item["path"]
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        print(f"Downloading: {item['title']}...")
        try:
            r = requests.get(item["url"], headers=headers, verify=False, timeout=25)
            if r.status_code == 200 and len(r.content) > 1000 and (b'%PDF' in r.content[:10] or 'pdf' in r.headers.get('content-type', '').lower()):
                with open(out_path, "wb") as f:
                    f.write(r.content)
                size_kb = len(r.content) / 1024
                print(f"  --> [SAVED] {out_path} ({size_kb:.1f} KB)")
                success_count += 1
            else:
                print(f"  --> [FAILED] Status: {r.status_code}, Length: {len(r.content)}")
        except Exception as e:
            print(f"  --> [ERROR] {e}")

    print(f"\nCompleted: {success_count}/{total_count} official PDFs successfully downloaded and saved.")

if __name__ == "__main__":
    download_all_official_pdfs()
