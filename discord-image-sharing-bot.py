import discord
import random
import pandas as pd
import ast
import sys
#version 0.7
#data
#first and only line is our bot token, so we are only reading it
bot_token = open("discord_token.txt", "r").read()
url_list = pd.read_csv("url_list.csv", index_col=0)

client = discord.Client()
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

#    if message.content.startswith('!exit'):
#        sys.exit(0)
#    use this thing when debugging bot, easier than restarting terminal

#       gets pic with title, i had some faulty results with it, but iloc[0][columns] solved the issue
    if message.content.startswith('!title'):
        try:
            #we strip title from any spaces and !title string and we make a mask to search on our dataframe
            #after that we send our results to discord channel
            title = message.content[7:].strip()
            mask  = "title=='{0}'".format(title)
            data  = url_list.query(mask)
            res_str = data.iloc[0]['title']
            res_url = data.iloc[0]['url']
            msg = 'title: {string} , url: {url}'.format(string=res_str, url=res_url)
            await message.channel.send(msg)  
        except Exception as e :
            #if an error occures we send error msg to discord channel, and print error here on terminal
            print(e)
            msg = 'Bir hata çıktı, girdiğiniz veriyi kontrol edin.'
            await message.channel.send(msg)

#       gets pic with the index 
    if message.content.startswith('!index'):
        try:
            #we strip text from !index string and get it as integer, so we can locate the image with that index
            #after that we send message to discord server
            index_num = int(message.content[7:])
            data = url_list.iloc[index_num]
            msg = 'title : {title} , url : {url}'.format(title=data['title'], url=data['url'])

            await message.channel.send(msg)

        except:
            #same as above
            msg = 'Bir hata çıktı, girdiğiniz sayıyı kontrol edin.'
            await message.channel.send(msg)

    if message.content.startswith('!help'):
        msg = "Kullanılabilecek komutlar: \n \
hello, size merhaba der, \n \
!random, rastgele bir fotoğraf paylaşır \n \
!index, size girdiğiniz indexteki fotoğrafı getirir, aklınızdan 0 ve {max_index} arasında bir sayı tutun! \n \
!title, size girdiğiniz isimdeki fotoğrafı getirir, \n \
!upload komutu ile resim listesine resim ekleyebilirsiniz. \n \
!upload 'title' : 'titleınız', 'url' : 'urlniz' şeklinde girdiğiniz zaman upload gerçekleşir".format(max_index=url_list.shape[0]-1)
        await message.channel.send(msg)
 
 
    if message.content.startswith('!random'):
        #crates random int between max index and 0 and sends it to discord server
        index = random.randint(0,url_list.shape[0])
        data = url_list.iloc[index]
        msg = 'title : {title} , url : {url}'.format(title=data['title'], url=data['url'])
        msg2 = data['url']
        await message.channel.send(msg)
    
 
    if message.content.startswith('!hello'):
        msg = 'Merhaba {0.author.mention}, iki zara yetmişlik olduk. Bizi mi koparıyosun {0.author.mention}!!!'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!upload'):
        #first we get text and surround it in {} so we can make a dictionary from text we got(at !help command i specified format of upload so it will work)
        #after making it a dictionary we add it to our csv list and save it, and we send success text to discord channel
        try:
            text = '{' + message.content[8:] + '}'
            text_dict = ast.literal_eval(text)
            url_list2 = url_list.append(text_dict, ignore_index=True)
            url_list2.to_csv('url_list.csv')
            msg = 'Yükleme başarılı, bot tekrar başlatıldığında paylaşma listesine eklenecek.(Bu feature şu an bozuktur, liste şekli değiştiğinde doğru çalışacak.)'
            await message.channel.send(msg)
        except Exception as e:
            #same as other commands
            print(e)
            msg = 'Yükleme başarısız, girdiğiniz değerleri kontrol edin'
            await message.channel.send(msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(bot_token)