# MWM HMI Interface — KD658 Barcode Reader and Work File

The KD658 barcode reader is used on the MWM HMI in two operating modes: **with a work file** and **without a work file**.

## Working with a work file

When a work file (batch file) is loaded, scanning a barcode requires only the **3 digits following the N character** in the barcode content. The HMI matches this number to the corresponding line in the work file and uses all production data from that line.

Example work file lines (`batch_test_1.txt`):

```
N000KStandard  P00001F001X06780Y07490Z00000C1717171700S001
N001KStandard  P00001F002X06780Y07490Z00000C1717171700S001
N002KStandard  P00001F003X06780Y07490Z00000C1717171700S001
```

In this example, list numbers such as `N000`, `N001`, and `N002` are used as the matching key when a barcode is scanned.

### Work file line format (KD6xx)

Each line consists of fields separated by fixed header characters. Field definitions are based on `KD6xx_BathcFile_Desc.xlsx`:

| Character | Header | Size | Type | Description |
|-----------|--------|------|------|-------------|
| N | List number | N + 3 characters | Numeric | Sequence number used for barcode matching |
| K | Profile code | K + 10 characters | Text | Profile definition (e.g. `Standard`, `Profiles01`) |
| P | BIN / Trolley number | P + 5 characters | Numeric | Pallet or trolley number |
| F | Window number | F + 3 characters | Numeric | Window sequence number |
| X | Frame X value | X + 5 characters | Numeric | The fifth character is the decimal place. E.g. `15005` = 1500.5 |
| Y | Frame Y value | Y + 5 characters | Numeric | The fifth character is the decimal place. E.g. `15005` = 1500.5 |
| Z | Unused | Z + 5 characters | Text | Reserved field |
| C | Operator information | C + 10 characters | Text | Additional information for the operator |
| S | Quantity | S + 3 characters | Numeric | Production quantity |

**Example line (xlsx):**

```
N000KProfiles01P00001F001X06780Y07490Z00000C1717171700S001
```

**Work file example ----->>>** [batch_test_1.txt](./batch_test_1.txt)

## Working without a work file

When no work file is loaded, barcode data is parsed directly from the scanned string. The required fields are configured on the MWM HMI **Load Barcode** screen.

![KD658 Load Barcode screen](./images/kd658-load-barcode.png)

### Load Barcode settings

| Field | First (Start) | Last / End (Length) | Description |
|-------|---------------|---------------------|-------------|
| Barcode ID | 1 | — | Barcode definition identifier |
| Barcode Length | 31 | — | Total barcode character length |
| Stan | 0 | 1 | Station information |
| Prof | 5 | 12 | Profile code |
| Color | 17 | 2 | Color code |
| X | 20 | 6 | X coordinate |
| Y | 26 | 5 | Y coordinate |
| Special first | — | — | Optional custom field start |
| Special end | — | — | Optional custom field length |

The **First** value specifies the starting position of the field within the barcode; **Last / End** specifies the field length in characters.

In work-file-less mode, the scanned 31-character barcode is parsed into Stan, Prof, Color, X, and Y fields according to the positions and lengths above.
