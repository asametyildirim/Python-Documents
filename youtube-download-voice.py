from pytube import YouTube


def download_voice:
	url = Youtube(input("Please enter the youtube url"))
	download_link = url.streams.filter(mime_type="audio/mp4").first()
	download_link.download()

	print("-"*25)
	print("Voice title: ",url.title)
	print("Voice author: ",url.author)
	print("Voice viewer count: ",url.views)
	print("Voice lenght: ",url.lenght,"second")
	print("-"*25)

download_voice()