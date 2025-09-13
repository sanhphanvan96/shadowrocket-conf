// IBISPaint Premium Script
// Version: 1.1
// Description: This script replaces the subscription response for IBISPaint to enable premium features and sets required cookies

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

// Set up custom headers with status 200 and all required cookies
const customHeaders = {
    "status": "200",
    "Set-Cookie": [
        "COOKIE_LOCALE=vi; Path=/",
        "JSESSIONID=7AC98C8C6966349BD201E1B07836651D.ibisPaintAP026; Path=/; HttpOnly",
        "IBPNT_APP_TYPE=2; Path=/; HttpOnly",
        "IBPNT_APP_VERSION=130111; Path=/; HttpOnly",
        "IBPNT_PLATFORM_TYPE=1; Path=/; HttpOnly",
        "IBPNT_IS_EDUCATION_VERSION=true; Path=/; HttpOnly"
    ]
};

$done({
    body: JSON.stringify(premiumResponse),
    headers: customHeaders,
    status: 200
});
