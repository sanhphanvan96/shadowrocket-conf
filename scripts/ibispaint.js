// IBISPaint Premium Script
// Version: 1.4
// Description: This script replaces the subscription response for IBISPaint to enable premium features and sets required cookies

// Premium response data
const premiumResponse = {
    "result": 1,
    "purchases": [
        {
            "cancel_date": null,
            "cancel_reason": 0,
            "first_purchase_date": 1757744139000,
            "first_purchase_id": "180002860455524",
            "item": 5,
            "last_expire_date": 4095530300,
            "last_purchase_date": 1757744138000,
            "last_purchase_id": "180002860455524",
            "next_purchase_id": "ibisPaintXPrimeYearly",
            "renew_state": true,
            "test_flag": false,
            "token": null,
            "trial_mode": true
        }
    ]
};

// Simplest solution: combine all cookies into one string with \r\n separator as per HTTP spec
const combinedSetCookie =
    "Set-Cookie: IBPNT_APP_TYPE=2; Path=/; HttpOnly\r\n" +
    "Set-Cookie: IBPNT_APP_VERSION=130111; Path=/; HttpOnly\r\n" +
    "Set-Cookie: IBPNT_PLATFORM_TYPE=1; Path=/; HttpOnly\r\n" +
    "Set-Cookie: IBPNT_IS_EDUCATION_VERSION=true; Path=/; HttpOnly\r\n";

// Create modified response
const modifiedHeaders = $response.headers || {};
modifiedHeaders["X"] = combinedSetCookie;

// Return modified response with status 200
$done({
    status: 200,
    headers: modifiedHeaders,
    body: JSON.stringify(premiumResponse)
});
