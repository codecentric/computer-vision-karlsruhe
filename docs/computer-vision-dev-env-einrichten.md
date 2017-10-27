# Computer Vision Entwicklungsumgebung (IDE) einrichten

* PyCharm
* Python 3.5
* OpenCV 3.3
* TensorFlow 1.4
* dlib 19.7
* CUDA 8, cuDNN 6
* keras, pytorch, jupyter, uvm. 

## Einleitung

Bei der Entwicklung von OpenCV Projekten gibt es unterschiedliche Herangehensweisen, die sich für uns im Laufe der Zeit
heraus kristalliert haben. Einerseits kann mit den lokalen Resourcen auf der eigenen Maschine entwickelt werden. Andererseits kann lokal auf der eigenen Maschine mit den Resourcen aus der Cloud entwickelt werden. Im Folgendem werden die beiden Ansätze sowie die Einrichtung beider Entwicklungsumgebungen beschrieben.

### Lokale Entwicklung
Bei der lokalen Entwicklung werden die Resourcen der eigenen Maschine beansprucht. Das bedeutet, dass keine Kommunikation bei der Verarbeitung der Bilder mit anderen Maschinen statt findet. Dieser Ansatz hat den Vorteil, dass die eigene Entwicklungsumgebung sehr schnell und einfach aufgesetzt werden kann. Weiterhin müssen unsere Daten nicht an Drittanbieter (bspw. Cloudanbieter) für die Verarbeitung nicht weitergegeben werden. Problematisch ist die lokale Entwicklung besonders dann, wenn wir resourcen intensive Berechnungen durchführen, bei denen oftmals auf die Grafikkarte und nicht auf die CPU zurückgegriffen werden. Da nicht jeder über die neusten Grafikkarten verfügt, können neue Entwicklungen aus dem Deep Learning Bereich nicht optimal dargestellt werden. 

### Cloud Entwicklung
Bei der Cloud Entwicklung findet die Entwicklung auf dem lokalen Computer statt, während die Ausführung auf einem anderen Computer stattfindet. Durch diesen Ansatz haben wir mehr Rechenpower zur Verfügung und können dadurch leichter Bleeding Edge Methoden testen. Leider sind mit dieser Vorgehensweise auch mehrere Nachteile verbunden. Wir müssen unsere Daten bei Drittanbietern für die Verarbeitung abspeichern, was je nach Domäne zu Datenschutzproblemen führen können. Weiterhin ist die Inbetriebnahme dieser Lösung etwas komplizierter.

### Was empfehlen wir euch?
Die Verwendung der lokalen und cloudbasierten Entwicklungsumgebung hängt stark vom Anwendungsfall ab. Wer OpenCV kennenlernen möchte und etwas damit herumspielen möchte, dem reicht die Entwicklung mit dem lokalen Setup. Wer sich mit resourcen intensiven Anwendungen herumschlagen möchte, die bspw. mit Deep Learning kombiniert werden, dem empfehlen wir ganz klar bei nicht vorhandener Hardware die Cloud Lösung. 

## Lokal einrichten

Vor der Installation von OpenCV müssen einige Abhängigkeiten installiert werden. Bei linux basierten Betriebssystem wie Ubuntu und OS X könnt ihr OpenCV über die Paketemanager (apt, brew) installieren. Dennoch empfehlen wir euch OpenCV selbst aufzusetzen. Dies hat den Vorteil, dass ihr neuste Versionen von OpenCV installieren könnt und es nach der Installation stabiler läuft.

Weiterhin empfehlen wir euch virtuelle Python Umgebungen mit bspw. virtualenv oder conda aufzusetzen. Ihr könnt auch 
lokal eine virtuelle Maschine installieren. Dazu verwenden wir zum Beispiel vmware Fusion. In der Regel sind die Pakete 
unter Ubuntu am einfachsten einzurichten - aber man kriegt sie auch auf dem Mac zum Laufen. 

### Ubuntu
Für die Installation von OpenCV auf einer Ubuntu Distribution empfehlen wir euch folgenden Guide:
* [Pyimagesearch - ubuntu 16.04. - how to install opencv](https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/)

### OS X
* [Brew opencv](https://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/)
* [OpenCV from Source](https://www.pyimagesearch.com/2016/12/05/macos-install-opencv-3-and-python-3-5/)


## Lokal coden, remote Execution

Falls ihr kein Notebook mit aktueller NVIDIA Grafikkarte habt, wird es schwierig Deep Learning 
auf lokaler Hardware zu machen. Wir schauen uns genauer an, wie man seine lokale IDE so einrichtet, 
dass man den Code auf dem Notebook in pyCharm entwickelt, er aber in der Cloud auf einer AWS Instanz 
ausgeführt wird.

### AWS Instanz einrichten

Als erstes müsst ihr eine AWS Instanz einrichten. Das dauert eine Weile und die etwas umfangreichere 
Anleitung findet ihr hier: [AWS Instanz einrichten mit GPU / CUDA](/docs/setup-aws-instance.md)

### PyCharm (professional) einrichten 

Wenn ihr PyCharm Professional nutzt kann man mit Remote Interpretern arbeiten. Wir konfigurieren PyCharm so, dass 
wir einen Remote Interpreter verwenden und dass wir vor jedem "Run" einen rsync mit dem Zielsystem machen. Per X11 
Forwarding können wir dann zusätzlich den Output der Fenster, die auf 
der AWS Instanz erzeugt werden, lokal anzeigen. Das funktioniert für Einzelbilder recht gut, bei Videos müssen wir 
evtl. andere Methoden verwenden. 

Geht im PyCharm auf Preferences / Deployment und richtet einen SFTP Server ein.
![remote_server](/resources/images/remote_deployment_server.png)

Unter Project Interpreter fügen wir einen Remote-Interpreter hinzu.
![remote_interpreter](/resources/images/remote_interpreter.png)

Bei der Default Run Configuration müssen div. Umgebungsvariablen gesetzt werden.
![run_config](/resources/images/run_config.png) 

Danach könnt ihr lokal in eurer PyCharm IDE entwickeln und den Code im Remote Interpreter auf der AWS Instanz laufen 
lassen. Damit das X-Forwarding funktioniert, müsst ihr wie folgt auf der Maschine angemeldet sein (-X Parameter für 
X-Forwarding):

```bash
 ssh -X -i ~/.ssh/gpuserver.pem ubuntu@YOUR_PUBLIC_IP
```

### jupyter notebook

## (streaming output)

... todo gestreamer oder ffserver oder jupyter oder ...

