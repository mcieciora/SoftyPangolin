
<h2>What is <i>SoftyPangolin</i></h2> 

Softy Pangolin is a <i>weather app</i> powered by [openweathermap.org](https://home.openweathermap.org)

<h2>About Pangolin</h2>    
The name "pangolin" comes from the Malay word <i>pengguling</i>, meaning "one who rolls up" and stands for a wild animal, which physical appearance is marked by large, hardened, overlapping, plate-like scales.   
Though pangolins are protected by an international ban on their trade and have their sad place in Zoological Society of London's list of evolutionarily distinct and endangered mammals, pangolins are threatened by poaching (for their meat and scales, which are used in traditional Chinese medicine) and heavy deforestation of their natural habitats. <b>They are the most trafficked mammals in the world</b>. This animal was chosen as mascot for this project to raise awareness, that even almost extinct animal may be still used by people to make money mostly in criminal way or satisfy illogical and unscientific beliefs.  
    
![pangolin.png](doc/pangolin.PNG)\  
<i>source:</i> [Pangolin - Wikipedia](https://en.wikipedia.org/wiki/Pangolin)  
<h2>How to install</h2>  
<h3>Prerequisites</h3>    
Python version: >= 3.9  
    
Python modules (list available in requirements.txt):    
```  
flask~=1.1.2  
Flask-SQLAlchemy  
Werkzeug~=1.0.1  
SQLAlchemy~=1.3.23  
requests==2.25.1  
```  
See: [How to install modules](https://packaging.python.org/tutorials/installing-packages/#use-pip-for-installing)  
See: [How to install modules from requirements.txt](https://packaging.python.org/tutorials/installing-packages/#requirements-files)    
  
  
<h3>Docker container</h3>    
WIP  
    
<h3>Lazy installation (not implemented yet; please use step-by-step guide instead)</h3>    
Simply run
   
```  
git clone -b latest_release https://github.com/mcieciora/SoftyPangolin.git  
cd SoftyPangolin  
sudo python3 setup.py  
```    
 <h3>Step-by-step installation</h3>    
<h4>1. Clone repository</h4>    
  
```  
git clone -b latest_release https://github.com/mcieciora/SoftyPangolin.git  
cd SoftyPangolin  
```  
<h4>2. Create service file in <i>/lib/systemd/system</i></h4>    
  
```  
sudo nano /lib/systemd/system/softy_pangolin.service  
```  
  
<h4>3. Write into <i>/lib/systemd/system</i></h4>    
  
```ini
[Unit] 
Description=Softy Pangolin Service 
After=multi-user.target

[Service] 
Type=idle 
User=<YOUR_USER_NAME> 
Group=<YOUR_USER_GROUP> 
ExecStart=<PATH_TO_PYTHON> <PATH TO CLONED REPOSITORY>/main.py 
Restart=always
 
[Install] 
WantedBy=multi-user.target 
``` 
<h4>4. Set access rights</h4>    
  
```
sudo chmod 644 /lib/systemd/system/softy_pangolin.service  
```
<h4>5. Start daemon </h4>    
  
```  
sudo systemctl daemon-reload  
sudo systemctl enable softy_pangolin.service  
``` 
<h4>6. Reboot machine</h4>    
  
```  
sudo reboot  
``` 
<h2>How to use</h2>    
<h3>Generate API keys</h3>    
  
First, you need to create free account on [openweathermap.org](https://home.openweathermap.org/users/sign_up). After successful login go to [<i>"My API keys"</i>](https://home.openweathermap.org/api_keys), generate API key and copy it.  
  
<h3>Setup Softy Pangolin</h3>  
  
Fill <i>Application ID</i> field with just generated API key. 
Choose plan, that is available on your openweathermap account. If you did not buy any plan then probably you can leave this option set to <i>Free</i> on default.  
Choose language from available: English, Deutsch, Polish  
  
![setup.png](doc/setup.PNG)  
  
<h3>Softy Pangolin is set up and running!</h3>  
  
After this one simple step you shall be able to see current weather in your exact location.  
  
![weather_app.png](doc/weather_app.PNG)  
  
Happy Pangoling ;)  
  
<i>mcieciora</i>
