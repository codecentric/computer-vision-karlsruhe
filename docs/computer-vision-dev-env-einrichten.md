# Computer Vision Entwicklungsumgebung (IDE) einrichten

## Einleitung

... lokal oder cloud? Nvidia? ... blabla

## Lokal einrichten

... Ubuntu oder MacOS ... verweis auf pyimagesearch

## Lokal coden, remote Execution

Falls ihr kein Notebook mit aktueller NVIDIA Grafikkarte habt, wird es schwierig Deep Learning 
auf lokaler Hardware zu machen. Wir schauen uns genauer an, wie man seine lokale IDE so einrichtet, 
dass man den Code auf dem Notebook in pyCharm entwickelt, er aber in der Cloud auf einer AWS Instanz 
ausgeführt wird.

### AWS Instanz einrichten

Als erstes müsst ihr eine AWS Instanz einrichten. Das dauert eine Weile und die etwas umfangreichere 
Anleitung findet ihr hier: [AWS Instanz einrichten mit GPU / CUDA](/docs/setup-aws-instance.md)

### PyCharm einrichten

Jetzt konfigurieren wir PyCharm so, dass wir einen Remote Interpreter verwenden und dass wir vor jedem "Run" einen 
rsync mit dem Zielsystem machen. Per X11 Forwarding können wir dann zusätzlich den Output der Fenster, die auf 
der AWS Instanz erzeugt werden, lokal anzeigen. Das funktioniert für Einzelbilder recht gut, bei Videos müssen wir 
evtl. andere Methoden verwenden. 

Geht im PyCharm auf Preferences / Deployment und richtet einen SFTP Server ein.
![remote_server](/resources/images/remote_deployment_server.png)

Unter Project Interpreter fügen wir einen Remote-Interpreter hinzu.
![remote_interpreter](/resources/images/remote_interpreter.png)

Bei der Default Run Configuration müssen div. Umgebungsvariablen gesetzt werden.
![run_config](/resources/images/run_config.png) 


... rsync script
... X11 forwarding / jupyter notebook

## (streaming output)

... todo gestreamer oder ffserver oder jupyter oder ...

