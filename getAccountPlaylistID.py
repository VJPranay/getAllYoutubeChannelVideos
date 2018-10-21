import requests
r = requests.get('https://www.googleapis.com/youtube/v3/channels?part=contentDetails&mine=true&key={YOUR_API_KEY}')
d = r.json()
print(d['items']['contentDetails']['relatedPlaylists']['uploads'])

# For more info visit here > https://developers.google.com/apis-explorer/?hl=en_US#p/youtube/v3/youtube.channels.list?part=contentDetails&mine=true&_h=1&

# for more info visit here > https://www.youtube.com/watch?v=nn5i_lBQ9kI

