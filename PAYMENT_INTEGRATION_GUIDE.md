# PAYMENT INTEGRATION GUIDE - MIBW DONATION SYSTEM

## Overview
This document provides step-by-step instructions to integrate payment processing for the MIBW donation page (/donate). We support M-Pesa, credit cards, and bank transfers.

---

## PAYMENT PROVIDERS AVAILABLE

### Option 1: M-Pesa Integration (RECOMMENDED FOR KENYA)
**Best for:** Kenyan donors, highest conversion rate

#### Providers:
1. **Pesapal** (Easiest for M-Pesa)
2. **Flutterwave** (Multi-payment)
3. **Mpesa Daraja API** (Direct M-Pesa)

#### Pesapal Integration (RECOMMENDED):

```html
<!-- Add this script to your donate.html <head> section -->
<script src="https://pesapal.com/api/pesapal-js-sdk.js"></script>

<!-- Add data attributes to your donation button -->
<button class="donate-form-btn" id="pay-button">Proceed to Donation</button>

<!-- JavaScript integration -->
<script>
document.getElementById('pay-button').addEventListener('click', async function() {
  const amount = document.getElementById('custom-amount').value || getSelectedAmount();
  
  if (!amount || amount < 100) {
    alert('Please enter a valid amount (minimum KES 100)');
    return;
  }

  const pesapal = new PesapalCheckout({
    clientId: "YOUR_PESAPAL_CLIENT_ID", // Get from Pesapal dashboard
    containerElement: "button-container", // Container element
  });

  // Redirect to payment page
  await pesapal.checkout({
    reference: "MIBW-" + Date.now(),
    amount: amount,
    currency: "KES",
    description: "Donation to MIBW Mental Health Support",
    callback_url: "https://www.mibw.org/payment-callback.html",
    notification_id: "YOUR_NOTIFICATION_ID",
    billing_details: {
      email_address: "donor@example.com",
      phone_number: "+254700000000",
      first_name: "Donor",
      last_name: "Name",
    }
  });
});
</script>
```

**Setup Steps:**
1. Go to https://pesapal.com
2. Create business account
3. Get Consumer Key and Consumer Secret
4. Replace CLIENT_ID, NOTIFICATION_ID in code above
5. Create callback page (payment-callback.html) to verify transaction

---

### Option 2: Flutterwave Integration (MULTI-CURRENCY)
**Best for:** Multiple payment methods in one integration

```html
<script src="https://checkout.flutterwave.com/v3.js"></script>

<script>
document.getElementById('pay-button').addEventListener('click', function() {
  const amount = document.getElementById('custom-amount').value || getSelectedAmount();
  
  FlutterwaveCheckout({
    public_key: "FLWPUBK_TEST_xxxxxxxxxxxxxx", // Get from Flutterwave dashboard
    tx_ref: "mibw-" + Date.now(),
    amount: amount,
    currency: "KES",
    payment_options: "card,mobilemoney,ussd",
    customer: {
      email: "donor@mibw.org",
      name: "Generous Donor"
    },
    customizations: {
      title: "Support MIBW - Help Men's Mental Health",
      description: "Your donation transforms lives",
      logo: "https://www.mibw.org/logo.png"
    },
    callback: function(data) {
      console.log(data);
      // Verify transaction on your server
    },
    onclose: function() {
      console.log("Payment modal closed");
    }
  });
});
</script>
```

**Setup Steps:**
1. Go to https://flutterwave.com
2. Create account
3. Get public key and secret key
4. Enable required payment methods in dashboard
5. Configure webhook for payment verification

---

### Option 3: Direct M-Pesa (Safaricom Daraja API)
**Best for:** Direct M-Pesa, lowest fees

```html
<script>
document.getElementById('pay-button').addEventListener('click', function() {
  const amount = document.getElementById('custom-amount').value || getSelectedAmount();
  const phone = document.getElementById('phone').value;
  
  fetch('YOUR_SERVER_ENDPOINT/initiate-payment', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      amount: amount,
      phone: phone,
      reference: "MIBW-" + Date.now(),
      description: "Donation to MIBW"
    })
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      alert('Check your phone for M-Pesa prompt');
    } else {
      alert('Payment initiation failed: ' + data.error);
    }
  });
});
</script>
```

**Setup Steps:**
1. Go to https://developer.safaricom.co.ke
2. Create M-Pesa Daraja app
3. Get Consumer Key and Consumer Secret
4. Implement server-side payment initiation (Python/Node.js)
5. Setup STK push callback verification

---

## RECOMMENDED SETUP FOR MIBW

### Phase 1: Quick Start (Week 1)
Use **Pesapal** - easiest integration
- Single API integration
- Supports M-Pesa, cards, bank transfer
- Best UX for Kenya
- Cost: ~3-4% per transaction

### Phase 2: Optimize (Week 2-3)
Add **Flutterwave** as backup
- Alternative payment option
- Better for international donors
- Cost: ~1.4% + KES 20 per transaction

