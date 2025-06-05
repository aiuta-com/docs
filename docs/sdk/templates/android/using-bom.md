??? tip "Using Bill of Materials"
    
    To ensure consistent dependency versions and simplify version management, you can use the Bill of Materials (BOM)

    === "Kotlin"
        ```kotlin
        dependencies {
            // 1. Add BOM 
            implementation(platform("com.aiuta:fashionsdk-bom:<version>"))

            // 2. Add all required for you dependencies
            implementation("com.aiuta:fashionsdk")
            implementation("com.aiuta:fashionsdk-configuration") 
            ...
        }
        ```

    === "Groovy"
        ```groovy
        dependencies {
            // 1. Add BOM
            implementation platform("com.aiuta:fashionsdk-bom:<version>")

            // 2. Add all required for you dependencies
            implementation "com.aiuta:fashionsdk"
            implementation "com.aiuta:fashionsdk-configuration"
            ...
        }
        ```
