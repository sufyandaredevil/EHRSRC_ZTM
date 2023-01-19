**Instructor: Paulo Silva**

#### OWASP Top 10 Risks

- #### **Injection**
  > **SQL**, **NoSQL**, **OS**, and **LDAP** injection, occur when untrusted data is sent to an interpreter as part of a command or query. The attacker's hostile data can trick the interpreter into executing unintended commands or accessing data without proper authorization.

  - **SQL Injection**: Type of security exploit in which an attacker inserts malicious code into a SQL statement, via user input, in order to gain unauthorized access to a database. The attacker can then retrieve, modify, or delete sensitive data, or use the database to launch further attacks. SQL injection is a common method of attack used to compromise websites and web applications. It is important to use prepared statements, parameterized queries or stored procedures to prevent SQL injection attacks.

    <ins>**Exploitation**</ins>: Consider the following source code that when given an authentication request from a **client** to the **server**
      ```js
      // Server Source Code:
      var record = query(`SELECT email, password FROM accounts WHERE 
          email = '${req.body.email}' AND password = '${req.body.password}'`);
      ```

      - Now a **legit request** for `email` and `password` would be something like `admin@123` and `$5up3rPa55&` making the query in the **server-side** look like this:
        ```js
        query(`SELECT email, password FROM accounts WHERE 
            email = '' AND password = '$5up3rPa55&' `)
        ```

        The SQL statement formed for the legit request would look as follows:
        ```sql
        SELECT email, password FROM accounts WHERE 
        email = 'admin@123' AND password = '$5up3rPa55&'
        ```

      - But in case of a **malicious request** for `email` and `password` would be something like `' OR '1'='1'--` and `<any_password_text_here>` making the query in the **server-side** look like this:
        ```js
        query(`SELECT email, password FROM accounts WHERE 
            email = '' OR '1'='1'--' AND password = '1' `)
        ```

        The SQL statement formed for the malicious request would look as follows:
        ```sql
        SELECT email, password FROM accounts WHERE 
        email = '' OR '1'='1'--' AND password = '1'
        ```
        This results in changing the SQL query itself i.e. only the `email` part with the `OR` condition `'1' = '1'` will be  processed as an **SQL** query and the rest will be processed as a comment due the presence of `--` symbol that is basically a comment delimiter for **SQL** (even `;` and multi-line comment `/* */`), so the remaining query `' AND password = '1'` is just a **comment** and not a part of the **SQL** query

    <ins>**Mitigation**</ins>:
    - **Server-side Input Validation**
    - **Escape** special characters using the specific escape syntax for that **interpreter**
    - Use **LIMIT** or other **SQL controls** within queries

- #### **Broken Authentication**
  > Application functions related to **authentication** and **session management** are often not implemented correctly, allowing attackers to compromise **passwords**, **keys**, or **session tokens**, or to exploit other implementation flaws to assume other users' identities.
