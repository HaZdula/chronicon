from ao3 import AO3
import getpass

def get_update():
    from ao3 import AO3
    api = AO3()
    api.login(input('Login: '), getpass.getpass('Pass: '))
    
    b_id, b_chapters = api.user.bookmarks_ids()
    
    empty = True
    for i in range(len(b_id)):
        work = api.work(b_id[i])
        if b_chapters[i] <= work.published_chapters:
            print('UPDATE: ', work.title, 
                  "\nChapters ahead: ", work.published_chapters - b_chapters[i] + 1,
                  "\nChapter now: ", b_chapters[i],
                  "\nFandom: ", work.fandoms[0],
                  "\nLink: ", work.url,
                  "\n"
                 )
            empty = False

    if empty:
        print("No updates")

get_update()