import requests
import csv
r = requests.get('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=UUBhADBpNLBo8IP027XrxKAw&key={YOUR_API_KEY}')
d = r.json()


with open('videos.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    fields = ["title","video"]
    writer = csv.DictWriter(csvFile, fieldnames=fields)
    writer.writeheader()
    for video in d['items']:
        data = {'video': 'https://www.youtube.com/watch?v='+ video['snippet']['resourceId']['videoId'],'title': video['snippet']['title']}
        print(data)
        writer.writerow(data)

    r = requests.get('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=UUBhADBpNLBo8IP027XrxKAw&key={YOUR_API_KEY}&pageToken=CDIQAA')
    d = r.json()

    for video in d['items']:
        data = {'video': 'https://www.youtube.com/watch?v='+ video['snippet']['resourceId']['videoId'],'title': video['snippet']['title']}
        print(data)
        writer.writerow(data)

    r = requests.get('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=UUBhADBpNLBo8IP027XrxKAw&key={YOUR_API_KEY}&pageToken=CGQQAA')
    d = r.json()

    for video in d['items']:
        data = {'video': 'https://www.youtube.com/watch?v='+ video['snippet']['resourceId']['videoId'],'title': video['snippet']['title']}
        print(data)
        writer.writerow(data)

csvFile.close()


print(d['nextPageToken'])