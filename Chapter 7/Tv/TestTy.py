from Tv import Tv

def main():
    tv1 = Tv()
    tv1.on = True
    tv1.setChannel(110)
    tv1.setVolume(3)

    tv2 = Tv()
    tv2.on = True
    tv2.channelUp()
    tv2.volumeUp()

    print("Tv1 channel is ", tv1.getChannel(), " and the volume is ", tv1.getVolume())
    print("Tv2 channel is ", tv2.getChannel(), " and the volume is ", tv2.getVolume())

main()