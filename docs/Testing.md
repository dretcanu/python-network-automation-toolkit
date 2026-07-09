# Testing Documentation

## Testing Summary

The toolkit was tested using a home/lab subnet and a sample device inventory.

---

## Ping Sweep Test

Test subnet:

```text
192.168.1.0/24
```

Observed results:

```text
Total Hosts Scanned: 254
Live Hosts: 6
Down Hosts: 248
```

---

## Device Inventory Test

The inventory module successfully processed 8 devices:

```text
switches: 4
router: 1
servers: 3
```

---

## Network Health Check Test

The health check module successfully processed 8 inventory devices and produced UP/DOWN results.

---

## Configuration Backup Test

The backup module created simulated configuration backup files for 5 network devices:

```text
CORE-SW
EDGE-RTR
ACCESS-SW-01
ACCESS-SW-02
ACCESS-SW-03
```

---

## Validation

The project successfully demonstrates:

- Reading input files
- Processing CSV data
- Running network ping checks
- Producing CSV and text reports
- Creating structured backup output
