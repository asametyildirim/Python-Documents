from pytube import YouTube

url = YouTube("https://www.youtube.com/watch?v=5Kx2I0wU96Y")

print("Video title: ",url.title)
print("Video author: ",url.author)