**Scanning mongo:4.4**
```

Testing mongo:4.4...

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: CVE-2023-26604
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-SYSTEMD-3339226
  Introduced through: systemd/libsystemd0@245.4-4ubuntu3.23, apt@2.0.10, procps/libprocps8@2:3.3.16-1ubuntu2.4, util-linux/bsdutils@1:2.34-0.1ubuntu9.6, util-linux/mount@2.34-0.1ubuntu9.6, systemd/libudev1@245.4-4ubuntu3.23
  From: systemd/libsystemd0@245.4-4ubuntu3.23
  From: apt@2.0.10 > systemd/libsystemd0@245.4-4ubuntu3.23
  From: procps/libprocps8@2:3.3.16-1ubuntu2.4 > systemd/libsystemd0@245.4-4ubuntu3.23
  and 6 more...

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: CVE-2023-7008
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-SYSTEMD-6137854
  Introduced through: systemd/libsystemd0@245.4-4ubuntu3.23, apt@2.0.10, procps/libprocps8@2:3.3.16-1ubuntu2.4, util-linux/bsdutils@1:2.34-0.1ubuntu9.6, util-linux/mount@2.34-0.1ubuntu9.6, systemd/libudev1@245.4-4ubuntu3.23
  From: systemd/libsystemd0@245.4-4ubuntu3.23
  From: apt@2.0.10 > systemd/libsystemd0@245.4-4ubuntu3.23
  From: procps/libprocps8@2:3.3.16-1ubuntu2.4 > systemd/libsystemd0@245.4-4ubuntu3.23
  and 6 more...

✗ Low severity vulnerability found in shadow/passwd
  Description: Arbitrary Code Injection
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-SHADOW-5425687
  Introduced through: shadow/passwd@1:4.8.1-1ubuntu5.20.04.5, adduser@3.118ubuntu2, shadow/login@1:4.8.1-1ubuntu5.20.04.5, util-linux/mount@2.34-0.1ubuntu9.6
  From: shadow/passwd@1:4.8.1-1ubuntu5.20.04.5
  From: adduser@3.118ubuntu2 > shadow/passwd@1:4.8.1-1ubuntu5.20.04.5
  From: shadow/login@1:4.8.1-1ubuntu5.20.04.5
  and 1 more...

✗ Low severity vulnerability found in shadow/passwd
  Description: Time-of-check Time-of-use (TOCTOU)
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-SHADOW-577863
  Introduced through: shadow/passwd@1:4.8.1-1ubuntu5.20.04.5, adduser@3.118ubuntu2, shadow/login@1:4.8.1-1ubuntu5.20.04.5, util-linux/mount@2.34-0.1ubuntu9.6
  From: shadow/passwd@1:4.8.1-1ubuntu5.20.04.5
  From: adduser@3.118ubuntu2 > shadow/passwd@1:4.8.1-1ubuntu5.20.04.5
  From: shadow/login@1:4.8.1-1ubuntu5.20.04.5
  and 1 more...

✗ Low severity vulnerability found in pcre3/libpcre3
  Description: Uncontrolled Recursion
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-PCRE3-580031
  Introduced through: pcre3/libpcre3@2:8.39-12ubuntu0.1, grep@3.4-1
  From: pcre3/libpcre3@2:8.39-12ubuntu0.1
  From: grep@3.4-1 > pcre3/libpcre3@2:8.39-12ubuntu0.1

✗ Low severity vulnerability found in openssl/libssl1.1
  Description: CVE-2024-2511
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-OPENSSL-6592107
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2ubuntu0.1, ca-certificates@20230311ubuntu0.20.04.1, mongodb-org@4.4.29
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2ubuntu0.1 > openssl/libssl1.1@1.1.1f-1ubuntu2.22
  From: ca-certificates@20230311ubuntu0.20.04.1 > openssl@1.1.1f-1ubuntu2.22 > openssl/libssl1.1@1.1.1f-1ubuntu2.22
  From: mongodb-org@4.4.29 > mongodb-org/mongodb-org-mongos@4.4.29 > openssl/libssl1.1@1.1.1f-1ubuntu2.22
  and 6 more...

✗ Low severity vulnerability found in openssl/libssl1.1
  Description: CVE-2024-4741
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-OPENSSL-7151336
  Introduced through: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2ubuntu0.1, ca-certificates@20230311ubuntu0.20.04.1, mongodb-org@4.4.29
  From: cyrus-sasl2/libsasl2-modules@2.1.27+dfsg-2ubuntu0.1 > openssl/libssl1.1@1.1.1f-1ubuntu2.22
  From: ca-certificates@20230311ubuntu0.20.04.1 > openssl@1.1.1f-1ubuntu2.22 > openssl/libssl1.1@1.1.1f-1ubuntu2.22
  From: mongodb-org@4.4.29 > mongodb-org/mongodb-org-mongos@4.4.29 > openssl/libssl1.1@1.1.1f-1ubuntu2.22
  and 6 more...

✗ Low severity vulnerability found in ncurses/libtinfo6
  Description: CVE-2023-50495
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-NCURSES-6123866
  Introduced through: ncurses/libtinfo6@6.2-0ubuntu2.1, bash@5.0-6ubuntu1.2, ncurses/libncurses6@6.2-0ubuntu2.1, ncurses/ncurses-bin@6.2-0ubuntu2.1, procps@2:3.3.16-1ubuntu2.4, util-linux/fdisk@2.34-0.1ubuntu9.6, util-linux/mount@2.34-0.1ubuntu9.6, ncurses/libncursesw6@6.2-0ubuntu2.1, ncurses/ncurses-base@6.2-0ubuntu2.1
  From: ncurses/libtinfo6@6.2-0ubuntu2.1
  From: bash@5.0-6ubuntu1.2 > ncurses/libtinfo6@6.2-0ubuntu2.1
  From: ncurses/libncurses6@6.2-0ubuntu2.1 > ncurses/libtinfo6@6.2-0ubuntu2.1
  and 12 more...

✗ Low severity vulnerability found in ncurses/libtinfo6
  Description: CVE-2023-45918
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-NCURSES-6253014
  Introduced through: ncurses/libtinfo6@6.2-0ubuntu2.1, bash@5.0-6ubuntu1.2, ncurses/libncurses6@6.2-0ubuntu2.1, ncurses/ncurses-bin@6.2-0ubuntu2.1, procps@2:3.3.16-1ubuntu2.4, util-linux/fdisk@2.34-0.1ubuntu9.6, util-linux/mount@2.34-0.1ubuntu9.6, ncurses/libncursesw6@6.2-0ubuntu2.1, ncurses/ncurses-base@6.2-0ubuntu2.1
  From: ncurses/libtinfo6@6.2-0ubuntu2.1
  From: bash@5.0-6ubuntu1.2 > ncurses/libtinfo6@6.2-0ubuntu2.1
  From: ncurses/libncurses6@6.2-0ubuntu2.1 > ncurses/libtinfo6@6.2-0ubuntu2.1
  and 12 more...

✗ Low severity vulnerability found in krb5/krb5-locales
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-KRB5-579303
  Introduced through: krb5/krb5-locales@1.17-6ubuntu4.4, mongodb-org@4.4.29
  From: krb5/krb5-locales@1.17-6ubuntu4.4
  From: mongodb-org@4.4.29 > mongodb-org/mongodb-org-tools@4.4.29 > mongodb-database-tools@100.9.4 > krb5/libkrb5support0@1.17-6ubuntu4.4
  From: mongodb-org@4.4.29 > mongodb-org/mongodb-org-shell@4.4.29 > curl/libcurl4@7.68.0-1ubuntu2.22 > krb5/libgssapi-krb5-2@1.17-6ubuntu4.4 > krb5/libkrb5support0@1.17-6ubuntu4.4
  and 10 more...

✗ Low severity vulnerability found in krb5/krb5-locales
  Description: CVE-2024-26461
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-KRB5-6281066
  Introduced through: krb5/krb5-locales@1.17-6ubuntu4.4, mongodb-org@4.4.29
  From: krb5/krb5-locales@1.17-6ubuntu4.4
  From: mongodb-org@4.4.29 > mongodb-org/mongodb-org-tools@4.4.29 > mongodb-database-tools@100.9.4 > krb5/libkrb5support0@1.17-6ubuntu4.4
  From: mongodb-org@4.4.29 > mongodb-org/mongodb-org-shell@4.4.29 > curl/libcurl4@7.68.0-1ubuntu2.22 > krb5/libgssapi-krb5-2@1.17-6ubuntu4.4 > krb5/libkrb5support0@1.17-6ubuntu4.4
  and 10 more...

✗ Low severity vulnerability found in krb5/krb5-locales
  Description: CVE-2024-26458
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-KRB5-6281078
  Introduced through: krb5/krb5-locales@1.17-6ubuntu4.4, mongodb-org@4.4.29
  From: krb5/krb5-locales@1.17-6ubuntu4.4
  From: mongodb-org@4.4.29 > mongodb-org/mongodb-org-tools@4.4.29 > mongodb-database-tools@100.9.4 > krb5/libkrb5support0@1.17-6ubuntu4.4
  From: mongodb-org@4.4.29 > mongodb-org/mongodb-org-shell@4.4.29 > curl/libcurl4@7.68.0-1ubuntu2.22 > krb5/libgssapi-krb5-2@1.17-6ubuntu4.4 > krb5/libkrb5support0@1.17-6ubuntu4.4
  and 10 more...

✗ Low severity vulnerability found in gnupg2/gpgv
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-GNUPG2-3035407
  Introduced through: gnupg2/gpgv@2.2.19-3ubuntu2.2, apt@2.0.10
  From: gnupg2/gpgv@2.2.19-3ubuntu2.2
  From: apt@2.0.10 > gnupg2/gpgv@2.2.19-3ubuntu2.2

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-GLIBC-1297554
  Introduced through: glibc/libc-bin@2.31-0ubuntu9.15, glibc/libc6@2.31-0ubuntu9.15
  From: glibc/libc-bin@2.31-0ubuntu9.15
  From: glibc/libc6@2.31-0ubuntu9.15

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-GLIBC-2415100
  Introduced through: glibc/libc-bin@2.31-0ubuntu9.15, glibc/libc6@2.31-0ubuntu9.15
  From: glibc/libc-bin@2.31-0ubuntu9.15
  From: glibc/libc6@2.31-0ubuntu9.15

✗ Low severity vulnerability found in coreutils
  Description: Improper Input Validation
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-COREUTILS-583876
  Introduced through: coreutils@8.30-3ubuntu2
  From: coreutils@8.30-3ubuntu2

✗ Medium severity vulnerability found in xz-utils/liblzma5
  Description: CVE-2020-22916
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-XZUTILS-5854646
  Introduced through: xz-utils/liblzma5@5.2.4-1ubuntu1.1
  From: xz-utils/liblzma5@5.2.4-1ubuntu1.1

✗ Medium severity vulnerability found in libgcrypt20
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-LIBGCRYPT20-6411449
  Introduced through: libgcrypt20@1.8.5-5ubuntu1.1, apt@2.0.10
  From: libgcrypt20@1.8.5-5ubuntu1.1
  From: apt@2.0.10 > apt/libapt-pkg6.0@2.0.10 > libgcrypt20@1.8.5-5ubuntu1.1
  From: apt@2.0.10 > gnupg2/gpgv@2.2.19-3ubuntu2.2 > libgcrypt20@1.8.5-5ubuntu1.1
  and 1 more...

✗ Medium severity vulnerability found in krb5/krb5-locales
  Description: CVE-2024-26462
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-KRB5-6281072
  Introduced through: krb5/krb5-locales@1.17-6ubuntu4.4, mongodb-org@4.4.29
  From: krb5/krb5-locales@1.17-6ubuntu4.4
  From: mongodb-org@4.4.29 > mongodb-org/mongodb-org-tools@4.4.29 > mongodb-database-tools@100.9.4 > krb5/libkrb5support0@1.17-6ubuntu4.4
  From: mongodb-org@4.4.29 > mongodb-org/mongodb-org-shell@4.4.29 > curl/libcurl4@7.68.0-1ubuntu2.22 > krb5/libgssapi-krb5-2@1.17-6ubuntu4.4 > krb5/libkrb5support0@1.17-6ubuntu4.4
  and 10 more...

✗ Medium severity vulnerability found in glibc/libc-bin
  Description: CVE-2024-33600
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-GLIBC-6674185
  Introduced through: glibc/libc-bin@2.31-0ubuntu9.15, glibc/libc6@2.31-0ubuntu9.15
  From: glibc/libc-bin@2.31-0ubuntu9.15
  From: glibc/libc6@2.31-0ubuntu9.15
  Fixed in: 2.31-0ubuntu9.16

✗ Medium severity vulnerability found in glibc/libc-bin
  Description: CVE-2024-33599
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-GLIBC-6674200
  Introduced through: glibc/libc-bin@2.31-0ubuntu9.15, glibc/libc6@2.31-0ubuntu9.15
  From: glibc/libc-bin@2.31-0ubuntu9.15
  From: glibc/libc6@2.31-0ubuntu9.15
  Fixed in: 2.31-0ubuntu9.16

✗ Medium severity vulnerability found in glibc/libc-bin
  Description: CVE-2024-33601
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-GLIBC-6674209
  Introduced through: glibc/libc-bin@2.31-0ubuntu9.15, glibc/libc6@2.31-0ubuntu9.15
  From: glibc/libc-bin@2.31-0ubuntu9.15
  From: glibc/libc6@2.31-0ubuntu9.15
  Fixed in: 2.31-0ubuntu9.16

✗ Medium severity vulnerability found in glibc/libc-bin
  Description: CVE-2024-33602
  Info: https://security.snyk.io/vuln/SNYK-UBUNTU2004-GLIBC-6674218
  Introduced through: glibc/libc-bin@2.31-0ubuntu9.15, glibc/libc6@2.31-0ubuntu9.15
  From: glibc/libc-bin@2.31-0ubuntu9.15
  From: glibc/libc6@2.31-0ubuntu9.15
  Fixed in: 2.31-0ubuntu9.16



Organization:      bhavdeep1304
Package manager:   deb
Project name:      docker-image|mongo
Docker image:      mongo:4.4
Platform:          linux/amd64
Licenses:          enabled

Tested 136 dependencies for known issues, found 23 issues.

Snyk wasn’t able to auto detect the base image, use `--file` option to get base image remediation advice.
Example: $ snyk container test mongo:4.4 --file=path/to/Dockerfile

To remove this message in the future, please run `snyk config set disableSuggestions=true`

-------------------------------------------------------

Testing mongo:4.4...

Organization:      bhavdeep1304
Package manager:   gomodules
Target file:       /usr/local/bin/gosu
Project name:      github.com/tianon/gosu
Docker image:      mongo:4.4
Licenses:          enabled

✔ Tested 2 dependencies for known issues, no vulnerable paths found.


Tested 2 projects, 1 contained vulnerable paths.



```
