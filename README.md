# AlwaysSunny
Some files and scripts needed for analyzing Always Sunny

The purpose of this pet project is to see if there are any patterns in the data I personally extracted from each episode of Always Sunny in Philadelphia, specifically: what makes a good episode? Data is tragically underutilized in the art world. While watching the show I noticed that the writers seemed to emphasize the fact that the core group splits up in different ways, and that in some episodes there seem to be a clear "winner." Ultimately this sort of "character grouping" analysis is applicable to all episodic, character-driven TV-shows.

I started with [this data coded by hand for fun](always%20sunny%20data.txt) and converted everything (again by hand but not as fun) to both episode production codes and episode codes used by imdb.

Then I turned that data into [a dictionary of matrices](asd-i.txt) to represent which character grouped with who and whether or not that team "won" for each episode using [this script](process_always_sunny_data.py). I tried running it on [a simple neural net](neural_net_always_sunny.py) with [IMDB ratings for the label data](label_data_always_sunny.py) just to see what happened (nothing useful).

I wanted to make some Tableau viz's of this but I couldn't think of a good way to convert my data into a MySQL database. Fortunately I found [Simba's Mongo->SQL->Tableau conversion drivers](http://www.simba.com/webinar/connect-tableau-mongodb/). I consolidated my raw data and imdb ratings in to a mongo database with [this script](mongo_process_always_sunny_data.py).

So far the most interesting thing all this work has produced is [this image I made in Tableau that shows what groups made for the best episodes](best-eps.png).
