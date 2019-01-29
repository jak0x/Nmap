#*****************Programa de prueba de mejora para nmap en Python***********************************************
# Author: jak0x

import shlex
import subprocess

#**************OPCIONES GENERALES********************************

opcion0 = int(input("Elija una opcion:\n"+"1-Descubrimiento\n"+"2-Analisis de Puertos\n"+"3-Analisis de Servicios y S.O\n"+"4-Evasión\n"+"0-Salir\n\n"))

#**************Descubrimiento************************************

if opcion0 == 1:
    print("**********************************************************************************************")
    objetivo = input("\nIntroduzca un objetivo: ")
    lista = shlex.split(objetivo)
    opcion1 = int(input("Elija una opción:\n"+"1-Ping compuesto\n"+"2-TCP SYN ping\n"+"3-TCP ACK ping\n"
    + "4-UPD ping\n"+"5-SCTP Init ping\n"+"6-ICMP echo pingn"+"7-ICMP Timestamp ping\n"+"8-ICMP adress mask ping\n"
    +"9-IP protocol ping\n"+"10-ARP ping"+"11-Traceroute\n"+"12-No realizar ping\n"+"13-Crear un listado de host\n"
    +"14-Leyenda_Opciones\n"+"0-Salir\n\n"))
    

    if opcion1 == 1:
        command_line = ('nmap -sP ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion1 == 2:
        command_line = ('nmap -PS ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion1 == 3:
        command_line = ('nmap -PA ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion1 == 4:
        command_line = ('nmap -PU ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion1 == 5:
        command_line = ('nmap -PY ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion1 == 6:
        command_line = ('nmap -PE ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion1 == 7:
        command_line = ('nmap -PP ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion1 == 8:
        command_line = ('nmap -PM ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion1 == 9:
        command_line = ('nmap -PO ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion1 == 10:
        command_line = ('nmap -PR ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion1 == 11:
        command_line = ('nmap -traceroute ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion1 == 12:
        command_line = ('nmap -Pn ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion1 == 13:
        command_line = ('nmap -sL ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion1 == 14:
        print("Leyenda:\n"+"")
    elif opcion1 == 0:
        exit()
        
#**************Análisis de Puertos******************************    

elif opcion0 == 2:
    objetivo = input("Introduzca un objetivo: ")
    opcion2 = int(input("\nElija una opción:\n"+
    "1- nmap -sT [objetivo]\t\t"+"Inicia conexiones completas.Muy fácil de detectar\n\n"+
    "2- nmap -sS [objetivo]\t\t"+"Envía un TCP SYN y espera la respuesta.Si el puerto está abierto se recibe un SYN-ACK y envía un RST para cerrar la conexión. Si está cerrado recibe un RST.\n\n"+
    "3- nmap -sF [objetivo]\t\t"+"Envía un paquete vacío con FIN.\n\n"+
    "4- nmap -sX [objetivo]"+"Activa los flags FIN,URG y PUSH. Esto se conoce como ataques XMAS.\n\n"+
    "5- nmap -sN [objetivo]\t\t"+"No activa ningún flag de la cabecera TCP.\n\n"+
    "6- nmap -sP [objetivo]\t\t"+"Con este comando, también utilizado para el descubrimiento de sistemas, se envía una solicitud ICMP y un paquete TCP SYN al puerto 80.\n\n"+
    "7- nmap -sU [objetivo]\t\t"+"Se envía una cabecera UDP(Sin datos) a cada puerto objetivo.Si se recibe un error ICMP, el puerto está cerrado; si se recibe un error ICMP 'no alcanzable', el puerto está filtrado;y, si recibe una respuesta UDP, el puerto estará abierto.\n\n"+
    "8- nmap -PT [objetivo]\t\t"+"Envía un TCP ACK y se espera un RST.\n\n"+
    "9- nmap -PS [objetivo]\t\t"+"Envía un TCP SYN y se espera un RST.\n\n"+
    "10- nmap -PI [objetivo]\t\t"+"Se utilizan paquetes ICMP.\n\n"+
    "11- nmap -PB [objetivo]\t\t"+"Se utilizan barridos '-PT' y '-PI' en paralelo\n\n"+
    "12- nmap -sW [objetivo]\t\t"+"Actúa igual que el escaneo '-PT',pero se aprovecha de un detalle de impolementación por el que, modificando la ventana TCP, se pueden listar puertos abiertos, en vez de no filtrados, cuando se envía un TCP ACK y se espera un RST.\n\n"+
    "0- salir\n\n"))

    if opcion2 == 1:
        command_line = ('nmap -sT ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion2 == 2:
        command_line = ('nmap -sS ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion2 == 3:
        command_line = ('nmap -sF ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion2 == 4:
        command_line = ('nmap -sX ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion2 == 5:
        command_line = ('nmap -sN ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion2 == 6:
        command_line = ('nmap -sP ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion2 == 7:
        command_line = ('nmap -sU ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion2 == 8:
        command_line = ('nmap -PT ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion2 == 9:
        command_line = ('nmap -PS ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion2 == 10:
        command_line = ('nmap -PI ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion2 == 11:
        command_line = ('nmap -PB ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion2 == 12:
        command_line = ('nmap -sW ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion2 == 0:
        exit()

#***********Analisis de Servicios y Sistemas Operativos***********************

elif opcion0 == 3:
    objetivo = input("Introduzca un objetivo: ")
    opcion3 = int(input("\nElija una opción:\n"+
    "1- nmap -sV [objetivo]\t\t"+"Detección de las versiones de los servicios.\n"+
    "2- nmap -sV --all-ports [objetivo]\t\t"+"Ningún puerto es excluido en este escaneo.\n\n"+
    "3- nmap -O --fuzzy [objetivo]\t\t"+"Descubrimiento de la versión del sistema operativo\n\n"+
    "4- nmap - O --osscan-guest\t\t"+"Nmap intenta adivinar el sistema operativo por aproximación"+
    "5- nmap -sR [objetivo]\t\t"+"Se envían órdenes de programa NULL SunRPC a todos los puertos TCP/UDP con el objetivo de determinar si son puertos RPC y su versión\n\n"))

    if opcion3 == 1:
        command_line = ('nmap -sV ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion3 == 2:
        command_line = ('nmap -sV --all-ports ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion3 == 3:
        command_line = ('nmap -O --fuzzy' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion3 == 4:
        command_line = ('nmap -O --osscan-guest ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion3 == 5:
        command_line = ('nmap -sR ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)

#********************Evasión*********************************************

elif opcion0 == 4:
    objetivo = input("Introduzca objetivo: ")
    opcion4 = int(input("\nElija una opción:\n"+
    "1- nmap -f [Objetivo]\t\t"+"Fragementa los paqeutes.\n"+
    "2- nmap --mtu [MTU] [Objetivo]\t\t"+"Se especifica un tamaño de MTU en concreto.\n"+
    "3- nmap -S [IP] [Objetivo]\t\t"+"Se falsea la dirección IP de origen.\n"+
    "4- nmap -sl [zombie] [Objetivo]\t\t"+"Se utiliza como origen una máquina inactiva (Zombie), de esta forma se produce un escaneo invisible al no enviar ningún paquete al destino con la IP de origen\n"+
    "5- nmap -D [Señuelo1] [Señuelo2] ... [Objetivo]\t\t"+"Se utulizan equipos señuelo con lo que lo ssitemas de seguridad creerán que se está llevando un escaneo en paralelo desde diferentes IP, sin saber cuál es la IP real que está realizando los escaneos\n"+
    "6- nmap -g [puerto_origen]\t\t"+"Se falsea el puerto origen.\n"+
    "7- nmap -spoof-mac[MAC_origen]\t\t"+"Se falsea la dirección MAC de origen.\n"))

    if opcion4 == 1:
        command_line = ('nmap -f ' + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion4 == 2:
        mtu = int(input("\nIntroduzca MTU: "))
        command_line = ('\nnmap --mtu ' + mtu +""+ objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion4 == 3:
        ip = int(input("\nIntroduzca IP: "))
        command_line = ('\nnmap -S ' + ip + "" + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion4 == 4:
        zombie = input("\nIntroduzca zombie: ")
        command_line = ('\nnmap -sl ' + zombie + "" + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion4 == 5:
        opcionSenyuelo = int(input("\nIntroduzca una opción:\n" + "1-Introducir señuelos manualmente.\n" + "2-Generar señuelos aleatoriamente.\n"))
        if opcionSenyuelo == 1:
            lista_senyuelos = []
            num_senyuelos = int(input("Introduzca número de señuelos: "))
            for k in range(num_senyuelos):
                lista_senyuelos.append(input("\nIntroduzca nombre de señuelo: ")) 
            print(lista_senyuelos)
            #Pendiente de revisión ya que hace los señuelos uno a uno y mi intención es usar todos a la vez.
            for senyuelos in lista_senyuelos:    
                command_line = ('nmap -D '+ senyuelos + "" + objetivo)  
                args = shlex.split(command_line)
                subprocess.call(args)
            
        elif opcionSenyuelo == 2:
            command_line = ('nmap -D RND: 10 ' + objetivo)  
            args = shlex.split(command_line)
            subprocess.call(args)
        else:
            print("Opción NO válida")
                        
    elif opcion4 == 6:
        port_origen = int(input("\nIntroduzca puerto de origen: "))
        command_line = ('\nnmap -g ' + port_origen + "" +objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)
    elif opcion4 == 7:
        mac_origen = int(input("Introduce dirección MAC de origen: "))
        command_line = ('\nnmap -spoof-mac '+ mac_origen + "" + objetivo)
        args = shlex.split(command_line)
        subprocess.call(args)


#********************Salir***********************************************

elif opcion0 == 0:
    exit()

#********************Opción NO válida************************************

else:
    print("Opción No Valida")