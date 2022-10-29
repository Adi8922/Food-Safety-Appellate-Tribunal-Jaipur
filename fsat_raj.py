import requests
from bs4 import BeautifulSoup

final_data = []
data_value = {}
appeal_number = input("Enter Your Appeal Number \n")
order_year = input("Enter Your Order Year \n")
session = requests.session()
url = "https://www.fsat-raj.in/case-status.php"
url1 = "https://www.fsat-raj.in/action.php"
response1 = session.get(url, verify = False)
html_content1 = response1.content
soup1 = BeautifulSoup(html_content1, "lxml")
# print(soup1)
Headers1 =  {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding" : "gzip, deflate, br",
        "Accept-Language" : "en-US,en;q=0.5",
        "Connection" : "keep-alive",
        "Host" : "www.fsat-raj.in",
        "Sec-Fetch-Dest" : "document",
        "Sec-Fetch-Mode" : "navigate",
        "Sec-Fetch-Site" : "none",
        "Sec-Fetch-User" : "?1",
        "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
    }

payload1 ={
        "search_type":"appeal",
        "appeal_number": appeal_number,
        "advocate_name":"",
        "order_year": order_year,
        "action":"appeal_case_search"
    }


responce2 = session.post(url1, headers = Headers1, data = payload1, verify=False)
html_content2 = responce2.content
soup2 = BeautifulSoup(html_content2,"lxml")
# print(soup2)
data = soup2.find_all("td")
s_no = data[0].text.strip().split("<\/td>")[0][8]
file_no = data[2].text.strip().split("<\/td>")[0]
appeal_no = data[4].text.strip().split("<\/td>")[0]#.split("\\")[0]
adjudicating_officer = data[6].text.strip().split("<\/td>")[0]
mobile_no = data[8].text.strip().split("<\/td>")[0]
name_of_appellant = data[10].text.strip().split("<\/td>")[0]
email_id = data[12].text.strip().split("<\/td>")[0]
name_of_advocate = data[14].text.strip().split("<\/td>")[0]
advocate_mobile_no = data[16].text.strip().split("<\/td>")[0]
advocate_email_id = data[18].text.strip().split("<\/td>")[0]
register_on_date = data[20].text.strip().split("<\/td>")[0]
status = data[22].text.strip().split("<\/td>")[0].split("<\/span>")[0]

data_value["S.No."] = s_no
data_value["File No"] = file_no
data_value["AppealNo"] = appeal_no
data_value["ADJUDICATING OFFICER"] = adjudicating_officer
data_value["MOBILE_NO"] = mobile_no
data_value["NAME OF APPELLANT"] = name_of_appellant
data_value["EMAIL ID"] = email_id
data_value["NAME OF ADVOCATE"] = name_of_advocate
data_value["Advocate Mobile"] = advocate_mobile_no
data_value["Advocate Email Id"] = advocate_email_id
data_value["Register On date"] = register_on_date
data_value["Status"] = status

final_data.append(data_value)
print(final_data)

