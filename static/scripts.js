function navbarExpand() {
    document.getElementsByClassName('navbar-links')[0].classList.toggle('active');
  }

document.getElementById("toTop").addEventListener('click', function(e) {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
});