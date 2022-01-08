let ele = document.querySelectorAll(".form-check-input");

ele.forEach(value => {
    value.addEventListener("click", evt => {
        if (!evt.target.hasAttribute("checked")) {
            ele.forEach(value1 => {
                if (value1.hasAttribute("checked")) {
                    value1.removeAttribute("checked");
                }
            })
            evt.target.setAttribute("checked", '');
        }
    })
})