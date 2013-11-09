Practica2: Aislamiento de una aplicación web.
=========

###Crear una mini-aplicación web (un hola mundo o un simple formulario) y aislarlo en una jaula chroot.


Vamos a crear una jaula Ubuntu con 'deboostrap' para poder instalar dicho sistema Ubuntu en la jaula. Ejecutamos por tanto lo siguiente:

`sudo debootstrap --arch=amd64 quantal /home/quantal/   http://archive.ubuntu.com/ubuntu`
