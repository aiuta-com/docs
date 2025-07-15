---
hide:
  - toc
---
# Debug Settings Scheme

The `DebugSettings` is helping to manage and troubleshoot the SDK's behavior. It provides a set of options that control logging and validation policies, ensuring that the SDK operates smoothly and any issues can be quickly identified and resolved.

## [:material-arrow-up-left:](/sdk/developer/configuration/#configuration) Debug Settings

```typescript
DebugSettings {
  isLoggingEnabled: Bool // (1)!
  emptyStringsPolicy: ValidationPolicy // (2)!
  unavailableResourcesPolicy: ValidationPolicy // (3)!
  infoPlistDescriptionsPolicy: ValidationPolicy // (4)!
  listSizePolicy: ValidationPolicy // (5)!
}
```

1.  Controls whether the SDK should log debug information, providing detailed logs to help developers understand its behavior.
2.  Validation policy for checking whether required strings in the SDK configuration are not empty, preventing runtime issues.
3.  Validation policy for checking whether required resources are available and properly configured.
4.  Validation policy for checking whether the `info.plist` file contains all required descriptions for enabled features.
5.  Validation policy for checking whether lists required by the SDK are of the correct size.

### [:material-arrow-up-left:](#debug-settings) Validation Policy

``` typescript
enum ValidationPolicy {
  ignore // (1)!
  warning // (2)!
  fatal // (3)!
}
```

1.  Ignores all validation errors, allowing the SDK to proceed without taking any action.
2.  Logs validation errors to the console for debugging purposes without interrupting execution.
3.  Stops the application's execution with a fatal error when validation errors occur.

The `ValidationPolicy` enum defines the severity of validation checks, determining whether errors are ignored, logged as warnings, or treated as fatal, halting execution.
