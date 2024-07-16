**Scanning grafana/grafana:9.3.0**
```

Testing grafana/grafana:9.3.0...

✗ Medium severity vulnerability found in openssl/libcrypto1.1
  Description: Information Exposure
  Info: https://security.snyk.io/vuln/SNYK-ALPINE315-OPENSSL-3314628
  Introduced through: openssl/libcrypto1.1@1.1.1q-r0, openssl/libssl1.1@1.1.1q-r0, apk-tools/apk-tools@2.12.7-r3, libretls/libretls@3.3.4-r3, ca-certificates/ca-certificates@20220614-r0
  From: openssl/libcrypto1.1@1.1.1q-r0
  From: openssl/libssl1.1@1.1.1q-r0 > openssl/libcrypto1.1@1.1.1q-r0
  From: apk-tools/apk-tools@2.12.7-r3 > openssl/libcrypto1.1@1.1.1q-r0
  and 5 more...
  Image layer: 'apk add --no-cache ca-certificates bash tzdata musl-utils'
  Fixed in: 1.1.1t-r0

✗ Medium severity vulnerability found in openssl/libcrypto1.1
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-ALPINE315-OPENSSL-5291790
  Introduced through: openssl/libcrypto1.1@1.1.1q-r0, openssl/libssl1.1@1.1.1q-r0, apk-tools/apk-tools@2.12.7-r3, libretls/libretls@3.3.4-r3, ca-certificates/ca-certificates@20220614-r0
  From: openssl/libcrypto1.1@1.1.1q-r0
  From: openssl/libssl1.1@1.1.1q-r0 > openssl/libcrypto1.1@1.1.1q-r0
  From: apk-tools/apk-tools@2.12.7-r3 > openssl/libcrypto1.1@1.1.1q-r0
  and 5 more...
  Image layer: 'apk add --no-cache ca-certificates bash tzdata musl-utils'
  Fixed in: 1.1.1t-r2

✗ Medium severity vulnerability found in openssl/libcrypto1.1
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-ALPINE315-OPENSSL-5661569
  Introduced through: openssl/libcrypto1.1@1.1.1q-r0, openssl/libssl1.1@1.1.1q-r0, apk-tools/apk-tools@2.12.7-r3, libretls/libretls@3.3.4-r3, ca-certificates/ca-certificates@20220614-r0
  From: openssl/libcrypto1.1@1.1.1q-r0
  From: openssl/libssl1.1@1.1.1q-r0 > openssl/libcrypto1.1@1.1.1q-r0
  From: apk-tools/apk-tools@2.12.7-r3 > openssl/libcrypto1.1@1.1.1q-r0
  and 5 more...
  Image layer: 'apk add --no-cache ca-certificates bash tzdata musl-utils'
  Fixed in: 1.1.1u-r0

✗ Medium severity vulnerability found in openssl/libcrypto1.1
  Description: Inefficient Regular Expression Complexity
  Info: https://security.snyk.io/vuln/SNYK-ALPINE315-OPENSSL-5788364
  Introduced through: openssl/libcrypto1.1@1.1.1q-r0, openssl/libssl1.1@1.1.1q-r0, apk-tools/apk-tools@2.12.7-r3, libretls/libretls@3.3.4-r3, ca-certificates/ca-certificates@20220614-r0
  From: openssl/libcrypto1.1@1.1.1q-r0
  From: openssl/libssl1.1@1.1.1q-r0 > openssl/libcrypto1.1@1.1.1q-r0
  From: apk-tools/apk-tools@2.12.7-r3 > openssl/libcrypto1.1@1.1.1q-r0
  and 5 more...
  Image layer: 'apk add --no-cache ca-certificates bash tzdata musl-utils'
  Fixed in: 1.1.1u-r2

✗ Medium severity vulnerability found in openssl/libcrypto1.1
  Description: Excessive Iteration
  Info: https://security.snyk.io/vuln/SNYK-ALPINE315-OPENSSL-5821139
  Introduced through: openssl/libcrypto1.1@1.1.1q-r0, openssl/libssl1.1@1.1.1q-r0, apk-tools/apk-tools@2.12.7-r3, libretls/libretls@3.3.4-r3, ca-certificates/ca-certificates@20220614-r0
  From: openssl/libcrypto1.1@1.1.1q-r0
  From: openssl/libssl1.1@1.1.1q-r0 > openssl/libcrypto1.1@1.1.1q-r0
  From: apk-tools/apk-tools@2.12.7-r3 > openssl/libcrypto1.1@1.1.1q-r0
  and 5 more...
  Image layer: 'apk add --no-cache ca-certificates bash tzdata musl-utils'
  Fixed in: 1.1.1v-r0

✗ Medium severity vulnerability found in openssl/libcrypto1.1
  Description: Improper Check for Unusual or Exceptional Conditions
  Info: https://security.snyk.io/vuln/SNYK-ALPINE315-OPENSSL-6070608
  Introduced through: openssl/libcrypto1.1@1.1.1q-r0, openssl/libssl1.1@1.1.1q-r0, apk-tools/apk-tools@2.12.7-r3, libretls/libretls@3.3.4-r3, ca-certificates/ca-certificates@20220614-r0
  From: openssl/libcrypto1.1@1.1.1q-r0
  From: openssl/libssl1.1@1.1.1q-r0 > openssl/libcrypto1.1@1.1.1q-r0
  From: apk-tools/apk-tools@2.12.7-r3 > openssl/libcrypto1.1@1.1.1q-r0
  and 5 more...
  Image layer: 'apk add --no-cache ca-certificates bash tzdata musl-utils'
  Fixed in: 1.1.1w-r1

✗ High severity vulnerability found in openssl/libcrypto1.1
  Description: Use After Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE315-OPENSSL-3314621
  Introduced through: openssl/libcrypto1.1@1.1.1q-r0, openssl/libssl1.1@1.1.1q-r0, apk-tools/apk-tools@2.12.7-r3, libretls/libretls@3.3.4-r3, ca-certificates/ca-certificates@20220614-r0
  From: openssl/libcrypto1.1@1.1.1q-r0
  From: openssl/libssl1.1@1.1.1q-r0 > openssl/libcrypto1.1@1.1.1q-r0
  From: apk-tools/apk-tools@2.12.7-r3 > openssl/libcrypto1.1@1.1.1q-r0
  and 5 more...
  Image layer: 'apk add --no-cache ca-certificates bash tzdata musl-utils'
  Fixed in: 1.1.1t-r0

✗ High severity vulnerability found in openssl/libcrypto1.1
  Description: Access of Resource Using Incompatible Type ('Type Confusion')
  Info: https://security.snyk.io/vuln/SNYK-ALPINE315-OPENSSL-3314622
  Introduced through: openssl/libcrypto1.1@1.1.1q-r0, openssl/libssl1.1@1.1.1q-r0, apk-tools/apk-tools@2.12.7-r3, libretls/libretls@3.3.4-r3, ca-certificates/ca-certificates@20220614-r0
  From: openssl/libcrypto1.1@1.1.1q-r0
  From: openssl/libssl1.1@1.1.1q-r0 > openssl/libcrypto1.1@1.1.1q-r0
  From: apk-tools/apk-tools@2.12.7-r3 > openssl/libcrypto1.1@1.1.1q-r0
  and 5 more...
  Image layer: 'apk add --no-cache ca-certificates bash tzdata musl-utils'
  Fixed in: 1.1.1t-r0

✗ High severity vulnerability found in openssl/libcrypto1.1
  Description: Double Free
  Info: https://security.snyk.io/vuln/SNYK-ALPINE315-OPENSSL-3314629
  Introduced through: openssl/libcrypto1.1@1.1.1q-r0, openssl/libssl1.1@1.1.1q-r0, apk-tools/apk-tools@2.12.7-r3, libretls/libretls@3.3.4-r3, ca-certificates/ca-certificates@20220614-r0
  From: openssl/libcrypto1.1@1.1.1q-r0
  From: openssl/libssl1.1@1.1.1q-r0 > openssl/libcrypto1.1@1.1.1q-r0
  From: apk-tools/apk-tools@2.12.7-r3 > openssl/libcrypto1.1@1.1.1q-r0
  and 5 more...
  Image layer: 'apk add --no-cache ca-certificates bash tzdata musl-utils'
  Fixed in: 1.1.1t-r0

✗ High severity vulnerability found in openssl/libcrypto1.1
  Description: Improper Certificate Validation
  Info: https://security.snyk.io/vuln/SNYK-ALPINE315-OPENSSL-3368753
  Introduced through: openssl/libcrypto1.1@1.1.1q-r0, openssl/libssl1.1@1.1.1q-r0, apk-tools/apk-tools@2.12.7-r3, libretls/libretls@3.3.4-r3, ca-certificates/ca-certificates@20220614-r0
  From: openssl/libcrypto1.1@1.1.1q-r0
  From: openssl/libssl1.1@1.1.1q-r0 > openssl/libcrypto1.1@1.1.1q-r0
  From: apk-tools/apk-tools@2.12.7-r3 > openssl/libcrypto1.1@1.1.1q-r0
  and 5 more...
  Image layer: 'apk add --no-cache ca-certificates bash tzdata musl-utils'
  Fixed in: 1.1.1t-r2

✗ High severity vulnerability found in ncurses/ncurses-terminfo-base
  Description: Out-of-bounds Write
  Info: https://security.snyk.io/vuln/SNYK-ALPINE315-NCURSES-5606598
  Introduced through: ncurses/ncurses-terminfo-base@6.3_p20211120-r1, ncurses/ncurses-libs@6.3_p20211120-r1, readline/readline@8.1.1-r0
  From: ncurses/ncurses-terminfo-base@6.3_p20211120-r1
  From: ncurses/ncurses-libs@6.3_p20211120-r1 > ncurses/ncurses-terminfo-base@6.3_p20211120-r1
  From: ncurses/ncurses-libs@6.3_p20211120-r1
  and 1 more...
  Image layer: Introduced by your base image (grafana/grafana:9.3.0)
  Fixed in: 6.3_p20211120-r2



Organization:      bhavdeep1304
Package manager:   apk
Project name:      docker-image|grafana/grafana
Docker image:      grafana/grafana:9.3.0
Platform:          linux/amd64
Base image:        grafana/grafana:9.3.0
Licenses:          enabled

Tested 24 dependencies for known issues, found 11 issues.

Base Image             Vulnerabilities  Severity
grafana/grafana:9.3.0  11               0 critical, 5 high, 6 medium, 0 low

Recommendations for base image upgrade:

Minor upgrades
Base Image              Vulnerabilities  Severity
grafana/grafana:9.5.20  8                0 critical, 0 high, 4 medium, 4 low

Major upgrades
Base Image              Vulnerabilities  Severity
grafana/grafana:11.0.1  8                0 critical, 0 high, 4 medium, 4 low

Alpine 3.15.6 is no longer supported by the Alpine maintainers. Vulnerability detection may be affected by a lack of security updates.

Learn more: https://docs.snyk.io/products/snyk-container/getting-around-the-snyk-container-ui/base-image-detection

-------------------------------------------------------

Testing grafana/grafana:9.3.0...

✗ Medium severity vulnerability found in google.golang.org/protobuf/internal/encoding/json
  Description: Infinite loop
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOOGLEGOLANGORGPROTOBUFINTERNALENCODINGJSON-6393704
  Introduced through: google.golang.org/protobuf/internal/encoding/json@v1.28.1
  From: google.golang.org/protobuf/internal/encoding/json@v1.28.1
  Fixed in: 1.33.0

✗ Medium severity vulnerability found in google.golang.org/protobuf/encoding/protojson
  Description: Stack-based Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOOGLEGOLANGORGPROTOBUFENCODINGPROTOJSON-6137908
  Introduced through: google.golang.org/protobuf/encoding/protojson@v1.28.1
  From: google.golang.org/protobuf/encoding/protojson@v1.28.1
  Fixed in: 1.32.0

✗ Medium severity vulnerability found in google.golang.org/protobuf/encoding/protojson
  Description: Infinite loop
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOOGLEGOLANGORGPROTOBUFENCODINGPROTOJSON-6393703
  Introduced through: google.golang.org/protobuf/encoding/protojson@v1.28.1
  From: google.golang.org/protobuf/encoding/protojson@v1.28.1
  Fixed in: 1.33.0

✗ Medium severity vulnerability found in golang.org/x/net/http2
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-3160322
  Introduced through: golang.org/x/net/http2@v0.1.0
  From: golang.org/x/net/http2@v0.1.0
  Fixed in: 0.4.0

✗ Medium severity vulnerability found in golang.org/x/net/http2
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-5958903
  Introduced through: golang.org/x/net/http2@v0.1.0
  From: golang.org/x/net/http2@v0.1.0
  Fixed in: 0.17.0

✗ Medium severity vulnerability found in golang.org/x/crypto/ssh
  Description: Authentication Bypass by Capture-replay
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXCRYPTOSSH-6130669
  Introduced through: golang.org/x/crypto/ssh@v0.0.0-20220622213112-05595931fe9d
  From: golang.org/x/crypto/ssh@v0.0.0-20220622213112-05595931fe9d
  Fixed in: 0.17.0

✗ Medium severity vulnerability found in github.com/prometheus/exporter-toolkit/web
  Description: Incorrect Implementation of Authentication Algorithm
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMPROMETHEUSEXPORTERTOOLKITWEB-3150818
  Introduced through: github.com/prometheus/exporter-toolkit/web@v0.7.1
  From: github.com/prometheus/exporter-toolkit/web@v0.7.1
  Fixed in: 0.7.2, 0.8.2

✗ Medium severity vulnerability found in github.com/go-git/go-git/v5/plumbing
  Description: Uncontrolled Resource Consumption ('Resource Exhaustion')
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMGOGITGOGITV5PLUMBING-6140319
  Introduced through: github.com/go-git/go-git/v5/plumbing@v5.4.2
  From: github.com/go-git/go-git/v5/plumbing@v5.4.2
  Fixed in: 5.11.0

✗ High severity vulnerability found in google.golang.org/grpc
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOOGLEGOLANGORGGRPC-5953328
  Introduced through: google.golang.org/grpc@v1.45.0
  From: google.golang.org/grpc@v1.45.0
  Fixed in: 1.56.3, 1.57.1, 1.58.3

✗ High severity vulnerability found in golang.org/x/net/http2/hpack
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2HPACK-3358253
  Introduced through: golang.org/x/net/http2/hpack@v0.1.0
  From: golang.org/x/net/http2/hpack@v0.1.0
  Fixed in: 0.7.0

✗ High severity vulnerability found in golang.org/x/net/http2
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-3323837
  Introduced through: golang.org/x/net/http2@v0.1.0
  From: golang.org/x/net/http2@v0.1.0
  Fixed in: 0.7.0

✗ High severity vulnerability found in golang.org/x/net/http2
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-5953327
  Introduced through: golang.org/x/net/http2@v0.1.0
  From: golang.org/x/net/http2@v0.1.0
  Fixed in: 0.17.0

✗ High severity vulnerability found in golang.org/x/net/http2
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-6531285
  Introduced through: golang.org/x/net/http2@v0.1.0
  From: golang.org/x/net/http2@v0.1.0
  Fixed in: 0.23.0

✗ High severity vulnerability found in github.com/mattn/go-sqlite3
  Description: Heap-based Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMMATTNGOSQLITE3-6139875
  Introduced through: github.com/mattn/go-sqlite3@v1.14.16
  From: github.com/mattn/go-sqlite3@v1.14.16
  Fixed in: 1.14.18

✗ High severity vulnerability found in github.com/elazarl/goproxy
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMELAZARLGOPROXY-5783247
  Introduced through: github.com/elazarl/goproxy@v0.0.0-20220115173737-adb46da277ac
  From: github.com/elazarl/goproxy@v0.0.0-20220115173737-adb46da277ac

✗ Critical severity vulnerability found in github.com/go-git/go-git/v5
  Description: Path Traversal
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMGOGITGOGITV5-6150754
  Introduced through: github.com/go-git/go-git/v5@v5.4.2
  From: github.com/go-git/go-git/v5@v5.4.2
  Fixed in: 5.11.0



Organization:      bhavdeep1304
Package manager:   gomodules
Target file:       /usr/share/grafana/bin/grafana-cli
Project name:      github.com/grafana/grafana
Docker image:      grafana/grafana:9.3.0
Licenses:          enabled

Tested 747 dependencies for known issues, found 16 issues.

Snyk wasn’t able to auto detect the base image, use `--file` option to get base image remediation advice.
Example: $ snyk container test grafana/grafana:9.3.0 --file=path/to/Dockerfile

Snyk found some vulnerabilities in your image applications (Snyk searches for these vulnerabilities by default). See https://snyk.co/app-vulns for more information.

To remove these messages in the future, please run `snyk config set disableSuggestions=true`

-------------------------------------------------------

Testing grafana/grafana:9.3.0...

✗ Medium severity vulnerability found in google.golang.org/protobuf/internal/encoding/json
  Description: Infinite loop
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOOGLEGOLANGORGPROTOBUFINTERNALENCODINGJSON-6393704
  Introduced through: google.golang.org/protobuf/internal/encoding/json@v1.28.1
  From: google.golang.org/protobuf/internal/encoding/json@v1.28.1
  Fixed in: 1.33.0

✗ Medium severity vulnerability found in google.golang.org/protobuf/encoding/protojson
  Description: Stack-based Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOOGLEGOLANGORGPROTOBUFENCODINGPROTOJSON-6137908
  Introduced through: google.golang.org/protobuf/encoding/protojson@v1.28.1
  From: google.golang.org/protobuf/encoding/protojson@v1.28.1
  Fixed in: 1.32.0

✗ Medium severity vulnerability found in google.golang.org/protobuf/encoding/protojson
  Description: Infinite loop
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOOGLEGOLANGORGPROTOBUFENCODINGPROTOJSON-6393703
  Introduced through: google.golang.org/protobuf/encoding/protojson@v1.28.1
  From: google.golang.org/protobuf/encoding/protojson@v1.28.1
  Fixed in: 1.33.0

✗ Medium severity vulnerability found in golang.org/x/net/http2
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-3160322
  Introduced through: golang.org/x/net/http2@v0.1.0
  From: golang.org/x/net/http2@v0.1.0
  Fixed in: 0.4.0

✗ Medium severity vulnerability found in golang.org/x/net/http2
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-5958903
  Introduced through: golang.org/x/net/http2@v0.1.0
  From: golang.org/x/net/http2@v0.1.0
  Fixed in: 0.17.0

✗ Medium severity vulnerability found in golang.org/x/crypto/ssh
  Description: Authentication Bypass by Capture-replay
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXCRYPTOSSH-6130669
  Introduced through: golang.org/x/crypto/ssh@v0.0.0-20220622213112-05595931fe9d
  From: golang.org/x/crypto/ssh@v0.0.0-20220622213112-05595931fe9d
  Fixed in: 0.17.0

✗ Medium severity vulnerability found in golang.org/x/crypto/openpgp/clearsign
  Description: Improper Verification of Cryptographic Signature
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXCRYPTOOPENPGPCLEARSIGN-5813980
  Introduced through: golang.org/x/crypto/openpgp/clearsign@v0.0.0-20220622213112-05595931fe9d
  From: golang.org/x/crypto/openpgp/clearsign@v0.0.0-20220622213112-05595931fe9d
  Fixed in: 0.1.0

✗ Medium severity vulnerability found in github.com/ua-parser/uap-go/uaparser
  Description: Regular Expression Denial of Service (ReDoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMUAPARSERUAPGOUAPARSER-1298048
  Introduced through: github.com/ua-parser/uap-go/uaparser@v0.0.0-20211112212520-00c877edfe0f
  From: github.com/ua-parser/uap-go/uaparser@v0.0.0-20211112212520-00c877edfe0f

✗ Medium severity vulnerability found in github.com/prometheus/exporter-toolkit/web
  Description: Incorrect Implementation of Authentication Algorithm
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMPROMETHEUSEXPORTERTOOLKITWEB-3150818
  Introduced through: github.com/prometheus/exporter-toolkit/web@v0.7.1
  From: github.com/prometheus/exporter-toolkit/web@v0.7.1
  Fixed in: 0.7.2, 0.8.2

✗ Medium severity vulnerability found in github.com/go-git/go-git/v5/plumbing
  Description: Uncontrolled Resource Consumption ('Resource Exhaustion')
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMGOGITGOGITV5PLUMBING-6140319
  Introduced through: github.com/go-git/go-git/v5/plumbing@v5.4.2
  From: github.com/go-git/go-git/v5/plumbing@v5.4.2
  Fixed in: 5.11.0

✗ High severity vulnerability found in google.golang.org/grpc
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOOGLEGOLANGORGGRPC-5953328
  Introduced through: google.golang.org/grpc@v1.45.0
  From: google.golang.org/grpc@v1.45.0
  Fixed in: 1.56.3, 1.57.1, 1.58.3

✗ High severity vulnerability found in golang.org/x/net/http2/hpack
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2HPACK-3358253
  Introduced through: golang.org/x/net/http2/hpack@v0.1.0
  From: golang.org/x/net/http2/hpack@v0.1.0
  Fixed in: 0.7.0

✗ High severity vulnerability found in golang.org/x/net/http2
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-3323837
  Introduced through: golang.org/x/net/http2@v0.1.0
  From: golang.org/x/net/http2@v0.1.0
  Fixed in: 0.7.0

✗ High severity vulnerability found in golang.org/x/net/http2
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-5953327
  Introduced through: golang.org/x/net/http2@v0.1.0
  From: golang.org/x/net/http2@v0.1.0
  Fixed in: 0.17.0

✗ High severity vulnerability found in golang.org/x/net/http2
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-6531285
  Introduced through: golang.org/x/net/http2@v0.1.0
  From: golang.org/x/net/http2@v0.1.0
  Fixed in: 0.23.0

✗ High severity vulnerability found in github.com/mattn/go-sqlite3
  Description: Heap-based Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMMATTNGOSQLITE3-6139875
  Introduced through: github.com/mattn/go-sqlite3@v1.14.16
  From: github.com/mattn/go-sqlite3@v1.14.16
  Fixed in: 1.14.18

✗ High severity vulnerability found in github.com/elazarl/goproxy
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMELAZARLGOPROXY-5783247
  Introduced through: github.com/elazarl/goproxy@v0.0.0-20220115173737-adb46da277ac
  From: github.com/elazarl/goproxy@v0.0.0-20220115173737-adb46da277ac

✗ Critical severity vulnerability found in github.com/go-git/go-git/v5
  Description: Path Traversal
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMGOGITGOGITV5-6150754
  Introduced through: github.com/go-git/go-git/v5@v5.4.2
  From: github.com/go-git/go-git/v5@v5.4.2
  Fixed in: 5.11.0



Organization:      bhavdeep1304
Package manager:   gomodules
Target file:       /usr/share/grafana/bin/grafana-server
Project name:      github.com/grafana/grafana
Docker image:      grafana/grafana:9.3.0
Licenses:          enabled

Tested 910 dependencies for known issues, found 18 issues.

Snyk wasn’t able to auto detect the base image, use `--file` option to get base image remediation advice.
Example: $ snyk container test grafana/grafana:9.3.0 --file=path/to/Dockerfile

Snyk found some vulnerabilities in your image applications (Snyk searches for these vulnerabilities by default). See https://snyk.co/app-vulns for more information.

To remove these messages in the future, please run `snyk config set disableSuggestions=true`


Tested 3 projects, 3 contained vulnerable paths.



```
