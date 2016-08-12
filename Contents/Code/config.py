ITV_CATCHUP                   = "http://www.ITVhttp://www.itv.com/_data/xml/CatchUpData/CatchUp360/CatchUpMenu.xml.co.uk"
ITV_URL                       = "http://www.ITVhttp://www.itv.com/_data/xml/CatchUpData/CatchUp360/CatchUpMenu.xml.co.uk"
ITV_FEED_URL                  = "http://feeds.ITV.co.uk"
ITV_SD_PLAYER_URL             = "%s/iplayer/episode/%%s" % ITV_URL
ITV_HD_PLAYER_URL             = "%s/iplayer/episode/%%s/hd" % ITV_URL
ITV_LIVE_TV_URL               = "%s/iplayer/tv/%%s/watchlive" % ITV_URL
ITV_TV_CHANNEL_THUMB_URL      = "%s/iplayer/img/tv/%%s.jpg" % ITV_URL
ITV_THUMB_URL                 = "http://ichef.ITVi.co.uk/programmeimages/%s/%s_640_360.jpg"

ITV_SEARCH_URL                = "%s/iplayer/search?q=%%s" % ITV_URL
ITV_SEARCH_TV_URL             = ITV_SEARCH_URL + "&filter=tv"

RE_ORDER = Regex('class="cta-add-to-favourites" href="pid-(.*?)"')
RE_PID = Regex('iplayer/episode/([^/$]{8})')

MP3_URL = String.Decode('aHR0cDovL29wZW4ubGl2ZS5iYmMuY28udWsvbWVkaWFzZWxlY3Rvci81L3NlbGVjdC9tZWRpYXNldC9odHRwLWljeS1tcDMtYS92cGlkLyVzL2Zvcm1hdC9wbHMucGxz')
HLS_URL = String.Decode('aHR0cDovL29wZW4ubGl2ZS5iYmMuY28udWsvbWVkaWFzZWxlY3Rvci81L3NlbGVjdC92ZXJzaW9uLzIuMC9mb3JtYXQvanNvbi9tZWRpYXNldC9hcHBsZS1pcGFkLWhscy92cGlkLyVz')

RADIO_IMG_URL = 'http://static.ITVi.co.uk/radio/690/1.39/img/backgrounds/services/%s_t1.jpg'


# def CATS():
#     addDir('ITV Player', 'http://www.itv.com/_data/xml/CatchUpData/CatchUp360/CatchUpMenu.xml', 1, icon, isFolder=True)
#     if os.path.exists(favorites) == True:
#         addDir('[COLOR yellow]Favorites[/COLOR]', 'url', 12, '')
#     addDir('ITV1 Live', 'http://itv1liveios-i.akamaihd.net/hls/live/203437/itvlive/ITV1MN/master_Main1800.m3u8', 7,
#            foricon + 'art/1.png', isFolder=False)  # sim1
#     addDir('ITV2 Live', 'http://itv2liveios-i.akamaihd.net/hls/live/203495/itvlive/ITV2MN/master_Main1800.m3u8', 7,
#            foricon + 'art/2.png', isFolder=False)  # sim2
#     addDir('ITV3 Live', 'http://itv3liveios-i.akamaihd.net/hls/live/207262/itvlive/ITV3MN/master_Main1800.m3u8', 7,
#            foricon + 'art/3.png', isFolder=False)  # sim3
#     addDir('ITV4 Live', 'http://itv4liveios-i.akamaihd.net/hls/live/207266/itvlive/ITV4MN/master_Main1800.m3u8', 7,
#            foricon + 'art/4.png', isFolder=False)  # sim4
#     addDir('ITVBe Live', 'http://itvbeliveios-i.akamaihd.net/hls/live/219078/itvlive/ITVBE/master_Main1800.m3u8', 7,
#            foricon + 'art/8.jpg', isFolder=False)
#     addDir('CITV Live', 'http://citvliveios-i.akamaihd.net/hls/live/207267/itvlive/CITVMN/master_Main1800.m3u8', 7,
#            foricon + 'art/7.png', isFolder=False)  # sim7
#     setView('tvshows', 'default')