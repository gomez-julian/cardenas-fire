// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.7.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.7.0/firebase-analytics.js";
import {
  getDatabase,
  ref,
  set,
  child,
  get,
} from "https://www.gstatic.com/firebasejs/9.7.0/firebase-database.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDjgSZ63OUKKOlG0NO2FqIFq1hGuTlvNco",
  authDomain: "cardenas-reports-backend.firebaseapp.com",
  databaseURL: "https://cardenas-reports-backend-default-rtdb.firebaseio.com",
  projectId: "cardenas-reports-backend",
  storageBucket: "cardenas-reports-backend.appspot.com",
  messagingSenderId: "671598383327",
  appId: "1:671598383327:web:9969ca7a9936a50220996a",
  measurementId: "G-LSYSGVNW6J",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

function writeReportData(type, reportID, data, callback) {
  const db = getDatabase();
  set(ref(db, `${type}/${reportID}`), data);
  callback();
  // set(ref(db, `mensual/200`), data);
}

async function getReportData(type, reportID, callback) {
  const dbRef = ref(getDatabase());
  await get(child(dbRef, `${type}/${reportID}`))
    .then((snapshot) => {
      if (snapshot.exists()) {
        console.log("Regresando datos");
        // console.log(snapshot.val());
        callback(snapshot.val());
      } else {
        console.log("No data available");
      }
    })
    .catch((error) => {
      console.error(error);
    });
}

function createJSON(table) {
  const [header] = table.tHead.rows;
  const props = [...header.cells].map((h) => h.textContent);
  const rows = [...table.rows].map((r) => {
    const entries = [...r.cells].map((c, i) => {
      return [props[i], c.textContent.trim()];
    });
    return Object.fromEntries(entries);
  });
  rows.shift();
  return rows;
}

function createTable(d) {
  let t = document.createElement("table");
  t.classList.add("table");
  let b = document.createElement("tbody");

  for (let i = 0; i < d.length; i++) {
    var a = document.createElement("tr");
    a.innerHTML =
      "<td contenteditable='true'>" +
      d[i].INDICE +
      "</td>" +
      "<td contenteditable='true'>" +
      d[i].DESCRIPCIÓN +
      "</td>" +
      "<td contenteditable='true'>" +
      d[i].F +
      "</td>" +
      "<td contenteditable='true'>" +
      d[i].SI +
      "</td>" +
      "<td contenteditable='true'>" +
      d[i].NA +
      "</td>" +
      "<td contenteditable='true'>" +
      d[i].NO +
      "</td>" +
      "<td contenteditable='true'>" +
      d[i].PARÁMETROS +
      "</td>" +
      "<td contenteditable='true'>" +
      d[i].LECTURAS +
      "</td>" +
      "<td contenteditable='true'>" +
      d[i].COMENTARIOS +
      "</td>";
    b.append(a);
  }
  t.append(b);
  const index = [
    "INDICE",
    "DESCRIPCIÓN",
    "F",
    "SI",
    "NA",
    "NO",
    "PARÁMETROS",
    "LECTURAS",
    "COMENTARIOS",
  ];
  let header = t.createTHead();
  var row = header.insertRow(0);
  for (var f = 0; f < 9; f++) {
    var cell = row.insertCell();
    cell.innerHTML = index[f];
  }
  t.append(b);
  document.body.append(t);
  return t;
}

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

function printJSON(typeJSON, keyJSON) {
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
  let ob = {
    data: form,
    type: typeJSON,
  };
  writeReportData(typeJSON, keyJSON, ob, () => {
    console.log("Se han guardado los cambios");
  });
}

$(document).ready(function () {
  const type = document.getElementById("type").textContent;
  const id = parseInt(document.getElementById("key").textContent);

  getReportData(type, id, (data) => {
    console.log(data);
    data.data.forEach((element) => {
      document.getElementById("form-container").append(createCard(element));
    });
  });

  $("#btnsave").click(() => {
    printJSON(type, id);
    $("#uploadToast").toast("show");
    console.log("Guardado finalizado");
  });
});
