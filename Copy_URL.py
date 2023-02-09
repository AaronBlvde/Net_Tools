from pywebcopy import save_webpage

def Webpage_downloader():
    kwargs = {'project_name':'uniciv_site'}

    input_url = input('URL: ')
    print('Please wait...')

    save_webpage(
        url=input_url,
        project_folder = 'Clone_web/',
        **kwargs
    )

Webpage_downloader()
