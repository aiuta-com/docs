# Quick Test

This guide describes how to test the Aiuta SDK in your Flutter application after installation.
It includes steps for setting up the configuration with a demo API key and using example products to start the TryOn.

```dart
import 'package:aiuta_flutter/aiuta_flutter.dart';
import 'package:aiuta_flutter/configuration/aiuta_configuration.dart';
import 'package:aiuta_flutter/configuration/analytics/aiuta_analytics.dart';
import 'package:aiuta_flutter/configuration/analytics/aiuta_analytics_handler.dart';
import 'package:aiuta_flutter/configuration/auth/aiuta_auth.dart';
import 'package:aiuta_flutter/configuration/features/try_on/cart/aiuta_try_on_cart_handler.dart';
import 'package:aiuta_flutter/models/product/aiuta_product.dart';
```

## Init

For quick test purposes you can use demo `apiKey` auth

```dart
final aiuta = Aiuta(
  configuration: AiutaConfiguration.builtIn(
    auth: AiutaApiKeyAuth(apiKey: "{{ aiuta.api_key }}"),
    termsOfServiceUrl: "https://aiuta.com/legal/terms-of-service.html",
    cartHandler: AiutaTryOnCartHandler(
      addToCart: (productId) {
        debugPrint("Add product id ${productId} to cart");
      },
    ),
    analytics: AiutaAnalytics(
      handler: AiutaAnalyticsHandler(
        onAnalyticsEvent: (event) {
          debugPrint("$event: ${event.toJson()}");
        },
      ),
    ),
  ),
);
```

## Start TryOn

You can use one of the following product examples that will work with the demo `apiKey`

{{ gen_test_products("sdk/templates/flutter/test-tryon.dart") }}

## Show History

```dart
aiuta.startHistoryFlow();
```
