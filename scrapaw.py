################################################################################
################################################################################
####																	   #####
####  Copyright (C) 2021-2022, Loubaris									   #####
####																	   #####
####  This program is free software; you can redistribute it and/or modify #####
####  it under the terms of the GNU General Public License as published by #####
####  the Free Software Foundation; either version 2 of the License, or	   #####
####  (at your option) any later version.								   #####
####																	   #####
####  This program is distributed in the hope that it will be useful,	   #####
####  but WITHOUT ANY WARRANTY; without even the implied warranty of	   #####
####  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the		   #####
####  GNU General Public License for more details.						   #####
####																	   #####
####  You must obey the GNU General Public License. If you will modify	   #####
####  this file(s), you may extend this exception to your version		   #####
####  of the file(s), but you are not obligated to do so.  If you do not   #####
####  wish to do so, delete this exception statement from your version.    #####
####  If you delete this exception statement from all source files in the  #####
####  program, then also delete it here.								   #####
####																	   #####
####  Contact:															   #####
#### 																	   #####
####		  Mail: adamou.loubaris@gmail.com							   #####
####																	   #####
################################################################################
################################################################################


import os
import time
import sys
try:
	import requests
except Exception as e:
	print(f"Module requests is not installed\nError {e}")
logo = """
.▄▄ ·  ▄▄· ▄▄▄   ▄▄▄·  ▄▄▄· ▄▄▄· ▄▄▌ ▐ ▄▌
▐█ ▀. ▐█ ▌▪▀▄ █·▐█ ▀█ ▐█ ▄█▐█ ▀█ ██· █▌▐█
▄▀▀▀█▄██ ▄▄▐▀▀▄ ▄█▀▀█  ██▀·▄█▀▀█ ██▪▐█▐▐▌
▐█▄▪▐█▐███▌▐█•█▌▐█ ▪▐▌▐█▪·•▐█ ▪▐▌▐█▌██▐█▌
 ▀▀▀▀ ·▀▀▀ .▀  ▀ ▀  ▀ .▀	▀  ▀  ▀▀▀▀ ▀▪
 made by Loubaris | github.com/Loubaris   

 """
 

menu = """
Commands
 - scrape <shodan> <sub+ject> <path_to_save> | Scrape IPs across the world
 - exit                                      | Exit program
API
 - 'from scrapaw import scrape'
 - 'scrape("shodan Example+Test+Android /Desktop/")'
(scrapaw)>"""

def scrape(command):
	print("(scrapaw) - Launching scraping module..\n")
	if command[1] == "shodan":
		argv1 = command[2]
		if argv1 == "":
			print("Error, subject of search is empty. \nUsage: scrape <shodan> <sub+ject>")
		else:
			try:
				print("- Connecting to shodan")
				#req = requests.get(f"https://www.shodan.io/search?query={argv1}", "html.parser")
				#curl_brut = open("curl_brut.txt", "w")
				#curl_brut.write(req.text)
				#curl_brut.close()
				curl_brut = open("curl_brut.txt", "r")
				curl_brut_content = curl_brut.read()
				curl_brut.close()
				os.remove("curl_brut.txt")
				curl_result = open("curl_result.txt", "w")
				print("- Filtering results")
				for line in curl_brut_content.splitlines():
					if "heading" in line:
						if "h6" in line:
							pass
						else:
							curl_result.write(f'{line}\n')
				curl_result.close()
				try:
					for line in curl_brut_content.splitlines():
						if "limit" in line:
							print(f"Error while connecting to https://www.shodan.io/search?query={argv1}\n- Shodan daily usage limit excecced")
							os.remove("curl_result.txt")
							os.remove("shodan_list_ip.txt")
						else: 
							try:
								curl_result = open('curl_result.txt', "r")
								content_curl = curl_result.readlines()
								curl_result.close()
								if command[3] == "":
									ips = open(f"shodan_list_ip.txt", "w")
								else:
									ips = open(f"{command[3]}/shodan_list_ip.txt", "w")
								for line in content_curl:
									line = line.split("title", 1)[0]
									result_ip = ''.join(i for i in line if i.isdigit() or i==".")
									ips.write(f'{result_ip}\n')
								ips.close()
							except Exception as e:
								print(f"Error while reading result \nError {e}")
					print(f"- Results: {command[3]}shodan_list_ip.txt")
					results = open(f'{command[3]}shodan_list_ip.txt', "r")
					print(f"- {results.read()}")
					results.close()
				except Exception as e:
					print(f"Error while reading https://www.shodan.io/search?query={argv1} result \nError {e}")
			except Exception as e:
				print(f"Error while connecting to https://www.shodan.io/search?query={argv1} \nError {e}")

	else:
		print("(scrapaw) - Usage: scrape <shodan> <sub+ject> <path_to_save>)")


def main():
	os.system("cls")
	print(logo)
	command = input(menu)
	command = command.split()
	for i in range(5):
		try:
			command[i]
		except Exception as e:
			command.append("")
	if command[0] == "scrape":
		scrape(command)
	else:
		print("(scrapaw) - Unknown command")

	if command[0] != "exit":
		os.system("set /p DUMMY=Press Enter to continue")
	else:
		sys.exit()
	os.system("cls")

while True:
	try:
		main()
	except KeyboardInterrupt:
		print(" Exiting..")
		sys.exit()