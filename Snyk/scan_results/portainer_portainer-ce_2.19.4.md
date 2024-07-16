**Scanning portainer/portainer-ce:2.19.4**
```

Testing portainer/portainer-ce:2.19.4...

Organization:      bhavdeep1304
Package manager:   linux
Project name:      docker-image|portainer/portainer-ce
Docker image:      portainer/portainer-ce:2.19.4
Platform:          linux/amd64
Licenses:          enabled

✔ Tested portainer/portainer-ce:2.19.4 for known issues, no vulnerable paths found.

Note that we do not currently have vulnerability data for your image.

-------------------------------------------------------

Testing portainer/portainer-ce:2.19.4...

✗ Medium severity vulnerability found in golang.org/x/net/http2
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-5958903
  Introduced through: golang.org/x/net/http2@v0.8.0
  From: golang.org/x/net/http2@v0.8.0
  Fixed in: 0.17.0

✗ Medium severity vulnerability found in golang.org/x/crypto/ssh
  Description: Authentication Bypass by Capture-replay
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXCRYPTOSSH-6130669
  Introduced through: golang.org/x/crypto/ssh@v0.7.0
  From: golang.org/x/crypto/ssh@v0.7.0
  Fixed in: 0.17.0

✗ Medium severity vulnerability found in golang.org/x/crypto/acme/autocert
  Description: Path Traversal
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXCRYPTOACMEAUTOCERT-7416897
  Introduced through: golang.org/x/crypto/acme/autocert@v0.7.0
  From: golang.org/x/crypto/acme/autocert@v0.7.0
  Fixed in: 0.24.0

✗ Medium severity vulnerability found in github.com/go-git/go-git/v5/plumbing
  Description: Uncontrolled Resource Consumption ('Resource Exhaustion')
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMGOGITGOGITV5PLUMBING-6140319
  Introduced through: github.com/go-git/go-git/v5/plumbing@v5.3.0
  From: github.com/go-git/go-git/v5/plumbing@v5.3.0
  Fixed in: 5.11.0

✗ Medium severity vulnerability found in github.com/docker/distribution/registry/api/v2
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMDOCKERDISTRIBUTIONREGISTRYAPIV2-5885037
  Introduced through: github.com/docker/distribution/registry/api/v2@v2.8.1+incompatible
  From: github.com/docker/distribution/registry/api/v2@v2.8.1+incompatible
  Fixed in: 2.8.2-beta.1

✗ High severity vulnerability found in golang.org/x/net/http2
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-5953327
  Introduced through: golang.org/x/net/http2@v0.8.0
  From: golang.org/x/net/http2@v0.8.0
  Fixed in: 0.17.0

✗ High severity vulnerability found in golang.org/x/net/http2
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-6531285
  Introduced through: golang.org/x/net/http2@v0.8.0
  From: golang.org/x/net/http2@v0.8.0
  Fixed in: 0.23.0

✗ High severity vulnerability found in github.com/containers/image/v5/docker
  Description: Improper Input Validation
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMCONTAINERSIMAGEV5DOCKER-6828757
  Introduced through: github.com/containers/image/v5/docker@v5.25.0
  From: github.com/containers/image/v5/docker@v5.25.0
  Fixed in: 5.30.1

✗ Critical severity vulnerability found in github.com/go-git/go-git/v5
  Description: Path Traversal
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMGOGITGOGITV5-6150754
  Introduced through: github.com/go-git/go-git/v5@v5.3.0
  From: github.com/go-git/go-git/v5@v5.3.0
  Fixed in: 5.11.0



Organization:      bhavdeep1304
Package manager:   gomodules
Target file:       /portainer
Project name:      github.com/portainer/portainer/api
Docker image:      portainer/portainer-ce:2.19.4
Licenses:          enabled

Tested 587 dependencies for known issues, found 9 issues.

Snyk wasn’t able to auto detect the base image, use `--file` option to get base image remediation advice.
Example: $ snyk container test portainer/portainer-ce:2.19.4 --file=path/to/Dockerfile

Snyk found some vulnerabilities in your image applications (Snyk searches for these vulnerabilities by default). See https://snyk.co/app-vulns for more information.

To remove these messages in the future, please run `snyk config set disableSuggestions=true`

-------------------------------------------------------

Testing portainer/portainer-ce:2.19.4...

✗ Medium severity vulnerability found in golang.org/x/net/http2
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-5958903
  Introduced through: golang.org/x/net/http2@v0.7.0
  From: golang.org/x/net/http2@v0.7.0
  Fixed in: 0.17.0

✗ Medium severity vulnerability found in golang.org/x/net/html
  Description: Cross-site Scripting (XSS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTML-5816820
  Introduced through: golang.org/x/net/html@v0.7.0
  From: golang.org/x/net/html@v0.7.0
  Fixed in: 0.13.0

✗ High severity vulnerability found in golang.org/x/net/http2
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-5953327
  Introduced through: golang.org/x/net/http2@v0.7.0
  From: golang.org/x/net/http2@v0.7.0
  Fixed in: 0.17.0

✗ High severity vulnerability found in golang.org/x/net/http2
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-6531285
  Introduced through: golang.org/x/net/http2@v0.7.0
  From: golang.org/x/net/http2@v0.7.0
  Fixed in: 0.23.0



Organization:      bhavdeep1304
Package manager:   gomodules
Target file:       /kubectl
Project name:      k8s.io/kubernetes
Docker image:      portainer/portainer-ce:2.19.4
Licenses:          enabled

Tested 230 dependencies for known issues, found 4 issues.

Snyk wasn’t able to auto detect the base image, use `--file` option to get base image remediation advice.
Example: $ snyk container test portainer/portainer-ce:2.19.4 --file=path/to/Dockerfile

Snyk found some vulnerabilities in your image applications (Snyk searches for these vulnerabilities by default). See https://snyk.co/app-vulns for more information.

To remove these messages in the future, please run `snyk config set disableSuggestions=true`

-------------------------------------------------------

Testing portainer/portainer-ce:2.19.4...

✗ Medium severity vulnerability found in golang.org/x/net/http2
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-5958903
  Introduced through: golang.org/x/net/http2@v0.8.0
  From: golang.org/x/net/http2@v0.8.0
  Fixed in: 0.17.0

✗ High severity vulnerability found in golang.org/x/net/http2
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-5953327
  Introduced through: golang.org/x/net/http2@v0.8.0
  From: golang.org/x/net/http2@v0.8.0
  Fixed in: 0.17.0

✗ High severity vulnerability found in golang.org/x/net/http2
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-6531285
  Introduced through: golang.org/x/net/http2@v0.8.0
  From: golang.org/x/net/http2@v0.8.0
  Fixed in: 0.23.0

✗ High severity vulnerability found in github.com/cyphar/filepath-securejoin
  Description: Directory Traversal
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMCYPHARFILEPATHSECUREJOIN-5889602
  Introduced through: github.com/cyphar/filepath-securejoin@v0.2.3
  From: github.com/cyphar/filepath-securejoin@v0.2.3
  Fixed in: 0.2.4



Organization:      bhavdeep1304
Package manager:   gomodules
Target file:       /helm
Project name:      helm.sh/helm/v3
Docker image:      portainer/portainer-ce:2.19.4
Licenses:          enabled

Tested 619 dependencies for known issues, found 4 issues.

Snyk wasn’t able to auto detect the base image, use `--file` option to get base image remediation advice.
Example: $ snyk container test portainer/portainer-ce:2.19.4 --file=path/to/Dockerfile

Snyk found some vulnerabilities in your image applications (Snyk searches for these vulnerabilities by default). See https://snyk.co/app-vulns for more information.

To remove these messages in the future, please run `snyk config set disableSuggestions=true`

-------------------------------------------------------

Testing portainer/portainer-ce:2.19.4...

✗ Medium severity vulnerability found in google.golang.org/protobuf/internal/encoding/json
  Description: Infinite loop
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOOGLEGOLANGORGPROTOBUFINTERNALENCODINGJSON-6393704
  Introduced through: google.golang.org/protobuf/internal/encoding/json@v1.30.0
  From: google.golang.org/protobuf/internal/encoding/json@v1.30.0
  Fixed in: 1.33.0

✗ Medium severity vulnerability found in google.golang.org/protobuf/encoding/protojson
  Description: Stack-based Buffer Overflow
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOOGLEGOLANGORGPROTOBUFENCODINGPROTOJSON-6137908
  Introduced through: google.golang.org/protobuf/encoding/protojson@v1.30.0
  From: google.golang.org/protobuf/encoding/protojson@v1.30.0
  Fixed in: 1.32.0

✗ Medium severity vulnerability found in google.golang.org/protobuf/encoding/protojson
  Description: Infinite loop
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOOGLEGOLANGORGPROTOBUFENCODINGPROTOJSON-6393703
  Introduced through: google.golang.org/protobuf/encoding/protojson@v1.30.0
  From: google.golang.org/protobuf/encoding/protojson@v1.30.0
  Fixed in: 1.33.0

✗ Medium severity vulnerability found in golang.org/x/net/http2
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-5958903
  Introduced through: golang.org/x/net/http2@v0.9.0
  From: golang.org/x/net/http2@v0.9.0
  Fixed in: 0.17.0

✗ Medium severity vulnerability found in golang.org/x/crypto/ssh
  Description: Authentication Bypass by Capture-replay
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXCRYPTOSSH-6130669
  Introduced through: golang.org/x/crypto/ssh@v0.7.0
  From: golang.org/x/crypto/ssh@v0.7.0
  Fixed in: 0.17.0

✗ High severity vulnerability found in google.golang.org/grpc
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOOGLEGOLANGORGGRPC-5953328
  Introduced through: google.golang.org/grpc@v1.56.2
  From: google.golang.org/grpc@v1.56.2
  Fixed in: 1.56.3, 1.57.1, 1.58.3

✗ High severity vulnerability found in golang.org/x/net/http2
  Description: Denial of Service (DoS)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-5953327
  Introduced through: golang.org/x/net/http2@v0.9.0
  From: golang.org/x/net/http2@v0.9.0
  Fixed in: 0.17.0

✗ High severity vulnerability found in golang.org/x/net/http2
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOLANGORGXNETHTTP2-6531285
  Introduced through: golang.org/x/net/http2@v0.9.0
  From: golang.org/x/net/http2@v0.9.0
  Fixed in: 0.23.0

✗ High severity vulnerability found in go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOOPENTELEMETRYIOCONTRIBINSTRUMENTATIONNETHTTPOTELHTTP-5963583
  Introduced through: go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp@v0.40.0
  From: go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp@v0.40.0
  Fixed in: 0.44.0

✗ High severity vulnerability found in go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOOPENTELEMETRYIOCONTRIBINSTRUMENTATIONNETHTTPOTELHTTP-5971109
  Introduced through: go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp@v0.40.0
  From: go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp@v0.40.0
  Fixed in: 0.44.0

✗ High severity vulnerability found in go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace
  Description: Allocation of Resources Without Limits or Throttling
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GOOPENTELEMETRYIOCONTRIBINSTRUMENTATIONNETHTTPHTTPTRACEOTELHTTPTRACE-5971114
  Introduced through: go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace@v0.40.0
  From: go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace@v0.40.0
  Fixed in: 0.44.0

✗ High severity vulnerability found in github.com/moby/buildkit/util/entitlements
  Description: Improper Handling of Insufficient Privileges (Leaky Vessels)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMMOBYBUILDKITUTILENTITLEMENTS-6209364
  Introduced through: github.com/moby/buildkit/util/entitlements@v0.12.1-0.20230717122532-faa0cc7da353
  From: github.com/moby/buildkit/util/entitlements@v0.12.1-0.20230717122532-faa0cc7da353
  Fixed in: 0.12.5

✗ High severity vulnerability found in github.com/moby/buildkit/client
  Description: Improper Handling of Insufficient Privileges (Leaky Vessels)
  Info: https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMMOBYBUILDKITCLIENT-6209355
  Introduced through: github.com/moby/buildkit/client@v0.12.1-0.20230717122532-faa0cc7da353
  From: github.com/moby/buildkit/client@v0.12.1-0.20230717122532-faa0cc7da353
  Fixed in: 0.12.5



Organization:      bhavdeep1304
Package manager:   gomodules
Target file:       /docker-compose
Project name:      github.com/docker/compose/v2
Docker image:      portainer/portainer-ce:2.19.4
Licenses:          enabled

Tested 755 dependencies for known issues, found 13 issues.

Snyk wasn’t able to auto detect the base image, use `--file` option to get base image remediation advice.
Example: $ snyk container test portainer/portainer-ce:2.19.4 --file=path/to/Dockerfile

Snyk found some vulnerabilities in your image applications (Snyk searches for these vulnerabilities by default). See https://snyk.co/app-vulns for more information.

To remove these messages in the future, please run `snyk config set disableSuggestions=true`


Tested 5 projects, 4 contained vulnerable paths.



```
