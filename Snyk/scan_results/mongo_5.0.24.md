**Scanning mongo:5.0.24**
```

Testing mongo:5.0.24...

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: CVE-2023-26604
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-SYSTEMD-3339226
  Introduced through: systemd/libsystemd0@245.4-4ubuntu3.23, apt@2.0.10, procps/libprocps8@2:3.3.16-1ubuntu2.4, util-linux/bsdutils@1:2.34-0.1ubuntu9.4, util-linux/mount@2.34-0.1ubuntu9.4, systemd/libudev1@245.4-4ubuntu3.23
  From: systemd/libsystemd0@245.4-4ubuntu3.23
  From: apt@2.0.10 > systemd/libsystemd0@245.4-4ubuntu3.23
  From: procps/libprocps8@2:3.3.16-1ubuntu2.4 > systemd/libsystemd0@245.4-4ubuntu3.23
  and 6 more...
  Image layer: 'apt-get install -y --no-install-recommends ca-certificates jq numactl procps'

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: CVE-2023-7008
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-SYSTEMD-6137854
  Introduced through: systemd/libsystemd0@245.4-4ubuntu3.23, apt@2.0.10, procps/libprocps8@2:3.3.16-1ubuntu2.4, util-linux/bsdutils@1:2.34-0.1ubuntu9.4, util-linux/mount@2.34-0.1ubuntu9.4, systemd/libudev1@245.4-4ubuntu3.23
  From: systemd/libsystemd0@245.4-4ubuntu3.23
  From: apt@2.0.10 > systemd/libsystemd0@245.4-4ubuntu3.23
  From: procps/libprocps8@2:3.3.16-1ubuntu2.4 > systemd/libsystemd0@245.4-4ubuntu3.23
  and 6 more...
  Image layer: 'apt-get install -y --no-install-recommends ca-certificates jq numactl procps'

✗ Low severity vulnerability found in shadow/passwd
  Description: Arbitrary Code Injection
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-SHADOW-5425687
  Introduced through: shadow/passwd@1:4.8.1-1ubuntu5.20.04.4, adduser@3.118ubuntu2, shadow/login@1:4.8.1-1ubuntu5.20.04.4, util-linux/mount@2.34-0.1ubuntu9.4
  From: shadow/passwd@1:4.8.1-1ubuntu5.20.04.4
  From: adduser@3.118ubuntu2 > shadow/passwd@1:4.8.1-1ubuntu5.20.04.4
  From: shadow/login@1:4.8.1-1ubuntu5.20.04.4
  and 1 more...
  Image layer: Introduced by your base image (mongo:5.0.24-focal)

✗ Low severity vulnerability found in shadow/passwd
  Description: Time-of-check Time-of-use (TOCTOU)
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-SHADOW-577863
  Introduced through: shadow/passwd@1:4.8.1-1ubuntu5.20.04.4, adduser@3.118ubuntu2, shadow/login@1:4.8.1-1ubuntu5.20.04.4, util-linux/mount@2.34-0.1ubuntu9.4
  From: shadow/passwd@1:4.8.1-1ubuntu5.20.04.4
  From: adduser@3.118ubuntu2 > shadow/passwd@1:4.8.1-1ubuntu5.20.04.4
  From: shadow/login@1:4.8.1-1ubuntu5.20.04.4
  and 1 more...
  Image layer: Introduced by your base image (mongo:5.0.24-focal)

✗ Low severity vulnerability found in shadow/passwd
  Description: Improper Authentication
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-SHADOW-5879186
  Introduced through: shadow/passwd@1:4.8.1-1ubuntu5.20.04.4, adduser@3.118ubuntu2, shadow/login@1:4.8.1-1ubuntu5.20.04.4, util-linux/mount@2.34-0.1ubuntu9.4
  From: shadow/passwd@1:4.8.1-1ubuntu5.20.04.4
  From: adduser@3.118ubuntu2 > shadow/passwd@1:4.8.1-1ubuntu5.20.04.4
  From: shadow/login@1:4.8.1-1ubuntu5.20.04.4
  and 1 more...
  Image layer: Introduced by your base image (mongo:5.0.24-focal)
  Fixed in: 1:4.8.1-1ubuntu5.20.04.5

✗ Low severity vulnerability found in pcre3/libpcre3
  Description: Uncontrolled Recursion
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-PCRE3-580031
  Introduced through: pcre3/libpcre3@2:8.39-12ubuntu0.1, grep@3.4-1
  From: pcre3/libpcre3@2:8.39-12ubuntu0.1
  From: grep@3.4-1 > pcre3/libpcre3@2:8.39-12ubuntu0.1
  Image layer: Introduced by your base image (mongo:5.0.24-focal)

✗ Low severity vulnerability found in openssl/libssl1.1
  Description: CVE-2024-2511
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-OPENSSL-6592107
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2ubuntu0.1, ca-certificates@20230311ubuntu0.20.04.1, mongodb-org@5.0.24
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2ubuntu0.1 > openssl/libssl1.1@1.1.1f-1ubuntu2.21
  From: ca-certificates@20230311ubuntu0.20.04.1 > openssl@1.1.1f-1ubuntu2.21 > openssl/libssl1.1@1.1.1f-1ubuntu2.21
  From: mongodb-org@5.0.24 > mongodb-org/mongodb-org-database@5.0.24 > mongodb-org/mongodb-org-mongos@5.0.24 > openssl/libssl1.1@1.1.1f-1ubuntu2.21
  and 6 more...
  Image layer: 'apt-get install -y --no-install-recommends ca-certificates jq numactl procps'

✗ Low severity vulnerability found in openssl/libssl1.1
  Description: CVE-2024-4741
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-OPENSSL-7151336
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2ubuntu0.1, ca-certificates@20230311ubuntu0.20.04.1, mongodb-org@5.0.24
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2ubuntu0.1 > openssl/libssl1.1@1.1.1f-1ubuntu2.21
  From: ca-certificates@20230311ubuntu0.20.04.1 > openssl@1.1.1f-1ubuntu2.21 > openssl/libssl1.1@1.1.1f-1ubuntu2.21
  From: mongodb-org@5.0.24 > mongodb-org/mongodb-org-database@5.0.24 > mongodb-org/mongodb-org-mongos@5.0.24 > openssl/libssl1.1@1.1.1f-1ubuntu2.21
  and 6 more...
  Image layer: 'apt-get install -y --no-install-recommends ca-certificates jq numactl procps'

✗ Low severity vulnerability found in ncurses/libtinfo6
  Description: CVE-2023-50495
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-NCURSES-6123866
  Introduced through: ncurses/libtinfo6@6.2-0ubuntu2.1, bash@5.0-6ubuntu1.2, ncurses/libncurses6@6.2-0ubuntu2.1, ncurses/ncurses-bin@6.2-0ubuntu2.1, procps@2:3.3.16-1ubuntu2.4, util-linux/fdisk@2.34-0.1ubuntu9.4, util-linux/mount@2.34-0.1ubuntu9.4, ncurses/libncursesw6@6.2-0ubuntu2.1, ncurses/ncurses-base@6.2-0ubuntu2.1
  From: ncurses/libtinfo6@6.2-0ubuntu2.1
  From: bash@5.0-6ubuntu1.2 > ncurses/libtinfo6@6.2-0ubuntu2.1
  From: ncurses/libncurses6@6.2-0ubuntu2.1 > ncurses/libtinfo6@6.2-0ubuntu2.1
  and 12 more...
  Image layer: 'apt-get install -y --no-install-recommends ca-certificates jq numactl procps'

✗ Low severity vulnerability found in ncurses/libtinfo6
  Description: CVE-2023-45918
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-NCURSES-6253014
  Introduced through: ncurses/libtinfo6@6.2-0ubuntu2.1, bash@5.0-6ubuntu1.2, ncurses/libncurses6@6.2-0ubuntu2.1, ncurses/ncurses-bin@6.2-0ubuntu2.1, procps@2:3.3.16-1ubuntu2.4, util-linux/fdisk@2.34-0.1ubuntu9.4, util-linux/mount@2.34-0.1ubuntu9.4, ncurses/libncursesw6@6.2-0ubuntu2.1, ncurses/ncurses-base@6.2-0ubuntu2.1
  From: ncurses/libtinfo6@6.2-0ubuntu2.1
  From: bash@5.0-6ubuntu1.2 > ncurses/libtinfo6@6.2-0ubuntu2.1
  From: ncurses/libncurses6@6.2-0ubuntu2.1 > ncurses/libtinfo6@6.2-0ubuntu2.1
  and 12 more...
  Image layer: 'apt-get install -y --no-install-recommends ca-certificates jq numactl procps'

✗ Low severity vulnerability found in krb5/krb5-locales
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-KRB5-579303
  Introduced through: krb5/krb5-locales@1.17-6ubuntu4.4, krb5/libkrb5support0@1.17-6ubuntu4.4, mongodb-org@5.0.24
  From: krb5/krb5-locales@1.17-6ubuntu4.4
  From: krb5/libkrb5support0@1.17-6ubuntu4.4
  From: mongodb-org@5.0.24 > mongodb-org/mongodb-org-tools@5.0.24 > mongodb-database-tools@100.9.4 > krb5/libk5crypto3@1.17-6ubuntu4.4
  and 7 more...
  Image layer: Introduced by your base image (mongo:5.0.24-focal)

✗ Low severity vulnerability found in krb5/krb5-locales
  Description: CVE-2024-26461
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-KRB5-6281066
  Introduced through: krb5/krb5-locales@1.17-6ubuntu4.4, krb5/libkrb5support0@1.17-6ubuntu4.4, mongodb-org@5.0.24
  From: krb5/krb5-locales@1.17-6ubuntu4.4
  From: krb5/libkrb5support0@1.17-6ubuntu4.4
  From: mongodb-org@5.0.24 > mongodb-org/mongodb-org-tools@5.0.24 > mongodb-database-tools@100.9.4 > krb5/libk5crypto3@1.17-6ubuntu4.4
  and 7 more...
  Image layer: Introduced by your base image (mongo:5.0.24-focal)

✗ Low severity vulnerability found in krb5/krb5-locales
  Description: CVE-2024-26458
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-KRB5-6281078
  Introduced through: krb5/krb5-locales@1.17-6ubuntu4.4, krb5/libkrb5support0@1.17-6ubuntu4.4, mongodb-org@5.0.24
  From: krb5/krb5-locales@1.17-6ubuntu4.4
  From: krb5/libkrb5support0@1.17-6ubuntu4.4
  From: mongodb-org@5.0.24 > mongodb-org/mongodb-org-tools@5.0.24 > mongodb-database-tools@100.9.4 > krb5/libk5crypto3@1.17-6ubuntu4.4
  and 7 more...
  Image layer: Introduced by your base image (mongo:5.0.24-focal)

✗ Low severity vulnerability found in gnupg2/gpgv
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-GNUPG2-3035407
  Introduced through: gnupg2/gpgv@2.2.19-3ubuntu2.2, apt@2.0.10
  From: gnupg2/gpgv@2.2.19-3ubuntu2.2
  From: apt@2.0.10 > gnupg2/gpgv@2.2.19-3ubuntu2.2
  Image layer: Introduced by your base image (mongo:5.0.24-focal)

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-GLIBC-1297554
  Introduced through: glibc/libc-bin@2.31-0ubuntu9.14, glibc/libc6@2.31-0ubuntu9.14
  From: glibc/libc-bin@2.31-0ubuntu9.14
  From: glibc/libc6@2.31-0ubuntu9.14
  Image layer: Introduced by your base image (mongo:5.0.24-focal)

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-GLIBC-2415100
  Introduced through: glibc/libc-bin@2.31-0ubuntu9.14, glibc/libc6@2.31-0ubuntu9.14
  From: glibc/libc-bin@2.31-0ubuntu9.14
  From: glibc/libc6@2.31-0ubuntu9.14
  Image layer: Introduced by your base image (mongo:5.0.24-focal)

✗ Low severity vulnerability found in coreutils
  Description: Improper Input Validation
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-COREUTILS-583876
  Introduced through: coreutils@8.30-3ubuntu2
  From: coreutils@8.30-3ubuntu2
  Image layer: Introduced by your base image (mongo:5.0.24-focal)

✗ Medium severity vulnerability found in xz-utils/liblzma5
  Description: CVE-2020-22916
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-XZUTILS-5854646
  Introduced through: xz-utils/liblzma5@5.2.4-1ubuntu1.1
  From: xz-utils/liblzma5@5.2.4-1ubuntu1.1
  Image layer: Introduced by your base image (mongo:5.0.24-focal)

✗ Medium severity vulnerability found in util-linux/libblkid1
  Description: CVE-2024-28085
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-UTILLINUX-6508371
  Introduced through: util-linux/libblkid1@2.34-0.1ubuntu9.4, e2fsprogs@1.45.5-2ubuntu1.1, util-linux/mount@2.34-0.1ubuntu9.4, util-linux/fdisk@2.34-0.1ubuntu9.4, util-linux/libuuid1@2.34-0.1ubuntu9.4, util-linux@2.34-0.1ubuntu9.4, sysvinit/sysvinit-utils@2.96-2.1ubuntu1, util-linux/bsdutils@1:2.34-0.1ubuntu9.4, util-linux/libfdisk1@2.34-0.1ubuntu9.4, util-linux/libmount1@2.34-0.1ubuntu9.4, util-linux/libsmartcols1@2.34-0.1ubuntu9.4
  From: util-linux/libblkid1@2.34-0.1ubuntu9.4
  From: e2fsprogs@1.45.5-2ubuntu1.1 > util-linux/libblkid1@2.34-0.1ubuntu9.4
  From: util-linux/mount@2.34-0.1ubuntu9.4 > util-linux/libblkid1@2.34-0.1ubuntu9.4
  and 23 more...
  Image layer: Introduced by your base image (mongo:5.0.24-focal)
  Fixed in: 2.34-0.1ubuntu9.5

✗ Medium severity vulnerability found in nghttp2/libnghttp2-14
  Description: CVE-2024-28182
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-NGHTTP2-6553931
  Introduced through: mongodb-org@5.0.24
  From: mongodb-org@5.0.24 > mongodb-org/mongodb-org-database@5.0.24 > mongodb-org/mongodb-org-shell@5.0.24 > curl/libcurl4@7.68.0-1ubuntu2.21 > nghttp2/libnghttp2-14@1.40.0-1ubuntu0.2
  Image layer: Introduced by your base image (mongo:5.0.24-focal)
  Fixed in: 1.40.0-1ubuntu0.3

✗ Medium severity vulnerability found in libgcrypt20
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-LIBGCRYPT20-6411449
  Introduced through: libgcrypt20@1.8.5-5ubuntu1.1, apt@2.0.10
  From: libgcrypt20@1.8.5-5ubuntu1.1
  From: apt@2.0.10 > apt/libapt-pkg6.0@2.0.10 > libgcrypt20@1.8.5-5ubuntu1.1
  From: apt@2.0.10 > gnupg2/gpgv@2.2.19-3ubuntu2.2 > libgcrypt20@1.8.5-5ubuntu1.1
  and 1 more...
  Image layer: Introduced by your base image (mongo:5.0.24-focal)

✗ Medium severity vulnerability found in krb5/krb5-locales
  Description: CVE-2024-26462
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-KRB5-6281072
  Introduced through: krb5/krb5-locales@1.17-6ubuntu4.4, krb5/libkrb5support0@1.17-6ubuntu4.4, mongodb-org@5.0.24
  From: krb5/krb5-locales@1.17-6ubuntu4.4
  From: krb5/libkrb5support0@1.17-6ubuntu4.4
  From: mongodb-org@5.0.24 > mongodb-org/mongodb-org-tools@5.0.24 > mongodb-database-tools@100.9.4 > krb5/libk5crypto3@1.17-6ubuntu4.4
  and 7 more...
  Image layer: Introduced by your base image (mongo:5.0.24-focal)

✗ Medium severity vulnerability found in gnutls28/libgnutls30
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-GNUTLS28-6481604
  Introduced through: gnutls28/libgnutls30@3.6.13-2ubuntu1.10, apt@2.0.10, mongodb-org@5.0.24
  From: gnutls28/libgnutls30@3.6.13-2ubuntu1.10
  From: apt@2.0.10 > gnutls28/libgnutls30@3.6.13-2ubuntu1.10
  From: mongodb-org@5.0.24 > mongodb-org/mongodb-org-database@5.0.24 > mongodb-org/mongodb-org-shell@5.0.24 > curl/libcurl4@7.68.0-1ubuntu2.21 > openldap/libldap-2.4-2@2.4.49+dfsg-2ubuntu1.10 > gnutls28/libgnutls30@3.6.13-2ubuntu1.10
  and 1 more...
  Image layer: Introduced by your base image (mongo:5.0.24-focal)
  Fixed in: 3.6.13-2ubuntu1.11

✗ Medium severity vulnerability found in glibc/libc-bin
  Description: CVE-2024-2961
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-GLIBC-6663150
  Introduced through: glibc/libc-bin@2.31-0ubuntu9.14, glibc/libc6@2.31-0ubuntu9.14
  From: glibc/libc-bin@2.31-0ubuntu9.14
  From: glibc/libc6@2.31-0ubuntu9.14
  Image layer: Introduced by your base image (mongo:5.0.24-focal)
  Fixed in: 2.31-0ubuntu9.15

✗ Medium severity vulnerability found in glibc/libc-bin
  Description: CVE-2024-33600
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-GLIBC-6674185
  Introduced through: glibc/libc-bin@2.31-0ubuntu9.14, glibc/libc6@2.31-0ubuntu9.14
  From: glibc/libc-bin@2.31-0ubuntu9.14
  From: glibc/libc6@2.31-0ubuntu9.14
  Image layer: Introduced by your base image (mongo:5.0.24-focal)
  Fixed in: 2.31-0ubuntu9.16

✗ Medium severity vulnerability found in glibc/libc-bin
  Description: CVE-2024-33599
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-GLIBC-6674200
  Introduced through: glibc/libc-bin@2.31-0ubuntu9.14, glibc/libc6@2.31-0ubuntu9.14
  From: glibc/libc-bin@2.31-0ubuntu9.14
  From: glibc/libc6@2.31-0ubuntu9.14
  Image layer: Introduced by your base image (mongo:5.0.24-focal)
  Fixed in: 2.31-0ubuntu9.16

✗ Medium severity vulnerability found in glibc/libc-bin
  Description: CVE-2024-33601
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-GLIBC-6674209
  Introduced through: glibc/libc-bin@2.31-0ubuntu9.14, glibc/libc6@2.31-0ubuntu9.14
  From: glibc/libc-bin@2.31-0ubuntu9.14
  From: glibc/libc6@2.31-0ubuntu9.14
  Image layer: Introduced by your base image (mongo:5.0.24-focal)
  Fixed in: 2.31-0ubuntu9.16

✗ Medium severity vulnerability found in glibc/libc-bin
  Description: CVE-2024-33602
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-GLIBC-6674218
  Introduced through: glibc/libc-bin@2.31-0ubuntu9.14, glibc/libc6@2.31-0ubuntu9.14
  From: glibc/libc-bin@2.31-0ubuntu9.14
  From: glibc/libc6@2.31-0ubuntu9.14
  Image layer: Introduced by your base image (mongo:5.0.24-focal)
  Fixed in: 2.31-0ubuntu9.16

✗ Medium severity vulnerability found in curl/libcurl4
  Description: CVE-2024-2398
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-CURL-6507270
  Introduced through: mongodb-org@5.0.24
  From: mongodb-org@5.0.24 > mongodb-org/mongodb-org-database@5.0.24 > mongodb-org/mongodb-org-mongos@5.0.24 > curl/libcurl4@7.68.0-1ubuntu2.21
  From: mongodb-org@5.0.24 > mongodb-org/mongodb-org-database@5.0.24 > mongodb-org/mongodb-org-server@5.0.24 > curl/libcurl4@7.68.0-1ubuntu2.21
  From: mongodb-org@5.0.24 > mongodb-org/mongodb-org-database@5.0.24 > mongodb-org/mongodb-org-shell@5.0.24 > curl/libcurl4@7.68.0-1ubuntu2.21
  Image layer: Introduced by your base image (mongo:5.0.24-focal)
  Fixed in: 7.68.0-1ubuntu2.22



Organization:      bhavdeep1304
Package manager:   deb
Project name:      docker-image|mongo
Docker image:      mongo:5.0.24
Platform:          linux/amd64
Base image:        mongo:5.0.24-focal
Licenses:          enabled

Tested 138 dependencies for known issues, found 29 issues.

Base Image          Vulnerabilities  Severity
mongo:5.0.24-focal  29               0 critical, 0 high, 12 medium, 17 low

Recommendations for base image upgrade:

Minor upgrades
Base Image          Vulnerabilities  Severity
mongo:5.0.26-focal  19               0 critical, 0 high, 3 medium, 16 low

Alternative image types
Base Image              Vulnerabilities  Severity
mongo:8.0.0-rc9         19               0 critical, 0 high, 3 medium, 16 low
mongo:8.0.0-rc9-jammy   19               0 critical, 0 high, 3 medium, 16 low
mongo:5.0.27-rc0-focal  19               0 critical, 0 high, 3 medium, 16 low
mongo:5.0.27-rc0        19               0 critical, 0 high, 3 medium, 16 low


Learn more: https://docs.snyk.io/products/snyk-container/getting-around-the-snyk-container-ui/base-image-detection

-------------------------------------------------------

Testing mongo:5.0.24...

Organization:      bhavdeep1304
Package manager:   gomodules
Target file:       /usr/local/bin/gosu
Project name:      github.com/tianon/gosu
Docker image:      mongo:5.0.24
Licenses:          enabled

✔ Tested 2 dependencies for known issues, no vulnerable paths found.


Tested 2 projects, 1 contained vulnerable paths.



```
