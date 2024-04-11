const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const previewContainer = document.getElementById('preview-container');

dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    const files = e.dataTransfer.files;
    handleFiles(files);
});

fileInput.addEventListener('change', () => {
    const files = fileInput.files;
    handleFiles(files);
});

function handleFiles(files) {
    if (files.length === 0) return;

    previewContainer.innerHTML = '';

    for (const file of files) {
        if (file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = () => {
                const img = document.createElement('img');
                img.src = reader.result;
                img.classList.add('preview-image');
                previewContainer.appendChild(img);
            };
        } else {
            alert(`File '${file.name}' is not an image.`);
        }
    }
}


function showForm() {
    var category = document.getElementById("category").value;
    var formContainer = document.getElementById("form-container");
  
    // Reset form container
    formContainer.innerHTML = '';
  
    // Show appropriate form based on category
    switch(category) {
      case "car":
        formContainer.innerHTML = `
        <form>
            <label for="model" class="lab" >Model:</label><br/>
            <input type="text" id="model" class="in" name="Model"><br/>
            <label for="finition" class="lab">finition:</label><br/>
            <input type="text" id="finition" class="in" name="finition"><br/>
            <label for="year" class="lab">year:</label><br/>
            <input type="text" id="year" class="in" name="year"><br/>
            <label for="engine" class="lab">engine:</label><br/>
            <input type="text" id="engine" class="in" name="engine"><br/>
            <label for="mileage" class="lab"> mileage:</label><br/>
            <input type="text" id="mileage" class="in" name="mileage"><br/>
            <label for="type" class="lab">type:</label><br/>
            <input type="text" id="type" class="in" name="type"><br/>
            <label for="Description" class="lab">Description:</label>
            <input type="text" id="Description" class="in" name="Description">
            <label for="Price" class="lab">Price:</label>
            <input type="text" id="Price" class="in" name="Price">
            <input type="submit" class="sub" value="Submit">
        </form>
        `;
        break;
      case "houses":
        formContainer.innerHTML = `
          <form>
            <label for="Type" class="lab">Type:</label>
            <input type="text" id="Type" class="in" name="Type">
            <label for="Location" class="lab">Location:</label>
            <input type="text" id="Location" class="in" name="Location">
            <label for="Facade" class="lab">Facade:</label>
            <input type="text" id="Facade" class="in" name="Facade">
            <label for="Area" class="lab">Area:</label>
            <input type="text" id="Area" class="in" name="Area">
            <label for="Floor" class="lab">Floor:</label>
            <input type="text" id="Floor" class="in" name="Floor">
            <label for="Rooms" class="lab">Rooms:</label>
            <input type="text" id="Rooms" class="in" name="Rooms">
            <label for="Description" class="lab">Description:</label>
            <input type="text" id="Description" class="in" name="Description">
            <label for="Price" class="lab">Price:</label>
            <input type="text" id="Price" class="in" name="Price">
            <input type="submit" class="sub" value="Submit">
          </form>
        `;
        break;
        case "laptop & phone":
        formContainer.innerHTML = `
          <form>
            <label for="Brand" class="lab" >Brand:</label><br/>
            <input type="text" id="Brand" class="in" name="Brand"><br/>
            <label for="Model" class="lab">Model:</label><br/>
            <input type="text" id="Model" class="in" name="Model"><br/>
            <label for="ROM" class="lab">ROM:</label><br/>
            <input type="text" id="ROM" class="in" name="ROM"><br/>
            <label for="RAM" class="lab">RAM:</label><br/>
            <input type="text" id="RAM" class="in" name="RAM"><br/>
            <label for="Processor" class="lab"> Processor:</label><br/>
            <input type="text" id="Processor" class="in" name="Processor"><br/>
            <label for="Display" class="lab"> Display:</label><br/>
            <input type="text" id="Display" class="in" name="Display"><br/>
            <label for="Graphic Card" class="lab"> Graphic Card:</label><br/>
            <input type="text" id="Graphic Card" class="in" name="Graphic Card"><br/>
            <label for="Description" class="lab">Description:</label>
            <input type="text" id="Description" class="in" name="Description">
            <label for="Price" class="lab"> Price:</label><br/>
            <input type="text" id="Price" class="in" name="Price"><br/>
            <input type="submit" class="sub" value="Submit">
          </form>
        `;
        break;
        case "home appliance":
        formContainer.innerHTML = `
          <form>
            <label for="Brand" class="lab" >Brand:</label><br/>
            <input type="text" id="Brand" class="in" name="Brand"><br/>
            <label for="Model" class="lab" >Model:</label><br/>
            <input type="text" id="Model" class="in" name="Model"><br/>
            <label for="Condition" class="lab">Condition:</label><br/>
            <input type="text" id="Condition" class="in" name="Condition"><br/>
            <label for="Description" class="lab">Description:</label>
            <input type="text" id="Description" class="in" name="Description">
            <label for="Price" class="lab"> Price:</label><br/>
            <input type="text" id="Price" class="in" name="Price"><br/>
            <input type="submit" class="sub" value="Submit">
          </form>
        `;
        break;
        case "clothing":
        formContainer.innerHTML = `
          <form>
            <label for="Brand" class="lab" >Brand:</label><br/>
            <input type="text" id="Brand" class="in" name="Brand"><br/>
            <label for="Model" class="lab" >Model:</label><br/>
            <input type="text" id="Model" class="in" name="Model"><br/>
            <label for="Size" class="lab">Size:</label><br/>
            <input type="text" id="Size" class="in" name="Size"><br/>
            <label for="Condition" class="lab">Condition:</label><br/>
            <input type="text" id="Condition" class="in" name="Condition"><br/>
            <label for="Description" class="lab">Description:</label>
            <input type="text" id="Description" class="in" name="Description">
            <label for="Price" class="lab"> Price:</label><br/>
            <input type="text" id="Price" class="in" name="Price"><br/> 
            <input type="submit" class="sub" value="Submit">
          </form>
        `;
        break;
        case "spare part":
        formContainer.innerHTML = `
          <form>
            <label for="Brand" class="lab" >Brand:</label><br/>
            <input type="text" id="Brand" class="in" name="Brand"><br/>
            <label for="Model" class="lab" >Model:</label><br/>
            <input type="text" id="Model" class="in" name="Model"><br/> 
            <label for="Condition" class="lab">Condition:</label><br/>
            <input type="text" id="Condition" class="in" name="Condition"><br/>
            <label for="Description" class="lab">Description:</label>
            <input type="text" id="Description" class="in" name="Description">
            <label for="Price" class="lab"> Price:</label><br/>
            <input type="text" id="Price" class="in" name="Price"><br/>
            <input type="submit" class="sub" value="Submit">
          </form>
        `;
        break;
        case "Accessories":
        formContainer.innerHTML = `
          <form>
            <label for="Brand" class="lab" >Brand:</label><br/>
            <input type="text" id="Brand" class="in" name="Brand"><br/>
            <label for="Model" class="lab" >Model:</label><br/>
            <input type="text" id="Model" class="in" name="Model"><br/> 
            <label for="Condition" class="lab">Condition:</label><br/>
            <input type="text" id="Condition" class="in" name="Condition"><br/>
            <label for="Description" class="lab">Description:</label>
            <input type="text" id="Description" class="in" name="Description">
            <label for="Price" class="lab"> Price:</label><br/>
            <input type="text" id="Price" class="in" name="Price"><br/>
            <input type="submit" class="sub" value="Submit">
          </form>
        `;
        break;
      default:
        formContainer.style.display = "none";
    }
  
    // Show form container if category is selected
    if(category !== "none") {
      formContainer.style.display = "block";
    } else {
      formContainer.style.display = "none";
    }
  }
  