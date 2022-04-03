from PIL import ImageGrab

def screen_capture(n, fdir):
    for i in range(n):
        img = ImageGrab.grab(bbox=(440, 320, 1300, 800))
        img.save(f'{fdir}/{str(i).zfill(2)}.png')

fdir = '/home/pi/Desktop/108python/imgs'
screen_capture(40, fdir)