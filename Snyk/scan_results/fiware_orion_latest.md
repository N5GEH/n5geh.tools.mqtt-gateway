**Scanning fiware/orion:latest**
```

Testing fiware/orion:latest...

✗ Low severity vulnerability found in util-linux/libblkid1
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-UTILLINUX-2401083
  Introduced through: util-linux/libblkid1@2.38.1-5+deb12u1, e2fsprogs@1.47.0-2, util-linux/libmount1@2.38.1-5+deb12u1, util-linux@2.38.1-5+deb12u1, util-linux/mount@2.38.1-5+deb12u1, util-linux/libuuid1@2.38.1-5+deb12u1, util-linux/libsmartcols1@2.38.1-5+deb12u1, util-linux/util-linux-extra@2.38.1-5+deb12u1, util-linux/bsdutils@1:2.38.1-5+deb12u1
  From: util-linux/libblkid1@2.38.1-5+deb12u1
  From: e2fsprogs@1.47.0-2 > util-linux/libblkid1@2.38.1-5+deb12u1
  From: util-linux/libmount1@2.38.1-5+deb12u1 > util-linux/libblkid1@2.38.1-5+deb12u1
  and 17 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff6
  Description: Missing Release of Resource after Effective Lifetime
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-1560922
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tiff/libtiff6
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-1561093
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tiff/libtiff6
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-1561130
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tiff/libtiff6
  Description: NULL Pointer Dereference
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-1561402
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tiff/libtiff6
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-1561632
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tiff/libtiff6
  Description: Improper Resource Shutdown or Release
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-2440572
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tiff/libtiff6
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-5416364
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tiff/libtiff6
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-5673710
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tiff/libtiff6
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-5747599
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tiff/libtiff6
  Description: Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-5749338
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tiff/libtiff6
  Description: NULL Pointer Dereference
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-5750144
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tiff/libtiff6
  Description: Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-5767899
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tiff/libtiff6
  Description: Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-5773187
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tiff/libtiff6
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-6079922
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tiff/libtiff6
  Description: Resource Exhaustion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-6084514
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tiff/libtiff6
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-6190608
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tiff/libtiff6
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TIFF-6190785
  Introduced through: tiff/libtiff6@4.5.0-6+deb12u1, glibc/libc-devtools@2.36-9+deb12u7
  From: tiff/libtiff6@4.5.0-6+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in tar
  Description: CVE-2005-2541
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TAR-1560620
  Introduced through: tar@1.34+dfsg-1.2+deb12u1, dash@0.5.12-2
  From: tar@1.34+dfsg-1.2+deb12u1
  From: dash@0.5.12-2 > dpkg@1.21.22 > tar@1.34+dfsg-1.2+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Link Following
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SYSTEMD-1560739
  Introduced through: systemd/libsystemd0@252.22-1~deb12u1, apt@2.6.1, util-linux@2.38.1-5+deb12u1, util-linux/bsdutils@1:2.38.1-5+deb12u1, systemd/libudev1@252.22-1~deb12u1
  From: systemd/libsystemd0@252.22-1~deb12u1
  From: apt@2.6.1 > systemd/libsystemd0@252.22-1~deb12u1
  From: util-linux@2.38.1-5+deb12u1 > systemd/libsystemd0@252.22-1~deb12u1
  and 5 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Improper Validation of Integrity Check Value
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SYSTEMD-5733385
  Introduced through: systemd/libsystemd0@252.22-1~deb12u1, apt@2.6.1, util-linux@2.38.1-5+deb12u1, util-linux/bsdutils@1:2.38.1-5+deb12u1, systemd/libudev1@252.22-1~deb12u1
  From: systemd/libsystemd0@252.22-1~deb12u1
  From: apt@2.6.1 > systemd/libsystemd0@252.22-1~deb12u1
  From: util-linux@2.38.1-5+deb12u1 > systemd/libsystemd0@252.22-1~deb12u1
  and 5 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Improper Validation of Integrity Check Value
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SYSTEMD-5733390
  Introduced through: systemd/libsystemd0@252.22-1~deb12u1, apt@2.6.1, util-linux@2.38.1-5+deb12u1, util-linux/bsdutils@1:2.38.1-5+deb12u1, systemd/libudev1@252.22-1~deb12u1
  From: systemd/libsystemd0@252.22-1~deb12u1
  From: apt@2.6.1 > systemd/libsystemd0@252.22-1~deb12u1
  From: util-linux@2.38.1-5+deb12u1 > systemd/libsystemd0@252.22-1~deb12u1
  and 5 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Improper Validation of Integrity Check Value
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SYSTEMD-5733398
  Introduced through: systemd/libsystemd0@252.22-1~deb12u1, apt@2.6.1, util-linux@2.38.1-5+deb12u1, util-linux/bsdutils@1:2.38.1-5+deb12u1, systemd/libudev1@252.22-1~deb12u1
  From: systemd/libsystemd0@252.22-1~deb12u1
  From: apt@2.6.1 > systemd/libsystemd0@252.22-1~deb12u1
  From: util-linux@2.38.1-5+deb12u1 > systemd/libsystemd0@252.22-1~deb12u1
  and 5 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: CVE-2023-50868
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SYSTEMD-6277509
  Introduced through: systemd/libsystemd0@252.22-1~deb12u1, apt@2.6.1, util-linux@2.38.1-5+deb12u1, util-linux/bsdutils@1:2.38.1-5+deb12u1, systemd/libudev1@252.22-1~deb12u1
  From: systemd/libsystemd0@252.22-1~deb12u1
  From: apt@2.6.1 > systemd/libsystemd0@252.22-1~deb12u1
  From: util-linux@2.38.1-5+deb12u1 > systemd/libsystemd0@252.22-1~deb12u1
  and 5 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 252.23-1~deb12u1

✗ Low severity vulnerability found in shadow/passwd
  Description: Access Restriction Bypass
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SHADOW-1559391
  Introduced through: shadow/passwd@1:4.13+dfsg1-1+b1, adduser@3.134, shadow/login@1:4.13+dfsg1-1+b1
  From: shadow/passwd@1:4.13+dfsg1-1+b1
  From: adduser@3.134 > shadow/passwd@1:4.13+dfsg1-1+b1
  From: shadow/login@1:4.13+dfsg1-1+b1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in shadow/passwd
  Description: Incorrect Permission Assignment for Critical Resource
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SHADOW-1559403
  Introduced through: shadow/passwd@1:4.13+dfsg1-1+b1, adduser@3.134, shadow/login@1:4.13+dfsg1-1+b1
  From: shadow/passwd@1:4.13+dfsg1-1+b1
  From: adduser@3.134 > shadow/passwd@1:4.13+dfsg1-1+b1
  From: shadow/login@1:4.13+dfsg1-1+b1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in shadow/passwd
  Description: Arbitrary Code Injection
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SHADOW-5423923
  Introduced through: shadow/passwd@1:4.13+dfsg1-1+b1, adduser@3.134, shadow/login@1:4.13+dfsg1-1+b1
  From: shadow/passwd@1:4.13+dfsg1-1+b1
  From: adduser@3.134 > shadow/passwd@1:4.13+dfsg1-1+b1
  From: shadow/login@1:4.13+dfsg1-1+b1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in shadow/passwd
  Description: Improper Authentication
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SHADOW-5879156
  Introduced through: shadow/passwd@1:4.13+dfsg1-1+b1, adduser@3.134, shadow/login@1:4.13+dfsg1-1+b1
  From: shadow/passwd@1:4.13+dfsg1-1+b1
  From: adduser@3.134 > shadow/passwd@1:4.13+dfsg1-1+b1
  From: shadow/login@1:4.13+dfsg1-1+b1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in perl/perl-base
  Description: Link Following
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-PERL-1556505
  Introduced through: perl/perl-base@5.36.0-7+deb12u1
  From: perl/perl-base@5.36.0-7+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in perl/perl-base
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-PERL-5489184
  Introduced through: perl/perl-base@5.36.0-7+deb12u1
  From: perl/perl-base@5.36.0-7+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in perl/perl-base
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-PERL-5489190
  Introduced through: perl/perl-base@5.36.0-7+deb12u1
  From: perl/perl-base@5.36.0-7+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in pam/libpam0g
  Description: CVE-2024-22365
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-PAM-6178914
  Introduced through: pam/libpam0g@1.5.2-6+deb12u1, shadow/login@1:4.13+dfsg1-1+b1, util-linux@2.38.1-5+deb12u1, adduser@3.134, pam/libpam-modules-bin@1.5.2-6+deb12u1, pam/libpam-modules@1.5.2-6+deb12u1, pam/libpam-runtime@1.5.2-6+deb12u1
  From: pam/libpam0g@1.5.2-6+deb12u1
  From: shadow/login@1:4.13+dfsg1-1+b1 > pam/libpam0g@1.5.2-6+deb12u1
  From: util-linux@2.38.1-5+deb12u1 > pam/libpam0g@1.5.2-6+deb12u1
  and 11 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openssl/libssl3
  Description: CVE-2023-6237
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENSSL-6157243
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.28+dfsg-10, ca-certificates@20230311, curl@7.88.1-10+deb12u5, openssl@3.0.11-1~deb12u2
  From: cyrus-sasl2/libsasl2-modules@2.1.28+dfsg-10 > openssl/libssl3@3.0.11-1~deb12u2
  From: ca-certificates@20230311 > openssl@3.0.11-1~deb12u2 > openssl/libssl3@3.0.11-1~deb12u2
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > openssl/libssl3@3.0.11-1~deb12u2
  and 4 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 3.0.13-1~deb12u1

✗ Low severity vulnerability found in openssl/libssl3
  Description: CVE-2024-2511
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENSSL-6592092
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.28+dfsg-10, ca-certificates@20230311, curl@7.88.1-10+deb12u5, openssl@3.0.11-1~deb12u2
  From: cyrus-sasl2/libsasl2-modules@2.1.28+dfsg-10 > openssl/libssl3@3.0.11-1~deb12u2
  From: ca-certificates@20230311 > openssl@3.0.11-1~deb12u2 > openssl/libssl3@3.0.11-1~deb12u2
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > openssl/libssl3@3.0.11-1~deb12u2
  and 4 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openssl/libssl3
  Description: CVE-2024-4603
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENSSL-6861561
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.28+dfsg-10, ca-certificates@20230311, curl@7.88.1-10+deb12u5, openssl@3.0.11-1~deb12u2
  From: cyrus-sasl2/libsasl2-modules@2.1.28+dfsg-10 > openssl/libssl3@3.0.11-1~deb12u2
  From: ca-certificates@20230311 > openssl@3.0.11-1~deb12u2 > openssl/libssl3@3.0.11-1~deb12u2
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > openssl/libssl3@3.0.11-1~deb12u2
  and 4 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openssl/libssl3
  Description: CVE-2024-4741
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENSSL-7151359
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.28+dfsg-10, ca-certificates@20230311, curl@7.88.1-10+deb12u5, openssl@3.0.11-1~deb12u2
  From: cyrus-sasl2/libsasl2-modules@2.1.28+dfsg-10 > openssl/libssl3@3.0.11-1~deb12u2
  From: ca-certificates@20230311 > openssl@3.0.11-1~deb12u2 > openssl/libssl3@3.0.11-1~deb12u2
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > openssl/libssl3@3.0.11-1~deb12u2
  and 4 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openssl/libssl3
  Description: CVE-2024-5535
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENSSL-7411350
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.28+dfsg-10, ca-certificates@20230311, curl@7.88.1-10+deb12u5, openssl@3.0.11-1~deb12u2
  From: cyrus-sasl2/libsasl2-modules@2.1.28+dfsg-10 > openssl/libssl3@3.0.11-1~deb12u2
  From: ca-certificates@20230311 > openssl@3.0.11-1~deb12u2 > openssl/libssl3@3.0.11-1~deb12u2
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > openssl/libssl3@3.0.11-1~deb12u2
  and 4 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openldap/libldap-2.5-0
  Description: Improper Initialization
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENLDAP-1555631
  Introduced through: curl@7.88.1-10+deb12u5, openldap/libldap-common@2.5.13+dfsg-5
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > openldap/libldap-2.5-0@2.5.13+dfsg-5
  From: openldap/libldap-common@2.5.13+dfsg-5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openldap/libldap-2.5-0
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENLDAP-1555724
  Introduced through: curl@7.88.1-10+deb12u5, openldap/libldap-common@2.5.13+dfsg-5
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > openldap/libldap-2.5-0@2.5.13+dfsg-5
  From: openldap/libldap-common@2.5.13+dfsg-5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openldap/libldap-2.5-0
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENLDAP-1555918
  Introduced through: curl@7.88.1-10+deb12u5, openldap/libldap-common@2.5.13+dfsg-5
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > openldap/libldap-2.5-0@2.5.13+dfsg-5
  From: openldap/libldap-common@2.5.13+dfsg-5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openldap/libldap-2.5-0
  Description: Cryptographic Issues
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENLDAP-1555941
  Introduced through: curl@7.88.1-10+deb12u5, openldap/libldap-common@2.5.13+dfsg-5
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > openldap/libldap-2.5-0@2.5.13+dfsg-5
  From: openldap/libldap-common@2.5.13+dfsg-5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openldap/libldap-2.5-0
  Description: NULL Pointer Dereference
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENLDAP-5660620
  Introduced through: curl@7.88.1-10+deb12u5, openldap/libldap-common@2.5.13+dfsg-5
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > openldap/libldap-2.5-0@2.5.13+dfsg-5
  From: openldap/libldap-common@2.5.13+dfsg-5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in nghttp2/libnghttp2-14
  Description: CVE-2024-28182
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-NGHTTP2-6541749
  Introduced through: curl@7.88.1-10+deb12u5
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > nghttp2/libnghttp2-14@1.52.0-1+deb12u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in ncurses/libtinfo6
  Description: CVE-2023-50495
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-NCURSES-6123823
  Introduced through: ncurses/libtinfo6@6.4-4, bash/bash@5.2.15-2+b2, ncurses/ncurses-bin@6.4-4, util-linux@2.38.1-5+deb12u1, ncurses/ncurses-base@6.4-4
  From: ncurses/libtinfo6@6.4-4
  From: bash/bash@5.2.15-2+b2 > ncurses/libtinfo6@6.4-4
  From: ncurses/ncurses-bin@6.4-4 > ncurses/libtinfo6@6.4-4
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in ncurses/libtinfo6
  Description: CVE-2023-45918
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-NCURSES-6252773
  Introduced through: ncurses/libtinfo6@6.4-4, bash/bash@5.2.15-2+b2, ncurses/ncurses-bin@6.4-4, util-linux@2.38.1-5+deb12u1, ncurses/ncurses-base@6.4-4
  From: ncurses/libtinfo6@6.4-4
  From: bash/bash@5.2.15-2+b2 > ncurses/libtinfo6@6.4-4
  From: ncurses/ncurses-bin@6.4-4 > ncurses/libtinfo6@6.4-4
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in libpng1.6/libpng16-16
  Description: Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-LIBPNG16-2363910
  Introduced through: libpng1.6/libpng16-16@1.6.39-2, glibc/libc-devtools@2.36-9+deb12u7
  From: libpng1.6/libpng16-16@1.6.39-2
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > libpng1.6/libpng16-16@1.6.39-2
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > fontconfig/libfontconfig1@2.14.1-4 > freetype/libfreetype6@2.12.1+dfsg-5 > libpng1.6/libpng16-16@1.6.39-2
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in libheif/libheif1
  Description: Divide By Zero
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-LIBHEIF-5498469
  Introduced through: libheif/libheif1@1.15.1-1, glibc/libc-devtools@2.36-9+deb12u7
  From: libheif/libheif1@1.15.1-1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > libheif/libheif1@1.15.1-1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in libheif/libheif1
  Description: CVE-2023-49462
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-LIBHEIF-6105360
  Introduced through: libheif/libheif1@1.15.1-1, glibc/libc-devtools@2.36-9+deb12u7
  From: libheif/libheif1@1.15.1-1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > libheif/libheif1@1.15.1-1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in libheif/libheif1
  Description: CVE-2023-49460
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-LIBHEIF-6105367
  Introduced through: libheif/libheif1@1.15.1-1, glibc/libc-devtools@2.36-9+deb12u7
  From: libheif/libheif1@1.15.1-1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > libheif/libheif1@1.15.1-1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in libheif/libheif1
  Description: CVE-2023-49464
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-LIBHEIF-6105368
  Introduced through: libheif/libheif1@1.15.1-1, glibc/libc-devtools@2.36-9+deb12u7
  From: libheif/libheif1@1.15.1-1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > libheif/libheif1@1.15.1-1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in libheif/libheif1
  Description: CVE-2023-49463
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-LIBHEIF-6105378
  Introduced through: libheif/libheif1@1.15.1-1, glibc/libc-devtools@2.36-9+deb12u7
  From: libheif/libheif1@1.15.1-1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > libheif/libheif1@1.15.1-1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in libheif/libheif1
  Description: CVE-2024-25269
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-LIBHEIF-6371532
  Introduced through: libheif/libheif1@1.15.1-1, glibc/libc-devtools@2.36-9+deb12u7
  From: libheif/libheif1@1.15.1-1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > libheif/libheif1@1.15.1-1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in libgcrypt20
  Description: Use of a Broken or Risky Cryptographic Algorithm
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-LIBGCRYPT20-1550206
  Introduced through: libgcrypt20/libgcrypt20-dev@1.10.1-3, apt@2.6.1
  From: libgcrypt20/libgcrypt20-dev@1.10.1-3 > libgcrypt20@1.10.1-3
  From: apt@2.6.1 > apt/libapt-pkg6.0@2.6.1 > libgcrypt20@1.10.1-3
  From: apt@2.6.1 > gnupg2/gpgv@2.2.40-1.1 > libgcrypt20@1.10.1-3
  and 2 more...
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in libgcrypt20
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-LIBGCRYPT20-6405981
  Introduced through: libgcrypt20/libgcrypt20-dev@1.10.1-3, apt@2.6.1
  From: libgcrypt20/libgcrypt20-dev@1.10.1-3 > libgcrypt20@1.10.1-3
  From: apt@2.6.1 > apt/libapt-pkg6.0@2.6.1 > libgcrypt20@1.10.1-3
  From: apt@2.6.1 > gnupg2/gpgv@2.2.40-1.1 > libgcrypt20@1.10.1-3
  and 2 more...
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in libde265/libde265-0
  Description: CVE-2023-51792
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-LIBDE265-6672145
  Introduced through: libde265/libde265-0@1.0.11-1+deb12u2, glibc/libc-devtools@2.36-9+deb12u7
  From: libde265/libde265-0@1.0.11-1+deb12u2
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > libheif/libheif1@1.15.1-1 > libde265/libde265-0@1.0.11-1+deb12u2
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in libde265/libde265-0
  Description: CVE-2024-38949
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-LIBDE265-7411271
  Introduced through: libde265/libde265-0@1.0.11-1+deb12u2, glibc/libc-devtools@2.36-9+deb12u7
  From: libde265/libde265-0@1.0.11-1+deb12u2
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > libheif/libheif1@1.15.1-1 > libde265/libde265-0@1.0.11-1+deb12u2
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in libde265/libde265-0
  Description: CVE-2024-38950
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-LIBDE265-7411272
  Introduced through: libde265/libde265-0@1.0.11-1+deb12u2, glibc/libc-devtools@2.36-9+deb12u7
  From: libde265/libde265-0@1.0.11-1+deb12u2
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > libheif/libheif1@1.15.1-1 > libde265/libde265-0@1.0.11-1+deb12u2
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in krb5/libkrb5support0
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-KRB5-1549480
  Introduced through: curl@7.88.1-10+deb12u5, libgcrypt20/libgcrypt20-dev@1.10.1-3, krb5/krb5-locales@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libk5crypto3@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libkrb5-3@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  and 6 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in krb5/libkrb5support0
  Description: CVE-2024-26461
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-KRB5-6277411
  Introduced through: curl@7.88.1-10+deb12u5, libgcrypt20/libgcrypt20-dev@1.10.1-3, krb5/krb5-locales@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libk5crypto3@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libkrb5-3@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  and 6 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in krb5/libkrb5support0
  Description: CVE-2024-26458
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-KRB5-6277412
  Introduced through: curl@7.88.1-10+deb12u5, libgcrypt20/libgcrypt20-dev@1.10.1-3, krb5/krb5-locales@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libk5crypto3@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libkrb5-3@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  and 6 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in krb5/libkrb5support0
  Description: CVE-2024-26462
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-KRB5-6277421
  Introduced through: curl@7.88.1-10+deb12u5, libgcrypt20/libgcrypt20-dev@1.10.1-3, krb5/krb5-locales@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libk5crypto3@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libkrb5-3@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  and 6 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in krb5/libkrb5support0
  Description: CVE-2024-37370
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-KRB5-7411314
  Introduced through: curl@7.88.1-10+deb12u5, libgcrypt20/libgcrypt20-dev@1.10.1-3, krb5/krb5-locales@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libk5crypto3@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libkrb5-3@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  and 6 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.20.1-2+deb12u2

✗ Low severity vulnerability found in krb5/libkrb5support0
  Description: CVE-2024-37371
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-KRB5-7411315
  Introduced through: curl@7.88.1-10+deb12u5, libgcrypt20/libgcrypt20-dev@1.10.1-3, krb5/krb5-locales@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libk5crypto3@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > krb5/libgssapi-krb5-2@1.20.1-2+deb12u1 > krb5/libkrb5-3@1.20.1-2+deb12u1 > krb5/libkrb5support0@1.20.1-2+deb12u1
  and 6 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.20.1-2+deb12u2

✗ Low severity vulnerability found in jbigkit/libjbig0
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-JBIGKIT-1549085
  Introduced through: jbigkit/libjbig0@2.1-6.1, glibc/libc-devtools@2.36-9+deb12u7
  From: jbigkit/libjbig0@2.1-6.1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > tiff/libtiff6@4.5.0-6+deb12u1 > jbigkit/libjbig0@2.1-6.1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in gnutls28/libgnutls30
  Description: Improper Input Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GNUTLS28-1547121
  Introduced through: apt@2.6.1, curl@7.88.1-10+deb12u5
  From: apt@2.6.1 > gnutls28/libgnutls30@3.7.9-2+deb12u2
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > rtmpdump/librtmp1@2.4+20151223.gitfa8646d.1-2+b2 > gnutls28/libgnutls30@3.7.9-2+deb12u2
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > openldap/libldap-2.5-0@2.5.13+dfsg-5 > gnutls28/libgnutls30@3.7.9-2+deb12u2
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in gnutls28/libgnutls30
  Description: Uncaught Exception
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GNUTLS28-6474581
  Introduced through: apt@2.6.1, curl@7.88.1-10+deb12u5
  From: apt@2.6.1 > gnutls28/libgnutls30@3.7.9-2+deb12u2
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > rtmpdump/librtmp1@2.4+20151223.gitfa8646d.1-2+b2 > gnutls28/libgnutls30@3.7.9-2+deb12u2
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > openldap/libldap-2.5-0@2.5.13+dfsg-5 > gnutls28/libgnutls30@3.7.9-2+deb12u2
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 3.7.9-2+deb12u3

✗ Low severity vulnerability found in gnutls28/libgnutls30
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GNUTLS28-6474586
  Introduced through: apt@2.6.1, curl@7.88.1-10+deb12u5
  From: apt@2.6.1 > gnutls28/libgnutls30@3.7.9-2+deb12u2
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > rtmpdump/librtmp1@2.4+20151223.gitfa8646d.1-2+b2 > gnutls28/libgnutls30@3.7.9-2+deb12u2
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > openldap/libldap-2.5-0@2.5.13+dfsg-5 > gnutls28/libgnutls30@3.7.9-2+deb12u2
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 3.7.9-2+deb12u3

✗ Low severity vulnerability found in gnupg2/gpgv
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GNUPG2-3330747
  Introduced through: gnupg2/gpgv@2.2.40-1.1, apt@2.6.1
  From: gnupg2/gpgv@2.2.40-1.1
  From: apt@2.6.1 > gnupg2/gpgv@2.2.40-1.1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GLIBC-1546991
  Introduced through: glibc/libc-bin@2.36-9+deb12u7, glibc/libc-devtools@2.36-9+deb12u7, glibc/libc6@2.36-9+deb12u7, libgcrypt20/libgcrypt20-dev@1.10.1-3
  From: glibc/libc-bin@2.36-9+deb12u7
  From: glibc/libc-devtools@2.36-9+deb12u7
  From: glibc/libc6@2.36-9+deb12u7
  and 2 more...
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Uncontrolled Recursion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GLIBC-1547039
  Introduced through: glibc/libc-bin@2.36-9+deb12u7, glibc/libc-devtools@2.36-9+deb12u7, glibc/libc6@2.36-9+deb12u7, libgcrypt20/libgcrypt20-dev@1.10.1-3
  From: glibc/libc-bin@2.36-9+deb12u7
  From: glibc/libc-devtools@2.36-9+deb12u7
  From: glibc/libc6@2.36-9+deb12u7
  and 2 more...
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Uncontrolled Recursion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GLIBC-1547069
  Introduced through: glibc/libc-bin@2.36-9+deb12u7, glibc/libc-devtools@2.36-9+deb12u7, glibc/libc6@2.36-9+deb12u7, libgcrypt20/libgcrypt20-dev@1.10.1-3
  From: glibc/libc-bin@2.36-9+deb12u7
  From: glibc/libc-devtools@2.36-9+deb12u7
  From: glibc/libc6@2.36-9+deb12u7
  and 2 more...
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Use of Insufficiently Random Values
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GLIBC-1547135
  Introduced through: glibc/libc-bin@2.36-9+deb12u7, glibc/libc-devtools@2.36-9+deb12u7, glibc/libc6@2.36-9+deb12u7, libgcrypt20/libgcrypt20-dev@1.10.1-3
  From: glibc/libc-bin@2.36-9+deb12u7
  From: glibc/libc-devtools@2.36-9+deb12u7
  From: glibc/libc6@2.36-9+deb12u7
  and 2 more...
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GLIBC-1547196
  Introduced through: glibc/libc-bin@2.36-9+deb12u7, glibc/libc-devtools@2.36-9+deb12u7, glibc/libc6@2.36-9+deb12u7, libgcrypt20/libgcrypt20-dev@1.10.1-3
  From: glibc/libc-bin@2.36-9+deb12u7
  From: glibc/libc-devtools@2.36-9+deb12u7
  From: glibc/libc6@2.36-9+deb12u7
  and 2 more...
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Resource Management Errors
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GLIBC-1547293
  Introduced through: glibc/libc-bin@2.36-9+deb12u7, glibc/libc-devtools@2.36-9+deb12u7, glibc/libc6@2.36-9+deb12u7, libgcrypt20/libgcrypt20-dev@1.10.1-3
  From: glibc/libc-bin@2.36-9+deb12u7
  From: glibc/libc-devtools@2.36-9+deb12u7
  From: glibc/libc6@2.36-9+deb12u7
  and 2 more...
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in glibc/libc-bin
  Description: CVE-2019-1010023
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GLIBC-1547373
  Introduced through: glibc/libc-bin@2.36-9+deb12u7, glibc/libc-devtools@2.36-9+deb12u7, glibc/libc6@2.36-9+deb12u7, libgcrypt20/libgcrypt20-dev@1.10.1-3
  From: glibc/libc-bin@2.36-9+deb12u7
  From: glibc/libc-devtools@2.36-9+deb12u7
  From: glibc/libc6@2.36-9+deb12u7
  and 2 more...
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in gcc-12/libstdc++6
  Description: Uncontrolled Recursion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GCC12-2606941
  Introduced through: abseil/libabsl20220623@20220623.1-1, apt@2.6.1, boost1.74/libboost-thread1.74.0@1.74.0+ds1-21, icu/libicu72@72.1-3, libavif/libavif15@0.11.1-1, glibc/libc-devtools@2.36-9+deb12u7, gcc-12/gcc-12-base@12.2.0-14, gcc-12/libgcc-s1@12.2.0-14
  From: abseil/libabsl20220623@20220623.1-1 > gcc-12/libstdc++6@12.2.0-14
  From: apt@2.6.1 > gcc-12/libstdc++6@12.2.0-14
  From: boost1.74/libboost-thread1.74.0@1.74.0+ds1-21 > gcc-12/libstdc++6@12.2.0-14
  and 10 more...
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in gcc-12/libstdc++6
  Description: CVE-2023-4039
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GCC12-5901316
  Introduced through: abseil/libabsl20220623@20220623.1-1, apt@2.6.1, boost1.74/libboost-thread1.74.0@1.74.0+ds1-21, icu/libicu72@72.1-3, libavif/libavif15@0.11.1-1, glibc/libc-devtools@2.36-9+deb12u7, gcc-12/gcc-12-base@12.2.0-14, gcc-12/libgcc-s1@12.2.0-14
  From: abseil/libabsl20220623@20220623.1-1 > gcc-12/libstdc++6@12.2.0-14
  From: apt@2.6.1 > gcc-12/libstdc++6@12.2.0-14
  From: boost1.74/libboost-thread1.74.0@1.74.0+ds1-21 > gcc-12/libstdc++6@12.2.0-14
  and 10 more...
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in expat/libexpat1
  Description: Resource Exhaustion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-EXPAT-6227597
  Introduced through: expat/libexpat1@2.5.0-1, glibc/libc-devtools@2.36-9+deb12u7
  From: expat/libexpat1@2.5.0-1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > fontconfig/libfontconfig1@2.14.1-4 > expat/libexpat1@2.5.0-1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in expat/libexpat1
  Description: Improper Restriction of Recursive Entity References in DTDs ('XML Entity Expansion')
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-EXPAT-6227603
  Introduced through: expat/libexpat1@2.5.0-1, glibc/libc-devtools@2.36-9+deb12u7
  From: expat/libexpat1@2.5.0-1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > fontconfig/libfontconfig1@2.14.1-4 > expat/libexpat1@2.5.0-1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in expat/libexpat1
  Description: CVE-2024-28757
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-EXPAT-6420595
  Introduced through: expat/libexpat1@2.5.0-1, glibc/libc-devtools@2.36-9+deb12u7
  From: expat/libexpat1@2.5.0-1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > fontconfig/libfontconfig1@2.14.1-4 > expat/libexpat1@2.5.0-1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in dav1d/libdav1d6
  Description: Race Condition
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-DAV1D-5518047
  Introduced through: dav1d/libdav1d6@1.0.0-2+deb12u1, libavif/libavif15@0.11.1-1, glibc/libc-devtools@2.36-9+deb12u7
  From: dav1d/libdav1d6@1.0.0-2+deb12u1
  From: libavif/libavif15@0.11.1-1 > dav1d/libdav1d6@1.0.0-2+deb12u1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > libheif/libheif1@1.15.1-1 > dav1d/libdav1d6@1.0.0-2+deb12u1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in curl/libcurl4
  Description: CVE-2024-2379
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-CURL-6501697
  Introduced through: curl@7.88.1-10+deb12u5
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5
  From: curl@7.88.1-10+deb12u5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in curl/libcurl4
  Description: CVE-2024-2398
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-CURL-6501702
  Introduced through: curl@7.88.1-10+deb12u5
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5
  From: curl@7.88.1-10+deb12u5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.88.1-10+deb12u6

✗ Low severity vulnerability found in curl/libcurl4
  Description: CVE-2024-2004
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-CURL-6501703
  Introduced through: curl@7.88.1-10+deb12u5
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5
  From: curl@7.88.1-10+deb12u5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.88.1-10+deb12u6

✗ Low severity vulnerability found in coreutils
  Description: Improper Input Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-COREUTILS-1543939
  Introduced through: coreutils@9.1-1
  From: coreutils@9.1-1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in coreutils
  Description: Race Condition
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-COREUTILS-1543947
  Introduced through: coreutils@9.1-1
  From: coreutils@9.1-1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in apt/libapt-pkg6.0
  Description: Improper Verification of Cryptographic Signature
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-APT-1541449
  Introduced through: apt/libapt-pkg6.0@2.6.1, apt@2.6.1
  From: apt/libapt-pkg6.0@2.6.1
  From: apt@2.6.1 > apt/libapt-pkg6.0@2.6.1
  From: apt@2.6.1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in aom/libaom3
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-AOM-5878995
  Introduced through: aom/libaom3@3.6.0-1, libavif/libavif15@0.11.1-1, glibc/libc-devtools@2.36-9+deb12u7
  From: aom/libaom3@3.6.0-1
  From: libavif/libavif15@0.11.1-1 > aom/libaom3@3.6.0-1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > libheif/libheif1@1.15.1-1 > aom/libaom3@3.6.0-1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in aom/libaom3
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-AOM-6140324
  Introduced through: aom/libaom3@3.6.0-1, libavif/libavif15@0.11.1-1, glibc/libc-devtools@2.36-9+deb12u7
  From: aom/libaom3@3.6.0-1
  From: libavif/libavif15@0.11.1-1 > aom/libaom3@3.6.0-1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > libheif/libheif1@1.15.1-1 > aom/libaom3@3.6.0-1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Low severity vulnerability found in aom/libaom3
  Description: CVE-2024-5171
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-AOM-7197979
  Introduced through: aom/libaom3@3.6.0-1, libavif/libavif15@0.11.1-1, glibc/libc-devtools@2.36-9+deb12u7
  From: aom/libaom3@3.6.0-1
  From: libavif/libavif15@0.11.1-1 > aom/libaom3@3.6.0-1
  From: glibc/libc-devtools@2.36-9+deb12u7 > libgd2/libgd3@2.3.3-9 > libheif/libheif1@1.15.1-1 > aom/libaom3@3.6.0-1
  Image layer: Introduced by your base image (debian:12.4-slim)

✗ Medium severity vulnerability found in openssl/libssl3
  Description: Improper Check for Unusual or Exceptional Conditions
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENSSL-6048820
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.28+dfsg-10, ca-certificates@20230311, curl@7.88.1-10+deb12u5, openssl@3.0.11-1~deb12u2
  From: cyrus-sasl2/libsasl2-modules@2.1.28+dfsg-10 > openssl/libssl3@3.0.11-1~deb12u2
  From: ca-certificates@20230311 > openssl@3.0.11-1~deb12u2 > openssl/libssl3@3.0.11-1~deb12u2
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > openssl/libssl3@3.0.11-1~deb12u2
  and 4 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 3.0.13-1~deb12u1

✗ Medium severity vulnerability found in openssl/libssl3
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENSSL-6148845
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.28+dfsg-10, ca-certificates@20230311, curl@7.88.1-10+deb12u5, openssl@3.0.11-1~deb12u2
  From: cyrus-sasl2/libsasl2-modules@2.1.28+dfsg-10 > openssl/libssl3@3.0.11-1~deb12u2
  From: ca-certificates@20230311 > openssl@3.0.11-1~deb12u2 > openssl/libssl3@3.0.11-1~deb12u2
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > openssl/libssl3@3.0.11-1~deb12u2
  and 4 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 3.0.13-1~deb12u1

✗ Medium severity vulnerability found in openssl/libssl3
  Description: CVE-2024-0727
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENSSL-6190223
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.28+dfsg-10, ca-certificates@20230311, curl@7.88.1-10+deb12u5, openssl@3.0.11-1~deb12u2
  From: cyrus-sasl2/libsasl2-modules@2.1.28+dfsg-10 > openssl/libssl3@3.0.11-1~deb12u2
  From: ca-certificates@20230311 > openssl@3.0.11-1~deb12u2 > openssl/libssl3@3.0.11-1~deb12u2
  From: curl@7.88.1-10+deb12u5 > curl/libcurl4@7.88.1-10+deb12u5 > openssl/libssl3@3.0.11-1~deb12u2
  and 4 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 3.0.13-1~deb12u1

✗ High severity vulnerability found in systemd/libsystemd0
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SYSTEMD-6277507
  Introduced through: systemd/libsystemd0@252.22-1~deb12u1, apt@2.6.1, util-linux@2.38.1-5+deb12u1, util-linux/bsdutils@1:2.38.1-5+deb12u1, systemd/libudev1@252.22-1~deb12u1
  From: systemd/libsystemd0@252.22-1~deb12u1
  From: apt@2.6.1 > systemd/libsystemd0@252.22-1~deb12u1
  From: util-linux@2.38.1-5+deb12u1 > systemd/libsystemd0@252.22-1~deb12u1
  and 5 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 252.23-1~deb12u1

✗ Critical severity vulnerability found in zlib/zlib1g
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-ZLIB-6008963
  Introduced through: curl@7.88.1-10+deb12u5, util-linux@2.38.1-5+deb12u1, apt@2.6.1, dash@0.5.12-2, glibc/libc-devtools@2.36-9+deb12u7
  From: curl@7.88.1-10+deb12u5 > zlib/zlib1g@1:1.2.13.dfsg-1
  From: util-linux@2.38.1-5+deb12u1 > zlib/zlib1g@1:1.2.13.dfsg-1
  From: apt@2.6.1 > apt/libapt-pkg6.0@2.6.1 > zlib/zlib1g@1:1.2.13.dfsg-1
  and 9 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'



Organization:      bhavdeep1304
Package manager:   deb
Project name:      docker-image|fiware/orion
Docker image:      fiware/orion:latest
Platform:          linux/amd64
Base image:        debian:12.4-slim
Licenses:          enabled

Tested 159 dependencies for known issues, found 95 issues.

Base Image        Vulnerabilities  Severity
debian:12.4-slim  48               1 critical, 3 high, 2 medium, 42 low

Recommendations for base image upgrade:

Minor upgrades
Base Image                     Vulnerabilities  Severity
debian:bookworm-20240701-slim  33               1 critical, 0 high, 0 medium, 32 low


Learn more: https://docs.snyk.io/products/snyk-container/getting-around-the-snyk-container-ui/base-image-detection


```
