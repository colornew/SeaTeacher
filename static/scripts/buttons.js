const buttons = document.querySelectorAll('.button')

for (let i = 0; i < buttons.length; i++) {
    const button = buttons[i];
    button.addEventListener('mousemove', rising);
    button.addEventListener('mouseout', stopRising);
}

function rising(event) {
    const button = this
    button.style.background = '#F64C72';
    button.style.transform = 'scale(1.2)'
}

function stopRising(event) {
    const button = this
    button.style.background = 'rgba(0,0,0,0)';
    button.style.transform = 'scale(1)'
}

document.addEventListener("DOMContentLoaded", function () {
    if (window.innerWidth < 992) {

        document.querySelectorAll('.navbar .dropdown').forEach(function (everydropdown) {
            everydropdown.addEventListener('hidden.bs.dropdown', function () {
                this.querySelectorAll('.submenu').forEach(function (everysubmenu) {
                    everysubmenu.style.display = 'none';
                });
            })
        });

        document.querySelectorAll('.dropdown-menu a').forEach(function (element) {
            element.addEventListener('click', function (e) {
                let nextEl = this.nextElementSibling;
                if (nextEl && nextEl.classList.contains('submenu')) {
                    e.preventDefault();
                    if (nextEl.style.display == 'block') {
                        nextEl.style.display = 'none';
                    } else {
                        nextEl.style.display = 'block';
                    }

                }
            });
        })
    }
});
