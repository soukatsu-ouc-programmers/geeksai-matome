import twint
c = twint.Config()
c.Search = '#技育祭'
c.Search = '#RoomC'
# c.Since = '2020-07-03 15:00:00'
# c.Until = '2020-07-05 15:00:00'
c.Since = '2020-07-04 00:00:00'
c.Until = '2020-07-06 00:00:00'
c.Store_json = True
c.Output = 'roomc.json'
c.Hide_output = True
twint.run.Search(c)
