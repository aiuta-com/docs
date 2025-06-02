# Try-On Errors & Aborts

This document describes all possible errors and cancelation reasons that can occur during the try-on process.

## Try-On Errors

!!! doc "Sent in the analytics event [`tryOn.tryOnError`](analytics.md#try-on-events) in the `errorType` field"

| Error Type | Description |
|------------|-------------|
| `preparePhotoFailed` | Any reason users' photo cannot be processed by the SDK,<br>that is not related to the try-on generation process on the server.<br>This covers failure to read, downscale, compress and get JPG data<br>of the photo. |
| `uploadPhotoFailed` | Any reason users' photo cannot be uploaded to the server.<br>This may be caused by network issues, server issues, or any other reason. |
| `authorizationFailed` | The request to the server was not authorized. |
| `requestOperationFailed` | SDK failed to make a request to the server to start the try-on process.<br>This may be caused by network issues, server issues, or any other reason. |
| `startOperationFailed` | SDK successfully made a request to the server to start the try-on process,<br>but the server returned an error. |
| `operationFailed` | SDK successfully made a request to the server to start the try-on process,<br>operation was started, but the server returned an error while processing<br>the operation, and it was failed. SDK stopped waiting for the result. |
| `operationTimeout` | SDK successfully made a request to the server to start the try-on process,<br>operation was started, but the status of the operation was not changed<br>for a long time, and the SDK stopped waiting for the result. |
| `operationEmptyResults` | Try-on operation was completed, but the empty result was returned. |
| `downloadResultFailed` | Try-on operation was completed, but the result was not downloaded.<br>This may be caused by network issues, server issues, or any other reason. |
| `internalSdkError` | Unexpected error occurred during the try-on process.<br>Those should be reported to the SDK developers, as it is not<br>supposed to happen. |

## Try-On Aborts

!!! doc "Sent in the analytics event [`tryOn.tryOnAborted`](analytics.md#try-on-events) in the `abortReason` field"

| Abort Type | Description |
|------------|-------------|
| `operationAborted` | SDK successfully made a request to the server to start the try-on process,<br>operation was started, but the server aborted the operation,<br>because of the [invalid user input photo](../pages/loading-screen.md#__tabbed_1_1). |
| `userCancelled` | Operation was in progress, but user closes the SDK<br>and [background execution](../developer/configuration.md#try-on) was disabled |
