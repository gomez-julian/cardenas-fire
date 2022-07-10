import { getDatabase, ref, set, child, get } from "https://www.gstatic.com/firebasejs/9.7.0/firebase-database.js";

function writeReportData(type, reportID, data, callback) {
  const db = getDatabase();
  set(ref(db, `${type}/${reportID}`), data);
  callback()
  // set(ref(db, `mensual/200`), data);
}

async function getReportData(type, reportID, callback){
  const dbRef = ref(getDatabase());
  await get(child(dbRef, `${type}/${reportID}`)).then((snapshot) => {
    if (snapshot.exists()) {
      console.log("Regresando datos");
      // console.log(snapshot.val());
      callback(snapshot.val());
    } else {
      console.log("No data available");
    }
  }).catch((error) => {
    console.error(error);
  });
}

export { writeReportData, getReportData }

// const userId = 1
// const dbRef = ref(getDatabase());
// get(child(dbRef, `users/${userId}`)).then((snapshot) => {
//   if (snapshot.exists()) {
//     console.log(snapshot.val());
//   } else {
//     console.log("No data available");
//   }
// }).catch((error) => {
//   console.error(error);
// });