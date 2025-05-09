# Typography

The table below contains all the text styles used in the SDK:

- :fontawesome-regular-eye-slash: This is optional and can be omitted if you are not using the corresponding feature

| Key | Description | Default |
| :-- | :---------- | :------ |
| [**Label**](#label) | |  
| `titleL` | Large titles | `System 24pt Bold` |
| `titleM` | Medium titles | `System 20pt Bold`<br>`kern -0.4` |
| `regular` | Regular text | `System 17pt Medium`<br>`kern -0.51, lhm 1.08` [^1] |
| `subtle` | Subtle text | `System 15pt Regular`<br>`kern -0.15, lhm 1.01` [^1] |
| [**Button**](#button) | |
| `buttonM` | Medium buttons | `System 17pt Semibold`<br>`kern -0.17, lhm 0.89` [^1] |
| `buttonS` | Small buttons | `System 13pt Semibold`<br>`kern -0.13, lhm 1.16` [^1] |
| [**PageBar**](#pagebar) | |
| `pageTitle` | Page titles | `System 17pt Medium`<br>`kern -0.51, lhm 1.08` [^1] |
| [**BottomSheet**](#bottomsheet) | |
| `iconButton` | Icon buttons | `System 17pt Medium`<br>`kern -0.17` |
| [**ProductBar**](#productbar) | |
| `product` | Product names | `System 13pt Regular` |
| `brand` | Brand names | `System 12pt Medium`<br>`kern -0.12` |
| [**ProductBar :octicons-arrow-right-24: Price**](#productbarprice) :fontawesome-regular-eye-slash:{ title="Optional" } | | |
| `price` | Price text | `System 14pt Bold`<br>`kern -0.14` |
| [**Welcome Screen**](#welcome-screen) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `welcomeTitle` | Welcome screen title | `System 40pt Heavy`<br>`lhm 0.92` |
| `welcomeDescription` | Welcome screen description | `System 16pt Medium`<br>`lhm 1.18` [^1] |
| [**TryOn :octicons-arrow-right-24: FitDisclaimer**](#tryonfitdisclaimer) :fontawesome-regular-eye-slash:{ title="Optional" } | |
| `disclaimer` | Fit disclaimer label | `System 12pt Regular`<br>`kern -0.12` |

[^1]: `lhm` is __Line Height Multiple__ relative to the original line height of the font
