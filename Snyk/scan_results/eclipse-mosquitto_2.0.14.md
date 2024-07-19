**Scanning eclipse-mosquitto:2.0.14**
```

Testing eclipse-mosquitto:2.0.14...

✗ Medium severity vulnerability found in openssl/libcrypto1.1
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-ALPINE314-OPENSSL-3314652
  Introduced through: openssl/libcrypto1.1@1.1.1q-r0, openssl/libssl1.1@1.1.1q-r0, apk-tools/apk-tools@2.12.7-r0, libretls/libretls@3.3.3p1-r3, ca-certificates/ca-certificates@20220614-r0
  From: openssl/libcrypto1.1@1.1.1q-r0
  From: openssl/libssl1.1@1.1.1q-r0 > openssl/libcrypto1.1@1.1.1q-r0
  From: apk-tools/apk-tools@2.12.7-r0 > openssl/libcrypto1.1@1.1.1q-r0
  and 5 more...
  Fixed in: 1.1.1t-r0

✗ Medium severity vulnerability found in openssl/libcrypto1.1
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-ALPINE314-OPENSSL-5291791
  Introduced through: openssl/libcrypto1.1@1.1.1q-r0, openssl/libssl1.1@1.1.1q-r0, apk-tools/apk-tools@2.12.7-r0, libretls/libretls@3.3.3p1-r3, ca-certificates/ca-certificates@20220614-r0
  From: openssl/libcrypto1.1@1.1.1q-r0
  From: openssl/libssl1.1@1.1.1q-r0 > openssl/libcrypto1.1@1.1.1q-r0
  From: apk-tools/apk-tools@2.12.7-r0 > openssl/libcrypto1.1@1.1.1q-r0
  and 5 more...
  Fixed in: 1.1.1t-r2

✗ High severity vulnerability found in openssl/libcrypto1.1
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE314-OPENSSL-3314637
  Introduced through: openssl/libcrypto1.1@1.1.1q-r0, openssl/libssl1.1@1.1.1q-r0, apk-tools/apk-tools@2.12.7-r0, libretls/libretls@3.3.3p1-r3, ca-certificates/ca-certificates@20220614-r0
  From: openssl/libcrypto1.1@1.1.1q-r0
  From: openssl/libssl1.1@1.1.1q-r0 > openssl/libcrypto1.1@1.1.1q-r0
  From: apk-tools/apk-tools@2.12.7-r0 > openssl/libcrypto1.1@1.1.1q-r0
  and 5 more...
  Fixed in: 1.1.1t-r0

✗ High severity vulnerability found in openssl/libcrypto1.1
  Description: Access of Resource Using Incompatible Type ('Type Confusion')
  Info: https://security.snyk.io/vuln/SNYK-ALPINE314-OPENSSL-3314646
  Introduced through: openssl/libcrypto1.1@1.1.1q-r0, openssl/libssl1.1@1.1.1q-r0, apk-tools/apk-tools@2.12.7-r0, libretls/libretls@3.3.3p1-r3, ca-certificates/ca-certificates@20220614-r0
  From: openssl/libcrypto1.1@1.1.1q-r0
  From: openssl/libssl1.1@1.1.1q-r0 > openssl/libcrypto1.1@1.1.1q-r0
  From: apk-tools/apk-tools@2.12.7-r0 > openssl/libcrypto1.1@1.1.1q-r0
  and 5 more...
  Fixed in: 1.1.1t-r0

✗ High severity vulnerability found in openssl/libcrypto1.1
  Description: Double Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE314-OPENSSL-3314653
  Introduced through: openssl/libcrypto1.1@1.1.1q-r0, openssl/libssl1.1@1.1.1q-r0, apk-tools/apk-tools@2.12.7-r0, libretls/libretls@3.3.3p1-r3, ca-certificates/ca-certificates@20220614-r0
  From: openssl/libcrypto1.1@1.1.1q-r0
  From: openssl/libssl1.1@1.1.1q-r0 > openssl/libcrypto1.1@1.1.1q-r0
  From: apk-tools/apk-tools@2.12.7-r0 > openssl/libcrypto1.1@1.1.1q-r0
  and 5 more...
  Fixed in: 1.1.1t-r0

✗ High severity vulnerability found in openssl/libcrypto1.1
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-ALPINE314-OPENSSL-3368739
  Introduced through: openssl/libcrypto1.1@1.1.1q-r0, openssl/libssl1.1@1.1.1q-r0, apk-tools/apk-tools@2.12.7-r0, libretls/libretls@3.3.3p1-r3, ca-certificates/ca-certificates@20220614-r0
  From: openssl/libcrypto1.1@1.1.1q-r0
  From: openssl/libssl1.1@1.1.1q-r0 > openssl/libcrypto1.1@1.1.1q-r0
  From: apk-tools/apk-tools@2.12.7-r0 > openssl/libcrypto1.1@1.1.1q-r0
  and 5 more...
  Fixed in: 1.1.1t-r1



Organization:      bhavdeep1304
Package manager:   apk
Project name:      docker-image|eclipse-mosquitto
Docker image:      eclipse-mosquitto:2.0.14
Platform:          linux/amd64
Base image:        alpine:3.14.8
Licenses:          enabled

Tested 20 dependencies for known issues, found 6 issues.

Base Image     Vulnerabilities  Severity
alpine:3.14.8  6                0 critical, 4 high, 2 medium, 0 low

Recommendations for base image upgrade:

Minor upgrades
Base Image  Vulnerabilities  Severity
alpine:3    1                0 critical, 0 high, 0 medium, 1 low

Alpine 3.14.8 is no longer supported by the Alpine maintainers. Vulnerability detection may be affected by a lack of security updates.

Learn more: https://docs.snyk.io/products/snyk-container/getting-around-the-snyk-container-ui/base-image-detection


```
