import requests
import urllib.request
from bs4 import BeautifulSoup

# Set the URL for one swimmer
url = 'https://www.swimcloud.com/swimmer/549377/'
webUrl  = urllib.request.urlopen('https://www.swimcloud.com/swimmer/549377/')
# Send a GET request to the website
response = requests.get(url)
#print(response)
#print(webUrl.read())

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup)
f = open("schml.txt", "w")
f.write(str(soup))
f.close()

name = soup.find('title')
titleString = name.string
s1=titleString.replace("| Swimcloud","",1)

college = soup.find(text = 'team')
collegeString = str(college)
print(collegeString)
print(s1) #-> gets only the name of the swimmer from the website
# f2 = open("namecheck.txt", "w")
# f2.write(titleString + "\n" + s1)
# f2.close()
#find the way to get datas from the team and display.
#find a way to get a full name -> its after <title>
#final = get the rank of it



# Find the swimmer's first name
# name_elem = soup.find('h1', class_='page-header-title')
# first_name = name_elem.text.split()[0] if name_elem is not None else 'Unknown'

# # Find the swimmer's college
# college_elem = soup.find('div', class_='swimmer-college')
# college = college_elem.text.strip() if college_elem is not None else 'Unknown'

# # Find the swimmer's hometown
# hometown_elem = soup.find('div', class_='swimmer-hometown')
# hometown = hometown_elem.text.strip() if hometown_elem is not None else 'Unknown'

# # Find the swimmer's best times
# best_times_table = soup.find('table', class_='table-best-times')
# if best_times_table is not None:
#     best_times = best_times_table.find_all('tr')
#     for time in best_times:
#         event_elem = time.find('td', class_='event-name')
#         event = event_elem.text.strip() if event_elem is not None else 'Unknown'
#         time_elem = time.find('td', class_='event-time')
#         time = time_elem.text.strip() if time_elem is not None else 'Unknown'
#         print(event, time)

# Print the swimmer's first name, college, best times, and hometown
# print('First Name:', first_name)
# print('College:', college)
# #print('Best Times:')
# print('Hometown:', hometown)
