	const menu = document.querySelector('#mobile-menu');
	const links = document.querySelector('.nav-menu');

menu.addEventListener('click', function() {
	menu.classList.toggle('is-active');
	links.classList.toggle('active');
})