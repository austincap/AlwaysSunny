<<<<<<< HEAD:mongo_process_always_sunny_data.py
import re
import pymongo
import json
import numpy
import operator
from pymongo import MongoClient
client = MongoClient(host='mongodb://austinc:apobianco@ds011238.mlab.com:11238/alwayssunny', port=11238)
db = client['alwayssunny']
collection = db['episodestats']

# import MySQLdb
# db=MySQLdb.connect(host="localhost", user="root", passwd="", db="test", port=3306)
# mysqlcursor = db.cursor()

#reading multi-type lists as arrays from text files is way harder than it needs to be
imdb_as_list = [['1.1', 8.6, 1316], ['1.2', 8.6, 1171], ['1.3', 8.7, 1154], ['1.4', 8.5, 1042], ['1.5', 8.4, 981], ['1.6', 8.5, 985], ['1.7', 8.7, 1059], ['2.1', 8.8, 1011], ['2.2', 8.8, 999], ['2.3', 9.1, 1202], ['2.4', 9.3, 1246], ['2.5', 9.0, 1104], ['2.6', 8.7, 908], ['2.7', 8.2, 846], ['2.8', 8.2, 827], ['2.9', 8.7, 894], ['2.10', 8.7, 852], ['3.1', 8.8, 946], ['3.2', 8.9, 988], ['3.3', 8.6, 814], ['3.4', 9.0, 990], ['3.5', 8.2, 815], ['3.6', 8.7, 820], ['3.7', 8.5, 756], ['3.8', 8.7, 808], ['3.9', 9.3, 1350], ['3.10', 9.1, 1033], ['3.11', 8.6, 774], ['3.12', 8.4, 720], ['3.13', 8.6, 711], ['3.14', 8.8, 805], ['3.15', 9.1, 1001], ['4.1', 8.6, 850], ['4.2', 9.2, 1135], ['4.3', 8.7, 752], ['4.4', 8.8, 748], ['4.5', 9.1, 855], ['4.6', 8.8, 740], ['4.7', 8.5, 908], ['4.8', 8.7, 737], ['4.9', 8.5, 753], ['4.10', 8.8, 831], ['4.11', 8.0, 786], ['4.12', 8.6, 762], ['4.13', 9.7, 2200], ['5.1', 8.4, 733], ['5.2', 9.1, 921], ['5.3', 8.2, 642], ['5.4', 8.9, 824], ['5.5', 8.8, 798], ['5.6', 8.4, 653], ['5.7', 8.5, 692], ['5.8', 9.1, 861], ['5.9', 8.6, 672], ['5.10', 9.2, 1057], ['5.11', 8.3, 662], ['5.12', 8.7, 680], ['6.1', 8.1, 684], ['6.2', 7.7, 621], ['6.3', 8.8, 755], ['6.4', 8.4, 626], ['6.5', 8.3, 622], ['6.6', 7.9, 584], ['6.7', 9.1, 822], ['6.8', 8.1, 605], ['6.9', 8.9, 717], ['6.10', 8.5, 641], ['6.11', 8.7, 631], ['6.12', 8.6, 608], ['6.13', 9.1, 1895], ['7.1', 8.8, 839], ['7.2', 9.1, 971], ['7.3', 8.3, 749], ['7.4', 8.0, 618], ['7.5', 7.0, 766], ['7.6', 8.3, 710], ['7.7', 9.1, 972], ['7.8', 8.5, 627], ['7.9', 8.7, 712], ['7.10', 8.0, 611], ['7.11', 8.9, 745], ['7.12', 8.3, 607], ['7.13', 8.5, 636], ['8.1', 8.2, 669], ['8.2', 8.4, 623], ['8.3', 8.8, 753], ['8.4', 9.1, 852], ['8.5', 8.8, 692], ['8.6', 7.8, 579], ['8.7', 8.2, 555], ['8.8', 8.4, 584], ['8.9', 8.8, 650], ['8.10', 8.8, 613], ['9.1', 8.8, 836], ['9.2', 8.3, 607], ['9.3', 9.3, 1016], ['9.4', 8.1, 551], ['9.5', 8.7, 670], ['9.6', 9.1, 876], ['9.7', 8.8, 630], ['9.8', 8.8, 648], ['9.9', 8.2, 607], ['9.10', 8.4, 543], ['10.1', 8.6, 868], ['10.2', 8.9, 774], ['10.3', 7.7, 652], ['10.4', 9.8, 2664], ['10.5', 8.4, 568], ['10.6', 9.0, 718], ['10.7', 8.2, 485], ['10.8', 8.8, 634], ['10.9', 8.3, 472], ['10.10', 7.8, 474], ['11.1', 8.9, 507], ['11.2', 8.2, 390], ['11.3', 8.9, 649], ['11.4', 7.7, 312], ['11.5', 9.3, 575], ['11.6', 8.5, 297],['11.7', 8.8, 386],['11.8', 9.1, 321],['11.9', 8.9, 136],['11.10', 9.0, 24]]

