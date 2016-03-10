import re

f = open("asd-imdb-codes.txt", "r")
megadict = {}

for ep in f: #for each episode
                minimatrix = [[0]*6 for _ in range(5)] #initialize blank matrix
                
                #convert letter data to number data
                newstr = ep.split(":") 
                production_num = newstr[0]
                
                g = newstr[1]
                g = re.sub(r'C', r'0', g)
                g = re.sub(r'M', r'1', g)
                g = re.sub(r'D', r'2', g)
                g = re.sub(r'B', r'3', g)
                g = re.sub(r'F', r'4', g)
                g = re.sub(r'\*', r'5', g)

                teams = g.split() #split each string into its team groups by spaces

                for number in range(0,5): #for each character
                                for team in teams: #for each team group
                                                for member in team: #for each member of each team
                                                                if str(number) in team: #if the character is in the team make the corresponding matrix location a 1
                                                                                minimatrix[int(number)][int(member)]=1
                                                                
                megadict[production_num] = minimatrix #add the minimatrix to a key for the episode
                                
                
        
print(megadict)

f = open("asd-i.txt", "w")
f.write(str(megadict))
