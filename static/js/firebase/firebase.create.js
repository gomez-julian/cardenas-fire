import { createJSON, createTable } from "./json-utilities.js";
import { writeReportData, getReportData } from "./firebase.repo.js";
import { mensual} from "./jsons.js"

const type = document.getElementById('type').textContent
const id = parseInt(document.getElementById('key').textContent)
writeReportData(type, id, mensual, ()=>{
    console.log('Se ha creado correctamente')
})
