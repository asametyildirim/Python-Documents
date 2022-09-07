from pytube import YouTube

""" 
get_link = YouTube("https://www.youtube.com/watch?v=wLlovxa3VJ0&ab_channel=CelestialDraconis")
show_stream = get_link.streams.filter(progressive="True").first()
show_stream.download()
"""

def download_video:
	url = Youtube(input("Please enter the youtube url"))
	download_link = url.streams.filter(progressive="True").first()
	download_link.download()

	print("-"*25)
	print("Video title: ",url.title)
	print("Video author: ",url.author)
	print("Video viewer count: ",url.views)
	print("Video lenght: ",url.lenght,"second")
	print("-"*25)

download_video()