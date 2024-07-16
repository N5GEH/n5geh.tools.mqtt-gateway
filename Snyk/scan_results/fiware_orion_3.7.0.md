**Scanning fiware/orion:3.7.0**
```

Testing fiware/orion:3.7.0...

✗ Low severity vulnerability found in util-linux/libblkid1
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-UTILLINUX-2401081
  Introduced through: util-linux/libblkid1@2.36.1-8+deb11u1, e2fsprogs@1.46.2-2, util-linux/libmount1@2.36.1-8+deb11u1, util-linux/mount@2.36.1-8+deb11u1, util-linux/libuuid1@2.36.1-8+deb11u1, glibc/libc-devtools@2.31-13+deb11u3, util-linux@2.36.1-8+deb11u1, util-linux/bsdutils@1:2.36.1-8+deb11u1, util-linux/libsmartcols1@2.36.1-8+deb11u1
  From: util-linux/libblkid1@2.36.1-8+deb11u1
  From: e2fsprogs@1.46.2-2 > util-linux/libblkid1@2.36.1-8+deb11u1
  From: util-linux/libmount1@2.36.1-8+deb11u1 > util-linux/libblkid1@2.36.1-8+deb11u1
  and 16 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in util-linux/libblkid1
  Description: CVE-2024-28085
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-UTILLINUX-6508632
  Introduced through: util-linux/libblkid1@2.36.1-8+deb11u1, e2fsprogs@1.46.2-2, util-linux/libmount1@2.36.1-8+deb11u1, util-linux/mount@2.36.1-8+deb11u1, util-linux/libuuid1@2.36.1-8+deb11u1, glibc/libc-devtools@2.31-13+deb11u3, util-linux@2.36.1-8+deb11u1, util-linux/bsdutils@1:2.36.1-8+deb11u1, util-linux/libsmartcols1@2.36.1-8+deb11u1
  From: util-linux/libblkid1@2.36.1-8+deb11u1
  From: e2fsprogs@1.46.2-2 > util-linux/libblkid1@2.36.1-8+deb11u1
  From: util-linux/libmount1@2.36.1-8+deb11u1 > util-linux/libblkid1@2.36.1-8+deb11u1
  and 16 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2.36.1-8+deb11u2

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-2434417
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Improper Resource Shutdown or Release
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-2440571
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-514595
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: NULL Pointer Dereference
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-516778
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Missing Release of Resource after Effective Lifetime
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-518574
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-520936
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-531474
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5416363
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5425904
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5673712
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: NULL Pointer Dereference
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5724641
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5747597
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5749339
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: NULL Pointer Dereference
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5750143
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5767900
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5773188
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Loop with Unreachable Exit Condition ('Infinite Loop')
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5853001
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-6079927
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Resource Exhaustion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-6084515
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-6190609
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-6190787
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in tar
  Description: CVE-2005-2541
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TAR-523480
  Introduced through: tar@1.34+dfsg-1
  From: tar@1.34+dfsg-1
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in tar
  Description: CVE-2023-39804
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TAR-6120424
  Introduced through: tar@1.34+dfsg-1
  From: tar@1.34+dfsg-1
  Image layer: Introduced by your base image (debian:11.2-slim)
  Fixed in: 1.34+dfsg-1+deb11u1

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Authentication Bypass
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-1291054
  Introduced through: systemd/libsystemd0@247.3-7, apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7
  From: systemd/libsystemd0@247.3-7
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7
  and 5 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Link Following
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-524969
  Introduced through: systemd/libsystemd0@247.3-7, apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7
  From: systemd/libsystemd0@247.3-7
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7
  and 5 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Improper Validation of Integrity Check Value
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-5733387
  Introduced through: systemd/libsystemd0@247.3-7, apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7
  From: systemd/libsystemd0@247.3-7
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7
  and 5 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Improper Validation of Integrity Check Value
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-5733391
  Introduced through: systemd/libsystemd0@247.3-7, apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7
  From: systemd/libsystemd0@247.3-7
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7
  and 5 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Improper Validation of Integrity Check Value
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-5733392
  Introduced through: systemd/libsystemd0@247.3-7, apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7
  From: systemd/libsystemd0@247.3-7
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7
  and 5 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: CVE-2023-7008
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-6137713
  Introduced through: systemd/libsystemd0@247.3-7, apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7
  From: systemd/libsystemd0@247.3-7
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7
  and 5 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: CVE-2023-50868
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-6277512
  Introduced through: systemd/libsystemd0@247.3-7, apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7
  From: systemd/libsystemd0@247.3-7
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7
  and 5 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in shadow/passwd
  Description: Access Restriction Bypass
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SHADOW-526940
  Introduced through: shadow/passwd@1:4.8.1-1, adduser@3.118, shadow/login@1:4.8.1-1, util-linux/mount@2.36.1-8+deb11u1
  From: shadow/passwd@1:4.8.1-1
  From: adduser@3.118 > shadow/passwd@1:4.8.1-1
  From: shadow/login@1:4.8.1-1
  and 1 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in shadow/passwd
  Description: Time-of-check Time-of-use (TOCTOU)
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SHADOW-528840
  Introduced through: shadow/passwd@1:4.8.1-1, adduser@3.118, shadow/login@1:4.8.1-1, util-linux/mount@2.36.1-8+deb11u1
  From: shadow/passwd@1:4.8.1-1
  From: adduser@3.118 > shadow/passwd@1:4.8.1-1
  From: shadow/login@1:4.8.1-1
  and 1 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in shadow/passwd
  Description: Incorrect Permission Assignment for Critical Resource
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SHADOW-539870
  Introduced through: shadow/passwd@1:4.8.1-1, adduser@3.118, shadow/login@1:4.8.1-1, util-linux/mount@2.36.1-8+deb11u1
  From: shadow/passwd@1:4.8.1-1
  From: adduser@3.118 > shadow/passwd@1:4.8.1-1
  From: shadow/login@1:4.8.1-1
  and 1 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in shadow/passwd
  Description: Arbitrary Code Injection
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SHADOW-5423922
  Introduced through: shadow/passwd@1:4.8.1-1, adduser@3.118, shadow/login@1:4.8.1-1, util-linux/mount@2.36.1-8+deb11u1
  From: shadow/passwd@1:4.8.1-1
  From: adduser@3.118 > shadow/passwd@1:4.8.1-1
  From: shadow/login@1:4.8.1-1
  and 1 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in shadow/passwd
  Description: Improper Authentication
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SHADOW-5879152
  Introduced through: shadow/passwd@1:4.8.1-1, adduser@3.118, shadow/login@1:4.8.1-1, util-linux/mount@2.36.1-8+deb11u1
  From: shadow/passwd@1:4.8.1-1
  From: adduser@3.118 > shadow/passwd@1:4.8.1-1
  From: shadow/login@1:4.8.1-1
  and 1 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in perl/perl-base
  Description: Improper Verification of Cryptographic Signature
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PERL-1925976
  Introduced through: perl/perl-base@5.32.1-4+deb11u2
  From: perl/perl-base@5.32.1-4+deb11u2
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in perl/perl-base
  Description: Link Following
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PERL-532614
  Introduced through: perl/perl-base@5.32.1-4+deb11u2
  From: perl/perl-base@5.32.1-4+deb11u2
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in perl/perl-base
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PERL-5489185
  Introduced through: perl/perl-base@5.32.1-4+deb11u2
  From: perl/perl-base@5.32.1-4+deb11u2
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in perl/perl-base
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PERL-5489191
  Introduced through: perl/perl-base@5.32.1-4+deb11u2
  From: perl/perl-base@5.32.1-4+deb11u2
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in pcre3/libpcre3
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PCRE3-523392
  Introduced through: pcre3/libpcre3@2:8.39-13, grep@3.6-1
  From: pcre3/libpcre3@2:8.39-13
  From: grep@3.6-1 > pcre3/libpcre3@2:8.39-13
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in pcre3/libpcre3
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PCRE3-525075
  Introduced through: pcre3/libpcre3@2:8.39-13, grep@3.6-1
  From: pcre3/libpcre3@2:8.39-13
  From: grep@3.6-1 > pcre3/libpcre3@2:8.39-13
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in pcre3/libpcre3
  Description: Uncontrolled Recursion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PCRE3-529298
  Introduced through: pcre3/libpcre3@2:8.39-13, grep@3.6-1
  From: pcre3/libpcre3@2:8.39-13
  From: grep@3.6-1 > pcre3/libpcre3@2:8.39-13
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in pcre3/libpcre3
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PCRE3-529490
  Introduced through: pcre3/libpcre3@2:8.39-13, grep@3.6-1
  From: pcre3/libpcre3@2:8.39-13
  From: grep@3.6-1 > pcre3/libpcre3@2:8.39-13
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in pcre3/libpcre3
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PCRE3-572353
  Introduced through: pcre3/libpcre3@2:8.39-13, grep@3.6-1
  From: pcre3/libpcre3@2:8.39-13
  From: grep@3.6-1 > pcre3/libpcre3@2:8.39-13
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in pcre2/libpcre2-8-0
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PCRE2-5788325
  Introduced through: pcre2/libpcre2-8-0@10.36-2
  From: pcre2/libpcre2-8-0@10.36-2
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in pam/libpam0g
  Description: CVE-2024-22365
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PAM-6178915
  Introduced through: pam/libpam0g@1.4.0-9+deb11u1, shadow/login@1:4.8.1-1, util-linux/mount@2.36.1-8+deb11u1, adduser@3.118, pam/libpam-modules-bin@1.4.0-9+deb11u1, pam/libpam-modules@1.4.0-9+deb11u1, pam/libpam-runtime@1.4.0-9+deb11u1
  From: pam/libpam0g@1.4.0-9+deb11u1
  From: shadow/login@1:4.8.1-1 > pam/libpam0g@1.4.0-9+deb11u1
  From: util-linux/mount@2.36.1-8+deb11u1 > util-linux@2.36.1-8+deb11u1 > pam/libpam0g@1.4.0-9+deb11u1
  and 11 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openssl/libssl1.1
  Description: Improper Check for Unusual or Exceptional Conditions
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-6048819
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openssl/libssl1.1
  Description: CVE-2024-0727
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-6190224
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openssl/libssl1.1
  Description: CVE-2024-2511
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-6592093
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openssl/libssl1.1
  Description: CVE-2024-4741
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-7151355
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openssl/libssl1.1
  Description: CVE-2024-5535
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-7411351
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openldap/libldap-2.4-2
  Description: Improper Initialization
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENLDAP-521320
  Introduced through: curl@7.74.0-1.3+deb11u1, openldap/libldap-common@2.4.57+dfsg-3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  From: openldap/libldap-common@2.4.57+dfsg-3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openldap/libldap-2.4-2
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENLDAP-531344
  Introduced through: curl@7.74.0-1.3+deb11u1, openldap/libldap-common@2.4.57+dfsg-3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  From: openldap/libldap-common@2.4.57+dfsg-3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openldap/libldap-2.4-2
  Description: Cryptographic Issues
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENLDAP-531747
  Introduced through: curl@7.74.0-1.3+deb11u1, openldap/libldap-common@2.4.57+dfsg-3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  From: openldap/libldap-common@2.4.57+dfsg-3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openldap/libldap-2.4-2
  Description: NULL Pointer Dereference
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENLDAP-5660622
  Introduced through: curl@7.74.0-1.3+deb11u1, openldap/libldap-common@2.4.57+dfsg-3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  From: openldap/libldap-common@2.4.57+dfsg-3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in openldap/libldap-2.4-2
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENLDAP-584937
  Introduced through: curl@7.74.0-1.3+deb11u1, openldap/libldap-common@2.4.57+dfsg-3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  From: openldap/libldap-common@2.4.57+dfsg-3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in nghttp2/libnghttp2-14
  Description: CVE-2024-28182
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-NGHTTP2-6541750
  Introduced through: curl@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > nghttp2/libnghttp2-14@1.43.0-1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in ncurses/libtinfo6
  Description: CVE-2023-50495
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-NCURSES-6123820
  Introduced through: ncurses/libtinfo6@6.2+20201114-2, bash/bash@5.1-2+b3, ncurses/ncurses-bin@6.2+20201114-2, util-linux/mount@2.36.1-8+deb11u1, ncurses/ncurses-base@6.2+20201114-2
  From: ncurses/libtinfo6@6.2+20201114-2
  From: bash/bash@5.1-2+b3 > ncurses/libtinfo6@6.2+20201114-2
  From: ncurses/ncurses-bin@6.2+20201114-2 > ncurses/libtinfo6@6.2+20201114-2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in ncurses/libtinfo6
  Description: CVE-2023-45918
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-NCURSES-6252771
  Introduced through: ncurses/libtinfo6@6.2+20201114-2, bash/bash@5.1-2+b3, ncurses/ncurses-bin@6.2+20201114-2, util-linux/mount@2.36.1-8+deb11u1, ncurses/ncurses-base@6.2+20201114-2
  From: ncurses/libtinfo6@6.2+20201114-2
  From: bash/bash@5.1-2+b3 > ncurses/libtinfo6@6.2+20201114-2
  From: ncurses/ncurses-bin@6.2+20201114-2 > ncurses/libtinfo6@6.2+20201114-2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in libzstd/libzstd1
  Description: Resource Exhaustion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBZSTD-5406388
  Introduced through: libzstd/libzstd1@1.4.8+dfsg-2.1, apt@2.2.4, glibc/libc-devtools@2.31-13+deb11u3
  From: libzstd/libzstd1@1.4.8+dfsg-2.1
  From: apt@2.2.4 > apt/libapt-pkg6.0@2.2.4 > libzstd/libzstd1@1.4.8+dfsg-2.1
  From: apt@2.2.4 > apt/libapt-pkg6.0@2.2.4 > systemd/libsystemd0@247.3-7 > libzstd/libzstd1@1.4.8+dfsg-2.1
  and 1 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in libsepol/libsepol1
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBSEPOL-1315627
  Introduced through: libsepol/libsepol1@3.1-1, adduser@3.118
  From: libsepol/libsepol1@3.1-1
  From: adduser@3.118 > shadow/passwd@1:4.8.1-1 > libsemanage/libsemanage1@3.1-1+b2 > libsepol/libsepol1@3.1-1
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in libsepol/libsepol1
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBSEPOL-1315629
  Introduced through: libsepol/libsepol1@3.1-1, adduser@3.118
  From: libsepol/libsepol1@3.1-1
  From: adduser@3.118 > shadow/passwd@1:4.8.1-1 > libsemanage/libsemanage1@3.1-1+b2 > libsepol/libsepol1@3.1-1
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in libsepol/libsepol1
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBSEPOL-1315635
  Introduced through: libsepol/libsepol1@3.1-1, adduser@3.118
  From: libsepol/libsepol1@3.1-1
  From: adduser@3.118 > shadow/passwd@1:4.8.1-1 > libsemanage/libsemanage1@3.1-1+b2 > libsepol/libsepol1@3.1-1
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in libsepol/libsepol1
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBSEPOL-1315641
  Introduced through: libsepol/libsepol1@3.1-1, adduser@3.118
  From: libsepol/libsepol1@3.1-1
  From: adduser@3.118 > shadow/passwd@1:4.8.1-1 > libsemanage/libsemanage1@3.1-1+b2 > libsepol/libsepol1@3.1-1
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in libpng1.6/libpng16-16
  Description: Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBPNG16-2363923
  Introduced through: libpng1.6/libpng16-16@1.6.37-3, glibc/libc-devtools@2.31-13+deb11u3
  From: libpng1.6/libpng16-16@1.6.37-3
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > libpng1.6/libpng16-16@1.6.37-3
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > fontconfig/libfontconfig1@2.13.1-4.2 > freetype/libfreetype6@2.10.4+dfsg-1 > libpng1.6/libpng16-16@1.6.37-3
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in libpng1.6/libpng16-16
  Description: Memory Leak
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBPNG16-529373
  Introduced through: libpng1.6/libpng16-16@1.6.37-3, glibc/libc-devtools@2.31-13+deb11u3
  From: libpng1.6/libpng16-16@1.6.37-3
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > libpng1.6/libpng16-16@1.6.37-3
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > fontconfig/libfontconfig1@2.13.1-4.2 > freetype/libfreetype6@2.10.4+dfsg-1 > libpng1.6/libpng16-16@1.6.37-3
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in libjpeg-turbo/libjpeg62-turbo
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBJPEGTURBO-2932112
  Introduced through: libjpeg-turbo/libjpeg62-turbo@1:2.0.6-4, glibc/libc-devtools@2.31-13+deb11u3
  From: libjpeg-turbo/libjpeg62-turbo@1:2.0.6-4
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > libjpeg-turbo/libjpeg62-turbo@1:2.0.6-4
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1 > libjpeg-turbo/libjpeg62-turbo@1:2.0.6-4
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in libgd2/libgd3
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBGD2-1536763
  Introduced through: libgd2/libgd3@2.3.0-2, glibc/libc-devtools@2.31-13+deb11u3
  From: libgd2/libgd3@2.3.0-2
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in libgd2/libgd3
  Description: Double Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBGD2-1570130
  Introduced through: libgd2/libgd3@2.3.0-2, glibc/libc-devtools@2.31-13+deb11u3
  From: libgd2/libgd3@2.3.0-2
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in libgd2/libgd3
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBGD2-1583889
  Introduced through: libgd2/libgd3@2.3.0-2, glibc/libc-devtools@2.31-13+deb11u3
  From: libgd2/libgd3@2.3.0-2
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in libgcrypt20
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBGCRYPT20-1297892
  Introduced through: libgcrypt20/libgcrypt20-dev@1.8.7-6, apt@2.2.4, curl@7.74.0-1.3+deb11u1
  From: libgcrypt20/libgcrypt20-dev@1.8.7-6 > libgcrypt20@1.8.7-6
  From: apt@2.2.4 > apt/libapt-pkg6.0@2.2.4 > libgcrypt20@1.8.7-6
  From: apt@2.2.4 > gnupg2/gpgv@2.2.27-2+deb11u1 > libgcrypt20@1.8.7-6
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in libgcrypt20
  Description: Use of a Broken or Risky Cryptographic Algorithm
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBGCRYPT20-523947
  Introduced through: libgcrypt20/libgcrypt20-dev@1.8.7-6, apt@2.2.4, curl@7.74.0-1.3+deb11u1
  From: libgcrypt20/libgcrypt20-dev@1.8.7-6 > libgcrypt20@1.8.7-6
  From: apt@2.2.4 > apt/libapt-pkg6.0@2.2.4 > libgcrypt20@1.8.7-6
  From: apt@2.2.4 > gnupg2/gpgv@2.2.27-2+deb11u1 > libgcrypt20@1.8.7-6
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in libgcrypt20
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBGCRYPT20-6405987
  Introduced through: libgcrypt20/libgcrypt20-dev@1.8.7-6, apt@2.2.4, curl@7.74.0-1.3+deb11u1
  From: libgcrypt20/libgcrypt20-dev@1.8.7-6 > libgcrypt20@1.8.7-6
  From: apt@2.2.4 > apt/libapt-pkg6.0@2.2.4 > libgcrypt20@1.8.7-6
  From: apt@2.2.4 > gnupg2/gpgv@2.2.27-2+deb11u1 > libgcrypt20@1.8.7-6
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in krb5/libk5crypto3
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-KRB5-524883
  Introduced through: curl@7.74.0-1.3+deb11u1, libgcrypt20/libgcrypt20-dev@1.8.7-6, krb5/libkrb5support0@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libk5crypto3@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libkrb5-3@1.18.3-6+deb11u1 > krb5/libk5crypto3@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libkrb5-3@1.18.3-6+deb11u1
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in krb5/libk5crypto3
  Description: CVE-2024-26462
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-KRB5-6277413
  Introduced through: curl@7.74.0-1.3+deb11u1, libgcrypt20/libgcrypt20-dev@1.8.7-6, krb5/libkrb5support0@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libk5crypto3@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libkrb5-3@1.18.3-6+deb11u1 > krb5/libk5crypto3@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libkrb5-3@1.18.3-6+deb11u1
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in krb5/libk5crypto3
  Description: CVE-2024-26461
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-KRB5-6277418
  Introduced through: curl@7.74.0-1.3+deb11u1, libgcrypt20/libgcrypt20-dev@1.8.7-6, krb5/libkrb5support0@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libk5crypto3@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libkrb5-3@1.18.3-6+deb11u1 > krb5/libk5crypto3@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libkrb5-3@1.18.3-6+deb11u1
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in krb5/libk5crypto3
  Description: CVE-2024-26458
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-KRB5-6277420
  Introduced through: curl@7.74.0-1.3+deb11u1, libgcrypt20/libgcrypt20-dev@1.8.7-6, krb5/libkrb5support0@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libk5crypto3@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libkrb5-3@1.18.3-6+deb11u1 > krb5/libk5crypto3@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libkrb5-3@1.18.3-6+deb11u1
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in krb5/libk5crypto3
  Description: CVE-2024-37371
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-KRB5-7411316
  Introduced through: curl@7.74.0-1.3+deb11u1, libgcrypt20/libgcrypt20-dev@1.8.7-6, krb5/libkrb5support0@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libk5crypto3@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libkrb5-3@1.18.3-6+deb11u1 > krb5/libk5crypto3@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libkrb5-3@1.18.3-6+deb11u1
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.18.3-6+deb11u5

✗ Low severity vulnerability found in krb5/libk5crypto3
  Description: CVE-2024-37370
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-KRB5-7411320
  Introduced through: curl@7.74.0-1.3+deb11u1, libgcrypt20/libgcrypt20-dev@1.8.7-6, krb5/libkrb5support0@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libk5crypto3@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libkrb5-3@1.18.3-6+deb11u1 > krb5/libk5crypto3@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libkrb5-3@1.18.3-6+deb11u1
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.18.3-6+deb11u5

✗ Low severity vulnerability found in jbigkit/libjbig0
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-JBIGKIT-514977
  Introduced through: jbigkit/libjbig0@2.1-3.1+b2, glibc/libc-devtools@2.31-13+deb11u3
  From: jbigkit/libjbig0@2.1-3.1+b2
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1 > jbigkit/libjbig0@2.1-3.1+b2
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in gnutls28/libgnutls30
  Description: Improper Input Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUTLS28-515971
  Introduced through: apt@2.2.4, curl@7.74.0-1.3+deb11u1
  From: apt@2.2.4 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > rtmpdump/librtmp1@2.4+20151223.gitfa8646d.1-2+b2 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > gnutls28/libgnutls30@3.7.1-5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in gnutls28/libgnutls30
  Description: Uncaught Exception
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUTLS28-6474582
  Introduced through: apt@2.2.4, curl@7.74.0-1.3+deb11u1
  From: apt@2.2.4 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > rtmpdump/librtmp1@2.4+20151223.gitfa8646d.1-2+b2 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > gnutls28/libgnutls30@3.7.1-5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in gnutls28/libgnutls30
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUTLS28-6474587
  Introduced through: apt@2.2.4, curl@7.74.0-1.3+deb11u1
  From: apt@2.2.4 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > rtmpdump/librtmp1@2.4+20151223.gitfa8646d.1-2+b2 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > gnutls28/libgnutls30@3.7.1-5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in gnupg2/gpgv
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUPG2-3330745
  Introduced through: gnupg2/gpgv@2.2.27-2+deb11u1, apt@2.2.4
  From: gnupg2/gpgv@2.2.27-2+deb11u1
  From: apt@2.2.4 > gnupg2/gpgv@2.2.27-2+deb11u1
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-521063
  Introduced through: glibc/libc-bin@2.31-13+deb11u3, glibc/libc-devtools@2.31-13+deb11u3, glibc/libc6@2.31-13+deb11u3, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: glibc/libc-bin@2.31-13+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3
  From: glibc/libc6@2.31-13+deb11u3
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Uncontrolled Recursion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-521199
  Introduced through: glibc/libc-bin@2.31-13+deb11u3, glibc/libc-devtools@2.31-13+deb11u3, glibc/libc6@2.31-13+deb11u3, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: glibc/libc-bin@2.31-13+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3
  From: glibc/libc6@2.31-13+deb11u3
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Use of Insufficiently Random Values
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-522385
  Introduced through: glibc/libc-bin@2.31-13+deb11u3, glibc/libc-devtools@2.31-13+deb11u3, glibc/libc6@2.31-13+deb11u3, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: glibc/libc-bin@2.31-13+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3
  From: glibc/libc6@2.31-13+deb11u3
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-529848
  Introduced through: glibc/libc-bin@2.31-13+deb11u3, glibc/libc-devtools@2.31-13+deb11u3, glibc/libc6@2.31-13+deb11u3, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: glibc/libc-bin@2.31-13+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3
  From: glibc/libc6@2.31-13+deb11u3
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in glibc/libc-bin
  Description: CVE-2019-1010023
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-531451
  Introduced through: glibc/libc-bin@2.31-13+deb11u3, glibc/libc-devtools@2.31-13+deb11u3, glibc/libc6@2.31-13+deb11u3, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: glibc/libc-bin@2.31-13+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3
  From: glibc/libc6@2.31-13+deb11u3
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Uncontrolled Recursion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-531492
  Introduced through: glibc/libc-bin@2.31-13+deb11u3, glibc/libc-devtools@2.31-13+deb11u3, glibc/libc6@2.31-13+deb11u3, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: glibc/libc-bin@2.31-13+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3
  From: glibc/libc6@2.31-13+deb11u3
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Resource Management Errors
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-532215
  Introduced through: glibc/libc-bin@2.31-13+deb11u3, glibc/libc-devtools@2.31-13+deb11u3, glibc/libc6@2.31-13+deb11u3, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: glibc/libc-bin@2.31-13+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3
  From: glibc/libc6@2.31-13+deb11u3
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-5894105
  Introduced through: glibc/libc-bin@2.31-13+deb11u3, glibc/libc-devtools@2.31-13+deb11u3, glibc/libc6@2.31-13+deb11u3, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: glibc/libc-bin@2.31-13+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3
  From: glibc/libc6@2.31-13+deb11u3
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-5894112
  Introduced through: glibc/libc-bin@2.31-13+deb11u3, glibc/libc-devtools@2.31-13+deb11u3, glibc/libc6@2.31-13+deb11u3, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: glibc/libc-bin@2.31-13+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3
  From: glibc/libc6@2.31-13+deb11u3
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in glibc/libc-bin
  Description: CVE-2024-2961
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-6617104
  Introduced through: glibc/libc-bin@2.31-13+deb11u3, glibc/libc-devtools@2.31-13+deb11u3, glibc/libc6@2.31-13+deb11u3, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: glibc/libc-bin@2.31-13+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3
  From: glibc/libc6@2.31-13+deb11u3
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2.31-13+deb11u9

✗ Low severity vulnerability found in glibc/libc-bin
  Description: CVE-2024-33599
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-6673955
  Introduced through: glibc/libc-bin@2.31-13+deb11u3, glibc/libc-devtools@2.31-13+deb11u3, glibc/libc6@2.31-13+deb11u3, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: glibc/libc-bin@2.31-13+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3
  From: glibc/libc6@2.31-13+deb11u3
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2.31-13+deb11u10

✗ Low severity vulnerability found in glibc/libc-bin
  Description: CVE-2024-33601
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-6673958
  Introduced through: glibc/libc-bin@2.31-13+deb11u3, glibc/libc-devtools@2.31-13+deb11u3, glibc/libc6@2.31-13+deb11u3, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: glibc/libc-bin@2.31-13+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3
  From: glibc/libc6@2.31-13+deb11u3
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2.31-13+deb11u10

✗ Low severity vulnerability found in glibc/libc-bin
  Description: CVE-2024-33600
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-6673967
  Introduced through: glibc/libc-bin@2.31-13+deb11u3, glibc/libc-devtools@2.31-13+deb11u3, glibc/libc6@2.31-13+deb11u3, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: glibc/libc-bin@2.31-13+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3
  From: glibc/libc6@2.31-13+deb11u3
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2.31-13+deb11u10

✗ Low severity vulnerability found in glibc/libc-bin
  Description: CVE-2024-33602
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-6673973
  Introduced through: glibc/libc-bin@2.31-13+deb11u3, glibc/libc-devtools@2.31-13+deb11u3, glibc/libc6@2.31-13+deb11u3, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: glibc/libc-bin@2.31-13+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3
  From: glibc/libc6@2.31-13+deb11u3
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2.31-13+deb11u10

✗ Low severity vulnerability found in gcc-9/gcc-9-base
  Description: CVE-2023-4039
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GCC9-5901306
  Introduced through: gcc-9/gcc-9-base@9.3.0-22
  From: gcc-9/gcc-9-base@9.3.0-22
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in gcc-10/libstdc++6
  Description: CVE-2023-4039
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GCC10-5901313
  Introduced through: apt@2.2.4, boost1.74/libboost-thread1.74.0@1.74.0-9, icu/libicu67@67.1-7, gcc-10/gcc-10-base@10.2.1-6, gcc-10/libgcc-s1@10.2.1-6
  From: apt@2.2.4 > gcc-10/libstdc++6@10.2.1-6
  From: boost1.74/libboost-thread1.74.0@1.74.0-9 > gcc-10/libstdc++6@10.2.1-6
  From: icu/libicu67@67.1-7 > gcc-10/libstdc++6@10.2.1-6
  and 3 more...
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in freetype/libfreetype6
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-FREETYPE-2848681
  Introduced through: freetype/libfreetype6@2.10.4+dfsg-1, glibc/libc-devtools@2.31-13+deb11u3
  From: freetype/libfreetype6@2.10.4+dfsg-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > freetype/libfreetype6@2.10.4+dfsg-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > fontconfig/libfontconfig1@2.13.1-4.2 > freetype/libfreetype6@2.10.4+dfsg-1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in expat/libexpat1
  Description: XML External Entity (XXE) Injection
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-EXPAT-524217
  Introduced through: expat/libexpat1@2.2.10-2+deb11u3, glibc/libc-devtools@2.31-13+deb11u3
  From: expat/libexpat1@2.2.10-2+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > fontconfig/libfontconfig1@2.13.1-4.2 > expat/libexpat1@2.2.10-2+deb11u3
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in expat/libexpat1
  Description: Improper Restriction of Recursive Entity References in DTDs ('XML Entity Expansion')
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-EXPAT-6227594
  Introduced through: expat/libexpat1@2.2.10-2+deb11u3, glibc/libc-devtools@2.31-13+deb11u3
  From: expat/libexpat1@2.2.10-2+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > fontconfig/libfontconfig1@2.13.1-4.2 > expat/libexpat1@2.2.10-2+deb11u3
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in expat/libexpat1
  Description: Resource Exhaustion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-EXPAT-6227598
  Introduced through: expat/libexpat1@2.2.10-2+deb11u3, glibc/libc-devtools@2.31-13+deb11u3
  From: expat/libexpat1@2.2.10-2+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > fontconfig/libfontconfig1@2.13.1-4.2 > expat/libexpat1@2.2.10-2+deb11u3
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in expat/libexpat1
  Description: CVE-2024-28757
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-EXPAT-6420594
  Introduced through: expat/libexpat1@2.2.10-2+deb11u3, glibc/libc-devtools@2.31-13+deb11u3
  From: expat/libexpat1@2.2.10-2+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > fontconfig/libfontconfig1@2.13.1-4.2 > expat/libexpat1@2.2.10-2+deb11u3
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in e2fsprogs/libcom-err2
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-E2FSPROGS-2628459
  Introduced through: e2fsprogs@1.46.2-2, curl@7.74.0-1.3+deb11u1, e2fsprogs/libext2fs2@1.46.2-2, e2fsprogs/libss2@1.46.2-2, e2fsprogs/logsave@1.46.2-2
  From: e2fsprogs@1.46.2-2 > e2fsprogs/libcom-err2@1.46.2-2
  From: e2fsprogs@1.46.2-2 > e2fsprogs/libss2@1.46.2-2 > e2fsprogs/libcom-err2@1.46.2-2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > e2fsprogs/libcom-err2@1.46.2-2
  and 8 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in db5.3/libdb5.3
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-DB53-2825168
  Introduced through: adduser@3.118, curl@7.74.0-1.3+deb11u1
  From: adduser@3.118 > shadow/passwd@1:4.8.1-1 > pam/libpam-modules@1.4.0-9+deb11u1 > db5.3/libdb5.3@5.3.28+dfsg1-0.8
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > cyrus-sasl2/libsasl2-2@2.1.27+dfsg-2.1+deb11u1 > cyrus-sasl2/libsasl2-modules-db@2.1.27+dfsg-2.1+deb11u1 > db5.3/libdb5.3@5.3.28+dfsg1-0.8
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in curl/libcurl4
  Description: Missing Initialization of Resource
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-1296884
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u2

✗ Low severity vulnerability found in curl/libcurl4
  Description: Use of Incorrectly-Resolved Name or Reference
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-1322658
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u2

✗ Low severity vulnerability found in curl/libcurl4
  Description: Insufficiently Protected Credentials
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-1322659
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in curl/libcurl4
  Description: Improper Validation of Integrity Check Value
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-1322667
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in curl/libcurl4
  Description: CVE-2022-35252
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-3012384
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u3

✗ Low severity vulnerability found in curl/libcurl4
  Description: Race Condition
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-5561869
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in curl/libcurl4
  Description: CVE-2023-28322
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-5561885
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u9

✗ Low severity vulnerability found in curl/libcurl4
  Description: CVE-2023-38546
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-5955029
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u10

✗ Low severity vulnerability found in curl/libcurl4
  Description: CVE-2024-2398
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-6501704
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u12

✗ Low severity vulnerability found in curl/libcurl4
  Description: CVE-2024-2379
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-6501711
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Low severity vulnerability found in coreutils/coreutils
  Description: Improper Input Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-COREUTILS-514776
  Introduced through: coreutils/coreutils@8.32-4+b1, fontconfig/fontconfig-config@2.13.1-4.2
  From: coreutils/coreutils@8.32-4+b1
  From: fontconfig/fontconfig-config@2.13.1-4.2 > ucf@3.0043 > coreutils/coreutils@8.32-4+b1
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in coreutils/coreutils
  Description: Race Condition
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-COREUTILS-527269
  Introduced through: coreutils/coreutils@8.32-4+b1, fontconfig/fontconfig-config@2.13.1-4.2
  From: coreutils/coreutils@8.32-4+b1
  From: fontconfig/fontconfig-config@2.13.1-4.2 > ucf@3.0043 > coreutils/coreutils@8.32-4+b1
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in bash/bash
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-BASH-3112361
  Introduced through: bash/bash@5.1-2+b3
  From: bash/bash@5.1-2+b3
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Low severity vulnerability found in apt/libapt-pkg6.0
  Description: Improper Verification of Cryptographic Signature
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-APT-522585
  Introduced through: apt/libapt-pkg6.0@2.2.4, apt@2.2.4
  From: apt/libapt-pkg6.0@2.2.4
  From: apt@2.2.4 > apt/libapt-pkg6.0@2.2.4
  From: apt@2.2.4
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-2774162
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Stack-based Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-2774167
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-2823289
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-2823291
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Divide By Zero
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-2938519
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Divide By Zero
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-2938520
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Divide By Zero
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-2938525
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-2964237
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Integer Underflow
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-2987009
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Integer Underflow
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-2987011
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Improper Validation of Specified Quantity in Input
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-2987014
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3008946
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Double Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3012393
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Incorrect Calculation of Buffer Size
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3012398
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Release of Invalid Pointer or Reference
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3012399
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3058771
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3058775
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3058778
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3058779
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3058787
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3058792
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3244453
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3319790
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u4

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3319791
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u4

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3319804
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u4

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3319810
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u4

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3319811
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u4

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3319813
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u4

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3319814
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u4

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3319820
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u4

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3319824
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u4

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3319826
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u4

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3339158
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5425902
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5518072
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5747608
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u4

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5862860
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u5

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5862861
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u5

✗ Medium severity vulnerability found in tiff/libtiff5
  Description: Memory Leak
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5934951
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u5

✗ Medium severity vulnerability found in tar
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TAR-3253527
  Introduced through: tar@1.34+dfsg-1
  From: tar@1.34+dfsg-1
  Image layer: Introduced by your base image (debian:11.2-slim)
  Fixed in: 1.34+dfsg-1+deb11u1

✗ Medium severity vulnerability found in systemd/libsystemd0
  Description: Off-by-one Error
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-3111119
  Introduced through: systemd/libsystemd0@247.3-7, apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7
  From: systemd/libsystemd0@247.3-7
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7
  and 5 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 247.3-7+deb11u2

✗ Medium severity vulnerability found in systemd/libsystemd0
  Description: CVE-2022-4415
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-3177742
  Introduced through: systemd/libsystemd0@247.3-7, apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7
  From: systemd/libsystemd0@247.3-7
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7
  and 5 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 247.3-7+deb11u2

✗ Medium severity vulnerability found in openssl/libssl1.1
  Description: Use of a Broken or Risky Cryptographic Algorithm
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-2941242
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.1.1n-0+deb11u4

✗ Medium severity vulnerability found in openssl/libssl1.1
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-3314592
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.1.1n-0+deb11u4

✗ Medium severity vulnerability found in openssl/libssl1.1
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-5291773
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.1.1n-0+deb11u5

✗ Medium severity vulnerability found in openssl/libssl1.1
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-5291777
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.1.1n-0+deb11u5

✗ Medium severity vulnerability found in openssl/libssl1.1
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-5661566
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.1.1n-0+deb11u5

✗ Medium severity vulnerability found in openssl/libssl1.1
  Description: Inefficient Regular Expression Complexity
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-5788324
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.1.1v-0~deb11u1

✗ Medium severity vulnerability found in openssl/libssl1.1
  Description: Excessive Iteration
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-5812634
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.1.1v-0~deb11u1

✗ Medium severity vulnerability found in libxpm/libxpm4
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBXPM-5927156
  Introduced through: libxpm/libxpm4@1:3.5.12-1, glibc/libc-devtools@2.31-13+deb11u3
  From: libxpm/libxpm4@1:3.5.12-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > libxpm/libxpm4@1:3.5.12-1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1:3.5.12-1.1+deb11u1

✗ Medium severity vulnerability found in libxpm/libxpm4
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBXPM-5927166
  Introduced through: libxpm/libxpm4@1:3.5.12-1, glibc/libc-devtools@2.31-13+deb11u3
  From: libxpm/libxpm4@1:3.5.12-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > libxpm/libxpm4@1:3.5.12-1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1:3.5.12-1.1+deb11u1

✗ Medium severity vulnerability found in libx11/libx11-data
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBX11-5927151
  Introduced through: libx11/libx11-data@2:1.7.2-1, glibc/libc-devtools@2.31-13+deb11u3, libx11/libx11-6@2:1.7.2-1
  From: libx11/libx11-data@2:1.7.2-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > libxpm/libxpm4@1:3.5.12-1 > libx11/libx11-6@2:1.7.2-1 > libx11/libx11-data@2:1.7.2-1
  From: libx11/libx11-6@2:1.7.2-1
  and 1 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2:1.7.2-1+deb11u2

✗ Medium severity vulnerability found in libx11/libx11-data
  Description: Loop with Unreachable Exit Condition ('Infinite Loop')
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBX11-5927154
  Introduced through: libx11/libx11-data@2:1.7.2-1, glibc/libc-devtools@2.31-13+deb11u3, libx11/libx11-6@2:1.7.2-1
  From: libx11/libx11-data@2:1.7.2-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > libxpm/libxpm4@1:3.5.12-1 > libx11/libx11-6@2:1.7.2-1 > libx11/libx11-data@2:1.7.2-1
  From: libx11/libx11-6@2:1.7.2-1
  and 1 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2:1.7.2-1+deb11u2

✗ Medium severity vulnerability found in krb5/libk5crypto3
  Description: Access of Uninitialized Pointer
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-KRB5-5825661
  Introduced through: curl@7.74.0-1.3+deb11u1, libgcrypt20/libgcrypt20-dev@1.8.7-6, krb5/libkrb5support0@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libk5crypto3@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libkrb5-3@1.18.3-6+deb11u1 > krb5/libk5crypto3@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libkrb5-3@1.18.3-6+deb11u1
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.18.3-6+deb11u4

✗ Medium severity vulnerability found in gnutls28/libgnutls30
  Description: NULL Pointer Dereference
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUTLS28-2419151
  Introduced through: apt@2.2.4, curl@7.74.0-1.3+deb11u1
  From: apt@2.2.4 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > rtmpdump/librtmp1@2.4+20151223.gitfa8646d.1-2+b2 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > gnutls28/libgnutls30@3.7.1-5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 3.7.1-5+deb11u1

✗ Medium severity vulnerability found in gnutls28/libgnutls30
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUTLS28-6062102
  Introduced through: apt@2.2.4, curl@7.74.0-1.3+deb11u1
  From: apt@2.2.4 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > rtmpdump/librtmp1@2.4+20151223.gitfa8646d.1-2+b2 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > gnutls28/libgnutls30@3.7.1-5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 3.7.1-5+deb11u4

✗ Medium severity vulnerability found in gnupg2/gpgv
  Description: Arbitrary Code Injection
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUPG2-2939851
  Introduced through: gnupg2/gpgv@2.2.27-2+deb11u1, apt@2.2.4
  From: gnupg2/gpgv@2.2.27-2+deb11u1
  From: apt@2.2.4 > gnupg2/gpgv@2.2.27-2+deb11u1
  Image layer: Introduced by your base image (debian:11.2-slim)
  Fixed in: 2.2.27-2+deb11u2

✗ Medium severity vulnerability found in curl/libcurl4
  Description: Insufficient Verification of Data Authenticity
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-1585148
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u2

✗ Medium severity vulnerability found in curl/libcurl4
  Description: Insufficiently Protected Credentials
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-2804158
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u2

✗ Medium severity vulnerability found in curl/libcurl4
  Description: Insufficiently Protected Credentials
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-2804167
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u2

✗ Medium severity vulnerability found in curl/libcurl4
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-2936232
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u2

✗ Medium severity vulnerability found in curl/libcurl4
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-2936233
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u2

✗ Medium severity vulnerability found in curl/libcurl4
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-2936235
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u2

✗ Medium severity vulnerability found in curl/libcurl4
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-3179186
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u5

✗ Medium severity vulnerability found in curl/libcurl4
  Description: Cleartext Transmission of Sensitive Information
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-3320492
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Medium severity vulnerability found in curl/libcurl4
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-3320498
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u7

✗ Medium severity vulnerability found in curl/libcurl4
  Description: Improper Authentication
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-3366760
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u8

✗ Medium severity vulnerability found in curl/libcurl4
  Description: Improper Authentication
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-3366763
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u8

✗ Medium severity vulnerability found in curl/libcurl4
  Description: Improper Authentication
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-3366765
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u8

✗ Medium severity vulnerability found in curl/libcurl4
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-5561876
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u9

✗ Medium severity vulnerability found in curl/libcurl4
  Description: CVE-2023-46218
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-6100976
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u11

✗ Medium severity vulnerability found in curl/libcurl4
  Description: Missing Encryption of Sensitive Data
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-6100978
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ High severity vulnerability found in tiff/libtiff5
  Description: Numeric Errors
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-3113871
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u3

✗ High severity vulnerability found in tiff/libtiff5
  Description: Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TIFF-5747600
  Introduced through: tiff/libtiff5@4.2.0-1+deb11u1, glibc/libc-devtools@2.31-13+deb11u3
  From: tiff/libtiff5@4.2.0-1+deb11u1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.2.0-1+deb11u4

✗ High severity vulnerability found in systemd/libsystemd0
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-6277510
  Introduced through: systemd/libsystemd0@247.3-7, apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7
  From: systemd/libsystemd0@247.3-7
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7
  and 5 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ High severity vulnerability found in perl/perl-base
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PERL-6085272
  Introduced through: perl/perl-base@5.32.1-4+deb11u2
  From: perl/perl-base@5.32.1-4+deb11u2
  Image layer: Introduced by your base image (debian:11.2-slim)
  Fixed in: 5.32.1-4+deb11u3

✗ High severity vulnerability found in openssl/libssl1.1
  Description: Access of Resource Using Incompatible Type ('Type Confusion')
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-3314584
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.1.1n-0+deb11u4

✗ High severity vulnerability found in openssl/libssl1.1
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-3314604
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.1.1n-0+deb11u4

✗ High severity vulnerability found in openssl/libssl1.1
  Description: Double Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-3314615
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.1.1n-0+deb11u4

✗ High severity vulnerability found in openssl/libssl1.1
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-3368735
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.1.1n-0+deb11u5

✗ High severity vulnerability found in nghttp2/libnghttp2-14
  Description: Resource Exhaustion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-NGHTTP2-5953384
  Introduced through: curl@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > nghttp2/libnghttp2-14@1.43.0-1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.43.0-1+deb11u1

✗ High severity vulnerability found in ncurses/libtinfo6
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-NCURSES-2767191
  Introduced through: ncurses/libtinfo6@6.2+20201114-2, bash/bash@5.1-2+b3, ncurses/ncurses-bin@6.2+20201114-2, util-linux/mount@2.36.1-8+deb11u1, ncurses/ncurses-base@6.2+20201114-2
  From: ncurses/libtinfo6@6.2+20201114-2
  From: bash/bash@5.1-2+b3 > ncurses/libtinfo6@6.2+20201114-2
  From: ncurses/ncurses-bin@6.2+20201114-2 > ncurses/libtinfo6@6.2+20201114-2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 6.2+20201114-2+deb11u1

✗ High severity vulnerability found in ncurses/libtinfo6
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-NCURSES-5421197
  Introduced through: ncurses/libtinfo6@6.2+20201114-2, bash/bash@5.1-2+b3, ncurses/ncurses-bin@6.2+20201114-2, util-linux/mount@2.36.1-8+deb11u1, ncurses/ncurses-base@6.2+20201114-2
  From: ncurses/libtinfo6@6.2+20201114-2
  From: bash/bash@5.1-2+b3 > ncurses/libtinfo6@6.2+20201114-2
  From: ncurses/ncurses-bin@6.2+20201114-2 > ncurses/libtinfo6@6.2+20201114-2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 6.2+20201114-2+deb11u2

✗ High severity vulnerability found in libxpm/libxpm4
  Description: Loop with Unreachable Exit Condition ('Infinite Loop')
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBXPM-3232725
  Introduced through: libxpm/libxpm4@1:3.5.12-1, glibc/libc-devtools@2.31-13+deb11u3
  From: libxpm/libxpm4@1:3.5.12-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > libxpm/libxpm4@1:3.5.12-1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1:3.5.12-1.1~deb11u1

✗ High severity vulnerability found in libxpm/libxpm4
  Description: Untrusted Search Path
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBXPM-3232730
  Introduced through: libxpm/libxpm4@1:3.5.12-1, glibc/libc-devtools@2.31-13+deb11u3
  From: libxpm/libxpm4@1:3.5.12-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > libxpm/libxpm4@1:3.5.12-1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1:3.5.12-1.1~deb11u1

✗ High severity vulnerability found in libxpm/libxpm4
  Description: Loop with Unreachable Exit Condition ('Infinite Loop')
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBXPM-3232736
  Introduced through: libxpm/libxpm4@1:3.5.12-1, glibc/libc-devtools@2.31-13+deb11u3
  From: libxpm/libxpm4@1:3.5.12-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > libxpm/libxpm4@1:3.5.12-1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1:3.5.12-1.1~deb11u1

✗ High severity vulnerability found in libx11/libx11-data
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBX11-5710893
  Introduced through: libx11/libx11-data@2:1.7.2-1, glibc/libc-devtools@2.31-13+deb11u3, libx11/libx11-6@2:1.7.2-1
  From: libx11/libx11-data@2:1.7.2-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > libxpm/libxpm4@1:3.5.12-1 > libx11/libx11-6@2:1.7.2-1 > libx11/libx11-data@2:1.7.2-1
  From: libx11/libx11-6@2:1.7.2-1
  and 1 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2:1.7.2-1+deb11u1

✗ High severity vulnerability found in libx11/libx11-data
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBX11-5927150
  Introduced through: libx11/libx11-data@2:1.7.2-1, glibc/libc-devtools@2.31-13+deb11u3, libx11/libx11-6@2:1.7.2-1
  From: libx11/libx11-data@2:1.7.2-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > libxpm/libxpm4@1:3.5.12-1 > libx11/libx11-6@2:1.7.2-1 > libx11/libx11-data@2:1.7.2-1
  From: libx11/libx11-6@2:1.7.2-1
  and 1 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2:1.7.2-1+deb11u2

✗ High severity vulnerability found in libwebp/libwebp6
  Description: Double Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBWEBP-5489177
  Introduced through: libwebp/libwebp6@0.6.1-2.1, glibc/libc-devtools@2.31-13+deb11u3
  From: libwebp/libwebp6@0.6.1-2.1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > libwebp/libwebp6@0.6.1-2.1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1 > libwebp/libwebp6@0.6.1-2.1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 0.6.1-2.1+deb11u1

✗ High severity vulnerability found in libwebp/libwebp6
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBWEBP-5893094
  Introduced through: libwebp/libwebp6@0.6.1-2.1, glibc/libc-devtools@2.31-13+deb11u3
  From: libwebp/libwebp6@0.6.1-2.1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > libwebp/libwebp6@0.6.1-2.1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > tiff/libtiff5@4.2.0-1+deb11u1 > libwebp/libwebp6@0.6.1-2.1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 0.6.1-2.1+deb11u2

✗ High severity vulnerability found in libtirpc/libtirpc3
  Description: Improper Handling of Exceptional Conditions
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBTIRPC-2959390
  Introduced through: adduser@3.118, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: adduser@3.118 > shadow/passwd@1:4.8.1-1 > pam/libpam-modules@1.4.0-9+deb11u1 > libtirpc/libtirpc3@1.3.1-1
  From: libgcrypt20/libgcrypt20-dev@1.8.7-6 > glibc/libc6-dev@2.31-13+deb11u3 > libnsl/libnsl-dev@1.3.0-2 > libtirpc/libtirpc-dev@1.3.1-1 > libtirpc/libtirpc3@1.3.1-1
  From: libgcrypt20/libgcrypt20-dev@1.8.7-6 > glibc/libc6-dev@2.31-13+deb11u3 > libnsl/libnsl-dev@1.3.0-2 > libnsl/libnsl2@1.3.0-2 > libtirpc/libtirpc3@1.3.1-1
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.3.1-1+deb11u1

✗ High severity vulnerability found in libssh2/libssh2-1
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBSSH2-5861756
  Introduced through: curl@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > libssh2/libssh2-1@1.9.0-2
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.9.0-2+deb11u1

✗ High severity vulnerability found in krb5/libk5crypto3
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-KRB5-3120880
  Introduced through: curl@7.74.0-1.3+deb11u1, libgcrypt20/libgcrypt20-dev@1.8.7-6, krb5/libkrb5support0@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libk5crypto3@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libkrb5-3@1.18.3-6+deb11u1 > krb5/libk5crypto3@1.18.3-6+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u1 > krb5/libkrb5-3@1.18.3-6+deb11u1
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.18.3-6+deb11u3

✗ High severity vulnerability found in gnutls28/libgnutls30
  Description: Double Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUTLS28-2964220
  Introduced through: apt@2.2.4, curl@7.74.0-1.3+deb11u1
  From: apt@2.2.4 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > rtmpdump/librtmp1@2.4+20151223.gitfa8646d.1-2+b2 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > gnutls28/libgnutls30@3.7.1-5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 3.7.1-5+deb11u2

✗ High severity vulnerability found in gnutls28/libgnutls30
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUTLS28-3318299
  Introduced through: apt@2.2.4, curl@7.74.0-1.3+deb11u1
  From: apt@2.2.4 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > rtmpdump/librtmp1@2.4+20151223.gitfa8646d.1-2+b2 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > gnutls28/libgnutls30@3.7.1-5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 3.7.1-5+deb11u3

✗ High severity vulnerability found in gnutls28/libgnutls30
  Description: Improper Verification of Cryptographic Signature
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUTLS28-6159417
  Introduced through: apt@2.2.4, curl@7.74.0-1.3+deb11u1
  From: apt@2.2.4 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > rtmpdump/librtmp1@2.4+20151223.gitfa8646d.1-2+b2 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > gnutls28/libgnutls30@3.7.1-5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 3.7.1-5+deb11u5

✗ High severity vulnerability found in gnutls28/libgnutls30
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUTLS28-6159419
  Introduced through: apt@2.2.4, curl@7.74.0-1.3+deb11u1
  From: apt@2.2.4 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > rtmpdump/librtmp1@2.4+20151223.gitfa8646d.1-2+b2 > gnutls28/libgnutls30@3.7.1-5
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > gnutls28/libgnutls30@3.7.1-5
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 3.7.1-5+deb11u5

✗ High severity vulnerability found in glibc/libc-bin
  Description: Off-by-one Error
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-2340919
  Introduced through: glibc/libc-bin@2.31-13+deb11u3, glibc/libc-devtools@2.31-13+deb11u3, glibc/libc6@2.31-13+deb11u3, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: glibc/libc-bin@2.31-13+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3
  From: glibc/libc6@2.31-13+deb11u3
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2.31-13+deb11u4

✗ High severity vulnerability found in glibc/libc-bin
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-5927133
  Introduced through: glibc/libc-bin@2.31-13+deb11u3, glibc/libc-devtools@2.31-13+deb11u3, glibc/libc6@2.31-13+deb11u3, libgcrypt20/libgcrypt20-dev@1.8.7-6
  From: glibc/libc-bin@2.31-13+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3
  From: glibc/libc6@2.31-13+deb11u3
  and 2 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2.31-13+deb11u7

✗ High severity vulnerability found in freetype/libfreetype6
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-FREETYPE-2774654
  Introduced through: freetype/libfreetype6@2.10.4+dfsg-1, glibc/libc-devtools@2.31-13+deb11u3
  From: freetype/libfreetype6@2.10.4+dfsg-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > freetype/libfreetype6@2.10.4+dfsg-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > fontconfig/libfontconfig1@2.13.1-4.2 > freetype/libfreetype6@2.10.4+dfsg-1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2.10.4+dfsg-1+deb11u1

✗ High severity vulnerability found in freetype/libfreetype6
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-FREETYPE-2774664
  Introduced through: freetype/libfreetype6@2.10.4+dfsg-1, glibc/libc-devtools@2.31-13+deb11u3
  From: freetype/libfreetype6@2.10.4+dfsg-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > freetype/libfreetype6@2.10.4+dfsg-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > fontconfig/libfontconfig1@2.13.1-4.2 > freetype/libfreetype6@2.10.4+dfsg-1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2.10.4+dfsg-1+deb11u1

✗ High severity vulnerability found in expat/libexpat1
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-EXPAT-3023031
  Introduced through: expat/libexpat1@2.2.10-2+deb11u3, glibc/libc-devtools@2.31-13+deb11u3
  From: expat/libexpat1@2.2.10-2+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > fontconfig/libfontconfig1@2.13.1-4.2 > expat/libexpat1@2.2.10-2+deb11u3
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2.2.10-2+deb11u4

✗ High severity vulnerability found in expat/libexpat1
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-EXPAT-3061093
  Introduced through: expat/libexpat1@2.2.10-2+deb11u3, glibc/libc-devtools@2.31-13+deb11u3
  From: expat/libexpat1@2.2.10-2+deb11u3
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > fontconfig/libfontconfig1@2.13.1-4.2 > expat/libexpat1@2.2.10-2+deb11u3
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2.2.10-2+deb11u5

✗ High severity vulnerability found in curl/libcurl4
  Description: Cleartext Transmission of Sensitive Information
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-1585138
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u2

✗ High severity vulnerability found in curl/libcurl4
  Description: CVE-2022-27775
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-2804164
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u2

✗ High severity vulnerability found in curl/libcurl4
  Description: Missing Authentication for Critical Function
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-2805482
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u2

✗ High severity vulnerability found in curl/libcurl4
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-2813769
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u2

✗ High severity vulnerability found in curl/libcurl4
  Description: Loop with Unreachable Exit Condition ('Infinite Loop')
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-2813773
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u2

✗ High severity vulnerability found in curl/libcurl4
  Description: Cleartext Transmission of Sensitive Information
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-3066040
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ High severity vulnerability found in curl/libcurl4
  Description: Cleartext Transmission of Sensitive Information
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-3179181
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ High severity vulnerability found in curl/libcurl4
  Description: Directory Traversal
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-3366762
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u8

✗ High severity vulnerability found in curl/libcurl4
  Description: Arbitrary Code Injection
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-3366772
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u8

✗ Critical severity vulnerability found in zlib/zlib1g
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-ZLIB-2976151
  Introduced through: zlib/zlib1g@1:1.2.11.dfsg-2+deb11u1
  From: zlib/zlib1g@1:1.2.11.dfsg-2+deb11u1
  Image layer: Introduced by your base image (debian:11.2-slim)
  Fixed in: 1:1.2.11.dfsg-2+deb11u2

✗ Critical severity vulnerability found in zlib/zlib1g
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-ZLIB-6008961
  Introduced through: zlib/zlib1g@1:1.2.11.dfsg-2+deb11u1
  From: zlib/zlib1g@1:1.2.11.dfsg-2+deb11u1
  Image layer: Introduced by your base image (debian:11.2-slim)

✗ Critical severity vulnerability found in pcre2/libpcre2-8-0
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PCRE2-2808697
  Introduced through: pcre2/libpcre2-8-0@10.36-2
  From: pcre2/libpcre2-8-0@10.36-2
  Image layer: Introduced by your base image (debian:11.2-slim)
  Fixed in: 10.36-2+deb11u1

✗ Critical severity vulnerability found in pcre2/libpcre2-8-0
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PCRE2-2808704
  Introduced through: pcre2/libpcre2-8-0@10.36-2
  From: pcre2/libpcre2-8-0@10.36-2
  Image layer: Introduced by your base image (debian:11.2-slim)
  Fixed in: 10.36-2+deb11u1

✗ Critical severity vulnerability found in openssl/libssl1.1
  Description: OS Command Injection
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-2933518
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1, ca-certificates@20210119, curl@7.74.0-1.3+deb11u1, openssl@1.1.1n-0+deb11u2
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2.1+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: ca-certificates@20210119 > openssl@1.1.1n-0+deb11u2 > openssl/libssl1.1@1.1.1n-0+deb11u2
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openssl/libssl1.1@1.1.1n-0+deb11u2
  and 3 more...
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 1.1.1n-0+deb11u3

✗ Critical severity vulnerability found in libtasn1-6
  Description: Off-by-one Error
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBTASN16-3061097
  Introduced through: curl@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > gnutls28/libgnutls30@3.7.1-5 > libtasn1-6@4.16.0-2
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 4.16.0-2+deb11u1

✗ Critical severity vulnerability found in freetype/libfreetype6
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-FREETYPE-2774656
  Introduced through: freetype/libfreetype6@2.10.4+dfsg-1, glibc/libc-devtools@2.31-13+deb11u3
  From: freetype/libfreetype6@2.10.4+dfsg-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > freetype/libfreetype6@2.10.4+dfsg-1
  From: glibc/libc-devtools@2.31-13+deb11u3 > libgd2/libgd3@2.3.0-2 > fontconfig/libfontconfig1@2.13.1-4.2 > freetype/libfreetype6@2.10.4+dfsg-1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 2.10.4+dfsg-1+deb11u1

✗ Critical severity vulnerability found in curl/libcurl4
  Description: Double Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-1585150
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u2

✗ Critical severity vulnerability found in curl/libcurl4
  Description: Incorrect Default Permissions
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-2936229
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u2

✗ Critical severity vulnerability found in curl/libcurl4
  Description: Exposure of Resource to Wrong Sphere
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-3065656
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u5

✗ Critical severity vulnerability found in curl/libcurl4
  Description: Cleartext Transmission of Sensitive Information
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-3320493
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'

✗ Critical severity vulnerability found in curl/libcurl4
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-CURL-5955037
  Introduced through: curl/libcurl4@7.74.0-1.3+deb11u1, curl@7.74.0-1.3+deb11u1
  From: curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1 > curl/libcurl4@7.74.0-1.3+deb11u1
  From: curl@7.74.0-1.3+deb11u1
  Image layer: 'apt-get -y install curl cmake libssl-dev git g++ libcurl4-openssl-dev libboost-dev libboost-regex-dev libboost-filesystem-dev libboost-thread-dev uuid-dev libgnutls28-dev libsasl2-dev libgcrypt-dev'
  Fixed in: 7.74.0-1.3+deb11u10



Organization:      bhavdeep1304
Package manager:   deb
Project name:      docker-image|fiware/orion
Docker image:      fiware/orion:3.7.0
Platform:          linux/amd64
Base image:        debian:11.2-slim
Licenses:          enabled

Tested 146 dependencies for known issues, found 247 issues.

Base Image        Vulnerabilities  Severity
debian:11.2-slim  120              11 critical, 20 high, 15 medium, 74 low

Recommendations for base image upgrade:

Minor upgrades
Base Image                     Vulnerabilities  Severity
debian:bullseye-20240701-slim  69               1 critical, 1 high, 0 medium, 67 low

Major upgrades
Base Image                     Vulnerabilities  Severity
debian:bookworm-20240701-slim  33               1 critical, 0 high, 0 medium, 32 low


Learn more: https://docs.snyk.io/products/snyk-container/getting-around-the-snyk-container-ui/base-image-detection


```
