import webbrowser

# Browser Paths
edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"


def search(txt, browser, engine):
    url_youtube_search = "https://www.youtube.com/results?search_query={}".format(txt)
    url_google_search = "https://www.google.com/search?gs_ssp=eJzj4tTP1TcwzqtKMzRg9OJMzcnPU8gtLc4GAEjMBtM&q={}&oq=elo&aqs=chrome.1.69i57j46i67i433j0i67i433l2j0i67j0i433i512j0i67i433j46i131i433j0i433i512j0i271.1591j0j7&sourceid=chrome&ie=UTF-8#cobssid=s".format(
        txt)
    url_edge = ''
    url_songs_playlist = "https://www.youtube.com/watch?v=Jbl_7LQudeI&list=RDMMJbl_7LQudeI&start_radio=1"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    if engine:
        webbrowser.get(browser).open_new_tab(url_youtube_search)
    elif "music" not in txt:
        webbrowser.get(browser).open_new_tab(url_google_search)
    elif "music" in txt:
        webbrowser.get(browser).open_new_tab(url_songs_playlist)
    if browser == 'edge':
        webbrowser.get(browser).open_new_tab(url_edge)

