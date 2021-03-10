const ham = document.getElementById('ham');
ham.addEventListener('click', function () {
    ham.classList.toggle('clicked');
    menu_wrapper.classList.toggle('clicked');
});

const header_list_item = document.querySelectorAll('.header-list-item');
header_list_item.forEach(value => {
    value.addEventListener('click', e => {
        ham.classList.toggle('clicked');
        menu_wrapper.classList.toggle('clicked');
    })
});