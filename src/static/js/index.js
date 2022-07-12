let items = document.querySelectorAll('.carousel .carousel-item')
// let shopImg = document.getElementById('shop-img')

items.forEach((el) => {
    const minPerSlide = 4
    let next = el.nextElementSibling
    for (var i=1; i<minPerSlide; i++) {
        if (!next) {
            // wrap carousel by using first child
        	next = items[0]
      	}
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})

// function hover(shopImg) {
//     shopImg.setAttribute('src', "{{ player['shop_item1_img2'] }}");
//     }
  
// function unhover(shopImg) {
//     shopImg.setAttribute('src', "{{ player['shop_item1_img1'] }}");
//     }