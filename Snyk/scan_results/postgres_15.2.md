**Scanning postgres:15.2**
```

Testing postgres:15.2...

✗ Low severity vulnerability found in util-linux/libblkid1
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-UTILLINUX-2401081
  Introduced through: util-linux/libblkid1@2.36.1-8+deb11u1, e2fsprogs@1.46.2-2, util-linux/libmount1@2.36.1-8+deb11u1, util-linux/mount@2.36.1-8+deb11u1, postgresql-15@15.2-1.pgdg110+1, util-linux@2.36.1-8+deb11u1, util-linux/bsdutils@1:2.36.1-8+deb11u1, util-linux/libsmartcols1@2.36.1-8+deb11u1
  From: util-linux/libblkid1@2.36.1-8+deb11u1
  From: e2fsprogs@1.46.2-2 > util-linux/libblkid1@2.36.1-8+deb11u1
  From: util-linux/libmount1@2.36.1-8+deb11u1 > util-linux/libblkid1@2.36.1-8+deb11u1
  and 15 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in util-linux/libblkid1
  Description: CVE-2024-28085
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-UTILLINUX-6508632
  Introduced through: util-linux/libblkid1@2.36.1-8+deb11u1, e2fsprogs@1.46.2-2, util-linux/libmount1@2.36.1-8+deb11u1, util-linux/mount@2.36.1-8+deb11u1, postgresql-15@15.2-1.pgdg110+1, util-linux@2.36.1-8+deb11u1, util-linux/bsdutils@1:2.36.1-8+deb11u1, util-linux/libsmartcols1@2.36.1-8+deb11u1
  From: util-linux/libblkid1@2.36.1-8+deb11u1
  From: e2fsprogs@1.46.2-2 > util-linux/libblkid1@2.36.1-8+deb11u1
  From: util-linux/libmount1@2.36.1-8+deb11u1 > util-linux/libblkid1@2.36.1-8+deb11u1
  and 15 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 2.36.1-8+deb11u2

✗ Low severity vulnerability found in tar
  Description: CVE-2005-2541
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TAR-523480
  Introduced through: tar@1.34+dfsg-1
  From: tar@1.34+dfsg-1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in tar
  Description: CVE-2023-39804
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TAR-6120424
  Introduced through: tar@1.34+dfsg-1
  From: tar@1.34+dfsg-1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 1.34+dfsg-1+deb11u1

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Authentication Bypass
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-1291054
  Introduced through: apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, postgresql-15@15.2-1.pgdg110+1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7+deb11u2
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7+deb11u2
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > systemd/libsystemd0@247.3-7+deb11u2
  and 5 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Link Following
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-524969
  Introduced through: apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, postgresql-15@15.2-1.pgdg110+1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7+deb11u2
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7+deb11u2
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > systemd/libsystemd0@247.3-7+deb11u2
  and 5 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Improper Validation of Integrity Check Value
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-5733387
  Introduced through: apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, postgresql-15@15.2-1.pgdg110+1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7+deb11u2
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7+deb11u2
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > systemd/libsystemd0@247.3-7+deb11u2
  and 5 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Improper Validation of Integrity Check Value
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-5733391
  Introduced through: apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, postgresql-15@15.2-1.pgdg110+1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7+deb11u2
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7+deb11u2
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > systemd/libsystemd0@247.3-7+deb11u2
  and 5 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: Improper Validation of Integrity Check Value
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-5733392
  Introduced through: apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, postgresql-15@15.2-1.pgdg110+1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7+deb11u2
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7+deb11u2
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > systemd/libsystemd0@247.3-7+deb11u2
  and 5 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: CVE-2023-7008
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-6137713
  Introduced through: apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, postgresql-15@15.2-1.pgdg110+1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7+deb11u2
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7+deb11u2
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > systemd/libsystemd0@247.3-7+deb11u2
  and 5 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in systemd/libsystemd0
  Description: CVE-2023-50868
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-6277512
  Introduced through: apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, postgresql-15@15.2-1.pgdg110+1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7+deb11u2
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7+deb11u2
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > systemd/libsystemd0@247.3-7+deb11u2
  and 5 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in sqlite3/libsqlite3-0
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SQLITE3-1569419
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/gpg@2.2.27-2+deb11u2 > sqlite3/libsqlite3-0@3.34.1-3
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in sqlite3/libsqlite3-0
  Description: Memory Leak
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SQLITE3-2407045
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/gpg@2.2.27-2+deb11u2 > sqlite3/libsqlite3-0@3.34.1-3
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in sqlite3/libsqlite3-0
  Description: Improper Validation of Array Index
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SQLITE3-2959400
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/gpg@2.2.27-2+deb11u2 > sqlite3/libsqlite3-0@3.34.1-3
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in sqlite3/libsqlite3-0
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SQLITE3-5562381
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/gpg@2.2.27-2+deb11u2 > sqlite3/libsqlite3-0@3.34.1-3
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in sqlite3/libsqlite3-0
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SQLITE3-6139925
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/gpg@2.2.27-2+deb11u2 > sqlite3/libsqlite3-0@3.34.1-3
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in shadow/passwd
  Description: Access Restriction Bypass
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SHADOW-526940
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2, shadow/login@1:4.8.1-1, util-linux/mount@2.36.1-8+deb11u1
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1
  From: shadow/login@1:4.8.1-1
  From: util-linux/mount@2.36.1-8+deb11u1 > util-linux@2.36.1-8+deb11u1 > shadow/login@1:4.8.1-1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in shadow/passwd
  Description: Time-of-check Time-of-use (TOCTOU)
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SHADOW-528840
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2, shadow/login@1:4.8.1-1, util-linux/mount@2.36.1-8+deb11u1
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1
  From: shadow/login@1:4.8.1-1
  From: util-linux/mount@2.36.1-8+deb11u1 > util-linux@2.36.1-8+deb11u1 > shadow/login@1:4.8.1-1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in shadow/passwd
  Description: Incorrect Permission Assignment for Critical Resource
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SHADOW-539870
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2, shadow/login@1:4.8.1-1, util-linux/mount@2.36.1-8+deb11u1
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1
  From: shadow/login@1:4.8.1-1
  From: util-linux/mount@2.36.1-8+deb11u1 > util-linux@2.36.1-8+deb11u1 > shadow/login@1:4.8.1-1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in shadow/passwd
  Description: Arbitrary Code Injection
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SHADOW-5423922
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2, shadow/login@1:4.8.1-1, util-linux/mount@2.36.1-8+deb11u1
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1
  From: shadow/login@1:4.8.1-1
  From: util-linux/mount@2.36.1-8+deb11u1 > util-linux@2.36.1-8+deb11u1 > shadow/login@1:4.8.1-1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in shadow/passwd
  Description: Improper Authentication
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SHADOW-5879152
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2, shadow/login@1:4.8.1-1, util-linux/mount@2.36.1-8+deb11u1
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1
  From: shadow/login@1:4.8.1-1
  From: util-linux/mount@2.36.1-8+deb11u1 > util-linux@2.36.1-8+deb11u1 > shadow/login@1:4.8.1-1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in perl/libperl5.32
  Description: Improper Verification of Cryptographic Signature
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PERL-1925976
  Introduced through: perl/libperl5.32@5.32.1-4+deb11u2, perl@5.32.1-4+deb11u2, perl/perl-modules-5.32@5.32.1-4+deb11u2, perl/perl-base@5.32.1-4+deb11u2
  From: perl/libperl5.32@5.32.1-4+deb11u2
  From: perl@5.32.1-4+deb11u2 > perl/libperl5.32@5.32.1-4+deb11u2
  From: perl/perl-modules-5.32@5.32.1-4+deb11u2
  and 4 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in perl/libperl5.32
  Description: Link Following
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PERL-532614
  Introduced through: perl/libperl5.32@5.32.1-4+deb11u2, perl@5.32.1-4+deb11u2, perl/perl-modules-5.32@5.32.1-4+deb11u2, perl/perl-base@5.32.1-4+deb11u2
  From: perl/libperl5.32@5.32.1-4+deb11u2
  From: perl@5.32.1-4+deb11u2 > perl/libperl5.32@5.32.1-4+deb11u2
  From: perl/perl-modules-5.32@5.32.1-4+deb11u2
  and 4 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in perl/libperl5.32
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PERL-5489185
  Introduced through: perl/libperl5.32@5.32.1-4+deb11u2, perl@5.32.1-4+deb11u2, perl/perl-modules-5.32@5.32.1-4+deb11u2, perl/perl-base@5.32.1-4+deb11u2
  From: perl/libperl5.32@5.32.1-4+deb11u2
  From: perl@5.32.1-4+deb11u2 > perl/libperl5.32@5.32.1-4+deb11u2
  From: perl/perl-modules-5.32@5.32.1-4+deb11u2
  and 4 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in perl/libperl5.32
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PERL-5489191
  Introduced through: perl/libperl5.32@5.32.1-4+deb11u2, perl@5.32.1-4+deb11u2, perl/perl-modules-5.32@5.32.1-4+deb11u2, perl/perl-base@5.32.1-4+deb11u2
  From: perl/libperl5.32@5.32.1-4+deb11u2
  From: perl@5.32.1-4+deb11u2 > perl/libperl5.32@5.32.1-4+deb11u2
  From: perl/perl-modules-5.32@5.32.1-4+deb11u2
  and 4 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in pcre3/libpcre3
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PCRE3-523392
  Introduced through: pcre3/libpcre3@2:8.39-13, grep@3.6-1+deb11u1
  From: pcre3/libpcre3@2:8.39-13
  From: grep@3.6-1+deb11u1 > pcre3/libpcre3@2:8.39-13
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in pcre3/libpcre3
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PCRE3-525075
  Introduced through: pcre3/libpcre3@2:8.39-13, grep@3.6-1+deb11u1
  From: pcre3/libpcre3@2:8.39-13
  From: grep@3.6-1+deb11u1 > pcre3/libpcre3@2:8.39-13
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in pcre3/libpcre3
  Description: Uncontrolled Recursion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PCRE3-529298
  Introduced through: pcre3/libpcre3@2:8.39-13, grep@3.6-1+deb11u1
  From: pcre3/libpcre3@2:8.39-13
  From: grep@3.6-1+deb11u1 > pcre3/libpcre3@2:8.39-13
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in pcre3/libpcre3
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PCRE3-529490
  Introduced through: pcre3/libpcre3@2:8.39-13, grep@3.6-1+deb11u1
  From: pcre3/libpcre3@2:8.39-13
  From: grep@3.6-1+deb11u1 > pcre3/libpcre3@2:8.39-13
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in pcre3/libpcre3
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PCRE3-572353
  Introduced through: pcre3/libpcre3@2:8.39-13, grep@3.6-1+deb11u1
  From: pcre3/libpcre3@2:8.39-13
  From: grep@3.6-1+deb11u1 > pcre3/libpcre3@2:8.39-13
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in pcre2/libpcre2-8-0
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PCRE2-5788325
  Introduced through: pcre2/libpcre2-8-0@10.36-2+deb11u1
  From: pcre2/libpcre2-8-0@10.36-2+deb11u1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in pam/libpam0g
  Description: CVE-2024-22365
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PAM-6178915
  Introduced through: postgresql-15@15.2-1.pgdg110+1, shadow/login@1:4.8.1-1, util-linux/mount@2.36.1-8+deb11u1, gnupg2/gnupg@2.2.27-2+deb11u2, pam/libpam-runtime@1.4.0-9+deb11u1
  From: postgresql-15@15.2-1.pgdg110+1 > pam/libpam0g@1.4.0-9+deb11u1
  From: shadow/login@1:4.8.1-1 > pam/libpam0g@1.4.0-9+deb11u1
  From: util-linux/mount@2.36.1-8+deb11u1 > util-linux@2.36.1-8+deb11u1 > pam/libpam0g@1.4.0-9+deb11u1
  and 9 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in openssl/libssl1.1
  Description: Improper Check for Unusual or Exceptional Conditions
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-6048819
  Introduced through: postgresql-15@15.2-1.pgdg110+1, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in openssl/libssl1.1
  Description: CVE-2024-0727
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-6190224
  Introduced through: postgresql-15@15.2-1.pgdg110+1, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in openssl/libssl1.1
  Description: CVE-2024-2511
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-6592093
  Introduced through: postgresql-15@15.2-1.pgdg110+1, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in openssl/libssl1.1
  Description: CVE-2024-4741
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-7151355
  Introduced through: postgresql-15@15.2-1.pgdg110+1, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in openssl/libssl1.1
  Description: CVE-2024-5535
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-7411351
  Introduced through: postgresql-15@15.2-1.pgdg110+1, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in openldap/libldap-2.4-2
  Description: Improper Initialization
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENLDAP-521320
  Introduced through: postgresql-15@15.2-1.pgdg110+1, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in openldap/libldap-2.4-2
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENLDAP-531344
  Introduced through: postgresql-15@15.2-1.pgdg110+1, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in openldap/libldap-2.4-2
  Description: Cryptographic Issues
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENLDAP-531747
  Introduced through: postgresql-15@15.2-1.pgdg110+1, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in openldap/libldap-2.4-2
  Description: NULL Pointer Dereference
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENLDAP-5660622
  Introduced through: postgresql-15@15.2-1.pgdg110+1, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in openldap/libldap-2.4-2
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENLDAP-584937
  Introduced through: postgresql-15@15.2-1.pgdg110+1, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in ncurses/libtinfo6
  Description: CVE-2023-50495
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-NCURSES-6123820
  Introduced through: bash@5.1-2+deb11u1, ncurses/ncurses-bin@6.2+20201114-2+deb11u1, postgresql-15@15.2-1.pgdg110+1, util-linux/mount@2.36.1-8+deb11u1, gnupg2/gnupg@2.2.27-2+deb11u2, ncurses/ncurses-base@6.2+20201114-2+deb11u1
  From: bash@5.1-2+deb11u1 > ncurses/libtinfo6@6.2+20201114-2+deb11u1
  From: ncurses/ncurses-bin@6.2+20201114-2+deb11u1 > ncurses/libtinfo6@6.2+20201114-2+deb11u1
  From: postgresql-15@15.2-1.pgdg110+1 > llvm-toolchain-11/libllvm11@1:11.0.1-2 > ncurses/libtinfo6@6.2+20201114-2+deb11u1
  and 8 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in ncurses/libtinfo6
  Description: CVE-2023-45918
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-NCURSES-6252771
  Introduced through: bash@5.1-2+deb11u1, ncurses/ncurses-bin@6.2+20201114-2+deb11u1, postgresql-15@15.2-1.pgdg110+1, util-linux/mount@2.36.1-8+deb11u1, gnupg2/gnupg@2.2.27-2+deb11u2, ncurses/ncurses-base@6.2+20201114-2+deb11u1
  From: bash@5.1-2+deb11u1 > ncurses/libtinfo6@6.2+20201114-2+deb11u1
  From: ncurses/ncurses-bin@6.2+20201114-2+deb11u1 > ncurses/libtinfo6@6.2+20201114-2+deb11u1
  From: postgresql-15@15.2-1.pgdg110+1 > llvm-toolchain-11/libllvm11@1:11.0.1-2 > ncurses/libtinfo6@6.2+20201114-2+deb11u1
  and 8 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in libzstd/libzstd1
  Description: Resource Exhaustion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBZSTD-5406388
  Introduced through: postgresql-15@15.2-1.pgdg110+1, apt@2.2.4, libzstd/zstd@1.4.8+dfsg-2.1
  From: postgresql-15@15.2-1.pgdg110+1 > libzstd/libzstd1@1.4.8+dfsg-2.1
  From: postgresql-15@15.2-1.pgdg110+1 > systemd/libsystemd0@247.3-7+deb11u2 > libzstd/libzstd1@1.4.8+dfsg-2.1
  From: apt@2.2.4 > apt/libapt-pkg6.0@2.2.4 > libzstd/libzstd1@1.4.8+dfsg-2.1
  and 2 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in libxslt/libxslt1.1
  Description: Use of Insufficiently Random Values
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBXSLT-514942
  Introduced through: postgresql-15@15.2-1.pgdg110+1
  From: postgresql-15@15.2-1.pgdg110+1 > libxslt/libxslt1.1@1.1.34-4+deb11u1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in libxml2
  Description: Cross-site Scripting (XSS)
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBXML2-2964223
  Introduced through: postgresql-15@15.2-1.pgdg110+1
  From: postgresql-15@15.2-1.pgdg110+1 > libxml2@2.9.10+dfsg-6.7+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > libxslt/libxslt1.1@1.1.34-4+deb11u1 > libxml2@2.9.10+dfsg-6.7+deb11u4
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in libxml2
  Description: NULL Pointer Dereference
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBXML2-5747746
  Introduced through: postgresql-15@15.2-1.pgdg110+1
  From: postgresql-15@15.2-1.pgdg110+1 > libxml2@2.9.10+dfsg-6.7+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > libxslt/libxslt1.1@1.1.34-4+deb11u1 > libxml2@2.9.10+dfsg-6.7+deb11u4
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in libxml2
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBXML2-5871334
  Introduced through: postgresql-15@15.2-1.pgdg110+1
  From: postgresql-15@15.2-1.pgdg110+1 > libxml2@2.9.10+dfsg-6.7+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > libxslt/libxslt1.1@1.1.34-4+deb11u1 > libxml2@2.9.10+dfsg-6.7+deb11u4
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in libxml2
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBXML2-5947664
  Introduced through: postgresql-15@15.2-1.pgdg110+1
  From: postgresql-15@15.2-1.pgdg110+1 > libxml2@2.9.10+dfsg-6.7+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > libxslt/libxslt1.1@1.1.34-4+deb11u1 > libxml2@2.9.10+dfsg-6.7+deb11u4
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in libxml2
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBXML2-6227804
  Introduced through: postgresql-15@15.2-1.pgdg110+1
  From: postgresql-15@15.2-1.pgdg110+1 > libxml2@2.9.10+dfsg-6.7+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > libxslt/libxslt1.1@1.1.34-4+deb11u1 > libxml2@2.9.10+dfsg-6.7+deb11u4
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in libxml2
  Description: CVE-2024-34459
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBXML2-6839381
  Introduced through: postgresql-15@15.2-1.pgdg110+1
  From: postgresql-15@15.2-1.pgdg110+1 > libxml2@2.9.10+dfsg-6.7+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > libxslt/libxslt1.1@1.1.34-4+deb11u1 > libxml2@2.9.10+dfsg-6.7+deb11u4
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in libsepol/libsepol1
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBSEPOL-1315627
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1 > libsemanage/libsemanage1@3.1-1+b2 > libsepol/libsepol1@3.1-1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in libsepol/libsepol1
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBSEPOL-1315629
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1 > libsemanage/libsemanage1@3.1-1+b2 > libsepol/libsepol1@3.1-1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in libsepol/libsepol1
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBSEPOL-1315635
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1 > libsemanage/libsemanage1@3.1-1+b2 > libsepol/libsepol1@3.1-1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in libsepol/libsepol1
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBSEPOL-1315641
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1 > libsemanage/libsemanage1@3.1-1+b2 > libsepol/libsepol1@3.1-1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in libgcrypt20
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBGCRYPT20-1297892
  Introduced through: postgresql-15@15.2-1.pgdg110+1, apt@2.2.4, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > systemd/libsystemd0@247.3-7+deb11u2 > libgcrypt20@1.8.7-6
  From: apt@2.2.4 > apt/libapt-pkg6.0@2.2.4 > libgcrypt20@1.8.7-6
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/gpgv@2.2.27-2+deb11u2 > libgcrypt20@1.8.7-6
  and 9 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in libgcrypt20
  Description: Use of a Broken or Risky Cryptographic Algorithm
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBGCRYPT20-523947
  Introduced through: postgresql-15@15.2-1.pgdg110+1, apt@2.2.4, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > systemd/libsystemd0@247.3-7+deb11u2 > libgcrypt20@1.8.7-6
  From: apt@2.2.4 > apt/libapt-pkg6.0@2.2.4 > libgcrypt20@1.8.7-6
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/gpgv@2.2.27-2+deb11u2 > libgcrypt20@1.8.7-6
  and 9 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in libgcrypt20
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-LIBGCRYPT20-6405987
  Introduced through: postgresql-15@15.2-1.pgdg110+1, apt@2.2.4, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > systemd/libsystemd0@247.3-7+deb11u2 > libgcrypt20@1.8.7-6
  From: apt@2.2.4 > apt/libapt-pkg6.0@2.2.4 > libgcrypt20@1.8.7-6
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/gpgv@2.2.27-2+deb11u2 > libgcrypt20@1.8.7-6
  and 9 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in krb5/libkrb5-3
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-KRB5-524883
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2, postgresql-15@15.2-1.pgdg110+1, krb5/libk5crypto3@1.18.3-6+deb11u3, krb5/libkrb5support0@1.18.3-6+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1 > pam/libpam-modules@1.4.0-9+deb11u1 > libnsl/libnsl2@1.3.0-2 > libtirpc/libtirpc3@1.3.1-1+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3 > krb5/libkrb5-3@1.18.3-6+deb11u3
  From: postgresql-15@15.2-1.pgdg110+1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in krb5/libkrb5-3
  Description: CVE-2024-26462
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-KRB5-6277413
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2, postgresql-15@15.2-1.pgdg110+1, krb5/libk5crypto3@1.18.3-6+deb11u3, krb5/libkrb5support0@1.18.3-6+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1 > pam/libpam-modules@1.4.0-9+deb11u1 > libnsl/libnsl2@1.3.0-2 > libtirpc/libtirpc3@1.3.1-1+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3 > krb5/libkrb5-3@1.18.3-6+deb11u3
  From: postgresql-15@15.2-1.pgdg110+1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in krb5/libkrb5-3
  Description: CVE-2024-26461
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-KRB5-6277418
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2, postgresql-15@15.2-1.pgdg110+1, krb5/libk5crypto3@1.18.3-6+deb11u3, krb5/libkrb5support0@1.18.3-6+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1 > pam/libpam-modules@1.4.0-9+deb11u1 > libnsl/libnsl2@1.3.0-2 > libtirpc/libtirpc3@1.3.1-1+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3 > krb5/libkrb5-3@1.18.3-6+deb11u3
  From: postgresql-15@15.2-1.pgdg110+1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in krb5/libkrb5-3
  Description: CVE-2024-26458
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-KRB5-6277420
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2, postgresql-15@15.2-1.pgdg110+1, krb5/libk5crypto3@1.18.3-6+deb11u3, krb5/libkrb5support0@1.18.3-6+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1 > pam/libpam-modules@1.4.0-9+deb11u1 > libnsl/libnsl2@1.3.0-2 > libtirpc/libtirpc3@1.3.1-1+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3 > krb5/libkrb5-3@1.18.3-6+deb11u3
  From: postgresql-15@15.2-1.pgdg110+1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in krb5/libkrb5-3
  Description: CVE-2024-37371
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-KRB5-7411316
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2, postgresql-15@15.2-1.pgdg110+1, krb5/libk5crypto3@1.18.3-6+deb11u3, krb5/libkrb5support0@1.18.3-6+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1 > pam/libpam-modules@1.4.0-9+deb11u1 > libnsl/libnsl2@1.3.0-2 > libtirpc/libtirpc3@1.3.1-1+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3 > krb5/libkrb5-3@1.18.3-6+deb11u3
  From: postgresql-15@15.2-1.pgdg110+1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 1.18.3-6+deb11u5

✗ Low severity vulnerability found in krb5/libkrb5-3
  Description: CVE-2024-37370
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-KRB5-7411320
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2, postgresql-15@15.2-1.pgdg110+1, krb5/libk5crypto3@1.18.3-6+deb11u3, krb5/libkrb5support0@1.18.3-6+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1 > pam/libpam-modules@1.4.0-9+deb11u1 > libnsl/libnsl2@1.3.0-2 > libtirpc/libtirpc3@1.3.1-1+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3 > krb5/libkrb5-3@1.18.3-6+deb11u3
  From: postgresql-15@15.2-1.pgdg110+1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 1.18.3-6+deb11u5

✗ Low severity vulnerability found in gnutls28/libgnutls30
  Description: Improper Input Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUTLS28-515971
  Introduced through: apt@2.2.4, gnupg2/gnupg@2.2.27-2+deb11u2
  From: apt@2.2.4 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in gnutls28/libgnutls30
  Description: Uncaught Exception
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUTLS28-6474582
  Introduced through: apt@2.2.4, gnupg2/gnupg@2.2.27-2+deb11u2
  From: apt@2.2.4 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in gnutls28/libgnutls30
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUTLS28-6474587
  Introduced through: apt@2.2.4, gnupg2/gnupg@2.2.27-2+deb11u2
  From: apt@2.2.4 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in gnupg2/gpgv
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUPG2-3330745
  Introduced through: apt@2.2.4, gnupg2/gnupg@2.2.27-2+deb11u2
  From: apt@2.2.4 > gnupg2/gpgv@2.2.27-2+deb11u2
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/gpgv@2.2.27-2+deb11u2
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > gnupg2/gpgconf@2.2.27-2+deb11u2
  and 17 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in glibc/libc6
  Description: Out-of-Bounds
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-521063
  Introduced through: glibc/libc6@2.31-13+deb11u6, glibc/locales@2.31-13+deb11u6, postgresql-15@15.2-1.pgdg110+1
  From: glibc/libc6@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-bin@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-l10n@2.31-13+deb11u6
  and 2 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in glibc/libc6
  Description: Uncontrolled Recursion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-521199
  Introduced through: glibc/libc6@2.31-13+deb11u6, glibc/locales@2.31-13+deb11u6, postgresql-15@15.2-1.pgdg110+1
  From: glibc/libc6@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-bin@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-l10n@2.31-13+deb11u6
  and 2 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in glibc/libc6
  Description: Use of Insufficiently Random Values
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-522385
  Introduced through: glibc/libc6@2.31-13+deb11u6, glibc/locales@2.31-13+deb11u6, postgresql-15@15.2-1.pgdg110+1
  From: glibc/libc6@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-bin@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-l10n@2.31-13+deb11u6
  and 2 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in glibc/libc6
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-529848
  Introduced through: glibc/libc6@2.31-13+deb11u6, glibc/locales@2.31-13+deb11u6, postgresql-15@15.2-1.pgdg110+1
  From: glibc/libc6@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-bin@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-l10n@2.31-13+deb11u6
  and 2 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in glibc/libc6
  Description: CVE-2019-1010023
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-531451
  Introduced through: glibc/libc6@2.31-13+deb11u6, glibc/locales@2.31-13+deb11u6, postgresql-15@15.2-1.pgdg110+1
  From: glibc/libc6@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-bin@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-l10n@2.31-13+deb11u6
  and 2 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in glibc/libc6
  Description: Uncontrolled Recursion
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-531492
  Introduced through: glibc/libc6@2.31-13+deb11u6, glibc/locales@2.31-13+deb11u6, postgresql-15@15.2-1.pgdg110+1
  From: glibc/libc6@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-bin@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-l10n@2.31-13+deb11u6
  and 2 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in glibc/libc6
  Description: Resource Management Errors
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-532215
  Introduced through: glibc/libc6@2.31-13+deb11u6, glibc/locales@2.31-13+deb11u6, postgresql-15@15.2-1.pgdg110+1
  From: glibc/libc6@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-bin@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-l10n@2.31-13+deb11u6
  and 2 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in glibc/libc6
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-5894105
  Introduced through: glibc/libc6@2.31-13+deb11u6, glibc/locales@2.31-13+deb11u6, postgresql-15@15.2-1.pgdg110+1
  From: glibc/libc6@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-bin@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-l10n@2.31-13+deb11u6
  and 2 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in glibc/libc6
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-5894112
  Introduced through: glibc/libc6@2.31-13+deb11u6, glibc/locales@2.31-13+deb11u6, postgresql-15@15.2-1.pgdg110+1
  From: glibc/libc6@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-bin@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-l10n@2.31-13+deb11u6
  and 2 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in glibc/libc6
  Description: CVE-2024-2961
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-6617104
  Introduced through: glibc/libc6@2.31-13+deb11u6, glibc/locales@2.31-13+deb11u6, postgresql-15@15.2-1.pgdg110+1
  From: glibc/libc6@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-bin@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-l10n@2.31-13+deb11u6
  and 2 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 2.31-13+deb11u9

✗ Low severity vulnerability found in glibc/libc6
  Description: CVE-2024-33599
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-6673955
  Introduced through: glibc/libc6@2.31-13+deb11u6, glibc/locales@2.31-13+deb11u6, postgresql-15@15.2-1.pgdg110+1
  From: glibc/libc6@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-bin@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-l10n@2.31-13+deb11u6
  and 2 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 2.31-13+deb11u10

✗ Low severity vulnerability found in glibc/libc6
  Description: CVE-2024-33601
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-6673958
  Introduced through: glibc/libc6@2.31-13+deb11u6, glibc/locales@2.31-13+deb11u6, postgresql-15@15.2-1.pgdg110+1
  From: glibc/libc6@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-bin@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-l10n@2.31-13+deb11u6
  and 2 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 2.31-13+deb11u10

✗ Low severity vulnerability found in glibc/libc6
  Description: CVE-2024-33600
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-6673967
  Introduced through: glibc/libc6@2.31-13+deb11u6, glibc/locales@2.31-13+deb11u6, postgresql-15@15.2-1.pgdg110+1
  From: glibc/libc6@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-bin@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-l10n@2.31-13+deb11u6
  and 2 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 2.31-13+deb11u10

✗ Low severity vulnerability found in glibc/libc6
  Description: CVE-2024-33602
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-6673973
  Introduced through: glibc/libc6@2.31-13+deb11u6, glibc/locales@2.31-13+deb11u6, postgresql-15@15.2-1.pgdg110+1
  From: glibc/libc6@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-bin@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-l10n@2.31-13+deb11u6
  and 2 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 2.31-13+deb11u10

✗ Low severity vulnerability found in gcc-9/gcc-9-base
  Description: CVE-2023-4039
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GCC9-5901306
  Introduced through: gcc-9/gcc-9-base@9.3.0-22
  From: gcc-9/gcc-9-base@9.3.0-22
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in gcc-10/libstdc++6
  Description: CVE-2023-4039
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GCC10-5901313
  Introduced through: apt@2.2.4, libzstd/zstd@1.4.8+dfsg-2.1, postgresql-15@15.2-1.pgdg110+1, gcc-10/gcc-10-base@10.2.1-6, gcc-10/libgcc-s1@10.2.1-6
  From: apt@2.2.4 > gcc-10/libstdc++6@10.2.1-6
  From: libzstd/zstd@1.4.8+dfsg-2.1 > gcc-10/libstdc++6@10.2.1-6
  From: postgresql-15@15.2-1.pgdg110+1 > gcc-10/libstdc++6@10.2.1-6
  and 6 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in e2fsprogs/libext2fs2
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-E2FSPROGS-2628459
  Introduced through: e2fsprogs/libext2fs2@1.46.2-2, e2fsprogs@1.46.2-2, e2fsprogs/libss2@1.46.2-2, e2fsprogs/logsave@1.46.2-2, e2fsprogs/libcom-err2@1.46.2-2
  From: e2fsprogs/libext2fs2@1.46.2-2
  From: e2fsprogs@1.46.2-2 > e2fsprogs/libext2fs2@1.46.2-2
  From: e2fsprogs/libss2@1.46.2-2
  and 5 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in db5.3/libdb5.3
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-DB53-2825168
  Introduced through: perl/libperl5.32@5.32.1-4+deb11u2, gnupg2/gnupg@2.2.27-2+deb11u2
  From: perl/libperl5.32@5.32.1-4+deb11u2 > db5.3/libdb5.3@5.3.28+dfsg1-0.8
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1 > pam/libpam-modules@1.4.0-9+deb11u1 > db5.3/libdb5.3@5.3.28+dfsg1-0.8
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > cyrus-sasl2/libsasl2-2@2.1.27+dfsg-2.1+deb11u1 > cyrus-sasl2/libsasl2-modules-db@2.1.27+dfsg-2.1+deb11u1 > db5.3/libdb5.3@5.3.28+dfsg1-0.8
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in coreutils/coreutils
  Description: Improper Input Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-COREUTILS-514776
  Introduced through: postgresql-15@15.2-1.pgdg110+1
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-common@248.pgdg110+1 > ucf@3.0043 > coreutils/coreutils@8.32-4+b1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in coreutils/coreutils
  Description: Race Condition
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-COREUTILS-527269
  Introduced through: postgresql-15@15.2-1.pgdg110+1
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-common@248.pgdg110+1 > ucf@3.0043 > coreutils/coreutils@8.32-4+b1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in bash
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-BASH-3112361
  Introduced through: bash@5.1-2+deb11u1
  From: bash@5.1-2+deb11u1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Low severity vulnerability found in apt/libapt-pkg6.0
  Description: Improper Verification of Cryptographic Signature
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-APT-522585
  Introduced through: apt/libapt-pkg6.0@2.2.4, apt@2.2.4
  From: apt/libapt-pkg6.0@2.2.4
  From: apt@2.2.4 > apt/libapt-pkg6.0@2.2.4
  From: apt@2.2.4
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ Medium severity vulnerability found in tar
  Description: Out-of-bounds Read
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-TAR-3253527
  Introduced through: tar@1.34+dfsg-1
  From: tar@1.34+dfsg-1
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 1.34+dfsg-1+deb11u1

✗ Medium severity vulnerability found in openssl/libssl1.1
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-5291773
  Introduced through: postgresql-15@15.2-1.pgdg110+1, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 1.1.1n-0+deb11u5

✗ Medium severity vulnerability found in openssl/libssl1.1
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-5291777
  Introduced through: postgresql-15@15.2-1.pgdg110+1, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 1.1.1n-0+deb11u5

✗ Medium severity vulnerability found in openssl/libssl1.1
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-5661566
  Introduced through: postgresql-15@15.2-1.pgdg110+1, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 1.1.1n-0+deb11u5

✗ Medium severity vulnerability found in openssl/libssl1.1
  Description: Inefficient Regular Expression Complexity
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-5788324
  Introduced through: postgresql-15@15.2-1.pgdg110+1, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 1.1.1v-0~deb11u1

✗ Medium severity vulnerability found in openssl/libssl1.1
  Description: Excessive Iteration
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-5812634
  Introduced through: postgresql-15@15.2-1.pgdg110+1, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 1.1.1v-0~deb11u1

✗ Medium severity vulnerability found in krb5/libkrb5-3
  Description: Access of Uninitialized Pointer
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-KRB5-5825661
  Introduced through: gnupg2/gnupg@2.2.27-2+deb11u2, postgresql-15@15.2-1.pgdg110+1, krb5/libk5crypto3@1.18.3-6+deb11u3, krb5/libkrb5support0@1.18.3-6+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > adduser@3.118 > shadow/passwd@1:4.8.1-1 > pam/libpam-modules@1.4.0-9+deb11u1 > libnsl/libnsl2@1.3.0-2 > libtirpc/libtirpc3@1.3.1-1+deb11u1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3 > krb5/libkrb5-3@1.18.3-6+deb11u3
  From: postgresql-15@15.2-1.pgdg110+1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > krb5/libgssapi-krb5-2@1.18.3-6+deb11u3
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 1.18.3-6+deb11u4

✗ Medium severity vulnerability found in gnutls28/libgnutls30
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUTLS28-6062102
  Introduced through: apt@2.2.4, gnupg2/gnupg@2.2.27-2+deb11u2
  From: apt@2.2.4 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 3.7.1-5+deb11u4

✗ High severity vulnerability found in systemd/libsystemd0
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-SYSTEMD-6277510
  Introduced through: apt@2.2.4, util-linux/bsdutils@1:2.36.1-8+deb11u1, postgresql-15@15.2-1.pgdg110+1, util-linux/mount@2.36.1-8+deb11u1, systemd/libudev1@247.3-7+deb11u2
  From: apt@2.2.4 > systemd/libsystemd0@247.3-7+deb11u2
  From: util-linux/bsdutils@1:2.36.1-8+deb11u1 > systemd/libsystemd0@247.3-7+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > systemd/libsystemd0@247.3-7+deb11u2
  and 5 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)

✗ High severity vulnerability found in perl/libperl5.32
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-PERL-6085272
  Introduced through: perl/libperl5.32@5.32.1-4+deb11u2, perl@5.32.1-4+deb11u2, perl/perl-modules-5.32@5.32.1-4+deb11u2, perl/perl-base@5.32.1-4+deb11u2
  From: perl/libperl5.32@5.32.1-4+deb11u2
  From: perl@5.32.1-4+deb11u2 > perl/libperl5.32@5.32.1-4+deb11u2
  From: perl/perl-modules-5.32@5.32.1-4+deb11u2
  and 4 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 5.32.1-4+deb11u3

✗ High severity vulnerability found in openssl/libssl1.1
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-OPENSSL-3368735
  Introduced through: postgresql-15@15.2-1.pgdg110+1, gnupg2/gnupg@2.2.27-2+deb11u2
  From: postgresql-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  From: postgresql-15@15.2-1.pgdg110+1 > postgresql-15/postgresql-client-15@15.2-1.pgdg110+1 > postgresql-15/libpq5@15.2-1.pgdg110+1 > openssl/libssl1.1@1.1.1n-0+deb11u4
  and 3 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 1.1.1n-0+deb11u5

✗ High severity vulnerability found in ncurses/libtinfo6
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-NCURSES-5421197
  Introduced through: bash@5.1-2+deb11u1, ncurses/ncurses-bin@6.2+20201114-2+deb11u1, postgresql-15@15.2-1.pgdg110+1, util-linux/mount@2.36.1-8+deb11u1, gnupg2/gnupg@2.2.27-2+deb11u2, ncurses/ncurses-base@6.2+20201114-2+deb11u1
  From: bash@5.1-2+deb11u1 > ncurses/libtinfo6@6.2+20201114-2+deb11u1
  From: ncurses/ncurses-bin@6.2+20201114-2+deb11u1 > ncurses/libtinfo6@6.2+20201114-2+deb11u1
  From: postgresql-15@15.2-1.pgdg110+1 > llvm-toolchain-11/libllvm11@1:11.0.1-2 > ncurses/libtinfo6@6.2+20201114-2+deb11u1
  and 8 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 6.2+20201114-2+deb11u2

✗ High severity vulnerability found in gnutls28/libgnutls30
  Description: Improper Verification of Cryptographic Signature
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUTLS28-6159417
  Introduced through: apt@2.2.4, gnupg2/gnupg@2.2.27-2+deb11u2
  From: apt@2.2.4 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 3.7.1-5+deb11u5

✗ High severity vulnerability found in gnutls28/libgnutls30
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GNUTLS28-6159419
  Introduced through: apt@2.2.4, gnupg2/gnupg@2.2.27-2+deb11u2
  From: apt@2.2.4 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  From: gnupg2/gnupg@2.2.27-2+deb11u2 > gnupg2/dirmngr@2.2.27-2+deb11u2 > openldap/libldap-2.4-2@2.4.57+dfsg-3+deb11u1 > gnutls28/libgnutls30@3.7.1-5+deb11u3
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 3.7.1-5+deb11u5

✗ High severity vulnerability found in glibc/libc6
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-GLIBC-5927133
  Introduced through: glibc/libc6@2.31-13+deb11u6, glibc/locales@2.31-13+deb11u6, postgresql-15@15.2-1.pgdg110+1
  From: glibc/libc6@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-bin@2.31-13+deb11u6
  From: glibc/locales@2.31-13+deb11u6 > glibc/libc-l10n@2.31-13+deb11u6
  and 2 more...
  Image layer: Introduced by your base image (postgres:15.2-bullseye)
  Fixed in: 2.31-13+deb11u7

✗ Critical severity vulnerability found in zlib/zlib1g
  Description: Integer Overflow or Wraparound
  Info: https://security.snyk.io/vuln/SNYK-DEBIAN11-ZLIB-6008961
  Introduced through: zlib/zlib1g@1:1.2.11.dfsg-2+deb11u2
  From: zlib/zlib1g@1:1.2.11.dfsg-2+deb11u2
  Image layer: Introduced by your base image (postgres:15.2-bullseye)



Organization:      bhavdeep1304
Package manager:   deb
Project name:      docker-image|postgres
Docker image:      postgres:15.2
Platform:          linux/amd64
Base image:        postgres:15.2-bullseye
Licenses:          enabled

Tested 146 dependencies for known issues, found 107 issues.

Base Image              Vulnerabilities  Severity
postgres:15.2-bullseye  107              1 critical, 7 high, 8 medium, 91 low

Recommendations for base image upgrade:

Minor upgrades
Base Image              Vulnerabilities  Severity
postgres:15.7-bullseye  93               1 critical, 1 high, 0 medium, 91 low

Major upgrades
Base Image                 Vulnerabilities  Severity
postgres:17beta2-bullseye  93               1 critical, 1 high, 0 medium, 91 low

Alternative image types
Base Image              Vulnerabilities  Severity
postgres:15.7-bookworm  58               1 critical, 0 high, 0 medium, 57 low


Learn more: https://docs.snyk.io/products/snyk-container/getting-around-the-snyk-container-ui/base-image-detection

-------------------------------------------------------

Testing postgres:15.2...

✗ Medium severity vulnerability found in golang.org/x/sys/unix
  Description: Incorrect Privilege Assignment
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXSYSUNIX-3310442
  Introduced through: golang.org/x/sys/unix@v0.0.0-20220907062415-87db552b00fd
  From: golang.org/x/sys/unix@v0.0.0-20220907062415-87db552b00fd
  Fixed in: 0.1.0



Organization:      bhavdeep1304
Package manager:   gomodules
Target file:       /usr/local/bin/gosu
Project name:      github.com/tianon/gosu
Docker image:      postgres:15.2
Licenses:          enabled

Tested 3 dependencies for known issues, found 1 issue.

Snyk wasn’t able to auto detect the base image, use `--file` option to get base image remediation advice.
Example: $ snyk container test postgres:15.2 --file=path/to/Dockerfile

Snyk found some vulnerabilities in your image applications (Snyk searches for these vulnerabilities by default). See https://snyk.co/app-vulns for more information.

To remove these messages in the future, please run `snyk config set disableSuggestions=true`


Tested 2 projects, 2 contained vulnerable paths.



```
