async function uploadPictures(){
    // $('#textprimary').text('Subiendo imágenes, por favor espere...')
    uploadFile('file3','pictureOne')
    uploadFile('file3','pictureTwo')
}

async function uploadFile(id, input){
    let photo = document.getElementById(id).files[0];
    let formData = new FormData();
     
    formData.append("file", photo);
    await fetch('http://127.0.0.1:8000/api/upload', {method: "POST", body: formData})
    .then(response => response.json())
    .then(data => {
        console.log(data)
        document.getElementById(input).value = data.uploaded_file_name;
        // $('#textsuccess').text('Imágenes subidas exitosamente')
        // $('#textprimary').text('Complete la descripción de la evidencia')
      })
    .catch(err => {
        console.error("ERROR: ", err)
        // $('#textprimary').text('A ocurrido un error, vuelva a intentarlo.')
      });
}