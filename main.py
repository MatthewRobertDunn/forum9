import personality as personality
#import contestant as contestant

announcer = personality.Somad()
#contestant = contestant.Contestent()


message = announcer.send("I'm here. Let's begin the show")
print(message)

#while True:
    #message = contestant.send_gpt(message)
    #print("----Contestant----")
    #print(message)
    #message = announcer.send_gpt(message)
    #print("----Announcer----")
    #print(message)