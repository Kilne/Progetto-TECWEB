// CARUSEL INNER ELEMENT GRABBING VIA QUERYSELECT
let inner_carousel_ele = document.querySelector(".carousel-inner");

// CARUSEL OUTER INDICAOR ANCHOR ELEMENT GRABBING VIA QUERY SELECT
let carousel_indicator_anchor_ele = document.querySelector(".carousel-indicators");

// CARD ADDING

for (let i = 0; i < 5; i++) {
    // CUSTOMIZING INDICATORS
    let carousel_indicator_ele = document.createElement("button");
    carousel_indicator_ele.type = "button";
    carousel_indicator_ele.setAttribute("data-bs-target", "#carouselExampleIndicators");
    carousel_indicator_ele.setAttribute("data-bs-slide-to", "" + i.toString());
    carousel_indicator_ele.setAttribute("aria-label", "Slide " + (i + 1).toString());

    if (i === 0) {
        carousel_indicator_ele.classList.add("active");
        carousel_indicator_ele.setAttribute("aria-current", "true");
    }

    // CUSTOMIZING ITEM ELEMENT

    let carousel_item_ele = document.createElement("div");

    if (i === 0) {
        carousel_item_ele.classList.add("active");
    }
    carousel_item_ele.classList.add("carousel-item");
    carousel_item_ele.setAttribute("data-bs-interval", "10000");

    // APPENDING CARD WITH CARD CREATOR
    carousel_item_ele.append(card_creator("Test Card", "Test Body", "/"));

    // APPENDING ELEMENTS TO THE ANCHORS

    carousel_indicator_anchor_ele.appendChild(carousel_indicator_ele);
    inner_carousel_ele.appendChild(carousel_item_ele);
}