/*Add the JavaScript here for the function billingFunction().  It is responsible for setting and clearing the fields in Billing Information */
function billingFunction(){
  var sName = document.getElementById('shippingName');
  var sZip = document.getElementById('shippingZip');
  var bName = document.getElementById('billingName');
  var bZip = document.getElementById('billingZip');
  var chkBox = document.getElementById('same');
  if (chkBox.checked === true) {
    bName.value = sName.value;
    bZip.value = sZip.value;
  } else {
    bName.value = '';
    bZip.value = '';
  }
}
