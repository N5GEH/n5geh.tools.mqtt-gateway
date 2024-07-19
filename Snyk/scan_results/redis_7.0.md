**Scanning redis:7.0**
```

Testing redis:7.0...

✗ Low severity vulnerability found in util-linux/libblkid1
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-UTILLINUX-2401083
  Introduced through: util-linux/libblkid1@2.38.1-5+deb12u1, e2fsprogs@1.47.0-2, util-linux/libmount1@2.38.1-5+deb12u1, util-linux@2.38.1-5+deb12u1, util-linux/mount@2.38.1-5+deb12u1, util-linux/libuuid1@2.38.1-5+deb12u1, util-linux/libsmartcols1@2.38.1-5+deb12u1, util-linux/util-linux-extra@2.38.1-5+deb12u1, util-linux/bsdutils@1:2.38.1-5+deb12u1
  From: util-linux/libblkid1@2.38.1-5+deb12u1
  From: e2fsprogs@1.47.0-2 > util-linux/libblkid1@2.38.1-5+deb12u1
  From: util-linux/libmount1@2.38.1-5+deb12u1 > util-linux/libblkid1@2.38.1-5+deb12u1
  and 17 more...

✗ Low severity vulnerability found in tar
  Description: CVE-2005-2541
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-TAR-1560620
  Introduced through: tar@1.34+dfsg-1.2+deb12u1, dash@0.5.12-2
  From: tar@1.34+dfsg-1.2+deb12u1
  From: dash@0.5.12-2 > dpkg@1.21.22 > tar@1.34+dfsg-1.2+deb12u1

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Link Following
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SYSTEMD-1560739
  Introduced through: systemd/libsystemd0@252.26-1~deb12u2, apt@2.6.1, util-linux@2.38.1-5+deb12u1, util-linux/bsdutils@1:2.38.1-5+deb12u1, systemd/libudev1@252.26-1~deb12u2
  From: systemd/libsystemd0@252.26-1~deb12u2
  From: apt@2.6.1 > systemd/libsystemd0@252.26-1~deb12u2
  From: util-linux@2.38.1-5+deb12u1 > systemd/libsystemd0@252.26-1~deb12u2
  and 5 more...

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Improper Validation of Integrity Check Value
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SYSTEMD-5733385
  Introduced through: systemd/libsystemd0@252.26-1~deb12u2, apt@2.6.1, util-linux@2.38.1-5+deb12u1, util-linux/bsdutils@1:2.38.1-5+deb12u1, systemd/libudev1@252.26-1~deb12u2
  From: systemd/libsystemd0@252.26-1~deb12u2
  From: apt@2.6.1 > systemd/libsystemd0@252.26-1~deb12u2
  From: util-linux@2.38.1-5+deb12u1 > systemd/libsystemd0@252.26-1~deb12u2
  and 5 more...

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Improper Validation of Integrity Check Value
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SYSTEMD-5733390
  Introduced through: systemd/libsystemd0@252.26-1~deb12u2, apt@2.6.1, util-linux@2.38.1-5+deb12u1, util-linux/bsdutils@1:2.38.1-5+deb12u1, systemd/libudev1@252.26-1~deb12u2
  From: systemd/libsystemd0@252.26-1~deb12u2
  From: apt@2.6.1 > systemd/libsystemd0@252.26-1~deb12u2
  From: util-linux@2.38.1-5+deb12u1 > systemd/libsystemd0@252.26-1~deb12u2
  and 5 more...

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Improper Validation of Integrity Check Value
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SYSTEMD-5733398
  Introduced through: systemd/libsystemd0@252.26-1~deb12u2, apt@2.6.1, util-linux@2.38.1-5+deb12u1, util-linux/bsdutils@1:2.38.1-5+deb12u1, systemd/libudev1@252.26-1~deb12u2
  From: systemd/libsystemd0@252.26-1~deb12u2
  From: apt@2.6.1 > systemd/libsystemd0@252.26-1~deb12u2
  From: util-linux@2.38.1-5+deb12u1 > systemd/libsystemd0@252.26-1~deb12u2
  and 5 more...

✗ Low severity vulnerability found in shadow/passwd
  Description: Access Restriction Bypass
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SHADOW-1559391
  Introduced through: shadow/passwd@1:4.13+dfsg1-1+b1, adduser@3.134, shadow/login@1:4.13+dfsg1-1+b1
  From: shadow/passwd@1:4.13+dfsg1-1+b1
  From: adduser@3.134 > shadow/passwd@1:4.13+dfsg1-1+b1
  From: shadow/login@1:4.13+dfsg1-1+b1

✗ Low severity vulnerability found in shadow/passwd
  Description: Incorrect Permission Assignment for Critical Resource
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SHADOW-1559403
  Introduced through: shadow/passwd@1:4.13+dfsg1-1+b1, adduser@3.134, shadow/login@1:4.13+dfsg1-1+b1
  From: shadow/passwd@1:4.13+dfsg1-1+b1
  From: adduser@3.134 > shadow/passwd@1:4.13+dfsg1-1+b1
  From: shadow/login@1:4.13+dfsg1-1+b1

✗ Low severity vulnerability found in shadow/passwd
  Description: Arbitrary Code Injection
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SHADOW-5423923
  Introduced through: shadow/passwd@1:4.13+dfsg1-1+b1, adduser@3.134, shadow/login@1:4.13+dfsg1-1+b1
  From: shadow/passwd@1:4.13+dfsg1-1+b1
  From: adduser@3.134 > shadow/passwd@1:4.13+dfsg1-1+b1
  From: shadow/login@1:4.13+dfsg1-1+b1

✗ Low severity vulnerability found in shadow/passwd
  Description: Improper Authentication
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-SHADOW-5879156
  Introduced through: shadow/passwd@1:4.13+dfsg1-1+b1, adduser@3.134, shadow/login@1:4.13+dfsg1-1+b1
  From: shadow/passwd@1:4.13+dfsg1-1+b1
  From: adduser@3.134 > shadow/passwd@1:4.13+dfsg1-1+b1
  From: shadow/login@1:4.13+dfsg1-1+b1

✗ Low severity vulnerability found in perl/perl-base
  Description: Link Following
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-PERL-1556505
  Introduced through: perl/perl-base@5.36.0-7+deb12u1
  From: perl/perl-base@5.36.0-7+deb12u1

✗ Low severity vulnerability found in perl/perl-base
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-PERL-5489184
  Introduced through: perl/perl-base@5.36.0-7+deb12u1
  From: perl/perl-base@5.36.0-7+deb12u1

✗ Low severity vulnerability found in perl/perl-base
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-PERL-5489190
  Introduced through: perl/perl-base@5.36.0-7+deb12u1
  From: perl/perl-base@5.36.0-7+deb12u1

✗ Low severity vulnerability found in pam/libpam0g
  Description: CVE-2024-22365
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-PAM-6178914
  Introduced through: pam/libpam0g@1.5.2-6+deb12u1, shadow/login@1:4.13+dfsg1-1+b1, util-linux@2.38.1-5+deb12u1, adduser@3.134, pam/libpam-modules-bin@1.5.2-6+deb12u1, pam/libpam-modules@1.5.2-6+deb12u1, pam/libpam-runtime@1.5.2-6+deb12u1
  From: pam/libpam0g@1.5.2-6+deb12u1
  From: shadow/login@1:4.13+dfsg1-1+b1 > pam/libpam0g@1.5.2-6+deb12u1
  From: util-linux@2.38.1-5+deb12u1 > pam/libpam0g@1.5.2-6+deb12u1
  and 11 more...

✗ Low severity vulnerability found in openssl/libssl3
  Description: CVE-2024-2511
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENSSL-6592092
  Introduced through: openssl/libssl3@3.0.13-1~deb12u1
  From: openssl/libssl3@3.0.13-1~deb12u1

✗ Low severity vulnerability found in openssl/libssl3
  Description: CVE-2024-4603
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENSSL-6861561
  Introduced through: openssl/libssl3@3.0.13-1~deb12u1
  From: openssl/libssl3@3.0.13-1~deb12u1

✗ Low severity vulnerability found in openssl/libssl3
  Description: CVE-2024-4741
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENSSL-7151359
  Introduced through: openssl/libssl3@3.0.13-1~deb12u1
  From: openssl/libssl3@3.0.13-1~deb12u1

✗ Low severity vulnerability found in openssl/libssl3
  Description: CVE-2024-5535
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-OPENSSL-7411350
  Introduced through: openssl/libssl3@3.0.13-1~deb12u1
  From: openssl/libssl3@3.0.13-1~deb12u1

✗ Low severity vulnerability found in ncurses/libtinfo6
  Description: CVE-2023-50495
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-NCURSES-6123823
  Introduced through: ncurses/libtinfo6@6.4-4, bash/bash@5.2.15-2+b7, ncurses/ncurses-bin@6.4-4, util-linux@2.38.1-5+deb12u1, ncurses/ncurses-base@6.4-4
  From: ncurses/libtinfo6@6.4-4
  From: bash/bash@5.2.15-2+b7 > ncurses/libtinfo6@6.4-4
  From: ncurses/ncurses-bin@6.4-4 > ncurses/libtinfo6@6.4-4
  and 3 more...

✗ Low severity vulnerability found in ncurses/libtinfo6
  Description: CVE-2023-45918
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-NCURSES-6252773
  Introduced through: ncurses/libtinfo6@6.4-4, bash/bash@5.2.15-2+b7, ncurses/ncurses-bin@6.4-4, util-linux@2.38.1-5+deb12u1, ncurses/ncurses-base@6.4-4
  From: ncurses/libtinfo6@6.4-4
  From: bash/bash@5.2.15-2+b7 > ncurses/libtinfo6@6.4-4
  From: ncurses/ncurses-bin@6.4-4 > ncurses/libtinfo6@6.4-4
  and 3 more...

✗ Low severity vulnerability found in libgcrypt20
  Description: Use of a Broken or Risky Cryptographic Algorithm
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-LIBGCRYPT20-1550206
  Introduced through: libgcrypt20@1.10.1-3, apt@2.6.1
  From: libgcrypt20@1.10.1-3
  From: apt@2.6.1 > apt/libapt-pkg6.0@2.6.1 > libgcrypt20@1.10.1-3
  From: apt@2.6.1 > gnupg2/gpgv@2.2.40-1.1 > libgcrypt20@1.10.1-3
  and 1 more...

✗ Low severity vulnerability found in libgcrypt20
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-LIBGCRYPT20-6405981
  Introduced through: libgcrypt20@1.10.1-3, apt@2.6.1
  From: libgcrypt20@1.10.1-3
  From: apt@2.6.1 > apt/libapt-pkg6.0@2.6.1 > libgcrypt20@1.10.1-3
  From: apt@2.6.1 > gnupg2/gpgv@2.2.40-1.1 > libgcrypt20@1.10.1-3
  and 1 more...

✗ Low severity vulnerability found in gnutls28/libgnutls30
  Description: Improper Input Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GNUTLS28-1547121
  Introduced through: gnutls28/libgnutls30@3.7.9-2+deb12u3, apt@2.6.1
  From: gnutls28/libgnutls30@3.7.9-2+deb12u3
  From: apt@2.6.1 > gnutls28/libgnutls30@3.7.9-2+deb12u3

✗ Low severity vulnerability found in gnupg2/gpgv
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GNUPG2-3330747
  Introduced through: gnupg2/gpgv@2.2.40-1.1, apt@2.6.1
  From: gnupg2/gpgv@2.2.40-1.1
  From: apt@2.6.1 > gnupg2/gpgv@2.2.40-1.1

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GLIBC-1546991
  Introduced through: glibc/libc-bin@2.36-9+deb12u7, glibc/libc6@2.36-9+deb12u7
  From: glibc/libc-bin@2.36-9+deb12u7
  From: glibc/libc6@2.36-9+deb12u7

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Uncontrolled Recursion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GLIBC-1547039
  Introduced through: glibc/libc-bin@2.36-9+deb12u7, glibc/libc6@2.36-9+deb12u7
  From: glibc/libc-bin@2.36-9+deb12u7
  From: glibc/libc6@2.36-9+deb12u7

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Uncontrolled Recursion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GLIBC-1547069
  Introduced through: glibc/libc-bin@2.36-9+deb12u7, glibc/libc6@2.36-9+deb12u7
  From: glibc/libc-bin@2.36-9+deb12u7
  From: glibc/libc6@2.36-9+deb12u7

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Use of Insufficiently Random Values
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GLIBC-1547135
  Introduced through: glibc/libc-bin@2.36-9+deb12u7, glibc/libc6@2.36-9+deb12u7
  From: glibc/libc-bin@2.36-9+deb12u7
  From: glibc/libc6@2.36-9+deb12u7

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GLIBC-1547196
  Introduced through: glibc/libc-bin@2.36-9+deb12u7, glibc/libc6@2.36-9+deb12u7
  From: glibc/libc-bin@2.36-9+deb12u7
  From: glibc/libc6@2.36-9+deb12u7

✗ Low severity vulnerability found in glibc/libc-bin
  Description: Resource Management Errors
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GLIBC-1547293
  Introduced through: glibc/libc-bin@2.36-9+deb12u7, glibc/libc6@2.36-9+deb12u7
  From: glibc/libc-bin@2.36-9+deb12u7
  From: glibc/libc6@2.36-9+deb12u7

✗ Low severity vulnerability found in glibc/libc-bin
  Description: CVE-2019-1010023
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GLIBC-1547373
  Introduced through: glibc/libc-bin@2.36-9+deb12u7, glibc/libc6@2.36-9+deb12u7
  From: glibc/libc-bin@2.36-9+deb12u7
  From: glibc/libc6@2.36-9+deb12u7

✗ Low severity vulnerability found in gcc-12/libstdc++6
  Description: Uncontrolled Recursion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GCC12-2606941
  Introduced through: gcc-12/libstdc++6@12.2.0-14, apt@2.6.1, gcc-12/gcc-12-base@12.2.0-14, gcc-12/libgcc-s1@12.2.0-14
  From: gcc-12/libstdc++6@12.2.0-14
  From: apt@2.6.1 > gcc-12/libstdc++6@12.2.0-14
  From: apt@2.6.1 > apt/libapt-pkg6.0@2.6.1 > gcc-12/libstdc++6@12.2.0-14
  and 2 more...

✗ Low severity vulnerability found in gcc-12/libstdc++6
  Description: CVE-2023-4039
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-GCC12-5901316
  Introduced through: gcc-12/libstdc++6@12.2.0-14, apt@2.6.1, gcc-12/gcc-12-base@12.2.0-14, gcc-12/libgcc-s1@12.2.0-14
  From: gcc-12/libstdc++6@12.2.0-14
  From: apt@2.6.1 > gcc-12/libstdc++6@12.2.0-14
  From: apt@2.6.1 > apt/libapt-pkg6.0@2.6.1 > gcc-12/libstdc++6@12.2.0-14
  and 2 more...

✗ Low severity vulnerability found in coreutils
  Description: Improper Input Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-COREUTILS-1543939
  Introduced through: coreutils@9.1-1
  From: coreutils@9.1-1

✗ Low severity vulnerability found in coreutils
  Description: Race Condition
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-COREUTILS-1543947
  Introduced through: coreutils@9.1-1
  From: coreutils@9.1-1

✗ Low severity vulnerability found in apt/libapt-pkg6.0
  Description: Improper Verification of Cryptographic Signature
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-APT-1541449
  Introduced through: apt/libapt-pkg6.0@2.6.1, apt@2.6.1
  From: apt/libapt-pkg6.0@2.6.1
  From: apt@2.6.1 > apt/libapt-pkg6.0@2.6.1
  From: apt@2.6.1

✗ Critical severity vulnerability found in zlib/zlib1g
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN12-ZLIB-6008963
  Introduced through: zlib/zlib1g@1:1.2.13.dfsg-1, util-linux@2.38.1-5+deb12u1, apt@2.6.1, dash@0.5.12-2
  From: zlib/zlib1g@1:1.2.13.dfsg-1
  From: util-linux@2.38.1-5+deb12u1 > zlib/zlib1g@1:1.2.13.dfsg-1
  From: apt@2.6.1 > apt/libapt-pkg6.0@2.6.1 > zlib/zlib1g@1:1.2.13.dfsg-1
  and 2 more...



Organization:      bhavdeep1304
Package manager:   deb
Project name:      docker-image|redis
Docker image:      redis:7.0
Platform:          linux/amd64
Licenses:          enabled

Tested 89 dependencies for known issues, found 37 issues.

Snyk wasn’t able to auto detect the base image, use `--file` option to get base image remediation advice.
Example: $ snyk container test redis:7.0 --file=path/to/Dockerfile

To remove this message in the future, please run `snyk config set disableSuggestions=true`

-------------------------------------------------------

Testing redis:7.0...

Organization:      bhavdeep1304
Package manager:   gomodules
Target file:       /usr/local/bin/gosu
Project name:      github.com/tianon/gosu
Docker image:      redis:7.0
Licenses:          enabled

✔ Tested 2 dependencies for known issues, no vulnerable paths found.


Tested 2 projects, 1 contained vulnerable paths.



```
