**Scanning n5gehtoolsmqtt-gateway-frontend:latest**
```

Testing n5gehtoolsmqtt-gateway-frontend:latest...

✗ Low severity vulnerability found in openssl/libcrypto3
  Description: CVE-2024-5535
  Info: https://security.snyk.io/vuln/SNYK-ALPINE320-OPENSSL-7413532
  Introduced through: openssl/libcrypto3@3.3.1-r0, apk-tools/apk-tools@2.14.4-r0, busybox/ssl_client@1.36.1-r29, openssl/libssl3@3.3.1-r0
  From: openssl/libcrypto3@3.3.1-r0
  From: apk-tools/apk-tools@2.14.4-r0 > openssl/libcrypto3@3.3.1-r0
  From: busybox/ssl_client@1.36.1-r29 > openssl/libcrypto3@3.3.1-r0
  and 4 more...
  Fixed in: 3.3.1-r1



Organization:      bhavdeep1304
Package manager:   apk
Project name:      docker-image|n5gehtoolsmqtt-gateway-frontend
Docker image:      n5gehtoolsmqtt-gateway-frontend:latest
Platform:          linux/amd64
Licenses:          enabled

Tested 16 dependencies for known issues, found 1 issue.

Snyk wasn’t able to auto detect the base image, use `--file` option to get base image remediation advice.
Example: $ snyk container test n5gehtoolsmqtt-gateway-frontend:latest --file=path/to/Dockerfile

To remove this message in the future, please run `snyk config set disableSuggestions=true`

-------------------------------------------------------

Testing n5gehtoolsmqtt-gateway-frontend:latest...

Organization:      bhavdeep1304
Package manager:   npm
Target file:       /app/package.json
Project name:      frontend
Docker image:      n5gehtoolsmqtt-gateway-frontend:latest
Licenses:          enabled

✔ Tested n5gehtoolsmqtt-gateway-frontend:latest for known issues, no vulnerable paths found.

-------------------------------------------------------

Testing n5gehtoolsmqtt-gateway-frontend:latest...

✗ Medium severity vulnerability found in golang.org/x/sys/unix
  Description: Incorrect Privilege Assignment
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXSYSUNIX-3310442
  Introduced through: golang.org/x/sys/unix@v0.0.0-20220715151400-c0bba94af5f8
  From: golang.org/x/sys/unix@v0.0.0-20220715151400-c0bba94af5f8
  Fixed in: 0.1.0



Organization:      bhavdeep1304
Package manager:   gomodules
Target file:       /usr/local/lib/node_modules/vite/node_modules/@esbuild/linux-x64/bin/esbuild
Project name:      github.com/evanw/esbuild
Docker image:      n5gehtoolsmqtt-gateway-frontend:latest
Licenses:          enabled

Tested 1 dependencies for known issues, found 1 issue.

Snyk wasn’t able to auto detect the base image, use `--file` option to get base image remediation advice.
Example: $ snyk container test n5gehtoolsmqtt-gateway-frontend:latest --file=path/to/Dockerfile

Snyk found some vulnerabilities in your image applications (Snyk searches for these vulnerabilities by default). See https://snyk.co/app-vulns for more information.

To remove these messages in the future, please run `snyk config set disableSuggestions=true`

-------------------------------------------------------

Testing n5gehtoolsmqtt-gateway-frontend:latest...

✗ Medium severity vulnerability found in golang.org/x/sys/unix
  Description: Incorrect Privilege Assignment
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXSYSUNIX-3310442
  Introduced through: golang.org/x/sys/unix@v0.0.0-20220715151400-c0bba94af5f8
  From: golang.org/x/sys/unix@v0.0.0-20220715151400-c0bba94af5f8
  Fixed in: 0.1.0



Organization:      bhavdeep1304
Package manager:   gomodules
Target file:       /app/node_modules/@esbuild/linux-x64/bin/esbuild
Project name:      github.com/evanw/esbuild
Docker image:      n5gehtoolsmqtt-gateway-frontend:latest
Licenses:          enabled

Tested 1 dependencies for known issues, found 1 issue.

Snyk wasn’t able to auto detect the base image, use `--file` option to get base image remediation advice.
Example: $ snyk container test n5gehtoolsmqtt-gateway-frontend:latest --file=path/to/Dockerfile

Snyk found some vulnerabilities in your image applications (Snyk searches for these vulnerabilities by default). See https://snyk.co/app-vulns for more information.

To remove these messages in the future, please run `snyk config set disableSuggestions=true`


Tested 4 projects, 3 contained vulnerable paths.



```