f = open("asd-imdb-codes.txt", "r")

megadict = []
for ep in f: #for each episode
	minidict = {} #initialize blank dict
	
	#get epID
	newstr = ep.split(":") 
	production_num = newstr[0]
	minidict['epID'] = production_num

	g = newstr[1]
	teams = g.split() #split each string into its team groups by spaces
	groups = []
	#add groups
	for team in teams:
		if '*' in team: #denote winner
			minidict['winner'] = team.replace('*','')
		groups += [team.replace('*','')]
		minidict['groups'] = groups
	#add imdb ratings
	for epg in imdb_as_list:
		if production_num in epg:
			minidict['imdbrating'] = epg[1]

	print(minidict)
	#collection.insert_one(minidict) #UNCOMMENT THIS LINE TO ADD TO MONGODB
	megadict += [minidict] #add the minidict to the overall list
f.close()


#create json 
with open('asd-mongo.json', 'w') as f:
	f.write(json.dumps(megadict))


=======
import re
import pymongo
import json
import numpy
import operator
from pymongo import MongoClient
client = MongoClient(host='mongodb://austinc:apobianco@ds011238.mongolab.com:11238/alwayssunny', port=11238)
db = client['alwayssunny']
collection = db['episodestats']

# import MySQLdb
# db=MySQLdb.connect(host="localhost", user="root", passwd="", db="test", port=3306)
# mysqlcursor = db.cursor()

