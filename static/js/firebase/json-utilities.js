function createJSON(table) {
  // const table = document.querySelector(tableSelector);
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
  t.classList.add('table')
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
t.append(b)
document.body.append(t)
  return t;
}

export { createJSON, createTable };
