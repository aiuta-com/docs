---
hide:
  - toc
---

# Installation

Use [Aiuta Flutter SDK package :octicons-link-external-24:]({{ pub_package("install") }}){:target="_blank"} as a library to integrate into your application.

## Depend on it

Run this command with Flutter:

```bash
 $ flutter pub add aiuta_flutter
```

This will add a line like this to your package's `pubspec.yaml` (and run an implicit `flutter pub get`):

```yaml
dependencies:
  aiuta_flutter: ^{{ latest(flutter) }}
```

!!! tip ""
    Alternatively, your editor might support `flutter pub get`.<br>Check the docs for your editor to learn more.

## Import it

Now in your Dart code, you can use:

```dart
import 'package:aiuta_flutter/aiuta_flutter.dart';
```

## Next Step

<div class="grid cards" markdown>

- :octicons-arrow-right-24: [Quick Test](/sdk/flutter/quick-test.md) SDK Propely Integrated
- :octicons-arrow-right-24: &nbsp; Initialize with [Configuration](/sdk/flutter/configuration.md)

</div>