#reading multi-type lists as arrays from text files is way harder than it needs to be
imdb_as_list = [['1.1', 8.6, 1316], ['1.2', 8.6, 1171], ['1.3', 8.7, 1154], ['1.4', 8.5, 1042], ['1.5', 8.4, 981], ['1.6', 8.5, 985], ['1.7', 8.7, 1059], ['2.1', 8.8, 1011], ['2.2', 8.8, 999], ['2.3', 9.1, 1202], ['2.4', 9.3, 1246], ['2.5', 9.0, 1104], ['2.6', 8.7, 908], ['2.7', 8.2, 846], ['2.8', 8.2, 827], ['2.9', 8.7, 894], ['2.10', 8.7, 852], ['3.1', 8.8, 946], ['3.2', 8.9, 988], ['3.3', 8.6, 814], ['3.4', 9.0, 990], ['3.5', 8.2, 815], ['3.6', 8.7, 820], ['3.7', 8.5, 756], ['3.8', 8.7, 808], ['3.9', 9.3, 1350], ['3.10', 9.1, 1033], ['3.11', 8.6, 774], ['3.12', 8.4, 720], ['3.13', 8.6, 711], ['3.14', 8.8, 805], ['3.15', 9.1, 1001], ['4.1', 8.6, 850], ['4.2', 9.2, 1135], ['4.3', 8.7, 752], ['4.4', 8.8, 748], ['4.5', 9.1, 855], ['4.6', 8.8, 740], ['4.7', 8.5, 908], ['4.8', 8.7, 737], ['4.9', 8.5, 753], ['4.10', 8.8, 831], ['4.11', 8.0, 786], ['4.12', 8.6, 762], ['4.13', 9.7, 2200], ['5.1', 8.4, 733], ['5.2', 9.1, 921], ['5.3', 8.2, 642], ['5.4', 8.9, 824], ['5.5', 8.8, 798], ['5.6', 8.4, 653], ['5.7', 8.5, 692], ['5.8', 9.1, 861], ['5.9', 8.6, 672], ['5.10', 9.2, 1057], ['5.11', 8.3, 662], ['5.12', 8.7, 680], ['6.1', 8.1, 684], ['6.2', 7.7, 621], ['6.3', 8.8, 755], ['6.4', 8.4, 626], ['6.5', 8.3, 622], ['6.6', 7.9, 584], ['6.7', 9.1, 822], ['6.8', 8.1, 605], ['6.9', 8.9, 717], ['6.10', 8.5, 641], ['6.11', 8.7, 631], ['6.12', 8.6, 608], ['6.13', 9.1, 1895], ['7.1', 8.8, 839], ['7.2', 9.1, 971], ['7.3', 8.3, 749], ['7.4', 8.0, 618], ['7.5', 7.0, 766], ['7.6', 8.3, 710], ['7.7', 9.1, 972], ['7.8', 8.5, 627], ['7.9', 8.7, 712], ['7.10', 8.0, 611], ['7.11', 8.9, 745], ['7.12', 8.3, 607], ['7.13', 8.5, 636], ['8.1', 8.2, 669], ['8.2', 8.4, 623], ['8.3', 8.8, 753], ['8.4', 9.1, 852], ['8.5', 8.8, 692], ['8.6', 7.8, 579], ['8.7', 8.2, 555], ['8.8', 8.4, 584], ['8.9', 8.8, 650], ['8.10', 8.8, 613], ['9.1', 8.8, 836], ['9.2', 8.3, 607], ['9.3', 9.3, 1016], ['9.4', 8.1, 551], ['9.5', 8.7, 670], ['9.6', 9.1, 876], ['9.7', 8.8, 630], ['9.8', 8.8, 648], ['9.9', 8.2, 607], ['9.10', 8.4, 543], ['10.1', 8.6, 868], ['10.2', 8.9, 774], ['10.3', 7.7, 652], ['10.4', 9.8, 2664], ['10.5', 8.4, 568], ['10.6', 9.0, 718], ['10.7', 8.2, 485], ['10.8', 8.8, 634], ['10.9', 8.3, 472], ['10.10', 7.8, 474], ['11.1', 8.9, 507], ['11.2', 8.2, 390], ['11.3', 8.9, 649], ['11.4', 7.7, 312], ['11.5', 9.3, 575], ['11.6', 8.5, 297]]

f = open("asd-imdb-codes.txt", "r")

megadict = []
for ep in f: #for each episode
	minidict = {} #initialize blank dict
	
	#get epID
	newstr = ep.split(":") 
	production_num = newstr[0]
	minidict['epID'] = production_num

	g = newstr[1]
	teams = g.split() #split each string into its team groups by spaces
	groups = []
	#add groups
	for team in teams:
		if '*' in team: #denote winner
			minidict['winner'] = team.replace('*','')
		groups += [team.replace('*','')]
		minidict['groups'] = groups
	#add imdb ratings
	for epg in imdb_as_list:
		if production_num in epg:
			minidict['imdbrating'] = epg[1]

	print(minidict)
	#collection.insert_one(minidict) #add to mongo
	megadict += [minidict] #add the minidict to the overall list
f.close()


#create json 
with open('ads-mongo.json', 'w') as f:
	f.write(json.dumps(megadict))


>>>>>>> origin/master:wrangling-scraping-scripts/mongo_process_always_sunny_data.py
