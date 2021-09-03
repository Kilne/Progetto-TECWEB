function ListGroupCreator(ProjectTitle, ProjectObj, Percentage, ProjLink) {

//    Single list group element
    const listItem = document.createElement("li");
    listItem.classList.add("list-group-item", "bg-warning", "m-2", "w-auto");

//    map for divs
    const div_map = new Map();

//    populating with 8 divs for List group structure
    for (let i = 0; i < 8; i++) {
        div_map.set(i, document.createElement("div"));
    }

//    creating the inner elements
    const paragraph = document.createElement("p");
    const header = document.createElement("h5");
    const anchor = document.createElement("a");

//    adding class and attribute keywords for each div level as they appear sequentially in the html structure

    div_map.get(0).classList.add("container-fluid");
    div_map.get(1).classList.add("row");
    div_map.get(2).classList.add("col-auto", "me-auto");
    div_map.get(3).classList.add("col-auto");
    div_map.get(4).classList.add("row");
    div_map.get(5).classList.add("col");
    div_map.get(6).classList.add("progress", "w-auto");
    div_map.get(7).classList.add("progress-bar", "progress-bar-striped", "bg-dark", "text-white");

//    adding inner elements attributes

    paragraph.id = "ProjectTabParagraph";
    paragraph.innerText = ProjectObj;

    header.id = "ProjectTabHead";
    header.innerText = ProjectTitle;

    anchor.id = "TabButton";
    anchor.innerText = "Project Page";
    anchor.href = ProjLink;
    anchor.classList.add("btn", "bg-dark", "text-warning");

//    Adding extra div class attributes

    div_map.get(7).setAttribute("role", "progressbar");
    div_map.get(7).setAttribute("style", "width: " + Percentage + "%");
    div_map.get(7).setAttribute("aria-valuenow", Percentage.toString());
    div_map.get(7).setAttribute("aria-valuemin", "0");
    div_map.get(7).setAttribute("aria-valuemax", "100");
    div_map.get(7).innerText = Percentage;

//    appending inner extra elements to their anchors
    div_map.get(2).append(header);
    div_map.get(2).append(paragraph);

    div_map.get(3).append(anchor);

//  appending the div elements in their nest form
    div_map.get(6).append(div_map.get(7));
    div_map.get(5).append(div_map.get(6));
    div_map.get(4).append(div_map.get(5));

    div_map.get(1).append(div_map.get(2));
    div_map.get(1).append(div_map.get(3));

    div_map.get(0).append(div_map.get(1));
    div_map.get(0).append(div_map.get(4));

//    appending all elements at the main anchor <li>

    listItem.append(div_map.get(0));

    return listItem;
}