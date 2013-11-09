Practica2: Aislamiento de una aplicación web.
=========

###Crear una mini-aplicación web (un hola mundo o un simple formulario) y aislarlo en una jaula chroot.

##Introdución

Vamos a crear una aplicación básica en Python que consistirá de un formulario. La ejecutaremos con una distribución Debian
encerrada previamente en una jaula.

##Doucumentación

Vamos a crear una jaula con un sistema Debian de 32 bits (ya que lo tenía instalado previamente) con 'deboostrap'.
Pero primero vamos a crearnos el directorio siguiente /home/jaulas/debian `sudo mkdir -p /home/jaulas/debian` y una vez
dentro de /home/jaulas ejecutamos:

`sudo debootstrap --arch=i386 wheezy debian http://ftp.debian.org/debian/`

Como vemos, en mi caso el sistema será de 32 bits (ya que mi sistema anfitrión es de 32 bits).

Accedemos a la distribución creada con `sudo chroot /home/jaulas/debian`

Configuramos un poco la distribución con:
```
mount -t proc proc /proc
apt-get install language-pack-es
```
Con esto hemos completado la distribución e instalado un paquete de idiomas para que soporte el español.
Ahora que tenemos nuestra distribución configurada correctamente tenemos que instalar las herramientas que harán falta
para nuestra aplicación.
Vamos a necesitar instalar 'python' y 'python-web2py'

```
apt-get install python
apt-get install python-web2py
```

Estoy teniendo problemas a la hora de ejecutar mi aplicación y me doy cuenta de que por algún casual el paquete 'python-web2py' 
no funciona correctamente, asique procedo a descargarmelo desde los repositorios 'github'. Para ello seguimos los siguientes
comandos:

```
apt-get install git
git clone git://github.com/webpy/webpy.git
cd webpy/
python setup.py install 
```
Ya lo tenemos instalado.

Ahora copiamos el formulario (que está en la máquina anfitriona) a la carpeta /home/jaulas/debian/home/webpy/web
`sudo cp formulario.py /home/jaulas/debian/home/` y ejecutamos la aplicación con `python formulario.py` .

![imagen1_p2](https://dl.dropboxusercontent.com/s/dacay8jzpp2x4x3/practica2_1.png)
![imagen2_p2](https://dl.dropboxusercontent.com/s/udaarjg5hio53zm/practica2_2.png)

Vemos que funciona perfectamente.


sd


