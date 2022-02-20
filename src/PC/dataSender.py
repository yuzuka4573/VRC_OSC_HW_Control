from pythonosc import udp_client
import argparse
import time
import serial


def main(ip, port, com):
    sr = serial.Serial(com,115200,timeout=0.1)
    client = udp_client.SimpleUDPClient(ip, port)
    print('init complete')

    while True:        
        result = int(sr.readline())
        print(str(result))
        if result >-1:
            client.send_message("/test/3/int",result )
            


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', default='127.0.0.1', type=str, help = 'The ip of target OSC server.')
    parser.add_argument('--port', default='9000', type=int, help = 'The port that target OSC server listening on')
    parser.add_argument('--com', default='COM9', type=str, help= 'The communication Port that listening device sensor value',required = True)
    args = parser.parse_args()
    main(args.ip,args.port,args.com,)

