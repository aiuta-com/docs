---
hide:
  - toc
---
# Activity Indicator Scheme

Appearance and customization of loading indicators.

![Activity Indicator](/media/components/activity-indicator.png){ width=30}

## [:material-arrow-up-left:](/sdk/developer/configuration/ui/theme/index.md#theme) Activity Indicator

```typescript
ActivityIndicatorTheme {
  icons {
    loading14: Icon | null // (1)!
  }

  colors {
    overlay: Color // (4)!
  }
  
  settings {
    indicationDelay: Number // (2)!
    spinDuration: Number // (3)!
  }
}

```

1. Optional icon for the activity indicator. If not provided, the system's default indicator will be used.

    !!! example ""
        <sub>![Activity Indicator](/media/components/activity-indicator.png){ width=30}</sub> <sup>System activity indicator by default</sup>

2. The time in milliseconds before the activity indicator appears. If the task completes before this delay, the indicator will not be shown. Otherwise, the indicator will appear.

3. The duration in milliseconds for one complete rotation of the activity indicator. This setting controls how fast the indicator spins, providing a visual cue of activity progress.
    
    !!! note ""
        The spin duration only applies when a custom icon is used for the activity indicator. If the system's default indicator is used, this setting will be ignored and the indicator will spin with the system default speed.

4. Overlay color used to cover any view when it needs to be locked for an activity. The activity indicator will be placed at the center of this overlay. 