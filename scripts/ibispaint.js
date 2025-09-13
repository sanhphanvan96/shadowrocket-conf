// IBISPaint Premium Script
// Version: 1.0
// Description: This script replaces the subscription response for IBISPaint to enable premium features

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

$done({body: JSON.stringify(premiumResponse)});
