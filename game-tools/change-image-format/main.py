from PIL import Image
import ui as UI

def isImage(path):
    ret = True
    try:
        Image.open(path).verify()
    except:
        ret = False
    return ret
def formatImage(path):
    if isImage(path):
        try:
            str = path.rsplit('.',1)
            output_path = str[0] + ".jpg"
            print(output_path)
            im = Image.open(path)
            rgb_img = im.convert('RGB')
            rgb_img.save(output_path, quality=100)
            return True
        except Exception as e:
            print('error', e)
            return False
    else:
        print('not image')
        return False

if __name__ == '__main__':
    path = 'bg.png'
    print(formatImage(path))
    ui = UI.MainUI()
    ui.run()
