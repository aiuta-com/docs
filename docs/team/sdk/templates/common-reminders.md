??? note "`Etag` and caching"

    - The SDK should store the `Etag` value from the response in local storage alongside the cached data. 
    - On subsequent requests the SDK should include cached `Etag` value in the `if-none-match` header. 
    - If the configuration hasn't changed, the server will respond with a `304` status code. Otherwise, it will return the updated configuration and a new `Etag` that shoul be updated in the storage for the further requests.

??? note "Convert from `snake_case`"
    While API uses `snake_case` for field names, the SDK schemes adhere to a `camelCase` convention.