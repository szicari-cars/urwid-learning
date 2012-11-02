import urwid

ask = urwid.Edit(u"What is your name?\n")
fill = urwid.Filler(ask)

def do_reply(input):
  if input is not 'enter':
    return
  if fill.body == ask:
    fill.body = urwid.Text(u"Nice to meet you, %s." % ask.edit_text)
    return True
  else:
    raise urwid.ExitMainLoop()

loop = urwid.MainLoop(fill, unhandled_input=do_reply)
loop.run()

