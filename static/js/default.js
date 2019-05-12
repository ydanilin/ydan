document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var options = {};
    var instances = M.Sidenav.init(elems);
    var collapsibleElem = document.querySelectorAll('.collapsible');
    var collapsibleInstance = M.Collapsible.init(collapsibleElem);
  });
