**Instructor: Sunil Gupta**

#### **Burp Suite Configuration**:

- **[OPEN]** `Burpsuite` from the **Application menu** or **[TYPE]** `burpsuite` in the **terminal**
  - **[CLICK]** <kbd>Proxy</kbd> tab > <kbd>Options</kbd> tab
  - Under `Proxy Listeners` section you'll see the interface column with value: `127.0.0.1:8080`. This is the interface where the triggered request are forwarded to, which is basically your **Attacker's PC** (**127.0.0.1 / localhost / loopback**)

- **[OPEN]** `Browser`(any, but **Firefox** in here)
  - <kbd>...</kbd> > <kbd>Preferences</kbd> OR <kbd>Settings</kbd> > **[SEARCH]** `Network Settings` section > **[CLICK]** <kbd>Settings...</kbd>
    - **[CHOOSE]** `Manual proxy configuration`
      - **[SET] HTTP Proxy** `127.0.0.1` & **Port** `8080`
      - **[CHECK]** `Use this proxy server for all protocols`
    - <kbd>OK</kbd>
  - **[OPEN]** New Tab > **[TYPE]** `http://burpsuite` >  <kbd>CA Certificate</kbd> > **[DOWNLOAD]** `cacert.der`
  - <kbd>...</kbd> > <kbd>Preferences</kbd> OR <kbd>Settings</kbd> > **[SEARCH]** `Certificates` section > **[CLICK]** <kbd>View Certificates...</kbd>
    - <kbd>Authorities</kbd> tab > <kbd>Import...</kbd>
      - **[SELECT]** `cacert.der` (cert that was downloaded earlier)
      - **[CHECK]** the following option:
        - [x] Trust this CA to identify websites.
        - [ ] Trust this CA to identify email users.
      - <kbd>OK</kbd>
