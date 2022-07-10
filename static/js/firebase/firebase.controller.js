import { createJSON, createTable } from "./json-utilities.js";
import { writeReportData, getReportData } from "./firebase.repo.js";

function createCard(data) {
  let a = document.createElement("div");
  a.classList.add("card", "my-3");
  let b = document.createElement("div");
  b.classList.add("card-body");
  let c = document.createElement("h4");
  c.classList.add("card-title");
  c.textContent = data.section;
  let d = document.createElement("p");
  d.classList.add("card-description");
  d.textContent = "Descripcion";
  let e = document.createElement("div");
  e.classList.add("table-responsive");
  e.appendChild(createTable(data.data));
  b.append(c, d, e);
  a.appendChild(b);
  return a;
}

getReportData("mensual", 200, (data) => {
  console.log(data);
  data.data.forEach((element) => {
    document.body.append(createCard(element));
  });
});

function printJSON() {
  //GENERAR JSON DE VUELTA
  let a = document.getElementsByClassName("table");
  let b = document.getElementsByClassName("card-title");
  let form = [];
  for (let i = 0; i < a.length; i++) {
    // console.log(a[i])
    // console.log(b[i].textContent)
    let c = createJSON(a[i]);
    // console.log(c)
    form.push({
      data: c,
      section: b[i].textContent,
    });
  }
  console.log("data completo");
  let ob = {
    data: form,
    type: "mensual",
  };
  console.log(ob);
  writeReportData("mensual", 200, ob, () => {
    console.log("Se han guardado los cambios");
  });
}

$("#jsoncreate").click(printJSON);
