from wxpy import *
import d11_training1
bot = Bot()

my_friend = bot.friends().search('家')[0]
my_friend.send('分享')

@bot.register(my_friend)

def get_msg(msg):
    if msg.type == 'Sharing':
      target_url = msg.url

      stats_msg = d11_training1.stats(target_url)
      my_friend.send(stats_msg)
    else :
        pass

embed()
   
