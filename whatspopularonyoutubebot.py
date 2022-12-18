import pytube
from pytube import Playlist
import py_youtube
#have to install py-youtube because the metadata from pytube is bugging

p = Playlist("https://www.youtube.com/playlist?list=PLrEnWoR732-BHrPp_Pm8_VleD68f9s14-")

keywordDict = {}
categoryDict = {}
for video in p.videos:
    print(type(video))
