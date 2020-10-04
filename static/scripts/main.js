function copyToClipboard() {
  var url_node = "fakeUrl"
  var text = document.getElementById(url_node)
  const listener = function(ev) {
    ev.preventDefault();
    ev.clipboardData.setData('text/plain', text);
  };
  document.addEventListener('copy', listener);
  document.execCommand('copy');
  document.removeEventListener('copy', listener);
}
