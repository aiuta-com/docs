# JWT server-side auth example

Here is the example of the required backend logic that needs to be implemented to support JWT authentication scheme.

Using this scheme, you can issue an authentication token for your client using your private key after properly validating the request parameters. This allows you to decide whether the client still has the ability to use the Aiuta product, enabling you to enforce any per-client limits. Additionally, you can include specific parameters in the JWT payload to ensure that the client uses these exact values when making requests to Aiuta. For example, you can include parameters required for image generation to ensure that the issued token will be used for this generation only.

You need to install the following dependencies:

```sh
pip install PyJWT
```

And then implement API handle like this:

```python
import datetime
import json

import jwt
from flask import Flask
from flask import request
from flask import Response

jwt_issuer = "<ISSUER_ID>" # (1)!
jwt_secret = "<JWT_SECRET>" # (2)!

token_valid_time = datetime.timedelta(seconds=60)

app = Flask(__name__)


@app.route("/aiuta_jwt", methods=["GET", "POST"])
def get_jwt_token():
    issued_at = datetime.datetime.utcnow()
    expires_at = issued_at + token_valid_time
    meta = {
        "iss": jwt_issuer,
        "iat": issued_at,
        "exp": expires_at,
    }

    payload = {}
    if request.args:
        payload.update(request.args)
    if request.is_json:
        payload.update(request.json)
    payload.update(meta)

    token = jwt.encode(
        payload,
        jwt_secret,
        algorithm="HS256",
    )
    return Response(
        json.dumps({"type": "jwt", "token": token}),
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
```

1.  Find the value in your [API plan subscription :octicons-link-external-24:](https://developer.aiuta.com/subscriptions){:target="_blank"}

    !!! abstract "Field in the UI"
        JWT key (iss)

2.  Find the value in your [API plan subscription :octicons-link-external-24:](https://developer.aiuta.com/subscriptions){:target="_blank"}
    
    !!! abstract "Field in the UI"
        JWT secret (to generate HS256 signature)