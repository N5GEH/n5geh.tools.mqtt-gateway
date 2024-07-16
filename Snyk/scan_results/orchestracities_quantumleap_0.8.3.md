**Scanning orchestracities/quantumleap:0.8.3**
```

Testing orchestracities/quantumleap:0.8.3...

✗ Low severity vulnerability found in openssl/libcrypto1.1
  Description: Inadequate Encryption Strength
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-OPENSSL-1075736
  Introduced through: openssl/libcrypto1.1@1.1.1g-r0, openssl/libssl1.1@1.1.1g-r0, .python-rundeps@20200804.041307, apk-tools/apk-tools@2.10.5-r1, libtls-standalone/libtls-standalone@2.9.1-r1, ca-certificates/ca-certificates@20191127-r3, curl/libcurl@7.79.1-r0, krb5-conf/krb5-conf@1.0-r2
  From: openssl/libcrypto1.1@1.1.1g-r0
  From: openssl/libssl1.1@1.1.1g-r0 > openssl/libcrypto1.1@1.1.1g-r0
  From: .python-rundeps@20200804.041307 > openssl/libcrypto1.1@1.1.1g-r0
  and 11 more...
  Image layer: 'apk --no-cache add curl'
  Fixed in: 1.1.1j-r0

✗ Low severity vulnerability found in busybox/busybox
  Description: ALPINE-13661
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-BUSYBOX-2606933
  Introduced through: busybox/busybox@1.31.1-r16, alpine-baselayout/alpine-baselayout@3.2.0-r6, ca-certificates/ca-certificates@20191127-r3, busybox/ssl_client@1.31.1-r16
  From: busybox/busybox@1.31.1-r16
  From: alpine-baselayout/alpine-baselayout@3.2.0-r6 > busybox/busybox@1.31.1-r16
  From: ca-certificates/ca-certificates@20191127-r3 > busybox/busybox@1.31.1-r16
  and 1 more...
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.31.1-r22

✗ Medium severity vulnerability found in util-linux/libuuid
  Description: Files or Directories Accessible to External Parties
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-UTILLINUX-2393736
  Introduced through: util-linux/libuuid@2.35.2-r0, .python-rundeps@20200804.041307
  From: util-linux/libuuid@2.35.2-r0
  From: .python-rundeps@20200804.041307 > util-linux/libuuid@2.35.2-r0
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.37.3-r0

✗ Medium severity vulnerability found in util-linux/libuuid
  Description: Files or Directories Accessible to External Parties
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-UTILLINUX-2393737
  Introduced through: util-linux/libuuid@2.35.2-r0, .python-rundeps@20200804.041307
  From: util-linux/libuuid@2.35.2-r0
  From: .python-rundeps@20200804.041307 > util-linux/libuuid@2.35.2-r0
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.37.3-r0

✗ Medium severity vulnerability found in util-linux/libuuid
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-UTILLINUX-2401803
  Introduced through: util-linux/libuuid@2.35.2-r0, .python-rundeps@20200804.041307
  From: util-linux/libuuid@2.35.2-r0
  From: .python-rundeps@20200804.041307 > util-linux/libuuid@2.35.2-r0
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.37.4-r0

✗ Medium severity vulnerability found in sqlite/sqlite-libs
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-SQLITE-1300270
  Introduced through: sqlite/sqlite-libs@3.32.1-r0, .python-rundeps@20200804.041307
  From: sqlite/sqlite-libs@3.32.1-r0
  From: .python-rundeps@20200804.041307 > sqlite/sqlite-libs@3.32.1-r0
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 3.32.1-r1

✗ Medium severity vulnerability found in sqlite/sqlite-libs
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-SQLITE-1300271
  Introduced through: sqlite/sqlite-libs@3.32.1-r0, .python-rundeps@20200804.041307
  From: sqlite/sqlite-libs@3.32.1-r0
  From: .python-rundeps@20200804.041307 > sqlite/sqlite-libs@3.32.1-r0
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 3.32.1-r1

✗ Medium severity vulnerability found in openssl/libcrypto1.1
  Description: NULL Pointer Dereference
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-OPENSSL-1050745
  Introduced through: openssl/libcrypto1.1@1.1.1g-r0, openssl/libssl1.1@1.1.1g-r0, .python-rundeps@20200804.041307, apk-tools/apk-tools@2.10.5-r1, libtls-standalone/libtls-standalone@2.9.1-r1, ca-certificates/ca-certificates@20191127-r3, curl/libcurl@7.79.1-r0, krb5-conf/krb5-conf@1.0-r2
  From: openssl/libcrypto1.1@1.1.1g-r0
  From: openssl/libssl1.1@1.1.1g-r0 > openssl/libcrypto1.1@1.1.1g-r0
  From: .python-rundeps@20200804.041307 > openssl/libcrypto1.1@1.1.1g-r0
  and 11 more...
  Image layer: 'apk --no-cache add curl'
  Fixed in: 1.1.1i-r0

✗ Medium severity vulnerability found in openssl/libcrypto1.1
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-OPENSSL-1075734
  Introduced through: openssl/libcrypto1.1@1.1.1g-r0, openssl/libssl1.1@1.1.1g-r0, .python-rundeps@20200804.041307, apk-tools/apk-tools@2.10.5-r1, libtls-standalone/libtls-standalone@2.9.1-r1, ca-certificates/ca-certificates@20191127-r3, curl/libcurl@7.79.1-r0, krb5-conf/krb5-conf@1.0-r2
  From: openssl/libcrypto1.1@1.1.1g-r0
  From: openssl/libssl1.1@1.1.1g-r0 > openssl/libcrypto1.1@1.1.1g-r0
  From: .python-rundeps@20200804.041307 > openssl/libcrypto1.1@1.1.1g-r0
  and 11 more...
  Image layer: 'apk --no-cache add curl'
  Fixed in: 1.1.1j-r0

✗ Medium severity vulnerability found in openssl/libcrypto1.1
  Description: NULL Pointer Dereference
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-OPENSSL-1089237
  Introduced through: openssl/libcrypto1.1@1.1.1g-r0, openssl/libssl1.1@1.1.1g-r0, .python-rundeps@20200804.041307, apk-tools/apk-tools@2.10.5-r1, libtls-standalone/libtls-standalone@2.9.1-r1, ca-certificates/ca-certificates@20191127-r3, curl/libcurl@7.79.1-r0, krb5-conf/krb5-conf@1.0-r2
  From: openssl/libcrypto1.1@1.1.1g-r0
  From: openssl/libssl1.1@1.1.1g-r0 > openssl/libcrypto1.1@1.1.1g-r0
  From: .python-rundeps@20200804.041307 > openssl/libcrypto1.1@1.1.1g-r0
  and 11 more...
  Image layer: 'apk --no-cache add curl'
  Fixed in: 1.1.1k-r0

✗ Medium severity vulnerability found in musl/musl-utils
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-MUSL-1042762
  Introduced through: musl/musl-utils@1.1.24-r8, libc-dev/libc-utils@0.7.2-r3, musl/musl@1.1.24-r9
  From: musl/musl-utils@1.1.24-r8
  From: libc-dev/libc-utils@0.7.2-r3 > musl/musl-utils@1.1.24-r8
  From: musl/musl@1.1.24-r9
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.1.24-r10

✗ Medium severity vulnerability found in krb5/krb5-libs
  Description: NULL Pointer Dereference
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-KRB5-2432004
  Introduced through: krb5/krb5-libs@1.18.2-r0, krb5-conf/krb5-conf@1.0-r2, libtirpc/libtirpc@1.2.6-r0
  From: krb5/krb5-libs@1.18.2-r0
  From: krb5-conf/krb5-conf@1.0-r2 > krb5/krb5-libs@1.18.2-r0
  From: libtirpc/libtirpc@1.2.6-r0 > krb5/krb5-libs@1.18.2-r0
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.18.5-r0

✗ Medium severity vulnerability found in expat/expat
  Description: Uncontrolled Recursion
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-EXPAT-2407751
  Introduced through: expat/expat@2.2.9-r1, .python-rundeps@20200804.041307
  From: expat/expat@2.2.9-r1
  From: .python-rundeps@20200804.041307 > expat/expat@2.2.9-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.2.10-r2

✗ Medium severity vulnerability found in curl/libcurl
  Description: Insufficiently Protected Credentials
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-CURL-2804930
  Introduced through: curl/libcurl@7.79.1-r0, curl/curl@7.79.1-r0
  From: curl/libcurl@7.79.1-r0
  From: curl/curl@7.79.1-r0 > curl/libcurl@7.79.1-r0
  From: curl/curl@7.79.1-r0
  Image layer: 'apk --no-cache add curl'
  Fixed in: 7.79.1-r1

✗ Medium severity vulnerability found in curl/libcurl
  Description: Insufficiently Protected Credentials
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-CURL-2804936
  Introduced through: curl/libcurl@7.79.1-r0, curl/curl@7.79.1-r0
  From: curl/libcurl@7.79.1-r0
  From: curl/curl@7.79.1-r0 > curl/libcurl@7.79.1-r0
  From: curl/curl@7.79.1-r0
  Image layer: 'apk --no-cache add curl'
  Fixed in: 7.79.1-r1

✗ Medium severity vulnerability found in busybox/busybox
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-BUSYBOX-1920717
  Introduced through: busybox/busybox@1.31.1-r16, alpine-baselayout/alpine-baselayout@3.2.0-r6, ca-certificates/ca-certificates@20191127-r3, busybox/ssl_client@1.31.1-r16
  From: busybox/busybox@1.31.1-r16
  From: alpine-baselayout/alpine-baselayout@3.2.0-r6 > busybox/busybox@1.31.1-r16
  From: ca-certificates/ca-certificates@20191127-r3 > busybox/busybox@1.31.1-r16
  and 1 more...
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.31.1-r21

✗ High severity vulnerability found in zlib/zlib
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-ZLIB-2434421
  Introduced through: zlib/zlib@1.2.11-r3, .python-rundeps@20200804.041307, apk-tools/apk-tools@2.10.5-r1, curl/libcurl@7.79.1-r0, curl/curl@7.79.1-r0
  From: zlib/zlib@1.2.11-r3
  From: .python-rundeps@20200804.041307 > zlib/zlib@1.2.11-r3
  From: apk-tools/apk-tools@2.10.5-r1 > zlib/zlib@1.2.11-r3
  and 2 more...
  Image layer: 'apk --no-cache add curl'
  Fixed in: 1.2.12-r0

✗ High severity vulnerability found in xz/xz-libs
  Description: Improper Input Validation
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-XZ-2445105
  Introduced through: xz/xz-libs@5.2.5-r0, .python-rundeps@20200804.041307
  From: xz/xz-libs@5.2.5-r0
  From: .python-rundeps@20200804.041307 > xz/xz-libs@5.2.5-r0
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 5.2.5-r1

✗ High severity vulnerability found in openssl/libcrypto1.1
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-OPENSSL-1075735
  Introduced through: openssl/libcrypto1.1@1.1.1g-r0, openssl/libssl1.1@1.1.1g-r0, .python-rundeps@20200804.041307, apk-tools/apk-tools@2.10.5-r1, libtls-standalone/libtls-standalone@2.9.1-r1, ca-certificates/ca-certificates@20191127-r3, curl/libcurl@7.79.1-r0, krb5-conf/krb5-conf@1.0-r2
  From: openssl/libcrypto1.1@1.1.1g-r0
  From: openssl/libssl1.1@1.1.1g-r0 > openssl/libcrypto1.1@1.1.1g-r0
  From: .python-rundeps@20200804.041307 > openssl/libcrypto1.1@1.1.1g-r0
  and 11 more...
  Image layer: 'apk --no-cache add curl'
  Fixed in: 1.1.1j-r0

✗ High severity vulnerability found in openssl/libcrypto1.1
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-OPENSSL-1089238
  Introduced through: openssl/libcrypto1.1@1.1.1g-r0, openssl/libssl1.1@1.1.1g-r0, .python-rundeps@20200804.041307, apk-tools/apk-tools@2.10.5-r1, libtls-standalone/libtls-standalone@2.9.1-r1, ca-certificates/ca-certificates@20191127-r3, curl/libcurl@7.79.1-r0, krb5-conf/krb5-conf@1.0-r2
  From: openssl/libcrypto1.1@1.1.1g-r0
  From: openssl/libssl1.1@1.1.1g-r0 > openssl/libcrypto1.1@1.1.1g-r0
  From: .python-rundeps@20200804.041307 > openssl/libcrypto1.1@1.1.1g-r0
  and 11 more...
  Image layer: 'apk --no-cache add curl'
  Fixed in: 1.1.1k-r0

✗ High severity vulnerability found in openssl/libcrypto1.1
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-OPENSSL-1569450
  Introduced through: openssl/libcrypto1.1@1.1.1g-r0, openssl/libssl1.1@1.1.1g-r0, .python-rundeps@20200804.041307, apk-tools/apk-tools@2.10.5-r1, libtls-standalone/libtls-standalone@2.9.1-r1, ca-certificates/ca-certificates@20191127-r3, curl/libcurl@7.79.1-r0, krb5-conf/krb5-conf@1.0-r2
  From: openssl/libcrypto1.1@1.1.1g-r0
  From: openssl/libssl1.1@1.1.1g-r0 > openssl/libcrypto1.1@1.1.1g-r0
  From: .python-rundeps@20200804.041307 > openssl/libcrypto1.1@1.1.1g-r0
  and 11 more...
  Image layer: 'apk --no-cache add curl'
  Fixed in: 1.1.1l-r0

✗ High severity vulnerability found in openssl/libcrypto1.1
  Description: Loop with Unreachable Exit Condition ('Infinite Loop')
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-OPENSSL-2426332
  Introduced through: openssl/libcrypto1.1@1.1.1g-r0, openssl/libssl1.1@1.1.1g-r0, .python-rundeps@20200804.041307, apk-tools/apk-tools@2.10.5-r1, libtls-standalone/libtls-standalone@2.9.1-r1, ca-certificates/ca-certificates@20191127-r3, curl/libcurl@7.79.1-r0, krb5-conf/krb5-conf@1.0-r2
  From: openssl/libcrypto1.1@1.1.1g-r0
  From: openssl/libssl1.1@1.1.1g-r0 > openssl/libcrypto1.1@1.1.1g-r0
  From: .python-rundeps@20200804.041307 > openssl/libcrypto1.1@1.1.1g-r0
  and 11 more...
  Image layer: 'apk --no-cache add curl'
  Fixed in: 1.1.1n-r0

✗ High severity vulnerability found in ncurses/ncurses-libs
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-NCURSES-2313024
  Introduced through: ncurses/ncurses-libs@6.2_p20200523-r0, readline/readline@8.0.4-r0, .python-rundeps@20200804.041307, ncurses/ncurses-terminfo-base@6.2_p20200523-r0
  From: ncurses/ncurses-libs@6.2_p20200523-r0
  From: readline/readline@8.0.4-r0 > ncurses/ncurses-libs@6.2_p20200523-r0
  From: .python-rundeps@20200804.041307 > ncurses/ncurses-libs@6.2_p20200523-r0
  and 2 more...
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 6.2_p20200523-r1

✗ High severity vulnerability found in krb5/krb5-libs
  Description: Uncontrolled Recursion
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-KRB5-1043934
  Introduced through: krb5/krb5-libs@1.18.2-r0, krb5-conf/krb5-conf@1.0-r2, libtirpc/libtirpc@1.2.6-r0
  From: krb5/krb5-libs@1.18.2-r0
  From: krb5-conf/krb5-conf@1.0-r2 > krb5/krb5-libs@1.18.2-r0
  From: libtirpc/libtirpc@1.2.6-r0 > krb5/krb5-libs@1.18.2-r0
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.18.3-r0

✗ High severity vulnerability found in krb5/krb5-libs
  Description: NULL Pointer Dereference
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-KRB5-1533463
  Introduced through: krb5/krb5-libs@1.18.2-r0, krb5-conf/krb5-conf@1.0-r2, libtirpc/libtirpc@1.2.6-r0
  From: krb5/krb5-libs@1.18.2-r0
  From: krb5-conf/krb5-conf@1.0-r2 > krb5/krb5-libs@1.18.2-r0
  From: libtirpc/libtirpc@1.2.6-r0 > krb5/krb5-libs@1.18.2-r0
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.18.4-r0

✗ High severity vulnerability found in expat/expat
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-EXPAT-2342149
  Introduced through: expat/expat@2.2.9-r1, .python-rundeps@20200804.041307
  From: expat/expat@2.2.9-r1
  From: .python-rundeps@20200804.041307 > expat/expat@2.2.9-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.2.10-r0

✗ High severity vulnerability found in expat/expat
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-EXPAT-2342151
  Introduced through: expat/expat@2.2.9-r1, .python-rundeps@20200804.041307
  From: expat/expat@2.2.9-r1
  From: .python-rundeps@20200804.041307 > expat/expat@2.2.9-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.2.10-r0

✗ High severity vulnerability found in expat/expat
  Description: Incorrect Calculation
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-EXPAT-2342155
  Introduced through: expat/expat@2.2.9-r1, .python-rundeps@20200804.041307
  From: expat/expat@2.2.9-r1
  From: .python-rundeps@20200804.041307 > expat/expat@2.2.9-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.2.10-r0

✗ High severity vulnerability found in expat/expat
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-EXPAT-2342156
  Introduced through: expat/expat@2.2.9-r1, .python-rundeps@20200804.041307
  From: expat/expat@2.2.9-r1
  From: .python-rundeps@20200804.041307 > expat/expat@2.2.9-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.2.10-r0

✗ High severity vulnerability found in expat/expat
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-EXPAT-2342159
  Introduced through: expat/expat@2.2.9-r1, .python-rundeps@20200804.041307
  From: expat/expat@2.2.9-r1
  From: .python-rundeps@20200804.041307 > expat/expat@2.2.9-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.2.10-r0

✗ High severity vulnerability found in expat/expat
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-EXPAT-2406623
  Introduced through: expat/expat@2.2.9-r1, .python-rundeps@20200804.041307
  From: expat/expat@2.2.9-r1
  From: .python-rundeps@20200804.041307 > expat/expat@2.2.9-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.2.10-r1

✗ High severity vulnerability found in expat/expat
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-EXPAT-2407745
  Introduced through: expat/expat@2.2.9-r1, .python-rundeps@20200804.041307
  From: expat/expat@2.2.9-r1
  From: .python-rundeps@20200804.041307 > expat/expat@2.2.9-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.2.10-r2

✗ High severity vulnerability found in curl/libcurl
  Description: Missing Authentication for Critical Function
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-CURL-2804929
  Introduced through: curl/libcurl@7.79.1-r0, curl/curl@7.79.1-r0
  From: curl/libcurl@7.79.1-r0
  From: curl/curl@7.79.1-r0 > curl/libcurl@7.79.1-r0
  From: curl/curl@7.79.1-r0
  Image layer: 'apk --no-cache add curl'
  Fixed in: 7.79.1-r1

✗ High severity vulnerability found in curl/libcurl
  Description: CVE-2022-27775
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-CURL-2804935
  Introduced through: curl/libcurl@7.79.1-r0, curl/curl@7.79.1-r0
  From: curl/libcurl@7.79.1-r0
  From: curl/curl@7.79.1-r0 > curl/libcurl@7.79.1-r0
  From: curl/curl@7.79.1-r0
  Image layer: 'apk --no-cache add curl'
  Fixed in: 7.79.1-r1

✗ High severity vulnerability found in busybox/busybox
  Description: Improper Handling of Exceptional Conditions
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-BUSYBOX-1089799
  Introduced through: busybox/busybox@1.31.1-r16, alpine-baselayout/alpine-baselayout@3.2.0-r6, ca-certificates/ca-certificates@20191127-r3, busybox/ssl_client@1.31.1-r16
  From: busybox/busybox@1.31.1-r16
  From: alpine-baselayout/alpine-baselayout@3.2.0-r6 > busybox/busybox@1.31.1-r16
  From: ca-certificates/ca-certificates@20191127-r3 > busybox/busybox@1.31.1-r16
  and 1 more...
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.31.1-r20

✗ High severity vulnerability found in busybox/busybox
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-BUSYBOX-1920710
  Introduced through: busybox/busybox@1.31.1-r16, alpine-baselayout/alpine-baselayout@3.2.0-r6, ca-certificates/ca-certificates@20191127-r3, busybox/ssl_client@1.31.1-r16
  From: busybox/busybox@1.31.1-r16
  From: alpine-baselayout/alpine-baselayout@3.2.0-r6 > busybox/busybox@1.31.1-r16
  From: ca-certificates/ca-certificates@20191127-r3 > busybox/busybox@1.31.1-r16
  and 1 more...
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.31.1-r21

✗ High severity vulnerability found in busybox/busybox
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-BUSYBOX-1920711
  Introduced through: busybox/busybox@1.31.1-r16, alpine-baselayout/alpine-baselayout@3.2.0-r6, ca-certificates/ca-certificates@20191127-r3, busybox/ssl_client@1.31.1-r16
  From: busybox/busybox@1.31.1-r16
  From: alpine-baselayout/alpine-baselayout@3.2.0-r6 > busybox/busybox@1.31.1-r16
  From: ca-certificates/ca-certificates@20191127-r3 > busybox/busybox@1.31.1-r16
  and 1 more...
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.31.1-r21

✗ High severity vulnerability found in busybox/busybox
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-BUSYBOX-1920712
  Introduced through: busybox/busybox@1.31.1-r16, alpine-baselayout/alpine-baselayout@3.2.0-r6, ca-certificates/ca-certificates@20191127-r3, busybox/ssl_client@1.31.1-r16
  From: busybox/busybox@1.31.1-r16
  From: alpine-baselayout/alpine-baselayout@3.2.0-r6 > busybox/busybox@1.31.1-r16
  From: ca-certificates/ca-certificates@20191127-r3 > busybox/busybox@1.31.1-r16
  and 1 more...
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.31.1-r21

✗ High severity vulnerability found in busybox/busybox
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-BUSYBOX-1920729
  Introduced through: busybox/busybox@1.31.1-r16, alpine-baselayout/alpine-baselayout@3.2.0-r6, ca-certificates/ca-certificates@20191127-r3, busybox/ssl_client@1.31.1-r16
  From: busybox/busybox@1.31.1-r16
  From: alpine-baselayout/alpine-baselayout@3.2.0-r6 > busybox/busybox@1.31.1-r16
  From: ca-certificates/ca-certificates@20191127-r3 > busybox/busybox@1.31.1-r16
  and 1 more...
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.31.1-r21

✗ High severity vulnerability found in busybox/busybox
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-BUSYBOX-1920730
  Introduced through: busybox/busybox@1.31.1-r16, alpine-baselayout/alpine-baselayout@3.2.0-r6, ca-certificates/ca-certificates@20191127-r3, busybox/ssl_client@1.31.1-r16
  From: busybox/busybox@1.31.1-r16
  From: alpine-baselayout/alpine-baselayout@3.2.0-r6 > busybox/busybox@1.31.1-r16
  From: ca-certificates/ca-certificates@20191127-r3 > busybox/busybox@1.31.1-r16
  and 1 more...
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.31.1-r21

✗ High severity vulnerability found in busybox/busybox
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-BUSYBOX-1920731
  Introduced through: busybox/busybox@1.31.1-r16, alpine-baselayout/alpine-baselayout@3.2.0-r6, ca-certificates/ca-certificates@20191127-r3, busybox/ssl_client@1.31.1-r16
  From: busybox/busybox@1.31.1-r16
  From: alpine-baselayout/alpine-baselayout@3.2.0-r6 > busybox/busybox@1.31.1-r16
  From: ca-certificates/ca-certificates@20191127-r3 > busybox/busybox@1.31.1-r16
  and 1 more...
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.31.1-r21

✗ High severity vulnerability found in busybox/busybox
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-BUSYBOX-1920739
  Introduced through: busybox/busybox@1.31.1-r16, alpine-baselayout/alpine-baselayout@3.2.0-r6, ca-certificates/ca-certificates@20191127-r3, busybox/ssl_client@1.31.1-r16
  From: busybox/busybox@1.31.1-r16
  From: alpine-baselayout/alpine-baselayout@3.2.0-r6 > busybox/busybox@1.31.1-r16
  From: ca-certificates/ca-certificates@20191127-r3 > busybox/busybox@1.31.1-r16
  and 1 more...
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.31.1-r21

✗ High severity vulnerability found in busybox/busybox
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-BUSYBOX-1920754
  Introduced through: busybox/busybox@1.31.1-r16, alpine-baselayout/alpine-baselayout@3.2.0-r6, ca-certificates/ca-certificates@20191127-r3, busybox/ssl_client@1.31.1-r16
  From: busybox/busybox@1.31.1-r16
  From: alpine-baselayout/alpine-baselayout@3.2.0-r6 > busybox/busybox@1.31.1-r16
  From: ca-certificates/ca-certificates@20191127-r3 > busybox/busybox@1.31.1-r16
  and 1 more...
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.31.1-r21

✗ High severity vulnerability found in busybox/busybox
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-BUSYBOX-1920758
  Introduced through: busybox/busybox@1.31.1-r16, alpine-baselayout/alpine-baselayout@3.2.0-r6, ca-certificates/ca-certificates@20191127-r3, busybox/ssl_client@1.31.1-r16
  From: busybox/busybox@1.31.1-r16
  From: alpine-baselayout/alpine-baselayout@3.2.0-r6 > busybox/busybox@1.31.1-r16
  From: ca-certificates/ca-certificates@20191127-r3 > busybox/busybox@1.31.1-r16
  and 1 more...
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.31.1-r21

✗ High severity vulnerability found in busybox/busybox
  Description: CVE-2022-28391
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-BUSYBOX-2440610
  Introduced through: busybox/busybox@1.31.1-r16, alpine-baselayout/alpine-baselayout@3.2.0-r6, ca-certificates/ca-certificates@20191127-r3, busybox/ssl_client@1.31.1-r16
  From: busybox/busybox@1.31.1-r16
  From: alpine-baselayout/alpine-baselayout@3.2.0-r6 > busybox/busybox@1.31.1-r16
  From: ca-certificates/ca-certificates@20191127-r3 > busybox/busybox@1.31.1-r16
  and 1 more...
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 1.31.1-r22

✗ High severity vulnerability found in apk-tools/apk-tools
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-APKTOOLS-1246338
  Introduced through: apk-tools/apk-tools@2.10.5-r1
  From: apk-tools/apk-tools@2.10.5-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.10.6-r0

✗ Critical severity vulnerability found in zlib/zlib
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-ZLIB-2977082
  Introduced through: zlib/zlib@1.2.11-r3, .python-rundeps@20200804.041307, apk-tools/apk-tools@2.10.5-r1, curl/libcurl@7.79.1-r0, curl/curl@7.79.1-r0
  From: zlib/zlib@1.2.11-r3
  From: .python-rundeps@20200804.041307 > zlib/zlib@1.2.11-r3
  From: apk-tools/apk-tools@2.10.5-r1 > zlib/zlib@1.2.11-r3
  and 2 more...
  Image layer: 'apk --no-cache add curl'
  Fixed in: 1.2.12-r2

✗ Critical severity vulnerability found in openssl/libcrypto1.1
  Description: Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-OPENSSL-1569452
  Introduced through: openssl/libcrypto1.1@1.1.1g-r0, openssl/libssl1.1@1.1.1g-r0, .python-rundeps@20200804.041307, apk-tools/apk-tools@2.10.5-r1, libtls-standalone/libtls-standalone@2.9.1-r1, ca-certificates/ca-certificates@20191127-r3, curl/libcurl@7.79.1-r0, krb5-conf/krb5-conf@1.0-r2
  From: openssl/libcrypto1.1@1.1.1g-r0
  From: openssl/libssl1.1@1.1.1g-r0 > openssl/libcrypto1.1@1.1.1g-r0
  From: .python-rundeps@20200804.041307 > openssl/libcrypto1.1@1.1.1g-r0
  and 11 more...
  Image layer: 'apk --no-cache add curl'
  Fixed in: 1.1.1l-r0

✗ Critical severity vulnerability found in expat/expat
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-EXPAT-2342150
  Introduced through: expat/expat@2.2.9-r1, .python-rundeps@20200804.041307
  From: expat/expat@2.2.9-r1
  From: .python-rundeps@20200804.041307 > expat/expat@2.2.9-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.2.10-r0

✗ Critical severity vulnerability found in expat/expat
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-EXPAT-2342157
  Introduced through: expat/expat@2.2.9-r1, .python-rundeps@20200804.041307
  From: expat/expat@2.2.9-r1
  From: .python-rundeps@20200804.041307 > expat/expat@2.2.9-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.2.10-r0

✗ Critical severity vulnerability found in expat/expat
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-EXPAT-2342158
  Introduced through: expat/expat@2.2.9-r1, .python-rundeps@20200804.041307
  From: expat/expat@2.2.9-r1
  From: .python-rundeps@20200804.041307 > expat/expat@2.2.9-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.2.10-r0

✗ Critical severity vulnerability found in expat/expat
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-EXPAT-2406624
  Introduced through: expat/expat@2.2.9-r1, .python-rundeps@20200804.041307
  From: expat/expat@2.2.9-r1
  From: .python-rundeps@20200804.041307 > expat/expat@2.2.9-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.2.10-r1

✗ Critical severity vulnerability found in expat/expat
  Description: Exposure of Resource to Wrong Sphere
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-EXPAT-2407740
  Introduced through: expat/expat@2.2.9-r1, .python-rundeps@20200804.041307
  From: expat/expat@2.2.9-r1
  From: .python-rundeps@20200804.041307 > expat/expat@2.2.9-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.2.10-r2

✗ Critical severity vulnerability found in expat/expat
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-EXPAT-2407741
  Introduced through: expat/expat@2.2.9-r1, .python-rundeps@20200804.041307
  From: expat/expat@2.2.9-r1
  From: .python-rundeps@20200804.041307 > expat/expat@2.2.9-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.2.10-r2

✗ Critical severity vulnerability found in expat/expat
  Description: Improper Encoding or Escaping of Output
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-EXPAT-2407742
  Introduced through: expat/expat@2.2.9-r1, .python-rundeps@20200804.041307
  From: expat/expat@2.2.9-r1
  From: .python-rundeps@20200804.041307 > expat/expat@2.2.9-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.2.10-r2

✗ Critical severity vulnerability found in apk-tools/apk-tools
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-ALPINE312-APKTOOLS-1533753
  Introduced through: apk-tools/apk-tools@2.10.5-r1
  From: apk-tools/apk-tools@2.10.5-r1
  Image layer: Introduced by your base image (python:3.8.5-alpine3.12)
  Fixed in: 2.10.7-r0



Organization:      bhavdeep1304
Package manager:   apk
Project name:      docker-image|orchestracities/quantumleap
Docker image:      orchestracities/quantumleap:0.8.3
Platform:          linux/amd64
Base image:        python:3.8.5-alpine3.12
Licenses:          enabled

Tested 38 dependencies for known issues, found 56 issues.

Base Image               Vulnerabilities  Severity
python:3.8.5-alpine3.12  52               10 critical, 28 high, 12 medium, 2 low

Recommendations for base image upgrade:

Alternative image types
Base Image                     Vulnerabilities  Severity
python:3.13.0b2-slim           43               1 critical, 0 high, 0 medium, 42 low
python:3.12.4-slim-bookworm    47               1 critical, 0 high, 0 medium, 46 low
python:3.13.0b2-slim-bullseye  78               1 critical, 1 high, 0 medium, 76 low
python:3.13.0b2-bookworm       197              2 critical, 0 high, 0 medium, 195 low

Alpine 3.12.0 is no longer supported by the Alpine maintainers. Vulnerability detection may be affected by a lack of security updates.

Learn more: https://docs.snyk.io/products/snyk-container/getting-around-the-snyk-container-ui/base-image-detection


```
