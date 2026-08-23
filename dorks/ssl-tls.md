# SSL/TLS Queries

Use these examples only for assets you own, administer, or are explicitly authorized to assess.

## Services with TLS metadata

```text
net:"203.0.113.0/24" has_ssl:true
```

## Certificate subject common name

```text
net:"203.0.113.0/24" ssl.cert.subject.cn:"example.com"
```

This can help correlate certificates with expected services inside an authorized boundary.

## Certificate issuer

```text
net:"203.0.113.0/24" ssl.cert.issuer.cn:"Let's Encrypt"
```

Issuer information can be useful for certificate-inventory and governance reviews.

## Certificate fingerprint

```text
net:"203.0.113.0/24" ssl.cert.fingerprint:"FINGERPRINT"
```

Fingerprints provide a strong certificate pivot, but certificate reuse does not by itself establish system ownership.

## Certificate serial

```text
net:"203.0.113.0/24" ssl.cert.serial:"SERIAL"
```

## TLS version

```text
net:"203.0.113.0/24" ssl.version:"TLSv1.2"
```

Validate protocol-version findings with current authorized testing because Shodan telemetry can be historical.

## ALPN

```text
net:"203.0.113.0/24" ssl.alpn:"h2"
```

## JARM

```text
net:"203.0.113.0/24" ssl.jarm:"JARM_FINGERPRINT"
```

JARM can help group similar TLS server implementations. A matching fingerprint is a correlation signal, not proof that two systems share ownership or purpose.

## JA3S

```text
net:"203.0.113.0/24" ssl.ja3s:"JA3S_FINGERPRINT"
```

## Defensive review combinations

```text
org:"Example Organization" has_ssl:true
org:"Example Organization" has_ssl:true port:443
net:"203.0.113.0/24" ssl.cert.subject.cn:"example.com"
```

## Interpretation guidance

Certificate metadata can be stale, shared, reissued, or associated with third-party infrastructure. Reconcile observations against your internal certificate inventory, DNS, cloud inventory, and approved hosting providers before assigning ownership.
