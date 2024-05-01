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
            <label for="brand" class="lab">brand:</label><br/>
            <input type="text" id="brand" class="in" name="brand" required><br/>
            <label for="Model" class="lab" >Model:</label><br/>
            <input type="text" id="Model" class="in" name="Model" required><br/>
            <label for="Finition" class="lab">Finition:</label><br/>
            <input type="text" id="Finition" class="in" name="Finition"><br/>
            <label for="fuel" class="lab">fuel:</label><br/>
            <input type="text" id="fuel" class="in" name="fuel" required><br/>
            <label for="Year" class="lab">Year:</label><br/>
            <input type="text" id="Year" class="in" name="Year" required><br/>
            <label for="Engine" class="lab">Engine:</label><br/>
            <input type="text" id="Engine" class="in" name="Engine" required><br/>
            <label for="Mileage" class="lab"> Mileage:</label><br/>
            <input type="text" id="Mileage" class="in" name="Mileage" required><br/>
            <label for="Description" class="lab">Description:</label>
            <textarea type="text" id="Description" class="in" name="Description" placeholder="Write something.." required></textarea>
            <label for="Price" class="lab">Price:</label>
            <input type="text" id="Price" class="in" name="Price" required>
            <input type="submit" class="sub" value="Submit">
        </form>
        `;
        break;
      case "houses":
        formContainer.innerHTML = `
          <form>
            <label for="Type" class="lab">Type:</label>
            <input type="text" id="Type" class="in" name="Type">
            <label for="location" class="lab">location:</label>
            <input type="text" id="location" class="in" name="location">
            <label for="Facade" class="lab">Facade:</label>
            <input type="text" id="Facade" class="in" name="Facade">
            <label for="Area" class="lab">Area:</label>
            <input type="text" id="Area" class="in" name="Area">
            <label for="Floor" class="lab">Floor:</label>
            <input type="text" id="Floor" class="in" name="Floor">
            <label for="Rooms" class="lab">Rooms:</label>
            <input type="text" id="Rooms" class="in" name="Rooms">
            <label for="Description" class="lab">Description:</label>
            <textarea type="text" id="Description" class="in" name="Description" placeholder="Write something.."></textarea>
            <label for="Price" class="lab">Price:</label>
            <input type="text" id="Price" class="in" name="Price">
            <input type="submit" class="sub" value="Submit">
          </form>
        `;
        break;
        case "laptop_phone":
        formContainer.innerHTML = `
          <form>
            <label for="Brand" class="lab" >Brand:</label><br/>
            <input type="text" id="Brand" class="in" name="Brand"><br/>
            <label for="Model" class="lab">Model:</label><br/>
            <input type="text" id="Model" class="in" name="Model"><br/>
            <label for="Processor" class="lab"> Processor:</label><br/>
            <input type="text" id="Processor" class="in" name="Processor"><br/>
            <label for="RAM" class="lab">RAM:</label><br/>
            <input type="text" id="RAM" class="in" name="RAM"><br/>
            <label for="ROM" class="lab">ROM:</label><br/>
            <input type="text" id="ROM" class="in" name="ROM"><br/>
            <label for="Display" class="lab"> Display:</label><br/>
            <input type="text" id="Display" class="in" name="Display"><br/>
            <label for="Graphic Card" class="lab"> Graphic Card:</label><br/>
            <input type="text" id="Graphic Card" class="in" name="Graphic_card"><br/>
            <label for="Description" class="lab">Description:</label>
            <textarea type="text" id="Description" class="in" name="Description" placeholder="Write something.."></textarea>
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
            <textarea type="text" id="Description" class="in" name="Description" placeholder="Write something.."></textarea>
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
            <textarea type="text" id="Description" class="in" name="Description" placeholder="Write something.."></textarea>
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
            <textarea type="text" id="Description" class="in" name="Description" placeholder="Write something.."></textarea>
            <label for="Price" class="lab"> Price:</label><br/>
            <input type="text" id="Price" class="in" name="Price"><br/>
            <input type="submit" class="sub" value="Submit">
          </form>
        `;
        break;
        case "accessories":
        formContainer.innerHTML = `
          <form>
            <label for="Brand" class="lab" >Brand:</label><br/>
            <input type="text" id="Brand" class="in" name="Brand"><br/>
            <label for="Model" class="lab" >Model:</label><br/>
            <input type="text" id="Model" class="in" name="Model"><br/> 
            <label for="Condition" class="lab">Condition:</label><br/>
            <input type="text" id="Condition" class="in" name="Condition"><br/>
            <label for="Description" class="lab">Description:</label>
            <textarea type="text" id="Description" class="in" name="Description" placeholder="Write something.."></textarea>
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
  


  function showFilter() {
    var category = document.getElementById("category1").value;
    var formContainer = document.getElementById("form-container");
  
    // Reset form container
    formContainer.innerHTML = '';
  
    // Show appropriate form based on category
    switch(category) {
      case "Laptop":
        formContainer.innerHTML = `
        <form>
            <select id="category" >
                            <option value="none">Brand</option>
                            <option value="Asus">Asus</option>
                            <option value="Dell">Dell </option>
                            <option value="Apple">Apple </option>
                            <option value="Lenovo">Lenovo </option>
                            <option value="MSI">MSI </option>
                            <option value="Acer">Acer </option>
                            <option value="Razer">Razer </option>
                            <option value="HP">HP </option>
            </select><br><br>

            <h3 class="filter">RAM :</h3><br>
            <input type="checkbox" id="4 GB" name="4 GB" value="4 GB">
            <label for="4 GB"> 4 GB</label><br>
            <input type="checkbox" id="6 GB" name="6 GB" value="6 GB">
            <label for="6 GB"> 6 GB</label><br>
            <input type="checkbox" id="8 GB" name="8 GB" value="8 GB">
            <label for="8 GB"> 8 GB</label><br>
            <input type="checkbox" id="12 GB" name="12 GB" value="12 GB">
            <label for="12 GB"> 12 GB</label><br>
            <input type="checkbox" id="16 GB" name="16 GB" value="16 GB">
            <label for="16 GB"> 16 GB</label><br>
            <input type="checkbox" id="32 GB" name="32 GB" value="32 GB">
            <label for="32 GB"> 32 GB</label><br><br>

            <h3 class="filter">ROM :</h3><br>
            <input type="checkbox" id="256 GB" name="256 GB" value="256 GB">
            <label for="256 GB"> 256 GB</label><br>
            <input type="checkbox" id="512 GB" name="512 GB" value="512 GB">
            <label for="512 GB"> 512 GB</label><br>
            <input type="checkbox" id="1 Tb" name="1 Tb" value="1 Tb">
            <label for="1 Tb"> 1 Tb</label><br><br>

            <h3 class="filter">Size :</h3><br>
            <input type="checkbox" id="13 inch" name="13 inch" value="13 inch">
            <label for="13 inch"> 13 inch</label><br>
            <input type="checkbox" id="15.6 inch" name="15.6 inch" value="15.6 inch">
            <label for="15.6 inch"> 15.6 inch</label><br>
            <input type="checkbox" id="17 inch" name="17 inch" value="17 inch">
            <label for="17 inch"> 17 inch</label><br><br>

            <h3 class="filter">Graphic card :</h3><br>
            <input type="checkbox" id="GTX" name="GTX" value="GTX">
            <label for="GTX "> GTX </label><br>
            <input type="checkbox" id="RTX" name="RTX" value="RTX">
            <label for="RTX"> RTX</label><br><br>

            <h3 class="filter">Processor :</h3><br>
            <input type="checkbox" id="intel" name="intel" value="intel">
            <label for="intel "> intel </label><br>
            <input type="checkbox" id="Ryzen" name="Ryzen" value="Ryzen">
            <label for="Ryzen"> Ryzen</label><br><br>

            <label for="Price" class="lab"> Price:</label><br>
            <input type="number" id="annee1" min="1" max="1000" placeholder="MIN">
            <input type="number" id="annee" min="1001" max="100000" placeholder="MAX" ><br>

          </form>
        `;
        break;
      case "Phone":
        formContainer.innerHTML = `
        <form>
            <select id="category" >
                <option value="none">Brand</option>
                <option value="Apple">Apple </option>
                <option value="Huawei">Huawei</option>
                <option value="Samsung">Samsung </option>
                <option value="Xiaomi">Xiaomi </option>
                <option value="OnePlus">OnePlus </option>
                <option value="OPPO">OPPO </option>
                <option value="Realme">Realme </option>
                <option value="Condor">Condor </option>
            </select><br><br><br>

            <h3 class="filter">RAM :</h3><br>
            <input type="checkbox" id="4 GB" name="4 GB" value="4 GB">
            <label for="4 GB"> 4 GB</label><br>
            <input type="checkbox" id="6 GB" name="6 GB" value="6 GB">
            <label for="6 GB"> 6 GB</label><br>
            <input type="checkbox" id="8 GB" name="8 GB" value="8 GB">
            <label for="8 GB"> 8 GB</label><br>
            <input type="checkbox" id="12 GB" name="12 GB" value="12 GB">
            <label for="12 GB"> 12 GB</label><br><br>

            <h3 class="filter">ROM :</h3><br>
            <input type="checkbox" id="64 GB" name="64 GB" value="64 GB">
            <label for="64 GB"> 64 GB</label><br>
            <input type="checkbox" id="128 GB" name="128 GB" value="128 GB">
            <label for="128 GB"> 128 GB</label><br>
            <input type="checkbox" id="256 GB" name="256 GB" value="256 GB">
            <label for="256 GB"> 256 GB</label><br>
            <input type="checkbox" id="512 GB" name="512 GB" value="512 GB">
            <label for="512 GB"> 512 GB</label><br><br>

            <h3 class="filter">Display :</h3><br>
            <input type="checkbox" id="4.7 inch" name="4.7 inch" value="4.7 inch">
            <label for="4.7 inch"> 4.7 inch</label><br>
            <input type="checkbox" id="5.5 inch" name="5.5 inch" value="5.5 inch">
            <label for="5.5 inch"> 5.5 inch</label><br>
            <input type="checkbox" id="6.4 inch" name="6.4 inch" value="6.4 inch">
            <label for="6.4 inch"> 6.4 inch</label><br><br>

            <h3 class="filter">Battery :</h3><br>
            <input type="checkbox" id="3000 mah" name="3000 mah" value="3000  mah">
            <label for="3000 mah "> 3000 mah </label><br>
            <input type="checkbox" id="3500 mah" name="3500 mah" value="3500 mah">
            <label for="3500 mah"> 3500 mah</label><br>
            <input type="checkbox" id="4000 mah" name="4000 mah" value="4000 mah">
            <label for="4000 mah"> 4000 mah</label><br>
            <input type="checkbox" id="4500 mah" name="4500 mah" value="4500 mah">
            <label for="4500 mah"> 4500 mah</label><br>
            <input type="checkbox" id="5000 mah" name="5000 mah" value="5000 mah">
            <label for="5000 mah"> 5000 mah</label><br><br>

            <label for="Price" class="lab"> Price:</label><br>
            <input type="number" id="annee1" min="1" max="1000" placeholder="MIN">
            <input type="number" id="annee" min="1001" max="100000" placeholder="MAX" ><br>
        </form>
        `;
        break;
        case "Tablet":
        formContainer.innerHTML = `
          <form>
            <select id="category" >
                <option value="none">Brand</option>
                <option value="Apple">Apple </option>
                <option value="Huawei">Huawei</option>
                <option value="Samsung">Samsung </option>
                <option value="Microsoft">Microsoft </option>
                <option value="Google">Google </option>
                <option value="Xiaomi">Xiaomi </option>
                <option value="Condor">Condor </option>
            </select><br><br>

            <h3 class="filter">RAM :</h3><br>
            <input type="checkbox" id="4 GB" name="4 GB" value="4 GB">
            <label for="4 GB"> 4 GB</label><br>
            <input type="checkbox" id="6 GB" name="6 GB" value="6 GB">
            <label for="6 GB"> 6 GB</label><br>
            <input type="checkbox" id="8 GB" name="8 GB" value="8 GB">
            <label for="8 GB"> 8 GB</label><br>
            <input type="checkbox" id="12 GB" name="12 GB" value="12 GB">
            <label for="12 GB"> 12 GB</label><br><br>
            <br>
            <h3 class="filter">ROM :</h3><br>
            <input type="checkbox" id="64 GB" name="64 GB" value="64 GB">
            <label for="64 GB"> 64 GB</label><br>
            <input type="checkbox" id="128 GB" name="128 GB" value="128 GB">
            <label for="128 GB"> 128 GB</label><br>
            <input type="checkbox" id="256 GB" name="256 GB" value="256 GB">
            <label for="256 GB"> 256 GB</label><br>
            <input type="checkbox" id="512 GB" name="512 GB" value="512 GB">
            <label for="512 GB"> 512 GB</label><br><br>
            <br>

            <h3 class="filter">Display :</h3><br>
            <input type="checkbox" id="5 inch " name="5 inch " value="5 inch ">
            <label for="5 inch "> 5  inch</label><br>
            <input type="checkbox" id="7 inch" name="7 inch" value="7 inch">
            <label for="7 inch"> 7 inch</label><br>
            <input type="checkbox" id="9 inch" name="9 inch" value="9 inch">
            <label for="9 inch"> 9 inch</label><br>
            <input type="checkbox" id="10 inch" name="10 inch" value="10 inch">
            <label for="10 inch"> 10 inch</label><br>
            <input type="checkbox" id="13 inch" name="13 inch" value="13 inch">
            <label for="13 inch"> 13 inch</label><br><br>
            <br>
            <label for="Price" class="lab"> Price:</label><br>
            <input type="number" id="annee1" min="1" max="1000" placeholder="MIN">
            <input type="number" id="annee" min="1001" max="100000" placeholder="MAX" ><br><br>

        </form>
        `;
        break;
        case "Smart watch":
        formContainer.innerHTML = `
          <form>
          <br>
            <select id="category" >
                <option value="none">Brand</option>
                <option value="Apple">Apple </option>
                <option value="Huawei">Huawei</option>
                <option value="Samsung">Samsung </option>
                <option value="Fitbit">Fitbit </option>
                <option value="Fossil">Fossil </option>
                <option value="Garmin">Garmin </option>
                <option value="Haylo">Haylo </option>
            </select><br><br><br>

            <h3 class="filter">Condition :</h3><br>
            <input type="checkbox" id="New" name="New" value="New">
            <label for="New"> New</label><br>
            <input type="checkbox" id="Used like new" name="Used like new" value="Used like new">
            <label for="Used like new"> Used like new</label><br>
            <input type="checkbox" id="Used" name="Used" value="Used">
            <label for="Used"> Used</label><br>
            <input type="checkbox" id="Bad" name="Bad" value="Bad">
            <label for="Bad"> Bad</label><br><br>

            <h3 class="filter">Display :</h3><br>
            <input type="checkbox" id="38 mm" name="38 mm" value="38 mm">
            <label for="38 mm"> 4.7 inch</label><br>
            <input type="checkbox" id="42 mm" name="42 mm" value="42 mm">
            <label for="42 mm"> 42 mm</label><br><br><br>

            <label for="Price" class="lab"> Price:</label><br>
            <input type="number" id="annee1" min="1" max="1000" placeholder="MIN">
            <input type="number" id="annee" min="1001" max="100000" placeholder="MAX" ><br><br>
            
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

  $(document).ready(function() {
    // Function to handle the click event of the "Approve" button
    $('.btn-approve').click(function() {
        var carId = $(this).data('car-id');
        // Here, you can perform an action to approve the car with the ID 'carId'
        console.log("Car ID " + carId + " approved.");
    });

    // Function to handle the click event of the "Delete" button
    $('.btn-delete').click(function() {
        var carId = $(this).closest('tr').attr('id').replace('car-', '');
        // Here, you can perform an action to delete the car with the ID 'carId'
        console.log("Car ID " + carId + " deleted.");
    });
});