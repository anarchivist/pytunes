import web, appscript

interface = appscript.app("iTunes")
render = web.template.render('templates/')

urls = (
  '/', 'main',
  '/prev', 'prev',
  '/next', 'next',
  '/playpause', 'playpause',

)

def curr():
  track = interface.current_track()
  return [track.artist(), track.name(), track.album()]

class main:
  def GET(self, query_string):
    ct = " - ".join(curr())
    print render.base(track = ct)
    print render.bottom

class prev:
  def GET(self):
    interface.previous_track()
    ct = " - ".join(curr())
    print render.base(track = ct)
    print "<b>Previous track requested</b>"
    print render.bottom
    
class next:
    interface.next_track()
    ct = " - ".join(curr())
    print render.base(track = ct)
    print "<b>Next track requested</b>"
    print render.bottom

class playpause:
    interface.playpause()
    ct = " - ".join(curr())
    print render.base(track = ct)
    print "<b>Toggled play/pause</b>"
    print render.bottom

web.webapi.internalerror = web.debugerror
if __name__ == '__main__': web.run(urls, globals())
