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

    outerDiv.classList.add("card", "border-dark", "border-1", "m-auto");
    outerDiv.style.width = "400px";

    innerDiv.classList.add("card-body", "bg-warning", "text-center", "bg-gradient");


    headTitle.classList.add("card-title");
    headTitle.innerText = CardTitle;

    paragraph.classList.add("card-text");
    paragraph.innerText = CardText;

    buttonLink.classList.add("btn", "btn-dark", "text-warning");
    buttonLink.href = BtnLink;
    buttonLink.innerText = "Go to project";

    innerDiv.append(headTitle, paragraph, buttonLink);

    outerDiv.append(innerDiv);

    return outerDiv;
}