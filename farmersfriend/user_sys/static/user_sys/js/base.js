const navSlide = () => {
    const burger = document.getElementById("burger");
    const nav = document.querySelector(".nav")
    burger.addEventListener('click', () => {
        burger.classList.toggle('cross');
        nav.classList.toggle('toggle');
    })
}

const callUp = () => {
    const contactButton = document.querySelector(".Contact-button")
    const hiddenDiv = document.querySelectorAll(".contact-links div")
    const contact_links = document.querySelector(".contact-links")
    const image = document.getElementById("phone-image");
    contactButton.addEventListener('click', () => {
        if (hiddenDiv[0].style.opacity == 1) {

            for (var i = 3; i >= 0; i--) {
                hiddenDiv[i].style.animation = `linksFadeOut 0.3s ease backwards ${0.2 - i/5}s`;
                hiddenDiv[i].style.opacity = 0;
            }
            image.src = "images/icons8-phone.svg";
            contactButton.style.animation = `mainButtonOut 0.4s`;
            contactButton.style.opacity = 1;
            setTimeout(() => { contact_links.style.display = "none"; }, 400);
        } else {
            contact_links.style.display = "block";
            hiddenDiv.forEach((divs, index) => {
                divs.style.animation = `linksFadeIn 0.2s ease backwards ${index/10 + 0.1}s`;
                divs.style.opacity = 1;
                image.src = "images/icons8-down.svg";
            })
            contactButton.style.animation = `mainButtonIn 0.3s`;
            contactButton.style.opacity = 0.5;
        }
    })
}

navSlide();
callUp();