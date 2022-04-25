How to disable Google Analytics and prevent advertising tracking
================================================================

This site does not use Google Analytics. This article was written originally as
a part of the [Privacy Policy](/terms) to let users reliably disable tracking
and help increase their privacy when it did.


Option #1: Switch to [Brave](https://brave.com), a modern browser based on
Chromium that blocks all trackers and tons of ads, than boasts about how much
time it saved for you. We don't mind not seeing you on Google Analytics, we
hardly ever look at it anyway and mostly to see what browsers and what sections
of the site people use these days to optimise and improve the site.




---


### Google's official method


Google's official method to disable Analytics tracking and advertising cookies
is to install an **opt out plugin** in your browser... each one of them. This
takes away control from you and leaves it with Google. It will also stop
functioning if you reinstall the browser clean. References are provided at the
end of this article for your information.


There is however a more convenient and persistent cross-browser method to
disable Google Analytics: editing a file on your device called the **hosts
file**. This will not only increase your privacy across the web, but could also
make your browsing slightly faster. Always a good thing.


### A very reliable method


You will need the administrator or root privileges, which is fine on your own
**desktop computer**, but more involved on mobile devices. Smartphones and
tablets have a hosts file too, but user needs root access to edit it, i.e. iOS
limitations removed.


### Step 1.


**Windows**: Click Start menu – search for “Notepad“, right-click and select
“Run as Administrator“. This will prompt you to launch Notepad with higher
privileges. Now, open the **hosts** file at **C:\windows\system32\drivers\etc\**
from the Notepad File menu.


**OS X, Ubuntu, other desktop \*NIX systems**: Launch Terminal utility and type
**sudo nano /etc/hosts**, this will ask for your password.


### Step 2.


**On all operating systems** add the following lines to the bottom of the hosts
file.


*127.0.0.1 www.google-analytics.com # block Analytics*    *127.0.0.1
ssl.google-analytics.com*    *127.0.0.1 google-analytics.com*    *127.0.0.1
www.googleadservices.com # block remarketing*    *127.0.0.1
googleadservices.com*


### Step 3.


**On Windows**: Save using CTRL+S and exit.    **On Unix-style OS**: Save file
using CTRL+X, confirm by pressing Y and exit.


### Step 4.


Make the changes effective:


* The changes to the hosts file will apply immediately on a newer OS X and \*NIX systems, Windows users will need to **restart computer**.
* You will also need to **delete cookies and cache** data websites stored on your computer, which will log you out of all websites. Power users can just delete website data for the domains we blocked in the hosts file in step 2 to prevent this.


Enjoy your newly gained increased privacy.


### Bonus points


1. Add a line for *facebook.com* in the same style to disable tracking associated with Facebook Like buttons. Conveniently this will also prevent you from using Facebook. Yay, freedom!
2. Find some other 3rd party domains that are used to track your way around the web and add them to your hosts file.
3. Leave your tips in the feedback box.




---


### Reversibility


If you'd wish to reverse the changes, use the same steps to remove the lines you
added above.


### Use cases


This solution is browser independent and will naturally work for all browsers
installed on your computer including Internet Explorer, Firefox, Safari, Chrome
and Opera without any need for installation of plugins in each browser.


If you run a website with Google Analytics installed like us, this is one of the
ways you can exclude your own traffic from Analytics charts, especially handy if
your IP address is dynamic.


### References


* [Google Analytics Opt-out Browser Add-on (BETA)](http://tools.google.com/dlpage/gaoptout)
* [Advertising Cookie Opt-out Plugin](http://www.google.com/ads/preferences/plugin/)