### Phase 3: Scale (Month 2)
Add direct **M-Pesa Daraja**
- Lowest fees (~1.5%)
- Best for large volume
- Requires backend setup

---

## IMPLEMENTATION CHECKLIST

- [ ] Choose payment provider (Pesapal recommended)
- [ ] Create business account on chosen provider
- [ ] Get API credentials (Consumer Key, Secret, etc.)
- [ ] Integrate payment SDK into donate.html
- [ ] Create payment callback page
- [ ] Setup backend payment verification
- [ ] Create thank you page (post-donation)
- [ ] Test with provider's test mode
  - Test successful payment
  - Test failed payment
  - Test M-Pesa
  - Test card payment
  - Test refund process
- [ ] Move to production
- [ ] Monitor transactions in provider dashboard
- [ ] Send donor receipts/thank you emails

---

## POST-PAYMENT SETUP

### 1. Create Thank You Page
```html
<!-- thank-you.html -->
<h1>Thank You for Your Generosity!</h1>
<p>Your donation of KES [AMOUNT] has been received and will make a real difference.</p>
<p>A receipt has been sent to [EMAIL].</p>

<!-- Suggested next steps -->
<h2>What Happens Next?</h2>
<ul>
  <li>Monthly impact reports showing how your donation helps men in need</li>
  <li>Exclusive donor updates on our progress</li>
  <li>Stories of lives changed by supporters like you</li>
</ul>

<a href="/" class="btn">Return Home</a>
```

### 2. Create Donor Receipt Email Template
```
Subject: Receipt for Your MIBW Donation - KES [AMOUNT]

Dear [NAME],

Thank you so much for your generous donation of KES [AMOUNT] to MIBW!

Your donation will:
✓ Provide [X] hours of crisis counseling
✓ Support [X] peer support group sessions
✓ Help us reach men in our community

Your Transaction Details:
- Amount: KES [AMOUNT]
- Date: [DATE]
- Reference: [REF_ID]
- Tax ID: XXXXX (for tax deduction)

We will send you monthly impact updates showing exactly how your support is transforming lives.

With gratitude,
The MIBW Team

P.S. Know someone who needs support? Share this: www.mibw.org
```

### 3. Create Dashboard to Track Donations
```html
<!-- admin/donations.html (internal use) -->
Display:
- Total donations today
- Total donations this month
- Total donations this year
- Recent donations (table)
- Donor retention rate
- Average donation amount
```

---

## SECURITY REQUIREMENTS

1. **SSL/HTTPS** - Already required (enable on Vercel)
2. **Data Encryption** - Payment providers handle this
3. **PCI Compliance** - Don't store card data directly
4. **Verification** - Always verify payments on server side
5. **Fraud Detection** - Monitor for suspicious patterns

---

## TRANSACTION FEES

| Provider | M-Pesa | Card | Bank | Notes |
|----------|--------|------|------|-------|
| **Pesapal** | 3% | 3.5% | 2.5% | Best all-around |
| **Flutterwave** | 2% | 1.4%+20 | 1% | Good alternative |
| **M-Pesa Daraja** | 1.5% | N/A | N/A | Direct, lowest cost |

**Note:** Factor 3-4% into your messaging. Example: "A KES 500 donation = KES 485 goes directly to support services"

---

## TESTING CREDENTIALS

### Pesapal Sandbox Testing
```
Consumer Key: xxxxxxxxxxxx
Consumer Secret: xxxxxxxxxxxx
API Endpoint: https://pesapal.com/api/postPesapalDirectOrderV4
Test M-Pesa Phone: 0700000000
```

### Flutterwave Sandbox Testing
```
Public Key: FLWPUBK_TEST_xxxxxxxxxxxx
Card: 4242 4242 4242 4242 (Visa)
CVV: 242, Exp: 04/25
```

---

## GO-LIVE CHECKLIST

- [ ] All payment flows tested successfully
- [ ] Thank you page working
- [ ] Email receipts being sent
- [ ] Provider webhook verification working
- [ ] Admin dashboard monitoring donations
- [ ] Tax receipts being generated
- [ ] Customer support email setup (donations@mibw.org)
- [ ] Terms & conditions updated
- [ ] Privacy policy covers payment data
- [ ] FAQ updated with payment questions

---

## SUPPORT CONTACTS

**Pesapal Support:** support@pesapal.com
**Flutterwave Support:** support@flutterwave.com  
**Safaricom Daraja:** https://developer.safaricom.co.ke/support

---

## NEXT STEPS

1. **This Week:** Choose payment provider & create account
2. **Week 2:** Integrate payment SDK
3. **Week 3:** Test all payment flows
4. **Week 4:** Go live and monitor transactions
5. **Ongoing:** Send monthly donor updates & impact reports

---

**Document Last Updated:** January 3, 2026
**Status:** Ready for Implementation
**Questions?** Contact the development team
