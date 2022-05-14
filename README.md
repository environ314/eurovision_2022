# Eurovision 2022

This is a repo hosting data and analysis from Eurovision 2022. The basic idea is that I suspect loads of people will be wanting to play around with Eurovision data both before and after the Grand Final, and there's no point everyone converting PDFs into CSVs (etc) separately when we could just do it all in one go.

My code's all in R but hopefully the files I produce will be usable regardless of language.

eurovision_spotify_data_2022.csv contains metadata from Spotify's "Eurovision 2022" playlist as of the afternoon of 2022.05.14. So if you want to know what key something's in or the BPM, you can get that here. You can also get estimates of things like "liveness", "acousticness", and so on. 

spotify features 2022.R is a script to produce that. To run your own, you'll need access to the Spotify API: this was straightforward when I set it up years ago but I can't comment on what it's like now.

semi qualifiers info.R adds variables for whether or not countries qualified, and which semi-final they were in.
