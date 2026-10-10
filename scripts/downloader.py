import os
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SYLLABUS_DOWNLOADS = [
    # APSC CCE
    {
        "url": "http://apsc.nic.in/cce_syllabus/CCE_Prelim_Syllabus.pdf",
        "output": "01_APSC/CCE_Prelims_Mains/APSC_CCE_Prelims_Syllabus.pdf",
        "title": "APSC CCE Prelims Official Syllabus"
    },
    {
        "url": "http://apsc.nic.in/cce_syllabus/CCE_Mains_Syllabus.pdf",
        "output": "01_APSC/CCE_Prelims_Mains/APSC_CCE_Mains_Syllabus.pdf",
        "title": "APSC CCE Mains Official Syllabus"
    },
    # APSC Engineering
    {
        "url": "http://apsc.nic.in/syllabus_2020/Syllabus_Civil_Engg_AE.pdf",
        "output": "01_APSC/AE_JE_Engineering/APSC_Civil_Engineering_Syllabus.pdf",
        "title": "APSC AE/JE Civil Engineering Syllabus"
    },
    {
        "url": "http://apsc.nic.in/syllabus_2020/Syllabus_Mechanical_Engg_AE.pdf",
        "output": "01_APSC/AE_JE_Engineering/APSC_Mechanical_Engineering_Syllabus.pdf",
        "title": "APSC AE/JE Mechanical Engineering Syllabus"
    },
    {
        "url": "http://apsc.nic.in/syllabus_2020/Syllabus_Electrical_Engg_AE.pdf",
        "output": "01_APSC/AE_JE_Engineering/APSC_Electrical_Engineering_Syllabus.pdf",
        "title": "APSC AE/JE Electrical Engineering Syllabus"
    },
    # APSC Forest Ranger
    {
        "url": "http://apsc.nic.in/syllabus/Forest_Ranger_Syllabus.pdf",
        "output": "01_APSC/Forestry_Services/APSC_Forest_Ranger_Syllabus.pdf",
        "title": "APSC Forest Ranger Syllabus"
    },
    # APSC Research Assistant
    {
        "url": "http://apsc.nic.in/syllabus_2022/Syllabus_Research_Assistant.pdf",
        "output": "01_APSC/Research_Assistant_Specialized/APSC_Research_Assistant_Syllabus.pdf",
        "title": "APSC Research Assistant Syllabus"
    },
    # Gauhati High Court AJS
    {
        "url": "https://ghconline.gov.in/Recruitment/AJS_Syllabus_Rules.pdf",
        "output": "06_Judiciary_Gauhati_HC/AJS_Grade_I_II_III/Assam_Judicial_Service_Rules_Syllabus.pdf",
        "title": "Assam Judicial Service Syllabus & Scheme"
    }
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

def download_files():
    for item in SYLLABUS_DOWNLOADS:
        out_path = item["output"]
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        print(f"Fetching: {item['title']} from {item['url']}...")
        try:
            r = requests.get(item["url"], headers=headers, verify=False, timeout=20)
            if r.status_code == 200 and len(r.content) > 1000 and (r.headers.get("content-type", "").lower().find("pdf") != -1 or r.content[:4] == b'%PDF'):
                with open(out_path, "wb") as f:
                    f.write(r.content)
                print(f"  [SUCCESS] Saved to {out_path} ({len(r.content)/1024:.1f} KB)")
            else:
                print(f"  [NOTE] Response status {r.status_code} / Content-Type {r.headers.get('content-type')}.")
        except Exception as e:
            print(f"  [ERROR] {e}")

if __name__ == "__main__":
    download_files()
