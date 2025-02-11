### Simple countdown ###

Ejercicio en Python de un contador que cuente los días para un determinado evento.



Para lanzarlo sin dejar abierta una ventana de cmd, crea un archivo con extensión .vbs con el siguiente código.

```
Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c run.bat"
oShell.Run strArgs, 0, false
```

Añada un archivo .bat que se llame run.bat con el siguiente formato:
 ```
@echo off
call "C:\TU\RUTA\TimeToJapan\.venv\Scripts\activate.bat" && cd "C:\TU\RUTA\TimeToJapan\" && python -m main.py

 ```

 !!! No te olvides de modificar "tu\ruta" por la dirección donde tengas tu proyecto.