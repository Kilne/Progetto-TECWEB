function cardCreator(CardTitle, CardText, BtnLink) {
    let outerDiv = document.createElement("div");
    let innerDiv = document.createElement("div");
    let headTitle = document.createElement("h5");
    let paragraph = document.createElement("p");
    let buttonLink = document.createElement("a");
    outerDiv.id = "card";
    innerDiv.id = "cardBody";
    headTitle.id = "titleCard";
    paragraph.id = "cardText";
    buttonLink.id = "cardButton";
    outerDiv.classList.add("card");
    innerDiv.classList.add("card-body");
    headTitle.classList.add("card-title");
    paragraph.classList.add("card-text");
    buttonLink.classList.add("btn");
    buttonLink.classList.add("btn-warning");
    buttonLink.href = BtnLink;
    buttonLink.innerText = "Go to project";
    paragraph.innerText = CardText;
    headTitle.innerText = CardTitle;

    innerDiv.append(headTitle, paragraph, buttonLink);
    outerDiv.append(innerDiv);

    return outerDiv;
}