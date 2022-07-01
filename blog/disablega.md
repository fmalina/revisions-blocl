How to disable adverts and analytics across the web
===================================================
Privacy matters. This site does not use Google Analytics.
It uses Google adverts for income, while also teaching you how to block them.
This article relates to the [Privacy Policy](/privacy).

---

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

You can get a big hosts file blocking hundreds of thousands of bad sites <https://github.com/StevenBlack/hosts>
Here we only list a few.

**On all operating systems** add the following lines to the bottom of the hosts file.

    0.0.0.0 www.google-analytics.com  # block Analytics
    0.0.0.0 google-analytics.com
    0.0.0.0 www.googleadservices.com  # block remarketing
    0.0.0.0 googleadservices.com
    0.0.0.0 www.googletagmanager.com
    0.0.0.0 googletagmanager.com
    0.0.0.0 pagead2.googlesyndication.com

### Step 3.

**On Windows**: Save using CTRL+S and exit.
**On Unix-style OS**: Save file using CTRL+X, confirm by pressing Y and exit.

### Step 4.

Make the changes effective:

* The changes to the hosts file will apply immediately on a newer OS X and \*NIX systems, Windows users will need to **restart computer**.
* You will also need to **delete cookies and cache** data websites stored on your computer, which will log you out of all websites. Power users can just delete website data for the domains we blocked in the hosts file in step 2 to prevent this.

Enjoy your newly gained increased privacy.

---

### Reversibility

If you'd wish to reverse the changes, use the same steps to remove the lines you added above.

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
