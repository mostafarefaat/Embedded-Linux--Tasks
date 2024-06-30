import webbrowser

WebSites ={

    'Facebook' : 'https://www.facebook.com',
    'YouTube' : 'https://www.youtube.com',
    'Reddit' : 'https://www.reddit.com/?rdt=37213',
    'Amazon' : 'https://www.amazon.com/',
    'Twitter' : 'https://x.com/',
    'Google' :  'https://www.google.com',

}


def FireFox(url):
    webbrowser.get('firefox').open_new_tab(url)

