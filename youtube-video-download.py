from pytube import YouTube

get_link = YouTube("https://www.youtube.com/watch?v=wLlovxa3VJ0&ab_channel=CelestialDraconis")
show_stream = get_link.streams.filter(progressive="True").first()
show_stream.download()