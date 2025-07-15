The sequence diagram of executing a virtual try-on operation.

``` mermaid
sequenceDiagram
    {% include-markdown "sdk/templates/diagrams/common-sd-participants.md" %}

    USR->>SDK: Pick a Photo / Tap Try-on button in the SDK UI
    activate SDK

    SDK->>API: Create operation<br>(image ID, product ID)
    activate API
    Note over SDK,API: Secure authenticated request
    API-->>SDK: Operation ID

    par
        API->>API: Generate image
        API->>GS: Save generated image
        deactivate API
        Note over API,GS: Anonymous.<br>The photo is associated with the<br>app entry, not the user entry
    and
        loop internal configuration delay
            SDK->>API: Request operation status
            API-->>SDK: Operation details
            Note over API,SDK: status, generated_images | error
            SDK-->>SDK: Check operation status
            Note over SDK: Repeat while<br>CREATED | IN_PROGRESS | PAUSED

        end
    end

    critical Check operation status
        option SUCCESS
            SDK->>SDK: Add images to the history
            SDK->>GS: Get result image by the URL
            activate GS
            GS-->>SDK: Image data
            deactivate GS
            SDK-->>USR: Present results
            Note over SDK,USR: User may interact with results

        option ABORTED
            rect
                SDK-->>USR: Report couldn't detect anyone
            end
            Note over SDK,USR: User may select other photo and start over

        option FAILED | CANCELLED
            rect
                SDK-->>USR: Show something went wrong error
                deactivate SDK
            end
            Note over SDK,USR: User may try again to start over
    end
```
