import telepot
import ENV

token = ENV.token
beerbot = telepot.Bot(token)
# print (beerbot.getMe())
beerbot.getUpdates()