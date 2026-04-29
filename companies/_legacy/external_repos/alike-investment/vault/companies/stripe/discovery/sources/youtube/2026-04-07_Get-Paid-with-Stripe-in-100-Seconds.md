---
ticker: STRIPE
type: youtube
title: "Get Paid with Stripe in 100 Seconds"
channel: "Fireship"
date: 2026-04-07
url: https://www.youtube.com/watch?v=7edR32QVp_A
transcript_method: yt-dlp_subtitle
language: en
chars: 2563
---

# Get Paid with Stripe in 100 Seconds

## 视频信息
- **频道**: Fireship
- **日期**: 2026-04-07
- **链接**: https://www.youtube.com/watch?v=7edR32QVp_A

## 转录全文

strike it's a toolkit that can monetize virtually any online business model it's api's or like low-level building blocks that can be used to accept payments manage customers handle recurring subscriptions and more lyft uses it to take payments from riders and payout drivers digitalocean uses it to sell a metered software-as-a-service product and Shopify uses it to implement a massive online marketplace it's extremely popular with startups because of its developer first approach instead of worrying about things like compliance security and fraud detection you can focus on the user experience and implement your payment system with just a few API calls so how does a credit card payment work when a user is ready to make a payment in your app you'll first need to create a payment intent on your server the payment intent is kind of like a session that manages the payment process currently it's in a state of requires payment method step two is obtaining the credit card details or payment method from the customer you can handle this process securely on the web using stripe j/s it's able to mount a customizable credit card forum directly in your application it automatically validates the users input so you don't have to worry about implementing your own form validation and all the edge cases that go along with it when the form is submitted you'll write a function that takes the payment intent from your server combines it with the credit card details entered by the user in the browser then calls stripe confirm card payment to send this data off to stripe servers it will attempt to finalize the payment but many parts of the world now have regulations in place that require additional authorization for the payment the payment intent now has a status of requires action a strike will handle this process for you entirely in the front end and once complete your payment intent will move to a status of succeeded congratulations you've just been paid but you're not done just yet you still need to fulfill the product somehow anytime something important happens in the stripe API like when a payment intent succeeds you can listen to these events by setting up web hooks when the event occurs stripe will send this data to your server so you can handle it accordingly like updating your apps database or printing out a shipping label this has been stripe payments in 100 seconds if you're serious about monetizing your product consider enrolling in my brand new stripe JavaScript course thanks for watching and I will see you in the next one [Music]
