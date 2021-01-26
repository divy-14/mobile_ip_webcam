<h1 align="center">Mobile IP Camera</h1>
<h2 align="center"> Turn your phone into a IP Webcam</h2>

<h3>Environment Setup</h3>
<ul>
<li> If you are on windows and using Conda I have included the opencv-env.yml file</li>
<li> Run command <b>conda env create -f opencv-env.yml</b> to replicate it</li>
<li> If you do not have conda I will list the packages that you need</li>
<ul> 
<li>requests</li>
<li>opencv</li>
</ul>
</ul>

<h3>Steps Involved:</h3>
<ul>
<li> Download and install IP Webcam app from the Google playstore: <a href="https://play.google.com/store/apps/details?id=com.pas.webcam">Ip Webcam</a> </li>
<li>Make sure your phone and mobile device are on the same network</li>
<li> On the Start Page of the App scroll down to the end of the page and you will see the Start Server option, Click on it to start the server.</li>
<li>After starting the server note down the IPv4 address mentioned in your app</li>
<li>Now run the ipcam.py script, it will ask you to enter the IP address that you noted down in the previous step, Enter the IP address</li>
<li><b>BAM!!</b> You now have the livefeed from your phone :smile:</li>
</ul>
