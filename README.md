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


