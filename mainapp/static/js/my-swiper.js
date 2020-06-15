const slider = document.querySelector('.swiper-container');

let mySwiper = new Swiper ('.swiper-container', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
    slidesPerView:8 ,
    spaceBetween: 20,

    // If we need pagination
    pagination: {
        el: '.swiper-pagination',
        type: 'fraction',
        clickable: true,
    },
    // breakpoints: {
    //     760: {
    //         slidesPerView: 4,
    //         spaceBetween: 20,
    //     },
    //     1024: {
    //         slidesPerView: 4,
    //         spaceBetween: 20,
    //     }
    // },

    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    // And if we need scrollbar
    scrollbar: {
        el: '.swiper-scrollbar',
    },
})
