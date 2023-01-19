**Instructor: Sunil Gupta**

#### **Burp Suite Configuration**:

- Open `Burpsuite` from the **Application menu** or type `burpsuite` in the **terminal**
  - **[CLICK]** <kbd>Proxy</kbd> > <kbd>Options</kbd>
  - Under **<a style="color:orange;">Proxy Listeners</a>** section you'll see the interface column with a value: `127.0.0.1:8080`. This is the interface where the triggered request are forwarded to, which is basically your **Attacker's PC** (**127.0.0.1 / localhost / loopback**)

- **[OPEN]** `Browser` (here we use <img src="./IMGS/firefox.svg" height="20" style="vertical-align:middle;display: inline-block;">) > <kbd>...</kbd> > <kbd>Preferences</kbd> OR <kbd>Settings</kbd> > **[SEARCH]** `Network Settings` section > **[CLICK]** <kbd>Settings...</kbd>
  - **[CHOOSE]** `Manual proxy configuration`
    - **[SET] HTTP Proxy** `127.0.0.1` & **Port** `8080`
    - **[CHECK]** `Use this proxy server for all protocols`
    - **[CLICK]** <kbd>OK</kbd>

- 