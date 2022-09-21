# ux_vcloud_clarocloud_com_br
experiencia de usuario con docker y selenium para el portal clarocloud.com.br

## uso / instalacion
para la ejecucion de la experiencia de usuario, se requiere solamente ejecutar
el siguiente comando con docker

```bash
docker run --rm --dns="8.8.8.8" ux_vcloud_br:latest /app/env/bin/python3 main.py
```

## debug
En caso de que se requiera debuggear de manera visual, solamente se ejecuta 
el comando para levantar el ambiente con docker compose

```bash
docker compose up -d
```

una vez que se haya levanta el ambiente, podremos ingresar a un navegador web
apuntando al puerto 7900 e ingresaremos al contenedor con noVNC, el password
para ingresar es **secret**