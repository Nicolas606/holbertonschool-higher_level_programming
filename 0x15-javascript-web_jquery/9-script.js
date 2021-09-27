$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (traductor) {
  $('#hello').text(traductor.hello);
});
