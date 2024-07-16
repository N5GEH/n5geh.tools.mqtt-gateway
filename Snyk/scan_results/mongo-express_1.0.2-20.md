**Scanning mongo-express:1.0.2-20**
```

Testing mongo-express:1.0.2-20...

✗ Low severity vulnerability found in openssl/libcrypto3
  Description: CVE-2024-2511
  Info: https://security.snyk.io/vuln/SNYK-ALPINE318-OPENSSL-6593964
  Introduced through: openssl/libcrypto3@3.1.4-r5, apk-tools/apk-tools@2.14.0-r2, busybox/ssl_client@1.36.1-r5, openssl/libssl3@3.1.4-r5
  From: openssl/libcrypto3@3.1.4-r5
  From: apk-tools/apk-tools@2.14.0-r2 > openssl/libcrypto3@3.1.4-r5
  From: busybox/ssl_client@1.36.1-r5 > openssl/libcrypto3@3.1.4-r5
  and 4 more...
  Image layer: 'apk add --no-cache bash tini'
  Fixed in: 3.1.4-r6

✗ Low severity vulnerability found in openssl/libcrypto3
  Description: CVE-2024-4603
  Info: https://security.snyk.io/vuln/SNYK-ALPINE318-OPENSSL-6928857
  Introduced through: openssl/libcrypto3@3.1.4-r5, apk-tools/apk-tools@2.14.0-r2, busybox/ssl_client@1.36.1-r5, openssl/libssl3@3.1.4-r5
  From: openssl/libcrypto3@3.1.4-r5
  From: apk-tools/apk-tools@2.14.0-r2 > openssl/libcrypto3@3.1.4-r5
  From: busybox/ssl_client@1.36.1-r5 > openssl/libcrypto3@3.1.4-r5
  and 4 more...
  Image layer: 'apk add --no-cache bash tini'
  Fixed in: 3.1.5-r0

✗ Low severity vulnerability found in openssl/libcrypto3
  Description: CVE-2024-5535
  Info: https://security.snyk.io/vuln/SNYK-ALPINE318-OPENSSL-7413525
  Introduced through: openssl/libcrypto3@3.1.4-r5, apk-tools/apk-tools@2.14.0-r2, busybox/ssl_client@1.36.1-r5, openssl/libssl3@3.1.4-r5
  From: openssl/libcrypto3@3.1.4-r5
  From: apk-tools/apk-tools@2.14.0-r2 > openssl/libcrypto3@3.1.4-r5
  From: busybox/ssl_client@1.36.1-r5 > openssl/libcrypto3@3.1.4-r5
  and 4 more...
  Image layer: 'apk add --no-cache bash tini'
  Fixed in: 3.1.6-r0

✗ Low severity vulnerability found in openssl/libcrypto3
  Description: CVE-2024-4741
  Info: https://security.snyk.io/vuln/SNYK-ALPINE318-OPENSSL-7413536
  Introduced through: openssl/libcrypto3@3.1.4-r5, apk-tools/apk-tools@2.14.0-r2, busybox/ssl_client@1.36.1-r5, openssl/libssl3@3.1.4-r5
  From: openssl/libcrypto3@3.1.4-r5
  From: apk-tools/apk-tools@2.14.0-r2 > openssl/libcrypto3@3.1.4-r5
  From: busybox/ssl_client@1.36.1-r5 > openssl/libcrypto3@3.1.4-r5
  and 4 more...
  Image layer: 'apk add --no-cache bash tini'
  Fixed in: 3.1.6-r0

✗ Medium severity vulnerability found in busybox/busybox
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-ALPINE318-BUSYBOX-6913411
  Introduced through: busybox/busybox@1.36.1-r5, alpine-baselayout/alpine-baselayout@3.4.3-r1, busybox/busybox-binsh@1.36.1-r5, bash/bash@5.2.15-r5, busybox/ssl_client@1.36.1-r5
  From: busybox/busybox@1.36.1-r5
  From: alpine-baselayout/alpine-baselayout@3.4.3-r1 > busybox/busybox-binsh@1.36.1-r5 > busybox/busybox@1.36.1-r5
  From: busybox/busybox-binsh@1.36.1-r5
  and 3 more...
  Image layer: 'apk add --no-cache bash tini'
  Fixed in: 1.36.1-r6

✗ Medium severity vulnerability found in busybox/busybox
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE318-BUSYBOX-7249236
  Introduced through: busybox/busybox@1.36.1-r5, alpine-baselayout/alpine-baselayout@3.4.3-r1, busybox/busybox-binsh@1.36.1-r5, bash/bash@5.2.15-r5, busybox/ssl_client@1.36.1-r5
  From: busybox/busybox@1.36.1-r5
  From: alpine-baselayout/alpine-baselayout@3.4.3-r1 > busybox/busybox-binsh@1.36.1-r5 > busybox/busybox@1.36.1-r5
  From: busybox/busybox-binsh@1.36.1-r5
  and 3 more...
  Image layer: 'apk add --no-cache bash tini'
  Fixed in: 1.36.1-r7

✗ Medium severity vulnerability found in busybox/busybox
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE318-BUSYBOX-7249265
  Introduced through: busybox/busybox@1.36.1-r5, alpine-baselayout/alpine-baselayout@3.4.3-r1, busybox/busybox-binsh@1.36.1-r5, bash/bash@5.2.15-r5, busybox/ssl_client@1.36.1-r5
  From: busybox/busybox@1.36.1-r5
  From: alpine-baselayout/alpine-baselayout@3.4.3-r1 > busybox/busybox-binsh@1.36.1-r5 > busybox/busybox@1.36.1-r5
  From: busybox/busybox-binsh@1.36.1-r5
  and 3 more...
  Image layer: 'apk add --no-cache bash tini'
  Fixed in: 1.36.1-r7

✗ Medium severity vulnerability found in busybox/busybox
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE318-BUSYBOX-7249419
  Introduced through: busybox/busybox@1.36.1-r5, alpine-baselayout/alpine-baselayout@3.4.3-r1, busybox/busybox-binsh@1.36.1-r5, bash/bash@5.2.15-r5, busybox/ssl_client@1.36.1-r5
  From: busybox/busybox@1.36.1-r5
  From: alpine-baselayout/alpine-baselayout@3.4.3-r1 > busybox/busybox-binsh@1.36.1-r5 > busybox/busybox@1.36.1-r5
  From: busybox/busybox-binsh@1.36.1-r5
  and 3 more...
  Image layer: 'apk add --no-cache bash tini'
  Fixed in: 1.36.1-r7

------------ Detected 5 vulnerabilities for node@20.13.1 ------------ 


✗ Low severity vulnerability found in node
  Description: Authorization Bypass
  Info: https://security.snyk.io/vuln/SNYK-UPSTREAM-NODE-7430907
  Introduced through: node@20.13.1
  From: node@20.13.1
  Image layer: Introduced by your base image (alpine:3.18.6)
  Fixed in: 20.15.1, 22.4.1

✗ Low severity vulnerability found in node
  Description: Authorization Bypass
  Info: https://security.snyk.io/vuln/SNYK-UPSTREAM-NODE-7430909
  Introduced through: node@20.13.1
  From: node@20.13.1
  Image layer: Introduced by your base image (alpine:3.18.6)
  Fixed in: 20.15.1, 22.4.1

✗ Low severity vulnerability found in node
  Description: Improper Handling of Values
  Info: https://security.snyk.io/vuln/SNYK-UPSTREAM-NODE-7430912
  Introduced through: node@20.13.1
  From: node@20.13.1
  Image layer: Introduced by your base image (alpine:3.18.6)
  Fixed in: 20.15.1, 22.4.1

✗ Medium severity vulnerability found in node
  Description: Improper Control of Generation of Code ('Code Injection')
  Info: https://security.snyk.io/vuln/SNYK-UPSTREAM-NODE-7430900
  Introduced through: node@20.13.1
  From: node@20.13.1
  Image layer: Introduced by your base image (alpine:3.18.6)
  Fixed in: 20.15.1

✗ Medium severity vulnerability found in node
  Description: Access Restriction Bypass
  Info: https://security.snyk.io/vuln/SNYK-UPSTREAM-NODE-7430905
  Introduced through: node@20.13.1
  From: node@20.13.1
  Image layer: Introduced by your base image (alpine:3.18.6)
  Fixed in: 20.15.1

Organization:      bhavdeep1304
Package manager:   apk
Project name:      docker-image|mongo-express
Docker image:      mongo-express:1.0.2-20
Platform:          linux/amd64
Base image:        alpine:3.18.6
Licenses:          enabled

Tested 22 dependencies for known issues, found 13 issues.

Base Image     Vulnerabilities  Severity
alpine:3.18.6  8                0 critical, 0 high, 4 medium, 4 low

Recommendations for base image upgrade:

Minor upgrades
Base Image  Vulnerabilities  Severity
alpine:3    1                0 critical, 0 high, 0 medium, 1 low


Learn more: https://docs.snyk.io/products/snyk-container/getting-around-the-snyk-container-ui/base-image-detection

-------------------------------------------------------

Testing mongo-express:1.0.2-20...

Tested 391 dependencies for known issues, found 14 issues.


Issues to fix by upgrading:

  Upgrade express@4.18.2 to express@4.19.2 to fix
  ✗ Open Redirect [Medium Severity][https://security.snyk.io/vuln/SNYK-JS-EXPRESS-6474509] in express@4.18.2
    introduced by express@4.18.2

  Upgrade mongodb@4.13.0 to mongodb@4.17.0 to fix
  ✗ Information Exposure [Medium Severity][https://security.snyk.io/vuln/SNYK-JS-MONGODB-5871303] in mongodb@4.13.0
    introduced by mongodb@4.13.0

  Upgrade mongodb-query-parser@2.4.6 to mongodb-query-parser@2.4.7 to fix
  ✗ Regular Expression Denial of Service (ReDoS) (new) [Medium Severity][https://security.snyk.io/vuln/SNYK-JS-ASYNC-7414156] in async@3.2.4
    introduced by mongodb-query-parser@2.4.6 > mongodb-extended-json@1.11.0 > async@3.2.4


Issues with no direct upgrade or patch:
  ✗ Incomplete List of Disallowed Inputs [Critical Severity][https://security.snyk.io/vuln/SNYK-JS-BABELTRAVERSE-5962462] in @babel/traverse@7.19.6
    introduced by nyc@15.1.0 > istanbul-lib-instrument@4.0.3 > @babel/core@7.19.6 > @babel/traverse@7.19.6 and 2 other path(s)
  This issue was fixed in versions: 7.23.2, 8.0.0-alpha.4
  ✗ Regular Expression Denial of Service (ReDoS) [High Severity][https://security.snyk.io/vuln/SNYK-JS-ES5EXT-6095076] in es5-ext@0.10.62
    introduced by cli-color@2.0.3 > es5-ext@0.10.62 and 91 other path(s)
  This issue was fixed in versions: 0.10.63
  ✗ Arbitrary File Upload [Medium Severity][https://security.snyk.io/vuln/SNYK-JS-EXPRESSFILEUPLOAD-2635697] in express-fileupload@1.4.0
    introduced by express-fileupload@1.4.0
  No upgrade or patch available
  ✗ Arbitrary File Upload [Medium Severity][https://security.snyk.io/vuln/SNYK-JS-EXPRESSFILEUPLOAD-2635946] in express-fileupload@1.4.0
    introduced by express-fileupload@1.4.0
  No upgrade or patch available
  ✗ Prototype Pollution [Medium Severity][https://security.snyk.io/vuln/SNYK-JS-FASTXMLPARSER-3325616] in fast-xml-parser@4.0.11
    introduced by mongodb@4.13.0 > @aws-sdk/credential-providers@3.204.0 > @aws-sdk/client-sts@3.204.0 > fast-xml-parser@4.0.11 and 2 other path(s)
  This issue was fixed in versions: 4.1.2
  ✗ Regular Expression Denial of Service (ReDoS) [High Severity][https://security.snyk.io/vuln/SNYK-JS-FASTXMLPARSER-5668858] in fast-xml-parser@4.0.11
    introduced by mongodb@4.13.0 > @aws-sdk/credential-providers@3.204.0 > @aws-sdk/client-sts@3.204.0 > fast-xml-parser@4.0.11 and 2 other path(s)
  This issue was fixed in versions: 4.2.4
  ✗ Missing Release of Resource after Effective Lifetime [Medium Severity][https://security.snyk.io/vuln/SNYK-JS-INFLIGHT-6095116] in inflight@1.0.6
    introduced by nyc@15.1.0 > glob@7.2.3 > inflight@1.0.6 and 4 other path(s)
  No upgrade or patch available
  ✗ Server-side Request Forgery (SSRF) [High Severity][https://security.snyk.io/vuln/SNYK-JS-IP-6240864] in ip@2.0.0
    introduced by mongodb@4.13.0 > socks@2.7.1 > ip@2.0.0
  This issue was fixed in versions: 1.1.9, 2.0.1
  ✗ Server-Side Request Forgery (SSRF) [Medium Severity][https://security.snyk.io/vuln/SNYK-JS-IP-7148531] in ip@2.0.0
    introduced by mongodb@4.13.0 > socks@2.7.1 > ip@2.0.0
  No upgrade or patch available
  ✗ Prototype Pollution [Medium Severity][https://security.snyk.io/vuln/SNYK-JS-JSON5-3182856] in json5@2.2.1
    introduced by nyc@15.1.0 > istanbul-lib-instrument@4.0.3 > @babel/core@7.19.6 > json5@2.2.1
  This issue was fixed in versions: 1.0.2, 2.2.2
  ✗ Regular Expression Denial of Service (ReDoS) [High Severity][https://security.snyk.io/vuln/SNYK-JS-SEMVER-3247795] in semver@6.3.0
    introduced by nyc@15.1.0 > make-dir@3.1.0 > semver@6.3.0 and 8 other path(s)
  This issue was fixed in versions: 5.7.2, 6.3.1, 7.5.2



Organization:      bhavdeep1304
Package manager:   yarn
Target file:       /app/package.json
Project name:      mongo-express
Docker image:      mongo-express:1.0.2-20
Licenses:          enabled

Snyk wasn’t able to auto detect the base image, use `--file` option to get base image remediation advice.
Example: $ snyk container test mongo-express:1.0.2-20 --file=path/to/Dockerfile

Snyk found some vulnerabilities in your image applications (Snyk searches for these vulnerabilities by default). See https://snyk.co/app-vulns for more information.

To remove these messages in the future, please run `snyk config set disableSuggestions=true`


Tested 2 projects, 2 contained vulnerable paths.



```
