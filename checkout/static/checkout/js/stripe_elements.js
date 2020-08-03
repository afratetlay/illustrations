var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

// Set up Stripe.js and Elements to use in checkout form

var style = {
  base: {
    color: '#000',
    fontFamily: '"helvetica Neue", Helvetica, sans-serif',
    fontSmooting: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
        color: '#aab7c4'
    }
},
invalid: {
    color: '#dc3545',
    iconColor: '#dc3545'
}
};
var card = elements.create('card', {style: style});

card.mount('#card-element');
// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html =
        <span class="icon" role="alert">
            <i class="fas fa-times"></i>
        </span>
    <span>${event.error.message}</span>
    ;
    $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    } 
});
