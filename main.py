from PIL import Image
import math

def main():
    img1 = Image.open('Entradas\cp0-1-a-1.png')
    img2 = Image.open('Entradas\cp0-1-a-2.png')

    """ img1.show() """
    resultado2 = mono_green(img1)
    operaciones(resultado2)

    r""" 
    resultado1 = cambiar_rojo_y_azul(img1)
    resultado1.show()
    resultado1.save(r'C:\Users\Jorge\Documents\UNI\UNI12\Lab Vision Comp\CpO_1826182\Salidas\cp0-2-a-1.png')
    resultado2 = mono_green(img1)
    resultado2.show()
    resultado2.save(r'C:\Users\Jorge\Documents\UNI\UNI12\Lab Vision Comp\CpO_1826182\Salidas\cp0-2-b-1.png')
    resultado3 = mono_red(img1)
    resultado3.show()
    resultado3.save(r'C:\Users\Jorge\Documents\UNI\UNI12\Lab Vision Comp\CpO_1826182\Salidas\cp0-2-c-1.png')

    reemplazo_pixeles(mono_green(img1),mono_green(img2)).save(r'C:\Users\Jorge\Documents\UNI\UNI12\Lab Vision Comp\CpO_1826182\Salidas\cp0-3-a-1.png')
    """


def cambiar_rojo_y_azul(img):
    img = img.copy()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b,v = img.getpixel((x,y))
            img.putpixel((x,y),(100,g,100))
    return img
   

def mono_green(img):
    img = img.copy()
    valores = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b,v = img.getpixel((x,y))
            valores.append(g)
            img.putpixel((x,y),(0,g,0))
    return img
    

def mono_red(img):
    img = img.copy() 
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b,v = img.getpixel((x,y))
            
            img.putpixel((x,y),(r,0,0))
    return img
    

def reemplazo_pixeles(img1,img2):
    recorte = img1.crop(((img1.size[0]-100)/2,(img1.size[1]-100)/2,(img1.size[0]+100)/2,(img1.size[1]+100)/2))
    img2.paste(recorte,(int((img2.size[0]-50)/2),int((img2.size[1]-50)/2)))
    return img2

def operaciones(img):
    valores = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b,v = img.getpixel((x,y))
            valores.append(g)
            img.putpixel((x,y),(0,g,0))
    minima = min(valores)
    maxima = max(valores)
    media = sum(valores)/len(valores)
    desviacion_estandar = 0

    for i in valores:
        desviacion_estandar += ((media-i)**2)

    desviacion_estandar = math.sqrt(desviacion_estandar / (len(valores)-1))

    print('Maxima = '+str(maxima)+'\nMinima = '+str(minima)+'\nMedia = '+str(media)+'\nDesviacion estandar: '+str(desviacion_estandar))

def

    


if __name__ == "__main__":
    main()