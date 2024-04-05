var remote = "http://127.0.0.1:8000/";

$(document).ready(function () {
  $.ajax({
    url: remote + "menus/",
    method: "GET",
  }).then(function (menus) {
    console.log(menus);
    for (i = 0; i < menus.length; i++) {
      var link = document.createElement("a");
      link.id = menus[i].link;
      link.textContent = menus[i].title;
      link.classList.add("nav-link");
      if (menus[i].hasChild === false) {
        link.href = remote + menus[i].link;
        link.classList.add("nav-item");
        $("#menus").append(link);
      } else {
        link.href = "#";
        link["data-bs-toggle"] = "dropdown";
        link.classList.add("dropdown-toggle");
        var div = document.createElement("div");
        div.classList.add("nav-item", "dropdown");
        div.append(link);
        var div2 = document.createElement("div");
        div2.classList.add(
          "dropdown-menu",
          "rounded-0",
          "rounded-bottom",
          "m-0"
        );
        for (j = 0; j < menus[i].items.length; j++) {
          var link = document.createElement("a");
          link.classList.add("dropdown-item");
          link.id = menus[i].items[j].link;
          link.textContent = menus[i].items[j].title;
          link.href = remote + menus[i].items[j].link;
          div2.append(link);
        }
        div.append(div2);
        $("#menus").append(div);
      }
    }
  });
});
